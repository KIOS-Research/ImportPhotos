# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos jpegs
                              -------------------
        begin                : 2018-02-20
        git sha              : $Format:%H$
        copyright            : (C) 2018 by KIOS Research Center
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

from qgis.PyQt.QtWidgets import (QAction, QFileDialog, QMessageBox)
from qgis.PyQt.QtGui import (QIcon)
from qgis.PyQt.QtCore import (QSettings, QTranslator, qVersion, QCoreApplication, Qt, QVariant)
from qgis.core import (QgsRectangle, QgsVectorFileWriter, QgsCoordinateReferenceSystem, QgsVectorLayer, \
                       QgsLayerTreeLayer, QgsProject, QgsTask, QgsApplication, QgsMessageLog, QgsFields, QgsField,
                       QgsWkbTypes, QgsFeature, QgsPointXY, QgsGeometry)
from qgis.utils import Qgis

# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .ImportPhotos_dialog import ImportPhotosDialog
from .MouseClick import MouseClick
import os.path
import platform
import uuid
import json

# Import python module
CHECK_MODULE = ''
try:
    import exifread
    CHECK_MODULE = 'exifread'
except:
    pass

try:
    if CHECK_MODULE == '':
        from PIL import Image
        from PIL.ExifTags import TAGS
        CHECK_MODULE = 'PIL'
