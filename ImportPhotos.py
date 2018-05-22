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
from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.core import QgsProject, QgsRectangle

# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .ImportPhotos_dialog import ImportPhotosDialog

from .MouseClick import MouseClick
import os.path
import exifread
import uuid

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
        self.clickPhotos.setEnabled(True)

        self.listPhotos = []
        self.layernamePhotos = []
        self.toolMouseClick = MouseClick(self.iface.mapCanvas(), self)

        self.fields = ['ID', 'Name', 'Date', 'Time', 'Lon', 'Lat', 'Altitude', 'North', 'Azimuth', 'Camera Maker',
                       'Camera Model', 'Path']

    def mouseClick(self):
        try:
            self.iface.setActiveLayer(self.iface.mapCanvas().layers()[0])
        except:
            pass
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
        self.dlg.ok.setEnabled(True)
        self.dlg.closebutton.setEnabled(True)
        self.dlg.toolButtonImport.setEnabled(True)
        self.dlg.toolButtonOut.setEnabled(True)
        self.clickPhotos.setEnabled(True)
        self.dlg.out.setText('')
        self.dlg.imp.setText('')
        self.dlg.progressBar.setValue(0)
        self.dlg.show()

    def close(self):
        self.dlg.close()

    def toolButtonOut(self):

        self.outDirectoryPhotosShapefile = QFileDialog.getSaveFileName(None, 'Save File', os.path.join(
            os.path.join(os.path.expanduser('~')),
            'Desktop'), 'GeoJSON (*.geojson *.GEOJSON)')
        self.outDirectoryPhotosShapefile = self.outDirectoryPhotosShapefile[0]
        self.dlg.out.setText(self.outDirectoryPhotosShapefile)

    def toolButtonImport(self):
        # try:
        self.directoryPhotos = QFileDialog.getExistingDirectory(None, 'Select a folder:',
                                                                os.path.join(os.path.join(os.path.expanduser('~')),
                                                                             'Desktop'), QFileDialog.ShowDirsOnly)
        if self.directoryPhotos == "":
            return
        self.dlg.imp.setText(self.directoryPhotos)

    def selectDir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Please select a folder with photos.')
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        msgBox.exec_()
        return True

    def selectOutp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle('Warning')
        msgBox.setText('Please define output file location.')
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        msgBox.exec_()
        return True

    def ok(self):
        if self.dlg.imp.text() == '':
            if self.selectDir():
                return
        if os.path.isdir(self.dlg.imp.text())==False:
            if self.selectDir():
                return
        if self.dlg.out.text() == '':
            if self.selectOutp():
                return
        if os.path.isabs(self.dlg.out.text())==False:
            if self.selectOutp():
                return
        self.outDirectoryPhotosShapefile = self.dlg.out.text()
        try:
            f = open(self.outDirectoryPhotosShapefile, "w")
            f.close()
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle('Warning')
            msgBox.setText('Please define output file location.')
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
            self.dlg.ok.setEnabled(True)
            self.dlg.closebutton.setEnabled(True)
            self.dlg.toolButtonImport.setEnabled(True)
            self.dlg.toolButtonOut.setEnabled(True)
            self.clickPhotos.setChecked(True)
            return

        self.total = 100.0 / len(photos)
        self.iface.mapCanvas().setMapTool(self.toolMouseClick)
        basename = os.path.basename(self.outDirectoryPhotosShapefile)
        lphoto = basename[:-8]

        self.layernamePhotos.append(lphoto)
        truePhotosCount = 0

        geoPhotoFile = open(self.outDirectoryPhotosShapefile, "w")
        geoPhotoFile.write('''{ "type": "FeatureCollection", ''')
        geoPhotoFile.write(
            '''"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } }, ''')
        geoPhotoFile.write('\n')
        geoPhotoFile.write('"features": [')

        for count, imgpath in enumerate(photos):
            self.dlg.progressBar.setValue(int(count * self.total))

            with open(imgpath, 'rb') as imgpathF:
                tags = exifread.process_file(imgpathF, details=False)
            if not tags.keys() & {"GPS GPSLongitude", "GPS GPSLatitude"}:
                continue

            name = os.path.basename(imgpath)
            imgpath = imgpath.replace('\\', '/')
            lat, lon = self.get_exif_location(tags, "lonlat")
            try:
                altitude = str(float(tags["GPS GPSAltitude"].values[0].num) / float(tags["GPS GPSAltitude"].values[0].den))
            except:
                altitude = ''
            uuid_ = str(uuid.uuid4())

            try:
                dt1, dt2 = tags["Image DateTime"].values.split()
                date = dt1.replace(':', '/')
                time_ = dt2
            except:
                try:
                    date = tags["GPS GPSDate"].values.replace(':', '/')
                    tt = [str(i) for i in tags["GPS GPSTimeStamp"].values]
                    time_ = "{:0>2}:{:0>2}:{:0>2}".format(tt[0], tt[1], tt[2])
                except:
                    date = ''
                    time_ = ''

            try:
                azimuth = str(tags["GPS GPSImgDirection"].values[0])
            except:
                azimuth = ''
            try:
                north = str(tags["GPS GPSImgDirectionRef"].values)
            except:
                north = ''

            maker = ''
            model = ''
            try:
                maker = tags['Image Make']
                model = tags['Image Model']
            except:
                pass

            truePhotosCount = truePhotosCount + 1
            geoPhotoFile.write('''{ "type": "Feature", "properties": {  "ID": ''' + '"' + uuid_ + '"' + ', "Name": ' +
                               '"' + name + '"' + ', "Date": ' + '"' + date + '"' + ', "Time": ' + '"' + time_ + '"' +
                               ', "Lon": ' + '"' + str(lon) + '"' + ', "Lat": ' + '"' + str(lat) + '"' + ', "Altitude":'
                               ' ' + '"' + altitude + '"' + ', "North": ' + '"' + north + '"' + ', "Azimuth": ' + '"' +
                               azimuth + '"' + ', "Camera Maker": ' + '"' + str(maker) + '"' + ', "Camera Model": ' +
                               '"' + str(model) + '"' + ', "Path": ' + '"' + imgpath + '"'+ ',}, "geometry": { "type": '
                               '"Point",  "coordinates": ' + '[' + str(lon) + ',' + str(lat) + ']')

            geoPhotoFile.write('}\n }')
            geoPhotoFile.write(',\n')

        geoPhotoFile.write('\n]\n}\n')
        geoPhotoFile.close()

        if len(QgsProject.instance().mapLayersByName(lphoto)) == 0:
            self.layerPhotos = self.iface.addVectorLayer(self.outDirectoryPhotosShapefile, lphoto, "ogr")
        else:
            for x in self.iface.mapCanvas().layers():
                if x.name() == lphoto:
                    self.layerPhotos = x
        try:
            self.layerPhotos.loadNamedStyle(self.plugin_dir + "/svg/photos.qml")
        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setWindowTitle('Warning')
            msgBox.setText('No geo-tagged images were detected.')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()
            return
        try:
            self.layerPhotos.setReadOnly()
            self.layerPhotos.reload()
            self.layerPhotos.triggerRepaint()
        except:
            pass
        try:
            self.iface.mapCanvas().setExtent(QgsRectangle(lon, lat, lon, lat))
        except:
            pass
        self.dlg.progressBar.setValue(100)
        self.dlg.progressBar.setValue(0)
        ###########################################
        initphotos = len(photos)
        noLocationPhotosCounter = initphotos - truePhotosCount
        if truePhotosCount == noLocationPhotosCounter == 0 or truePhotosCount == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle('Import Photos')
            msgBox.setText('Import Completed.\n\nDetails:\n  No new photos were added.')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()
        elif (truePhotosCount == initphotos) or ((noLocationPhotosCounter + truePhotosCount) == initphotos):
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle('Import Photos')
            msgBox.setText(
                'Import Completed.\n\nDetails:\n  ' + str(truePhotosCount) + ' photo(s) added without error.\n  ' + str(
                    noLocationPhotosCounter) + ' photo(s) skipped (because of missing location).')
            msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
            msgBox.exec_()

        self.dlg.ok.setEnabled(True)
        self.dlg.closebutton.setEnabled(True)
        self.dlg.toolButtonImport.setEnabled(True)
        self.dlg.toolButtonOut.setEnabled(True)
        self.clickPhotos.setChecked(True)

    def refresh(self):  # Deselect features
        mc = self.iface.mapCanvas()
        for layer in mc.layers():
            if layer.type() == layer.VectorLayer:
                layer.removeSelection()
        mc.refresh()



######################################################
# based on http://www.codegists.com/snippet/python/exif_gpspy_snakeye_python

    def _get_if_exist(self, data, key):
        if key in data:
            return data[key]

        return None


    def _convert_to_degress(self, value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format

        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)


    def get_exif_location(self, exif_data, lonlat):
        """
        Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
        """

        if lonlat=='lonlat':
            lat = ''
            lon = ''
            gps_latitude = self._get_if_exist(exif_data, 'GPS GPSLatitude')
            gps_latitude_ref = self._get_if_exist(exif_data, 'GPS GPSLatitudeRef')
            gps_longitude = self._get_if_exist(exif_data, 'GPS GPSLongitude')
            gps_longitude_ref = self._get_if_exist(exif_data, 'GPS GPSLongitudeRef')

            if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
                lat = self._convert_to_degress(gps_latitude)
                if gps_latitude_ref.values[0] != 'N':
                    lat = 0 - lat

                lon = self._convert_to_degress(gps_longitude)
                if gps_longitude_ref.values[0] != 'E':
                    lon = 0 - lon

            return lat, lon
