# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos
        last update          : 04/01/2023
        begin                : February 2018
        copyright            : (C) 2019 by KIOS Research Center
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

from qgis.PyQt.QtWidgets import QAction, QFileDialog, QMessageBox, QInputDialog, QLabel
from qgis.PyQt.QtGui import QIcon, QGuiApplication
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt, QTextCodec
from qgis.core import *
from qgis.gui import QgsRuleBasedRendererWidget

# Initialize Qt resources from file resources.py
from . import resources
# Import the code for the dialog
from .code.MouseClick import MouseClick
import os
import uuid
import json

# Import python module
CHECK_MODULE = ''
try:
    import exifread

    CHECK_MODULE = 'exifread'
except:
    try:
        subprocess.call(['pip', 'install', 'exifread'])
        CHECK_MODULE = ''
    except ModuleNotFoundError:
        pass
try:
    if CHECK_MODULE == '':
        from PIL import Image
        from PIL.ExifTags import TAGS
        CHECK_MODULE = 'PIL'
except:
    try:
        subprocess.call(['pip', 'install', 'pillow'])
        CHECK_MODULE = ''
    except ModuleNotFoundError:
        pass

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui/impphotos.ui'))

FIELDS = ['fid', 'ID', 'Name', 'Date', 'Time', 'Lon', 'Lat', 'Altitude', 'North', 'Azimuth', 'Cam. Maker',
          'Cam. Model', 'Title', 'Comment', 'Path', 'RelPath', 'Timestamp', 'Images']

SUPPORTED_PHOTOS_EXTENSIONS = ['jpg', 'jpeg', 'JPG', 'JPEG']

SUPPORTED_OUTPUT_FILE_EXTENSIONS = {
    "GeoPackage (*.gpkg *.GPKG)": ".gpkg",
    "ESRI Shapefile (*.shp *.SHP)": ".shp",
    "GeoJSON (*.geojson *.GEOJSON)": ".geojson",
    "Comma Separated Value (*.csv *.CSV)": ".csv",
    "Keyhole Markup Language (*.kml *.KML)": ".kml",
    "Mapinfo TAB (*.tab *.TAB)": ".tab"
}

EXTENSION_DRIVERS = {
    ".gpkg": "GPKG",
    ".shp": "ESRI Shapefile",
    ".geojson": "GeoJSON",
    ".csv": "CSV",
    ".kml": "KML",
    ".tab": "MapInfo File"
}

CODEC = QTextCodec.codecForName("UTF-8")


