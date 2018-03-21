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
from qgis.PyQt import QtCore
from PIL import Image
import ctypes
import platform

try:
    from AppKit import NSScreen
except:
    pass
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class MouseClick(QgsMapTool):
    afterLeftClick = pyqtSignal()
    afterRightClick = pyqtSignal()
    afterDoubleClick = pyqtSignal()

    def __init__(self, canvas, drawSelf):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas
        self.drawSelf = drawSelf
        self.drawSelf.rb = None
        self.screensize = []
        try:
            user32 = ctypes.windll.user32
            self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        except:
            self.screensize.append(NSScreen.mainScreen().frame().size.width)
            self.screensize.append(NSScreen.mainScreen().frame().size.height)

    def canvasPressEvent(self, event):
        if event.button() == 1:
            self.drawSelf.refresh()

            try:
                if platform.system() == 'Darwin':
                    self.drawSelf.photosDLG.webView.history().clear()
            except:
                pass
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
                #try:
                if (layer.name() in self.drawSelf.layernamePhotos)==True:
                    lRect = self.canvas.mapSettings().mapToLayerCoordinates(layer, rect)
                    layer.select(lRect, False)
                    selected_features = layer.selectedFeatures()
                    if selected_features != []:
                        layersSelected.append(layer)
                        ########## SHOW PHOTOS ############
                        feature = selected_features[0]

                        imPath = feature.attributes()[feature.fieldNameIndex('Path')]
                        im = Image.open(imPath)
                        width, height = im.size
                        x=0
                        y=0
                        if height < width:
                            if width>1000:
                                if width>self.screensize[0]:
                                    width = self.screensize[0]*0.6
                                else:
                                    width = width*0.252#width/(width/1000)
                            elif width<200:
                                width = 200
                                x=113
                            if height>700:
                                if height>self.screensize[1]:
                                    height = self.screensize[1]*0.8
                                else:
                                    height = height*0.252

                            elif height < 200:
                                height = 200
                                y=60
                        elif width < height:
                            if height>1000:
                                height = 756
                                width = 0.793*height
                        self.drawSelf.photosDLG.setMinimumSize(QSize(width, height))
                        self.drawSelf.photosDLG.setMaximumSize(QSize(width, height))
                        self.drawSelf.photosDLG.webView.setGeometry(QRect(x, y, width, height))
                        self.drawSelf.photosDLG.webView.setMinimumSize(QSize(width, height))
                        self.drawSelf.photosDLG.webView.setMaximumSize(QSize(width, height))
                        self.drawSelf.photosDLG.webView.history().clear()
                        self.drawSelf.photosDLG.webView.load(QUrl("file:///"+imPath))
                        self.drawSelf.photosDLG.infoPhoto1.setText('Date: '+str(feature.attributes()[feature.fieldNameIndex('Date')].toString('yyyy-MM-dd')))
                        self.drawSelf.photosDLG.infoPhoto2.setText('Time: '+str(feature.attributes()[feature.fieldNameIndex('Time')].toString('hh:mm:ss')))
                        self.drawSelf.photosDLG.infoPhoto3.setText("Altitude: "+str(feature.attributes()[feature.fieldNameIndex('Altitude')])+' m')
                        self.drawSelf.photosDLG.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
                        self.drawSelf.photosDLG.exec_()
                        self.drawSelf.photosDLG.webView.history().clear()
                        return

    def deactivate(self):
        self.drawSelf.clickPhotos.setChecked(False)

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True