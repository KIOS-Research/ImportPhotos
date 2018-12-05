# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos jpegs
                              -------------------
        begin                : 2018-05-17
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

from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.core import QgsRectangle
from qgis.gui import QgsMapTool, QgsRubberBand
from .PhotosViewer import PhotoWindow
import os


class MouseClick(QgsMapTool):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    afterDoubleClick = pyqtSignal()

    def __init__(self, canvas, drawSelf):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.drawSelf = drawSelf
        self.drawSelf.rb = None

    def canvasPressEvent(self, event):
        if event.button() == 1:
            self.drawSelf.refresh()

    def canvasMoveEvent(self, event):
        pass

    def canvasReleaseEvent(self, event):
        pass

    def canvasDoubleClickEvent(self, event):

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
                try:
                    layer.selectByRect(lRect, False)
                except:
                    layer.select(lRect, False)
                selected_features = layer.selectedFeatures()
                if selected_features != []:
                    layersSelected.append(layer)
                    ########## SHOW PHOTOS ############
                    feature = selected_features[0]
                    self.drawSelf.featureIndex = feature.id()
                    self.drawSelf.layerActive = layer
                    self.drawSelf.fields = fields
                    self.drawSelf.maxlen = len(self.drawSelf.layerActive.name())
                    self.drawSelf.layerActiveName = layer.name()
                    if self.drawSelf.maxlen>13:
                        self.drawSelf.maxlen = 14
                        self.drawSelf.layerActiveName = self.drawSelf.layerActive.name()+'...'
                    self.photosDLG = PhotoWindow(self.drawSelf)

                    if 'PATH' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('Path')]
                    elif 'PHOTO' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('photo')]
                    else:
                        return

                    try:
                        if os.path.exists(imPath) == False:
                            c = self.drawSelf.noImageFound()
                            if c: return
                    except:
                        c = self.drawSelf.noImageFound()
                        if c: return

                    self.photosDLG.viewer.scene.clear()
                    pixmap = QPixmap.fromImage(QImage(imPath))
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
                        self.photosDLG.infoPhoto1.setText('Date: ' + dateTrue)
                        self.photosDLG.infoPhoto2.setText('Time: ' + timeTrue[0:8])
                    except:
                        pass
                    self.photosDLG.infoPhoto3.setText('Layer: ' + self.drawSelf.layerActiveName)

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