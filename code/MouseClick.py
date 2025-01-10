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

import os.path

from qgis.PyQt.QtCore import (Qt, pyqtSignal, QCoreApplication, QFileInfo, QRectF)
from qgis.PyQt.QtGui import (QPixmap, QImage)
from qgis.core import (QgsRectangle, QgsProject)
from qgis.gui import (QgsMapTool)

from .PhotosViewer import PhotoWindow


# Mouseclik import file
class MouseClick(QgsMapTool):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    afterDoubleClick = pyqtSignal()

    def __init__(self, canvas, drawSelf):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.drawSelf = drawSelf
        self.drawSelf.rb = None
        self.photosDLG = None

    def canvasPressEvent(self, event):
        if event.button() == 1:
            # sigeal : keep photo viewer on top of other windows
            if self.photosDLG is not None:
                self.photosDLG.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.drawSelf.refresh()

    def canvasMoveEvent(self, event):
        pass

    # sigeal : display photo on click instead of double-click
    # def canvasReleaseEvent(self, event):
    def canvasDoubleClickEvent(self, event):
        pass

    # sigeal : display photo on click instead of double-click
    # def canvasDoubleClickEvent(self, event):
    def canvasReleaseEvent(self, event):
        layers = self.canvas.layers()
        p = self.toMapCoordinates(event.pos())
        w = self.canvas.mapUnitsPerPixel() * 10
        try:
            rect = QgsRectangle(p.x() - w, p.y() - w, p.x() + w, p.y() + w)
        except:
            return
        layersSelected = []
        for layer in layers:
            if layer.type():
                continue
            fields = [field.name().upper() for field in layer.fields()]
            if 'PATH' or 'PHOTO' in fields:
                lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)
                layer.selectByRect(lRect)
                selected_features = layer.selectedFeatures()
                if selected_features != []:
                    layersSelected.append(layer)
                    ########## SHOW PHOTOS ############
                    feature = selected_features[0]
                    self.drawSelf.featureIndex = feature.id()
                    activeLayerChanged = not hasattr(self.drawSelf, 'layerActive') or (
                            self.drawSelf.layerActive != layer)
                    self.drawSelf.layerActive = layer
                    self.drawSelf.fields = fields
                    self.drawSelf.maxlen = len(self.drawSelf.layerActive.name())
                    self.drawSelf.layerActiveName = layer.name()
                    self.drawSelf.iface.setActiveLayer(layer)

                    if self.drawSelf.maxlen > 13:
                        self.drawSelf.maxlen = 14
                        self.drawSelf.layerActiveName = self.drawSelf.layerActive.name() + '...'

                    if 'PATH' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('Path')]
                    elif 'PHOTO' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('photo')]
                    else:
                        return

                    self.drawSelf.prj = QgsProject.instance()
                    try:
                        if not os.path.exists(imPath):
                            if self.drawSelf.prj.fileName() and 'RELPATH' in fields:
                                imPath = os.path.join(QFileInfo(self.drawSelf.prj.fileName()).absolutePath(),
                                                      feature.attributes()[feature.fieldNameIndex('RelPath')])
                            else:
                                c = self.drawSelf.noImageFound()
                                if c:
                                    return
                    except:
                        c = self.drawSelf.noImageFound()
                        if c:
                            return

                    self.drawSelf.getImage = QImage(imPath)

                    if self.photosDLG is None or activeLayerChanged:
                        self.photosDLG = PhotoWindow(self.drawSelf)
                    self.photosDLG.viewer.scene.clear()
                    pixmap = QPixmap.fromImage(self.drawSelf.getImage)
                    self.photosDLG.viewer.scene.addPixmap(pixmap)
                    self.photosDLG.viewer.setSceneRect(QRectF(pixmap.rect()))
                    self.photosDLG.viewer.resizeEvent([])

                    try:
                        dateTrue = str(feature.attributes()[feature.fieldNameIndex('Date')].toString('yyyy-MM-dd'))
                    except:
                        dateTrue = str(feature.attributes()[feature.fieldNameIndex('Date')])
                    try:
                        timeTrue = str(feature.attributes()[feature.fieldNameIndex('Time')].toString('hh:mm:ss'))
                    except:
                        timeTrue = str(feature.attributes()[feature.fieldNameIndex('Time')])

                    try:
                        name_ = feature.attributes()[feature.fieldNameIndex('Name')]
                        name_ = name_[:-4]
                    except:
                        try:
                            name_ = feature.attributes()[feature.fieldNameIndex('filename')]
                        except:
                            name_ = ''

                    try:
                        self.photosDLG.infoPhoto1.setText(self.tr('Date: ') + dateTrue)
                        self.photosDLG.infoPhoto2.setText(self.tr('Time: ') + timeTrue[0:8])
                    except:
                        pass
                    self.photosDLG.infoPhoto3.setText(self.tr('Layer: ') + self.drawSelf.layerActiveName)
                    try:
                        name_ = feature.attributes()[feature.fieldNameIndex('Description')]
                    except:
                        pass

                    self.photosDLG.add_window_place.setText(name_)

                    azimuth = feature.attributes()[feature.fieldNameIndex('Azimuth')]

                    if type(azimuth) is str:
                        try:
                            azimuth = float(azimuth)
                        except:
                            pass
                    if type(azimuth) is float:
                        if azimuth > 0:
                            self.photosDLG.rotate_azimuth.setEnabled(True)
                            self.photosDLG.showNormal()
                            return
                    self.photosDLG.rotate_azimuth.setEnabled(False)
                    self.photosDLG.showNormal()
                    return

    def deactivate(self):
        self.drawSelf.clickPhotos.setChecked(False)

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True

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
        return QCoreApplication.translate('PhotoWindow', message)