# Import ui file
class ImportPhotosDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        # """Constructor."""
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        super(ImportPhotosDialog, self).__init__(parent)
        self.setupUi(self)


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
        self.canvas = self.iface.mapCanvas()
        self.project_instance = QgsProject.instance()
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

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr('&ImportPhotos')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar('ImportPhotos')
        self.toolbar.setObjectName('ImportPhotos')
        # Renderer that will be set after the import process
        self.layer_renderer = None

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
            checkable=False,
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
        if checkable:
            action.setCheckable(checkable)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = ':/plugins/ImportPhotos/icons/ImportImage.svg'
        self.add_action(
            icon_path,
            text=self.tr('Import Photos'),
            callback=self.run,
            parent=self.iface.mainWindow())
        icon_path = ':/plugins/ImportPhotos/icons/SelectImage.svg'
        self.clickPhotos = self.add_action(
            icon_path,
            checkable=True,
            text=self.tr('Click Photos'),
            callback=self.setMouseClickMapTool,
            parent=self.iface.mainWindow())
        icon_path = ':/plugins/ImportPhotos/icons/sync_views.svg'
        self.add_action(
            icon_path,
            text=self.tr('Update Photos'),
            callback=self.update_photos,
            parent=self.iface.mainWindow())

        self.dlg = ImportPhotosDialog()
        self.dlg.ok.clicked.connect(self.import_photos)
        self.dlg.closebutton.clicked.connect(self.dlg.close)
        self.dlg.toolButtonImport.clicked.connect(self.toolButtonImport)
        self.dlg.toolButtonOut.clicked.connect(self.toolButtonOut)

        # Add QgsRuleBasedRendererWidget
        # temp_layer is a class variable because we need to keep its reference
        # so the RendererWidget does not crash QGIS
        # If it's not a class variable, then it goes out of scope after this method
        # and as mentioned, QGIS crashes because it tries to access it.
        self.temp_layer = QgsVectorLayer(
            'Point?crs=epsg:4326&field=ID:string&field=Name:string&field=Date:date&field=Time:text&field=Lon:double&field=Lat:double&field=Altitude:double&field=Cam.Mak:string&field=Cam.Mod:string&field=Title:string&field=Comment:string&field=Path:string&field=RelPath:string&field=Timestamp:string&field=Images:string',
            'temp_layer',
            'memory')
        self.temp_layer.setRenderer(QgsFeatureRenderer.defaultRenderer(QgsWkbTypes.PointGeometry))
        self.temp_layer.loadNamedStyle(os.path.join(self.plugin_dir, 'icons', "photos.qml"))
        renderer_widget = QgsRuleBasedRendererWidget(
            self.temp_layer, QgsStyle.defaultStyle(),
            self.temp_layer.renderer())
        renderer_widget.setObjectName("renderer_widget")
        self.dlg.gridLayout.addWidget(QLabel("Output layer style"), 4, 0)
        self.dlg.gridLayout.addWidget(renderer_widget, 4, 2)

        self.toolMouseClick = MouseClick(self.canvas, self)

    def setMouseClickMapTool(self):

        # Set photos layer as active layer
        for layer in self.project_instance.mapLayers().values():
            if layer.type() == QgsMapLayerType.VectorLayer and layer.fields().names() == FIELDS:
                self.iface.setActiveLayer(layer)
                break

        self.canvas.setMapTool(self.toolMouseClick)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr('&ImportPhotos'),
                action)
            self.iface.removeToolBarIcon(action)
            # remove the toolbar
        del self.toolbar

    def run(self):
        if CHECK_MODULE == '':
            self.showMessage(
                self.tr('Python Modules'),
                self.tr('Please install python module "exifread" or "PIL".'),
                'Warning')
            return

        self.dlg.out.setText('')
        self.dlg.imp.setText('')
        self.dlg.canvas_extent.setChecked(False)
        self.dlg.show()

    def toolButtonOut(self):

        outputPath, selected_extension_filter = QFileDialog.getSaveFileName(
            self.dlg,
            self.tr("Save output layer"), os.path.expanduser('~'),
            ";;".join(list(SUPPORTED_OUTPUT_FILE_EXTENSIONS.keys())))

        if outputPath:
            extension = SUPPORTED_OUTPUT_FILE_EXTENSIONS[selected_extension_filter]
            if os.path.splitext(outputPath)[1] == '':
                # Add extension to filepath if user did not specify it
                self.dlg.out.setText(outputPath + extension)
            else:
                # Set extension with the specified filter
                self.dlg.out.setText(os.path.splitext(outputPath)[0] + extension)

    def toolButtonImport(self):
        directory_path = QFileDialog.getExistingDirectory(
            self.dlg, self.tr('Select a folder:'),
            os.path.expanduser('~'), QFileDialog.ShowDirsOnly)

        if directory_path:
            self.selected_folder = directory_path[:]
            self.selected_folder = './' + os.path.basename(os.path.normpath(self.selected_folder)) + '/'
            self.dlg.imp.setText(directory_path)

    def import_photos(self):
        self.layer_renderer = self.dlg.findChild(QgsRuleBasedRendererWidget, "renderer_widget").renderer()

        file_not_found = False
        if self.dlg.imp.text() == '' and not os.path.isdir(self.dlg.imp.text()):
            file_not_found = True
            msg = self.tr('Please select a directory photos.')
        if self.dlg.out.text() == '' and not os.path.isabs(self.dlg.out.text()):
            file_not_found = True
            msg = self.tr('Please define output file location.')

        if file_not_found:
            self.showMessage('Warning', msg, 'Warning')
            return

        # get paths of photos
        self.photos_to_import = []
        for root, dirs, files in os.walk(self.dlg.imp.text()):
            for filename in files:
                if filename.lower().endswith(tuple(SUPPORTED_PHOTOS_EXTENSIONS)):
                    self.photos_to_import.append(os.path.join(root, filename))

        if len(self.photos_to_import) == 0:
            self.showMessage('Warning', self.tr('No photos were found!'), 'Warning')
            return

        self.dlg.close()
        self.call_import_photos()
        # QGuiApplication.setOverrideCursor(Qt.WaitCursor)
        # photos_to_import.sort()
        # try:
        #     result = self.import_photos_task(photos_to_import)
        #     self.completed(result)
        # except Exception as e:
        #     self.showMessage(self.tr('Unexpected Error'), str(e), 'Warning')
        #     QGuiApplication.restoreOverrideCursor()

    def call_import_photos(self):
        # self.import_photos_task('', '')
        # self.completed('')
        self.taskPhotos = QgsTask.fromFunction('ImportPhotos', self.import_photos_task,
                                               on_finished=self.completed, wait_time=4)
        QgsApplication.taskManager().addTask(self.taskPhotos)

    def stopped(self, task):
        QgsMessageLog.logMessage(
            'Task "{name}" was canceled'.format(
                name=task.description()),
            'ImportPhotos', Qgis.Info)

    def import_photos_task(self, task, wait_time):
        self.temp_photos_layer = self.project_instance.addMapLayer(
            QgsVectorLayer("Point?crs=epsg:4326", None, "memory"), False)

        imported_photos_counter = 0
        out_of_bounds_photos_counter = 0
        no_location_photos_counter = 0
        editing_started = self.temp_photos_layer.startEditing()

        self.photos = []
        self.photos_names = []
        for root, dirs, files in os.walk(self.selected_folder):
            for name in files:
                if name.lower().endswith(tuple(SUPPORTED_PHOTOS_EXTENSIONS)):
                    self.photos.append(os.path.join(root, name))

        self.initphotos = len(self.photos)
        if editing_started:
            # Import new pictures
            attribute_fields_set = False

            for count, photo_path in enumerate(self.photos_to_import):
                try:
                    if not os.path.isdir(photo_path) and photo_path.lower().endswith(
                            tuple(SUPPORTED_PHOTOS_EXTENSIONS)):
                        geo_info = self.get_geo_infos_from_photo(photo_path)
                        if geo_info and geo_info["properties"]["Lat"] and geo_info["properties"]["Lon"]:
                            geo_info = json.dumps(geo_info)
                            fields = QgsJsonUtils.stringToFields(geo_info, CODEC)

                            if not attribute_fields_set:
                                attribute_fields_set = True
                                for field in fields.toList():
                                    self.temp_photos_layer.addAttribute(field)

                            feature = QgsJsonUtils.stringToFeatureList(
                                geo_info, fields, CODEC)[0]

                            self.temp_photos_layer.addFeature(feature)
                            imported_photos_counter += 1
                        elif geo_info == 'out':
                            out_of_bounds_photos_counter += 1
                        elif geo_info is False:
                            no_location_photos_counter += 1
                except:
                    pass

        if not editing_started or not self.temp_photos_layer.commitChanges():
            self.project_instance.removeMapLayer(self.temp_photos_layer)
            title = self.tr('Import Photos')
            msg = "{}\n\n{} {}".format(
                self.tr("Import Failed."),
                self.tr("Details:"),
                "\n".join(self.temp_photos_layer.commitErrors()))
            self.showMessage(title, msg, 'Warning')
            self.result = False, len(
                self.photos_to_import), imported_photos_counter, out_of_bounds_photos_counter, no_location_photos_counter

        # Save vector layer as a Shapefile
        driver = EXTENSION_DRIVERS[os.path.splitext(self.dlg.out.text())[1]]
        error_code, error_message = QgsVectorFileWriter.writeAsVectorFormat(
            self.temp_photos_layer, self.dlg.out.text(), "utf-8",
            QgsCoordinateReferenceSystem(self.temp_photos_layer.crs().authid()),
            driver)

        if error_code != 0:
            self.project_instance.removeMapLayer(self.temp_photos_layer)
            self.showMessage(self.tr('Writing output file error'), error_message, 'Warning')
            return False, len(
                self.photos_to_import), imported_photos_counter, out_of_bounds_photos_counter, no_location_photos_counter

        self.project_instance.removeMapLayer(self.temp_photos_layer)
        self.setMouseClickMapTool()

        self.result = True, len(
            self.photos_to_import), imported_photos_counter, out_of_bounds_photos_counter, no_location_photos_counter

    def completed(self, result):

        import_ok, photos_to_import_number, imported_photos_counter, out_of_bounds_photos_counter, no_location_photos_counter = self.result
        no_location_photos_counter = no_location_photos_counter + photos_to_import_number - imported_photos_counter - out_of_bounds_photos_counter

        if import_ok:
            if imported_photos_counter == 0:
                title = self.tr('ImportPhotos')
                msg = '{}\n\n{}\n  {}'.format(
                    self.tr('Import Completed.'),
                    self.tr('Details:'),
                    self.tr('No new photos were added.'))
            else:
                title = self.tr('ImportPhotos')
                msg = '{}\n\n{}\n  {} {}\n  {} {}\n  {} {}\n'.format(
                    self.tr('Import Completed.'),
                    self.tr('Details:'),
                    str(int(imported_photos_counter)),
                    self.tr('photo(s) added without error.'),
                    str(int(no_location_photos_counter)),
                    self.tr('photo(s) skipped (because of missing location).'),
                    str(int(out_of_bounds_photos_counter)),
                    self.tr('photo(s) skipped (because not in canvas extent).'))
            self.showMessage(title, msg, self.tr('Information'))

        self.layerPhotos_final = QgsVectorLayer(
            self.dlg.out.text(),
            os.path.basename(self.dlg.out.text()).split(".")[0],
            "ogr")

        self.layerPhotos_final.setReadOnly(False)
        self.layerPhotos_final.setRenderer(self.layer_renderer.clone())
        self.layerPhotos_final.reload()
        self.layerPhotos_final.triggerRepaint()
        self.project_instance.addMapLayer(self.layerPhotos_final)

        expression = """
            <table>
                <tr>
                    <th>[% Name %]</th>
                </tr> 
                <tr>
                <th><img src="file:///[% Path %]" width="350" height="250"></th>
                </tr>
            </table>
        """
        self.layerPhotos_final.setMapTipTemplate(expression)

    def update_photos(self):
        layers = {}

        for layer in self.project_instance.mapLayers().values():
            if layer.type() == QgsMapLayerType.VectorLayer and all(
                    field in layer.fields().names() for field in FIELDS):
                layers[layer.name()] = layer

        if layers.keys():
            selected_layer_name, ok = QInputDialog.getItem(
                self.iface.mainWindow(),
                self.tr("Select layer to update"),
                "Layer List:", layers.keys(), 0, False)
        else:
            self.showMessage('Error', self.tr('No photos layer(s) found'), 'Warning')
            return

        if not ok:
            return
        self.selected_layer = layers[selected_layer_name]

        # All picture paths that are currently saved in the shapefile layer
        picture_paths = []
        # Path of the parent directory where the pictures are saved in
        base_picture_directory = ""
        # Feature fields
        basic_feature_fields = None

        for feature in self.selected_layer.getFeatures():
            if not base_picture_directory:
                base_picture_directory = os.path.dirname(feature.attribute("Path"))
                basic_feature_fields = feature.fields()
            picture_paths.append(os.path.basename(feature.attribute("Path")))

        # Pictures that should be removed from the layer
        self.selected_folder = './' + os.path.basename(os.path.normpath(base_picture_directory)) + '/'
        list_pictures = []
        try:
            for root, dirs, files in os.walk(base_picture_directory):
                for name in files:
                    if name.lower().endswith(tuple(SUPPORTED_PHOTOS_EXTENSIONS)):
                        list_pictures.append(name)
        except:
            pass

        pictures_to_remove = list(set(picture_paths) - set(list_pictures))
        pictures_to_add = list(set(list_pictures) - set(picture_paths))

        editing_started = self.selected_layer.startEditing()
        if editing_started:

            try:
                # Remove pictures that do not exist anymore in base_picture_directory
                for feature in self.selected_layer.getFeatures():
                    if os.path.basename(feature.attribute("Path")) in pictures_to_remove:
                        self.selected_layer.deleteFeature(feature.id())

                # Import new pictures
                imported_pictures_counter = 0
                out_of_bounds_photos_counter = 0
                photos_to_import_counter = 0
                no_location_photos_counter = 0
                if self.selected_layer.source().lower().endswith("gpkg"):
                    idx = self.selected_layer.dataProvider().fieldNameIndex('fid')
                    counter = self.selected_layer.maximumValue(idx)
                for picture_path in pictures_to_add:
                    if picture_path.lower().endswith(tuple(SUPPORTED_PHOTOS_EXTENSIONS)):
                        photos_to_import_counter += 1
                        geo_info = self.get_geo_infos_from_photo(os.path.join(base_picture_directory, picture_path))
                        if geo_info and geo_info["properties"]["Lat"] and geo_info["properties"]["Lon"]:
                            # QGIS automatically adds the fid attribute when saving the photos layer
                            if self.selected_layer.source().lower().endswith("gpkg"):
                                geo_info["properties"]["fid"] = counter + 1
                                counter += 1
                            self.selected_layer.addFeatures(
                                QgsJsonUtils.stringToFeatureList(
                                    json.dumps(geo_info), basic_feature_fields, CODEC))
                            imported_pictures_counter += 1
                        elif geo_info == 'out':
                            out_of_bounds_photos_counter += 1
                        elif geo_info is False:
                            no_location_photos_counter += 1
            except:
                pass

        if not editing_started or not self.selected_layer.commitChanges():
            title = self.tr('Update Photos')
            msg = self.tr(
                "Update Failed.\n\nDetails:\n  Could not update the photos layer.\n  "
                "Layer is either read-only or you don't have permissions to edit it.")
            self.showMessage(title, msg, 'Warning')
            return

        no_location_photos_counter = no_location_photos_counter + photos_to_import_counter - imported_pictures_counter - out_of_bounds_photos_counter
        title = self.tr('Update Photos')
        msg = '{}\n\n{}\n  {} {}\n  {} {}\n  {} {}\n  {} {}'.format(
            self.tr('Update Completed.'),
            self.tr('Details:'),
            str(int(imported_pictures_counter)),
            self.tr('photo(s) added without error.'),
            str(int(no_location_photos_counter)),
            self.tr('photo(s) skipped (because of missing location).'),
            str(int(out_of_bounds_photos_counter)),
            self.tr('photo(s) skipped (because not in canvas extent).'),
            str(int(len(pictures_to_remove))),
            self.tr('photo(s) removed.'))

        self.showMessage(title, msg, 'Information')

    def get_geo_infos_from_photo(self, photo_path):
        try:
            rel_path = self.selected_folder + os.path.basename(photo_path)
            ImagesSrc = '<img src = "' + rel_path + '" width="300" height="225"/>'
            if CHECK_MODULE == 'exifread':
                with open(photo_path, 'rb') as imgpathF:
                    tags = exifread.process_file(imgpathF, details=False)

                if not set(tags.keys()).union({"GPS GPSLongitude", "GPS GPSLatitude"}):
                    return False

                lat, lon = self.get_exif_location(tags, "lonlat")

                if 'GPS GPSAltitude' in tags and abs(float(tags.get("GPS GPSAltitude").values[0].den)) > 0:
                    altitude = float(tags.get("GPS GPSAltitude").values[0].num) / float(
                        tags.get("GPS GPSAltitude").values[0].den)
                else:
                    altitude = None

                uuid_ = str(uuid.uuid4())

                try:
                    dt1, dt2 = tags["EXIF DateTimeOriginal"].values.split(' ')
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
                        date = None
                        time_ = None
                        timestamp = None

                try:
                    if 'GPS GPSImgDirection' in tags:
                        azimuth = float(tags["GPS GPSImgDirection"].values[0].num) / float(
                            tags["GPS GPSImgDirection"].values[0].den)
                    else:
                        azimuth = None
                except:
                    azimuth = None

                try:
                    if 'GPS GPSImgDirectionRef' in tags:
                        north = str(tags["GPS GPSImgDirectionRef"].values)
                    else:
                        north = ''
                except:
                    north = ''

                try:
                    if 'Image Make' in tags:
                        maker = tags['Image Make']
                    else:
                        maker = ''
                except:
                    maker = ''

                try:
                    if 'Image Model' in tags:
                        model = tags['Image Model']
                    else:
                        model = ''
                except:
                    model = ''

                try:
                    if 'Image ImageDescription' in tags:
                        title = tags['Image ImageDescription']
                    else:
                        title = ''
                except:
                    title = ''

                try:
                    if 'EXIF UserComment' in tags:
                        user_comm = tags['EXIF UserComment'].printable
                    else:
                        user_comm = ''
                except:
                    user_comm = ''

            elif CHECK_MODULE == 'PIL':
                a = {}
                with Image.open(photo_path) as img:
                    info = img._getexif()

                if info is None:
                    return False

                for tag, value in info.items():
                    if (
                            TAGS.get(tag, tag) == 'GPSInfo' or
                            TAGS.get(tag, tag) == 'DateTime' or
                            TAGS.get(tag, tag) == 'DateTimeOriginal'
                    ):
                        a[TAGS.get(tag, tag)] = value

                if a == {}:
                    return False

                if a['GPSInfo'] != {}:
                    if 1 and 2 and 3 and 4 in a['GPSInfo']:
                        lat = a['GPSInfo'][2]
                        latref = a['GPSInfo'][1]
                        lon = a['GPSInfo'][4]
                        lonref = a['GPSInfo'][3]

                        lat = float(lat[0] + lat[1] / 60 + lat[2] / 3600)
                        lon = float(lon[0] + lon[1] / 60 + lon[2] / 3600)

                        if latref == 'S':
                            lat = -lat
                        if lonref == 'W':
                            lon = -lon
                    else:
                        return False

                    uuid_ = str(uuid.uuid4())
                    if 'DateTime' or 'DateTimeOriginal' in a:
                        if 'DateTime' in a:
                            dt1, dt2 = a['DateTime'].split()
                        if 'DateTimeOriginal' in a:
                            dt1, dt2 = a['DateTimeOriginal'].split()
                        date = dt1.replace(':', '/')
                        time_ = dt2
                        timestamp = dt1.replace(':', '-') + 'T' + time_

                    try:
                        if 6 in a['GPSInfo']:
                            altitude = float(a['GPSInfo'][6])
                        else:
                            altitude = None
                    except:
                        altitude = None

                    try:
                        if 16 and 17 in a['GPSInfo']:
                            north = a['GPSInfo'][16]
                            azimuth = float(a['GPSInfo'][17])
                        else:
                            north = ''
                            azimuth = None
                    except:
                        north = ''
                        azimuth = None

                    maker = ''
                    model = ''
                    user_comm = ''
                    title = ''

            if self.dlg.canvas_extent.isChecked():
                if not (self.canvas.extent().xMaximum() > lon > self.canvas.extent().xMinimum() \
                        and self.canvas.extent().yMaximum() > lat > self.canvas.extent().yMinimum()):
                    return 'out'

            geo_info = {
                "type": "Feature",
                "properties": {
                    'ID': uuid_, 'Name': os.path.basename(photo_path),
                    'Date': date, 'Time': time_,
                    'Lon': lon, 'Lat': lat, 'Altitude': altitude,
                    'North': north, 'Azimuth': azimuth,
                    'Cam. Maker': str(maker), 'Cam. Model': str(model),
                    'Title': str(title), 'Comment': user_comm,
                    'Path': photo_path, 'RelPath': rel_path,
                    'Timestamp': timestamp, 'Images': ImagesSrc
                },
                "geometry": {
                    "coordinates": [lon, lat],
                    "type": "Point"
                }
            }

            try:
                if self.selected_layer.source().lower().endswith("gpkg"):
                    geo_info = {
                        "type": "Feature",
                        "properties": {
                            'fid': 0, 'ID': uuid_, 'Name': os.path.basename(photo_path),
                            'Date': date, 'Time': time_,
                            'Lon': lon, 'Lat': lat, 'Altitude': altitude,
                            'North': north, 'Azimuth': azimuth,
                            'Cam. Maker': str(maker), 'Cam. Model': str(model),
                            'Title': str(title), 'Comment': user_comm,
                            'Path': photo_path, 'RelPath': rel_path,
                            'Timestamp': timestamp, 'Images': ImagesSrc
                        },
                        "geometry": {
                            "coordinates": [lon, lat],
                            "type": "Point"
                        }
                    }
            except:
                pass

            return geo_info

        except Exception as e:
            return ''

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
        QGuiApplication.restoreOverrideCursor()
        msgBox.exec_()

    def refresh(self):
        self.iface.mainWindow().findChild(
            QAction, 'mActionDeselectAll').trigger()
        self.canvas.refresh()

    ######################################################
    # based on http://www.codegists.com/snippet/python/exif_gpspy_snakeye_python

    def get_exif_location(self, exif_data, lonlat):
        """
        Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
        """

        if lonlat == 'lonlat':
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
