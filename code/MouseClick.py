# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos jpegs
                              -------------------
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

from qgis.PyQt.QtWidgets import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from qgis.core import QgsRectangle, QgsProject
from qgis.gui import QgsMapTool, QgsRubberBand
from .PhotosViewer import PhotoWindow
import os.path

from win32gui import SetWindowPos
import win32con


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
            self.photosDLG.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.drawSelf.refresh()

    def canvasMoveEvent(self, event):
        pass

    # sigeal : Affichage de la photo sur clic au lieu de double-clic
    #def canvasReleaseEvent(self, event):
    def canvasDoubleClickEvent(self, event):
        pass

    # sigeal : Affichage de la photo sur clic au lieu de double-clic
    #def canvasDoubleClickEvent(self, event):
    def canvasReleaseEvent(self, event):
        print('Affichage photo1')
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
                layer.selectByRect(lRect, False)
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
                    self.drawSelf.iface.setActiveLayer(layer)

                    if self.drawSelf.maxlen>13:
                        self.drawSelf.maxlen = 14
                        self.drawSelf.layerActiveName = self.drawSelf.layerActive.name()+'...'

                    if 'PATH' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('Path')]
                    elif 'PHOTO' in fields:
                        imPath = feature.attributes()[feature.fieldNameIndex('photo')]
                    else:
                        return

                    try:
                        if not os.path.exists(imPath):
                            self.prj = QgsProject.instance()
                            if self.prj.fileName() and 'RELPATH' in fields:
                                imPath = os.path.join(QFileInfo(prj.fileName()).absolutePath(), feature.attributes()[feature.fieldNameIndex('RelPath')])
                            else:
                                c = self.drawSelf.noImageFound()
                                if c: return
                    except:
                        c = self.drawSelf.noImageFound()
                        if c: return

                    self.drawSelf.getImage = QImage(imPath)

                    print('Affichage photo2')
                    if self.photosDLG == None:
                        self.photosDLG = PhotoWindow(self.drawSelf)
                        print('Affichage photo3')
                    self.photosDLG.viewer.scene.clear()
                    pixmap = QPixmap.fromImage(self.drawSelf.getImage)
                    self.photosDLG.viewer.scene.addPixmap(pixmap)
                    self.photosDLG.viewer.setSceneRect(QRectF(pixmap.rect()))
                    self.photosDLG.viewer.resizeEvent([])
                    print('Affichage photo4')

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
                            # sigeal : Forcer l'affichage de la fenêtre au premier plan
                            #self.photosDLG.setWindowFlags(Qt.WindowStaysOnTopHint)
                            self.photosDLG.showNormal()
                            #self.photosDLG.setWindowState(self.photosDLG.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                            #self.photosDLG.activateWindow()
                            print('Affichage photo5')
                            return
                    self.photosDLG.rotate_azimuth.setEnabled(False)
                    self.photosDLG.showNormal()
                    # sigeal : Forcer l'affichage de la fenêtre au premier plan
                    """
                    SetWindowPos(self.photosDLG.winId(),
                                 win32con.HWND_TOPMOST, # = always on top. only reliable way to bring it to the front on windows
                                 0, 0, 0, 0,
                                 win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
                    SetWindowPos(self.photosDLG.winId(),
                                 win32con.HWND_NOTOPMOST, # disable the always on top, but leave window at its top position
                                 0, 0, 0, 0,
                                 win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
                    self.photosDLG.raise_()
                    self.photosDLG.show()
                    self.photosDLG.activateWindow()
                    """
                    self.photosDLG.setWindowState(window.windowState() & ~QtCore.Qt.WindowMinimized | QtCore.Qt.WindowActive)
                    self.photosDLG.activateWindow()
                    #self.photosDLG.setWindowFlags(Qt.WindowStaysOnTopHint)
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
