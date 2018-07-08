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

from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.core import QgsRectangle
from qgis.gui import QgsMapTool, QgsRubberBand
from .PhotosViewer import PhotoWindow
from qgis.PyQt import QtCore


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
        layer = self.drawSelf.iface.activeLayer()
        try:
            try:
                selected_features = layer.selectedFeatures()
            except:
                self.drawSelf.iface.setActiveLayer(self.drawSelf.layerPhotos)
                selected_features=[]
        except:
            return
        if selected_features == []:
            layers = self.canvas.layers()
            p = self.toMapCoordinates(event.pos())
            w = self.canvas.mapUnitsPerPixel() * 10
            try:
                rect = QgsRectangle(p.x() - w, p.y() - w, p.x() + w, p.y() + w)
            except:
                return
            layersSelected = []

            for layer in layers:
                fields = [field.name().upper() for field in layer.fields()]
                if 'PATH' in fields:
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
                        self.photosDLG = PhotoWindow()

                        imPath = feature.attributes()[feature.fieldNameIndex('Path')]

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

                        self.photosDLG.infoPhoto1.setText('Date: ' + dateTrue)
                        self.photosDLG.infoPhoto2.setText('Time: ' + timeTrue)

                        self.photosDLG.showNormal()
                        self.photosDLG.show()
                        return

    def deactivate(self):
        self.drawSelf.clickPhotos.setChecked(False)

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True