# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos jpegs
                              -------------------
        begin                : 2017-10-17
        git sha              : $Format:%H$
        copyright            : (C) 2017 by KIOS Research Center
        email                : mariosmsk@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QVariant, Qt
from PyQt4.QtGui import QAction, QIcon, QMessageBox, QWidget, QFileDialog
from qgis.core import QgsMapLayerRegistry, QgsVectorLayer, QgsField, QgsVectorFileWriter, QgsFeature, QgsPoint, QgsGeometry, QgsSvgMarkerSymbolLayerV2
from qgis.gui import QgsEncodingFileDialog

# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from ImportPhotos_dialog import ImportPhotosDialog

from MouseClick import MouseClick
from Photos_dialog import PhotosDialog
import os.path
from PIL import Image
from PIL.ExifTags import TAGS
import uuid
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

class ImportPhotos:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'ImportPhotos_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&ImportPhotos')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'ImportPhotos')
        self.toolbar.setObjectName(u'ImportPhotos')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('ImportPhotos', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)
             
        return action

        
    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.plugin_path = os.path.join(os.environ['USERPROFILE']) + '/.qgis2/python/plugins/ImportPhotos'#os.path.dirname(__file__)
        icon_path = ':/plugins/ImportPhotos/svg/ImportImage.svg'
        self.add_action(
            icon_path,
            text=self.tr(u'Import Photos'),
            callback=self.run,
            parent=self.iface.mainWindow())
        icon_path = ':/plugins/ImportPhotos/svg/SelectImage.svg'
        self.clickPhotos = self.add_action(
            icon_path,
            text=self.tr(u'Click Photos'),
            callback=self.mouseClick,
            parent=self.iface.mainWindow())
        self.dlg = ImportPhotosDialog()
        self.dlg.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)

        self.dlg.ok.clicked.connect(self.ok)
        self.dlg.closebutton.clicked.connect(self.close)
        self.dlg.toolButtonImport.clicked.connect(self.toolButtonImport)
        self.dlg.toolButtonOut.clicked.connect(self.toolButtonOut)

        self.clickPhotos.setCheckable(True)
        self.clickPhotos.setEnabled(False)
        self.photosDLG = PhotosDialog()
        self.clickPhotos.setChecked(True)

        self.layernamePhotos = []
        self.listPhotos = []
        self.dirname = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.toolMouseClick = MouseClick(self.iface.mapCanvas(), self)

    def mouseClick(self):
        self.iface.mapCanvas().setMapTool(self.toolMouseClick)
        self.clickPhotos.setChecked(True)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
            self.tr(u'&ImportPhotos'),
            action)
            self.iface.removeToolBarIcon(action)
         # remove the toolbar
        del self.toolbar

    def run(self):
        self.clickPhotos.setEnabled(True)
        self.dlg.out.setText('')
        self.dlg.imp.setText('')
        self.dlg.progressBar.setValue(0)
        self.dlg.show()

    def close(self):
        self.dlg.close()

    def toolButtonOut(self):

        self.outDirectoryPhotosShapefile = QFileDialog.getSaveFileName(None, 'Save File', os.path.join(os.path.join(os.environ['USERPROFILE']),
                                                                   'Desktop'), 'ESRI Shapefiles (*.shp *.SHP)')
        self.dlg.out.setText(self.outDirectoryPhotosShapefile)

    def toolButtonImport(self):
        self.directoryPhotos = QFileDialog.getExistingDirectory(None, 'Select a folder:',
                                                      os.path.join(os.path.join(os.environ['USERPROFILE']),
                                                                   'Desktop'), QFileDialog.ShowDirsOnly)
        if self.directoryPhotos == "":
            return
        self.dlg.imp.setText(self.directoryPhotos)

    def ok(self):
        if self.dlg.imp.text()=='':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Please select a directory photos.')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()
            return
        if self.dlg.out.text()=='':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Please write ouptut shapefile.')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()
            return

        self.dlg.ok.setEnabled(False)
        self.dlg.closebutton.setEnabled(False)
        self.dlg.toolButtonImport.setEnabled(False)
        self.dlg.toolButtonOut.setEnabled(False)
        extens = ['jpg', 'jpeg', 'JPG', 'JPEG']
        photos = []
        for root, dirs, files in os.walk(self.directoryPhotos):
            photos.extend(os.path.join(root, name) for name in files
                          if name.lower().endswith(tuple(extens)))

        if len(photos) == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle('Warning')
            msgBox.setText('No images.')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()
            return
        #    return
        self.total = 100.0 / len(photos)
        self.iface.mapCanvas().setMapTool(self.toolMouseClick)
        fields = ["ID", "Name", "Date", "Time", "Altitude", "Lon", "Lat", "North", "Azimuth", "Path"]
        fieldsCode=[0,0,0,0,2,2,2,0,0,0]
        self.outDirectoryPhotosShapefile=self.dlg.out.text()
        basename = os.path.basename(self.outDirectoryPhotosShapefile)
        lphoto = basename[:-4]
        self.layernamePhotos.append(lphoto)
        self.layerPhotos = self.makeLayers(lphoto, fields, fieldsCode, "Point")
        try:
            self.layerPhotos.setLayerName(lphoto)
        except:
            self.dlg.ok.setEnabled(True)
            self.dlg.closebutton.setEnabled(True)
            self.dlg.toolButtonImport.setEnabled(True)
            self.dlg.toolButtonOut.setEnabled(True)
            return #message here

        try: self.layerPhotos.loadNamedStyle(self.plugin_path + "/svg/photos.qml")
        except: pass
        svgStyle = {}
        svgStyle['fill'] = '#0000ff'
        svgStyle['name'] = self.plugin_path + "/svg/Camera.svg"
        svgStyle['outline'] = '#0000000'
        svgStyle['outline-width'] = '6.8'
        svgStyle['size'] = '6'
        symLyr1 = QgsSvgMarkerSymbolLayerV2.create(svgStyle)
        self.layerPhotos.rendererV2().symbols()[0].changeSymbolLayer(0, symLyr1)
        QgsMapLayerRegistry.instance().addMapLayer(self.layerPhotos)
        self.layerPhotos.triggerRepaint()
        self.layerPhotos.setReadOnly(False)
        qgisTView = self.iface.layerTreeView()
        actions = qgisTView.defaultActions()
        actions.showFeatureCount()
        actions.showFeatureCount()
        # getPhotoProperties(extens, photos)
        for count, imgpath in enumerate(photos):
            print ''
            self.dlg.progressBar.setValue(int(count * self.total))
            a = self.get_exif(imgpath)
            #try:
            if 'GPSInfo' in a:
                if a is not None and a['GPSInfo'] != {}:
                    lat = [float(x) / float(y) for x, y in a['GPSInfo'][2]]
                    latref = a['GPSInfo'][1]
                    lon = [float(x) / float(y) for x, y in a['GPSInfo'][4]]
                    lonref = a['GPSInfo'][3]

                    lat = lat[0] + lat[1] / 60 + lat[2] / 3600
                    lon = lon[0] + lon[1] / 60 + lon[2] / 3600

                    if latref == 'S':
                        lat = -lat
                    if lonref == 'W':
                        lon = -lon
                    name = os.path.basename(imgpath)
                    uuid_ = str(uuid.uuid4())
                    try: dt1, dt2 = a['DateTime'].split()
                    except: dt1, dt2 = a['DateTimeOriginal'].split()
                    date = dt1.replace(':','/')
                    time = dt2
                    mAltitude = float(a['GPSInfo'][6][0])
                    mAltitudeDec = float(a['GPSInfo'][6][1])
                    altidude = mAltitude / mAltitudeDec
                    try:
                        north = str(a['GPSInfo'][16])
                        azimuth = str(a['GPSInfo'][17][0])
                    except:
                        north = ''
                        azimuth = ''

                    feature = QgsFeature()
                    point1 = QgsPoint(lon, lat)
                    # ADD ATTRIBUTE COLUMN
                    self.layerPhotos.startEditing()
                    feature.setGeometry(QgsGeometry.fromPoint(point1))
                    feature.setAttributes([uuid_, name, date, time, altidude, lon, lat, north, azimuth, imgpath])
                    self.layerPhotos.dataProvider().addFeatures([feature])
            #except: pass
        self.dlg.progressBar.setValue(100)
        #####################################
        self.layerPhotos.commitChanges()
        self.dlg.progressBar.setValue(0)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle('ImportPhotos')
        msgBox.setText('Import sucessfull.')
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        msgBox.exec_()
        self.dlg.ok.setEnabled(True)
        self.dlg.closebutton.setEnabled(True)
        self.dlg.toolButtonImport.setEnabled(True)
        self.dlg.toolButtonOut.setEnabled(True)

    def get_exif(self, imagepath):
        ret = {}
        try:
            info = Image.open(imagepath)._getexif()
            if info is not None:
                for tag, value in info.items():
                    ret[TAGS.get(tag, tag)] = value
                del tag
                return ret
        except:
            return None

    def refresh(self): # Deselect features
        mc = self.iface.mapCanvas()
        for layer in mc.layers():
            if layer.type() == layer.VectorLayer:
                layer.removeSelection()
        mc.refresh()

    def makeLayers(self,layername,fields,fieldsCode,type):
        pos = QgsVectorLayer(type, layername, "memory")
        pr = pos.dataProvider()
        shapename = layername + ".shp"
        dest = self.outDirectoryPhotosShapefile
        for i in range(len(fieldsCode)):
            if fieldsCode[i]==0:
                pr.addAttributes( [ QgsField(fields[i], QVariant.String) ] )
            elif fieldsCode[i]==1:
                pr.addAttributes( [ QgsField(fields[i], QVariant.Int) ] )
            elif fieldsCode[i]==2:
                pr.addAttributes( [ QgsField(fields[i], QVariant.Double) ] )
        pos.startEditing()
        QgsVectorFileWriter.writeAsVectorFormat(pos,dest,"utf-8",None,"ESRI Shapefile")
        self.iface.messageBar().clearWidgets()
        crs = pos.crs()
        crs.createFromId(4326)
        pos.setCrs(crs)
        return self.iface.addVectorLayer(dest, shapename[:-4], "ogr")