except:
    pass


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
        #self.dlg.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)

        self.dlg.ok.clicked.connect(self.ok)
        self.dlg.closebutton.clicked.connect(self.close)
        self.dlg.toolButtonImport.clicked.connect(self.toolButtonImport)
        self.dlg.toolButtonOut.clicked.connect(self.toolButtonOut)
        self.dlg.input_load_style.clicked.connect(self.loadstyle)

        self.clickPhotos.setCheckable(True)
        self.clickPhotos.setEnabled(True)

        self.listPhotos = []
        self.layernamePhotos = []
        self.canvas = self.iface.mapCanvas()
        self.toolMouseClick = MouseClick(self.canvas, self)

        self.fields = ['ID', 'Name', 'Date', 'Time', 'Lon', 'Lat', 'Altitude', 'North', 'Azimuth', 'Camera Maker',
                       'Camera Model', 'Title', 'Comment', 'Path', 'RelPath', 'Timestamp']

        self.extension_switch = {
            ".shp": "ESRI Shapefile",
            ".geojson": "GeoJSON",
            ".gpkg":"GPKG",
            ".csv": "CSV",
            ".kml": "KML",
            ".tab": "MapInfo File"
        }

        self.extension_switch2 = {
            "ESRI Shapefile (*.shp *.SHP)": ".shp",
            "GeoJSON (*.geojson *.GEOJSON)": ".geojson",
            "GeoPackage (*.gpkg *.GPKG)":".gpkg",
            "Comma Separated Value (*.csv *.CSV)": ".csv",
            "Keyhole Markup Language (*.kml *.KML)": ".kml",
            "Mapinfo TAB (*.tab *.TAB)": ".tab"
        }

        self.extension_switch_types = {
            ".shp": "ESRI Shapefile",
            ".geojson": "GeoJSON",
            ".gpkg":"GPKG",
            ".csv": "CSV",
            ".kml": "KML",
            ".tab": "MapInfo File"
        }

    def mouseClick(self):
        try:
            self.iface.setActiveLayer(self.canvas.layers()[0])
        except:
            pass
        self.canvas.setMapTool(self.toolMouseClick)
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
        self.dlg.input_load_style.setEnabled(True)
        self.clickPhotos.setEnabled(True)
        self.dlg.out.setText('')
        self.dlg.imp.setText('')
        self.dlg.load_style_path.setText('')
        self.dlg.show()

    def close(self):
        self.dlg.close()

    def toolButtonOut(self):
        typefiles = 'ESRI Shapefile (*.shp *.SHP);; GeoJSON (*.geojson *.GEOJSON);; GeoPackage (*.gpkg *.GPKG);; Comma Separated Value (*.csv *.CSV);; Keyhole Markup Language (*.kml *.KML);; Mapinfo TAB (*.tab *.TAB)'
        if platform.system() == 'Linux':
            try:
                self.outputPath, self.extension = QFileDialog.getSaveFileNameAndFilter(None, 'Save File', os.path.join(
                    os.path.join(os.path.expanduser('~')),
                    'Desktop'), typefiles)
            except:
                self.outputPath = QFileDialog.getSaveFileName(None, 'Save File', os.path.join(
                    os.path.join(os.path.expanduser('~')),
                    'Desktop'), typefiles) #hack line
        else:
            self.outputPath = QFileDialog.getSaveFileName(None, 'Save File', os.path.join(
                os.path.join(os.path.expanduser('~')),
                'Desktop'), typefiles)

        self.extension_type = self.outputPath[1]
        self.outputPath = self.outputPath[0]
        if self.extension_type:
            self.extension2 = self.extension_switch2[self.extension_type]

        self.dlg.out.setText(self.outputPath)

    def toolButtonImport(self):
        self.directoryPhotos = QFileDialog.getExistingDirectory(None, 'Select a folder:',
                                                                os.path.join(os.path.join(os.path.expanduser('~')),
                                                                             'Desktop'), QFileDialog.ShowDirsOnly)
        self.selected_folder = self.directoryPhotos[:]; p = '/'
        if '/' in self.selected_folder:
            self.selected_folder = self.selected_folder.split('/')[-1]; p = '/'
        if '\\' in self.selected_folder:
            self.selected_folder = self.selected_folder.split('\\')[-1]; p = '\\'
        if '//' in self.selected_folder:
            self.selected_folder = self.selected_folder.split('//')[-1]; p = '//'
        self.selected_folder = './' + self.selected_folder + p

        self.dlg.imp.setText(self.directoryPhotos)

    def loadstyle(self):
        self.load_style = QFileDialog.getOpenFileName(None, "Load style",
                                               os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop'),
                                               "(*.qml)")
        if self.load_style[0] == "":
            return
        else:
            self.load_style = self.load_style[0]

        self.dlg.load_style_path.setText(self.load_style)

    def selectDir(self):
        title = 'Warning'
        msg = 'Please select a directory photos.'
        self.showMessage(title, msg, 'Warning')
        return True

    def selectOutp(self):
        title = 'Warning'
        msg = 'Please define output file location.'
        self.showMessage(title, msg, 'Warning')
        return True

    def noImageFound(self):
        title = 'Warning'
        msg = 'No image path found.'
        self.showMessage(title, msg, 'Warning')
        return True

    def ok(self):
        if self.dlg.imp.text() == '':
            if self.selectDir():
                return
        if not os.path.isdir(self.dlg.imp.text()):
            if self.selectDir():
                return
        if self.dlg.out.text() == '':
            if self.selectOutp():
                return
        if not os.path.isabs(self.dlg.out.text()):
            if self.selectOutp():
                return

        self.outputPath = self.dlg.out.text()
        self.directoryPhotos = self.dlg.imp.text()

        if self.dlg.input_load_style.text() == '':
            self.load_style = os.path.join(self.plugin_dir, "svg", "photos.qml")
        else:
            self.load_style = self.dlg.load_style_path.text()

        if self.load_style != '':
            if not os.path.exists(self.load_style):
                title = 'Warning'
                msg = 'No style path found.'
                self.showMessage(title, msg, 'Warning')
                return

        showMessageHide = True
        self.import_photos(self.directoryPhotos, self.outputPath, self.load_style, showMessageHide)

    def import_photos(self, directoryPhotos, outputPath, load_style, showMessageHide=True):

        if load_style == '':
            self.load_style = os.path.join(self.plugin_dir, "svg", "photos.qml")
        else:
            self.load_style = load_style
        self.showMessageHide = showMessageHide
        self.outputPath = outputPath
        self.directoryPhotos = directoryPhotos

        if platform.system() == 'Linux':
            self.lphoto = os.path.basename(self.outputPath)
            try:
                self.extension = '.'+self.extension.split()[-1][2:-1].lower()
            except:
                self.extension = '.shp' #hack line, temporary
        else:
            _ , self.extension = os.path.splitext(self.outputPath)
            basename = os.path.basename(self.outputPath)
            self.lphoto = basename[:-len(self.extension)]

        self.outDirectoryPhotosGeoJSON = os.path.join(self.plugin_dir, 'tmp.geojson')

        self.dlg.ok.setEnabled(False)
        self.dlg.closebutton.setEnabled(False)
        self.dlg.toolButtonImport.setEnabled(False)
        self.dlg.toolButtonOut.setEnabled(False)
        self.dlg.input_load_style.setEnabled(False)

        # get paths of photos
        extens = ['jpg', 'jpeg', 'JPG', 'JPEG']
        self.photos = []
        self.photos_names = []
        for root, dirs, files in os.walk(self.directoryPhotos):
            for name in files:
                if name.lower().endswith(tuple(extens)):
                    self.photos.append(os.path.join(root, name))
                    self.photos_names.append(name)

        self.initphotos = len(self.photos)

        if self.initphotos == 0 and self.showMessageHide:
            title = 'Warning'
            msg = 'No photos.'
            self.showMessage(title, msg, 'Warning')
            self.dlg.ok.setEnabled(True)
            self.dlg.closebutton.setEnabled(True)
            self.dlg.toolButtonImport.setEnabled(True)
            self.dlg.toolButtonOut.setEnabled(True)
            self.dlg.input_load_style.setEnabled(True)
            self.clickPhotos.setChecked(True)
            return

        self.canvas.setMapTool(self.toolMouseClick)

        self.truePhotosCount = 0

        self.Qpr_inst = QgsProject.instance()
        if platform.system()=='Darwin':
            self.layernamePhotos.append(self.lphoto+' OGRGeoJSON Point')
        else:
            self.layernamePhotos.append(self.lphoto)

        if platform.system() == 'Linux':
            self.outputPath = self.outputPath + self.extension
            self.extension = self.extension_switch[self.extension]
        else:
            self.extension = self.extension_switch[self.extension.lower()]

        self.exifread_module = False
        self.pil_module = False

        if CHECK_MODULE == '' and self.showMessageHide:
            self.showMessage('Python Modules', 'Please install python module "exifread" or "PIL".' , 'Warning')

        #self.import_photos_task('', '')
        self.call_import_photos()
        self.dlg.close()

    def refresh(self):  # Deselect features
        mc = self.canvas
        for layer in mc.layers():
            if layer.type() == layer.VectorLayer:
                layer.removeSelection()
        mc.refresh()

    def showMessage(self, title, msg, icon):
        if icon == 'Warning':
            icon = QMessageBox.Warning
        elif icon == 'Information':
            icon = QMessageBox.Information

        msgBox = QMessageBox()
        msgBox.setIcon(icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(msg)
        msgBox.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        msgBox.exec_()

    def completed(self, exception, result=None):
        geojson = {"type": "FeatureCollection",
                   "name": self.lphoto,
                   "crs": {"type": "name", "properties": {"name": "crs:OGC:1.3:CRS84"}},
                   "features": self.geoPhotos}

        geofile = open(self.plugin_dir + '/tmp.geojson', 'w')
        json.dump(geojson, geofile)
        geofile.close()
        del self.geoPhotos, geojson

        try:
            for layer in self.canvas.layers():
                if layer.publicSource() == self.outputPath:
                    self.Qpr_inst.instance().removeMapLayer(layer.id())
                    os.remove(self.outputPath)
        except:
            pass

        self.layerPhotos = QgsVectorLayer(self.outDirectoryPhotosGeoJSON, self.lphoto, "ogr")
        QgsVectorFileWriter.writeAsVectorFormat(self.layerPhotos, self.outputPath, "utf-8",
                                                    QgsCoordinateReferenceSystem(self.layerPhotos.crs().authid()),
                                                    self.extension)
        self.layerPhotos_final = QgsVectorLayer(self.outputPath, self.lphoto, "ogr")

        # clear temp.geojson file
        try:
            f = open(self.outDirectoryPhotosGeoJSON, 'r+')
            f.truncate(0)  # need '0' when using r+
        except:
            pass

        try:
            self.layerPhotos_final.loadNamedStyle(self.load_style)
        except:
            title = 'Warning'
            msg = 'No geo-tagged images were detected.'
            self.showMessage(title, msg, 'Warning')
            self.taskPhotos.destroyed()
            return

        self.layerPhotos_final.setReadOnly(False)
        self.layerPhotos_final.reload()
        self.layerPhotos_final.triggerRepaint()

        try:
            xmin = min(self.lon)
            ymin = min(self.lat)
            xmax = max(self.lon)
            ymax = max(self.lat)
            self.canvas.zoomToSelected(self.layerPhotos_final)
            self.canvas.setExtent(QgsRectangle(xmin, ymin, xmax, ymax))
        except:
            pass

        ###########################################
        self.dlg.ok.setEnabled(True)
        self.dlg.closebutton.setEnabled(True)
        self.dlg.toolButtonImport.setEnabled(True)
        self.dlg.toolButtonOut.setEnabled(True)
        self.dlg.input_load_style.setEnabled(True)
        self.clickPhotos.setChecked(True)

        noLocationPhotosCounter = self.initphotos - self.truePhotosCount
        if (self.truePhotosCount == noLocationPhotosCounter == 0 or self.truePhotosCount == 0 ) and self.showMessageHide:
            title = 'Import Photos'
            msg = 'Import Completed.\n\nDetails:\n  No new photos were added.'
            self.showMessage(title, msg, 'Information')
            self.taskPhotos.destroyed()
            return
        elif ((self.truePhotosCount == self.initphotos) or ((noLocationPhotosCounter + self.truePhotosCount) == self.initphotos) )and self.showMessageHide:
            title = 'Import Photos'
            msg = 'Import Completed.\n\nDetails:\n  ' + str(
                int(self.truePhotosCount)) + ' photo(s) added without error.\n  ' + str(
                int(noLocationPhotosCounter)) + ' photo(s) skipped (because of missing location).'
            self.showMessage(title, msg, 'Information')

        g = self.Qpr_inst.layerTreeRoot().insertGroup(0, self.lphoto)
        self.Qpr_inst.addMapLayer(self.layerPhotos_final, False)
        nn = QgsLayerTreeLayer(self.layerPhotos_final)
        g.insertChildNode(0, nn)

    def stopped(self, task):
        QgsMessageLog.logMessage(
            'Task "{name}" was canceled'.format(
                name=task.description()),
            'ImportPhotos', Qgis.Info)

    def import_photos_task(self, task, wait_time):
        self.geoPhotos = []
        self.lon = []
        self.lat = []
        for count, imgpath in enumerate(self.photos):
            try:
                name = os.path.basename(imgpath)
                RelPath = self.selected_folder + self.photos_names[count]
                if CHECK_MODULE == 'exifread' and not self.pil_module:
                    self.exifread_module = True
                    self.taskPhotos.setProgress(count/self.initphotos)
                    with open(imgpath, 'rb') as imgpathF:
                        tags = exifread.process_file(imgpathF, details=False)
                    if not tags.keys() & {"GPS GPSLongitude", "GPS GPSLatitude"}:
                        continue

                    lat, lon = self.get_exif_location(tags, "lonlat")
                    if 'GPS GPSAltitude' in tags:
                        altitude = float(tags["GPS GPSAltitude"].values[0].num) / float(
                            tags["GPS GPSAltitude"].values[0].den)
                    else:
                        altitude = ''
                    uuid_ = str(uuid.uuid4())

                    try:
                        dt1, dt2 = tags["EXIF DateTimeOriginal"].values.split()
                        date = dt1.replace(':', '/')
                        time_ = dt2
                        timestamp = dt1.replace(':', '-') + 'T' + time_
                    except:
                        try:
                            date = tags["GPS GPSDate"].values.replace(':', '/')
                            tt = [str(i) for i in tags["GPS GPSTimeStamp"].values]
                            time_ = "{:0>2}:{:0>2}:{:0>2}".format(tt[0], tt[1], tt[2])
                            timestamp = tags["GPS GPSDate"].values.replace(':', '-') + 'T' + time_
                        except:
                            date = ''
                            time_ = ''
                            timestamp = ''

                    if 'GPS GPSImgDirection' in tags:
                        azimuth = float(tags["GPS GPSImgDirection"].values[0].num) / float(
                            tags["GPS GPSImgDirection"].values[0].den)
                    else:
                        azimuth = ''

                    if 'GPS GPSImgDirectionRef' in tags:
                        north = str(tags["GPS GPSImgDirectionRef"].values)
                    else:
                        north = ''

                    if 'Image Make' in tags:
                        maker = tags['Image Make']
                    else:
                        maker = ''

                    if 'Image Model' in tags:
                        model = tags['Image Model']
                    else:
                        model = ''

                    if 'Image ImageDescription' in tags:
                        title = tags['Image ImageDescription']
                    else:
                        title = ''

                    if 'EXIF UserComment' in tags:
                        user_comm = tags['EXIF UserComment'].printable
                    else:
                        user_comm = ''

                if CHECK_MODULE == 'PIL' and not self.exifread_module:
                    self.pil_module = True
                    a = {}
                    info = Image.open(imgpath)
                    info = info._getexif()

                    if info == None:
                        continue

                    for tag, value in info.items():
                        if TAGS.get(tag, tag) == 'GPSInfo' or TAGS.get(tag, tag) == 'DateTime' or TAGS.get(tag,
                                                                                                           tag) == 'DateTimeOriginal':
                            a[TAGS.get(tag, tag)] = value

                    if a == {}:
                        continue

                    if a['GPSInfo'] != {}:
                        if 1 and 2 and 3 and 4 in a['GPSInfo']:
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
                        else:
                            continue

                        uuid_ = str(uuid.uuid4())
                        if 'DateTime' or 'DateTimeOriginal' in a:
                            if 'DateTime' in a:
                                dt1, dt2 = a['DateTime'].split()
                            if 'DateTimeOriginal' in a:
                                dt1, dt2 = a['DateTimeOriginal'].split()
                            date = dt1.replace(':', '/')
                            time_ = dt2
                            timestamp = dt1.replace(':', '-') + 'T' + time_

                        if 6 in a['GPSInfo']:
                            if len(a['GPSInfo'][6]) > 1:
                                mAltitude = float(a['GPSInfo'][6][0])
                                mAltitudeDec = float(a['GPSInfo'][6][1])
                                altitude = mAltitude / mAltitudeDec
                        else:
                            altitude = ''

                        if 16 and 17 in a['GPSInfo']:
                            north = str(a['GPSInfo'][16])
                            azimuth = float(a['GPSInfo'][17][0]) / float(a['GPSInfo'][17][1])
                        else:
                            north = ''
                            azimuth = ''

                        maker = ''
                        model = ''
                        user_comm = ''
                        title = ''
                self.lon.append(lon)
                self.lat.append(lat)
                self.truePhotosCount = self.truePhotosCount + 1

                geo_info = {"type": "Feature",
                            "properties": {'ID': uuid_, 'Name': name, 'Date': date, 'Time': time_,
                                           'Lon': lon,
                                           'Lat': lat, 'Altitude': altitude, 'North': north,
                                           'Azimuth': azimuth,
                                           'Camera Maker': str(maker), 'Camera Model': str(model), 'Title': str(title),
                                           'Comment': user_comm,'Path': imgpath, 'RelPath': RelPath,
                                           'Timestamp': timestamp},
                            "geometry": {"coordinates": [lon, lat], "type": "Point"}}
                self.geoPhotos.append(geo_info)

                if self.taskPhotos.isCanceled():
                    self.stopped(self.taskPhotos)
                    self.taskPhotos.destroyed()
                    return None
            except:
                pass
        return True

    def call_import_photos(self):
        self.taskPhotos = QgsTask.fromFunction(u'ImportPhotos', self.import_photos_task,
                                 on_finished=self.completed, wait_time=4)
        QgsApplication.taskManager().addTask(self.taskPhotos)

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
