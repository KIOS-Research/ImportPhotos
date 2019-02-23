# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ImportPhotos
                                 A QGIS plugin
 Import photos jpegs
                              -------------------
        begin                : 2018-08-27
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
from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QVBoxLayout, QHBoxLayout, QWidget, \
    QLineEdit, QLabel, QSizePolicy, QPushButton, QFrame)
from PyQt5.QtCore import (Qt, pyqtSignal, QRectF, QRect, QSize)
from PyQt5.QtGui import (QPainterPath, QIcon, QPixmap, QImage)
import os.path


class PhotosViewer(QGraphicsView):
    afterLeftClick = pyqtSignal(float, float)
    afterLeftClickReleased = pyqtSignal(float, float)
    afterDoubleClick = pyqtSignal(float, float)
    keyPressed = pyqtSignal(int)

    def __init__(self, selfwindow):
        QGraphicsView.__init__(self)

        self.selfwindow = selfwindow
        self.panSelect = False
        self.zoomSelect = False
        self.rotate_value = 0
        self.rotate_azimuth_value = 0

        self.zoom_data = []
        size = 36
        self.scene = QGraphicsScene()
        if len(self.selfwindow.allpictures) > 1:
            self.leftClick = QPushButton(self)
            self.leftClick.setIcon(QIcon(self.selfwindow.path+'//svg//arrowLeft.png'))
            self.leftClick.clicked.connect(self.selfwindow.leftClickButton)
            self.leftClick.setToolTip('Show previous photo')
            self.leftClick.setStyleSheet("QPushButton{border: 0px;}")
            self.leftClick.setIconSize(QSize(size, size))
            self.leftClick.setFocusPolicy(Qt.NoFocus)

            self.rightClick = QPushButton(self)
            self.rightClick.setIcon(QIcon(self.selfwindow.path+'//svg//arrowRight.png'))
            self.rightClick.clicked.connect(self.selfwindow.rightClickButton)
            self.rightClick.setToolTip('Show next photo')
            self.rightClick.setStyleSheet("QPushButton{border: 0px;}")
            self.rightClick.setIconSize(QSize(size, size))
            self.rightClick.setFocusPolicy(Qt.NoFocus)

        self.setScene(self.scene)
        self.setMouseTracking(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.NoDrag)

    def mousePressEvent(self, event):
        sc_pos = self.mapToScene(event.pos())
        if self.panSelect:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        if self.zoomSelect:
            self.setDragMode(QGraphicsView.RubberBandDrag)
        self.afterLeftClick.emit(sc_pos.x(), sc_pos.y())
        QGraphicsView.mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        sc_pos = self.mapToScene(event.pos())
        if self.zoomSelect or self.panSelect:
            self.zoom_data = []
            self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        self.afterDoubleClick.emit(sc_pos.x(), sc_pos.y())
        QGraphicsView.mouseDoubleClickEvent(self, event)

    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)
        sc_pos = self.mapToScene(event.pos())
        if self.zoomSelect:
            view_bb = self.sceneRect()
            if self.zoom_data:
                view_bb = self.zoom_data
            selection_bb = self.scene.selectionArea().boundingRect().intersected(view_bb)
            self.scene.setSelectionArea(QPainterPath())
            if selection_bb.isValid() and (selection_bb != view_bb):
                self.zoom_data = selection_bb
                self.fitInView(self.zoom_data, Qt.KeepAspectRatio)
        self.setDragMode(QGraphicsView.NoDrag)
        self.afterLeftClickReleased.emit(sc_pos.x(), sc_pos.y())

    def resizeEvent(self, event):
        self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

        if len(self.selfwindow.allpictures) > 1:
            loc = self.viewport().geometry()
            self.left_newloc =  list(loc.getRect())
            self.left_newloc[0] = self.left_newloc[0] # x
            self.left_newloc[1] = self.left_newloc[3]/2.4 # y
            self.left_newloc[2] = self.left_newloc[2]/5 # width
            self.left_newloc[3] = self.left_newloc[3]/5 # height
            self.leftClick.setGeometry(QRect(self.left_newloc[0], self.left_newloc[1], self.left_newloc[2], self.left_newloc[3]))
            newloc =  list(loc.getRect())
            newloc[0] = newloc[2] - newloc[2]/5 # x
            newloc[1] = newloc[3]/2.4 # y
            newloc[2] = newloc[2]/5 # width
            newloc[3] = newloc[3]/5 # height
            self.rightClick.setGeometry(QRect(newloc[0], newloc[1], newloc[2], newloc[3]))

        # Fix rotate for the next photo
        self.rotate(-self.rotate_value)
        self.rotate_value = 0

        # Fix azimuth rotate for the next photo
        if self.rotate_azimuth_value > 0:
            self.rotate(-self.rotate_azimuth_value)
            self.rotate_azimuth_value = 0

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Right:
            self.selfwindow.drawSelf.featureIndex = self.selfwindow.drawSelf.featureIndex+1

            if self.selfwindow.drawSelf.featureIndex > len(self.selfwindow.allpictures)-1:
                self.selfwindow.drawSelf.featureIndex = 0
            self.selfwindow.updateWindow()

        if e.key() == Qt.Key_Left:
            self.selfwindow.drawSelf.featureIndex = self.selfwindow.drawSelf.featureIndex - 1

            if self.selfwindow.drawSelf.featureIndex < 0:
                self.selfwindow.drawSelf.featureIndex = len(self.selfwindow.allpictures)-1
            self.selfwindow.updateWindow()

        if e.key() == Qt.Key_Escape:
            if self.selfwindow.isFullScreen():
                self.selfwindow.showMaximized()
                return

        if e.key() == Qt.Key_F11:
            if self.selfwindow.isFullScreen():
                self.selfwindow.showMaximized()
            else:
                self.selfwindow.showFullScreen()

        if e.key() == Qt.Key_Escape:
            self.selfwindow.close()


class PhotoWindow(QWidget):
    def __init__(self, drawSelf):
        super(PhotoWindow, self).__init__()
        self.drawSelf = drawSelf
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__)))

        ## Update for photo
        self.allpictures = []
        self.allpicturesdates = []
        self.allpicturestimes = []
        self.allpicturesImpath= []
        self.allpicturesAzimuth=[]
        for i, f in enumerate(self.drawSelf.layerActive.getFeatures()):
            if 'PATH' in self.drawSelf.fields:
                imPath = f.attributes()[f.fieldNameIndex('Path')]
            elif 'PHOTO' in self.drawSelf.fields :
                imPath = f.attributes()[f.fieldNameIndex('photo')]
            else:
                imPath = ''
            try:
                dateTrue = str(f.attributes()[f.fieldNameIndex('Date')].toString('yyyy-MM-dd'))
            except:
                dateTrue = str(f.attributes()[f.fieldNameIndex('Date')])
            try:
                timeTrue = str(f.attributes()[f.fieldNameIndex('Time')].toString('hh:mm:ss'))
            except:
                timeTrue = str(f.attributes()[f.fieldNameIndex('Time')])

            if not os.path.exists(imPath):
                if self.drawSelf.prj.fileName() and 'RELPATH' in self.drawSelf.fields:
                    imPath = QFileInfo(prj.fileName()).absolutePath() + \
                             feature.attributes()[feature.fieldNameIndex('RelPath')]

            azimuth = f.attributes()[f.fieldNameIndex('Azimuth')]
            self.allpictures.append(f.attributes()[f.fieldNameIndex('Name')])
            self.allpicturesdates.append(dateTrue)
            self.allpicturestimes.append(timeTrue)
            self.allpicturesImpath.append(imPath)
            self.allpicturesAzimuth.append(azimuth)

        self.viewer = PhotosViewer(self)

        ######################################################################################

        self.setWindowTitle('Photo')
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(self.path + "//icon.png"))

        self.infoPhoto1 = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.infoPhoto1.setSizePolicy(sizePolicy)
        self.infoPhoto1.setFrameShape(QFrame.Box)

        self.infoPhoto2 = QLabel(self)
        self.infoPhoto2.setSizePolicy(sizePolicy)
        self.infoPhoto2.setFrameShape(QFrame.Box)

        self.infoPhoto3 = QLabel(self)
        self.infoPhoto3.setSizePolicy(sizePolicy)
        self.infoPhoto3.setFrameShape(QFrame.Box)

        self.extent = QPushButton(self)
        self.extent.setSizePolicy(sizePolicy)
        self.extent.setIcon(QIcon(self.path + '//svg//mActionZoomFullExtent.svg'))
        self.extent.clicked.connect(self.extentbutton)

        self.zoom = QPushButton(self)
        self.zoom.setSizePolicy(sizePolicy)
        self.zoom.setIcon(QIcon(self.path + '//svg//method-draw-image.svg'))
        self.zoom.clicked.connect(self.zoombutton)

        self.pan = QPushButton(self)
        self.pan.setSizePolicy(sizePolicy)
        self.pan.setIcon(QIcon(self.path + '//svg//mActionPan.svg'))
        self.pan.clicked.connect(self.panbutton)

        self.zoom_to_select = QPushButton(self)
        self.zoom_to_select.setSizePolicy(sizePolicy)
        self.zoom_to_select.setIcon(QIcon(self.path + '//svg//mActionZoomToSelected.svg'))
        self.zoom_to_select.clicked.connect(self.zoom_to_selectbutton)

        self.rotate_option = QPushButton(self)
        self.rotate_option.setSizePolicy(sizePolicy)
        self.rotate_option.setIcon(QIcon(self.path + '//svg//rotate.png'))
        self.rotate_option.clicked.connect(self.rotatebutton)

        self.rotate_azimuth = QPushButton(self)
        self.rotate_azimuth.setSizePolicy(sizePolicy)
        self.rotate_azimuth.setIcon(QIcon(self.path + '//svg//tonorth.png'))
        self.rotate_azimuth.clicked.connect(self.rotate_azimuthbutton)

        self.hide_arrow = QPushButton(self)
        self.hide_arrow.setSizePolicy(sizePolicy)
        self.hide_arrow.setIcon(QIcon(self.path + '//svg//arrowRight.png'))
        self.hide_arrow.clicked.connect(self.hide_arrow_button)
        if len(self.allpictures) > 1:
            self.hide_arrow.setEnabled(True)
        else:
            self.hide_arrow.setEnabled(False)

        # Add tips on buttons
        self.extent.setToolTip('Extent photo')
        self.zoom.setToolTip('Select area to zoom')
        self.pan.setToolTip('Pan')
        self.zoom_to_select.setToolTip('Zoom to selected photo')
        self.rotate_option.setToolTip('Rotate 45°')
        self.rotate_azimuth.setToolTip('Rotate to azimuth')
        self.hide_arrow.setToolTip('Hide arrows')

        # Arrange layout
        VBlayout = QVBoxLayout(self)
        HBlayout = QHBoxLayout()
        HBlayout2 = QHBoxLayout()
        HBlayout2.addWidget(self.viewer)
        HBlayout.setAlignment(Qt.AlignCenter)
        HBlayout.addWidget(self.infoPhoto1)
        HBlayout.addWidget(self.infoPhoto2)
        HBlayout.addWidget(self.infoPhoto3)
        HBlayout.addWidget(self.extent)
        HBlayout.addWidget(self.zoom)
        HBlayout.addWidget(self.pan)
        HBlayout.addWidget(self.rotate_option)
        HBlayout.addWidget(self.rotate_azimuth)
        HBlayout.addWidget(self.zoom_to_select)
        HBlayout.addWidget(self.hide_arrow)

        VBlayout.addLayout(HBlayout2)
        VBlayout.addLayout(HBlayout)

    def hide_arrow_button(self):
        if self.viewer.leftClick.icon().isNull():
            self.viewer.leftClick.setIcon(QIcon(self.path+'//svg//arrowLeft.png'))
            self.viewer.rightClick.setIcon(QIcon(self.path+'//svg//arrowRight.png'))
            self.hide_arrow.setIcon(QIcon(self.path + '//svg//arrowRight.png'))
            self.hide_arrow.setToolTip('Hide arrows')
        else:
            self.viewer.leftClick.setIcon(QIcon(''))
            self.viewer.rightClick.setIcon(QIcon(''))
            self.hide_arrow.setToolTip('Show arrows')
            self.hide_arrow.setIcon(QIcon(self.path + '//svg//arrowRight.png'))

    def leftClickButton(self):
        self.drawSelf.featureIndex = self.drawSelf.featureIndex - 1
        if self.drawSelf.featureIndex < 0:
            self.drawSelf.featureIndex = len(self.allpictures) - 1
        self.updateWindow()

    def rightClickButton(self):
        self.drawSelf.featureIndex = self.drawSelf.featureIndex + 1
        if self.drawSelf.featureIndex > len(self.allpictures) - 1:
            self.drawSelf.featureIndex = 0
        self.updateWindow()

    def updateWindow(self):
        imPath = self.allpicturesImpath[self.drawSelf.featureIndex]
        try:
            if os.path.exists(imPath) == False:
                c = self.drawSelf.noImageFound()
                imPath = ''
        except:
            c = self.drawSelf.noImageFound()
            imPath = ''

        self.viewer.scene.clear()
        pixmap = QPixmap.fromImage(QImage(imPath))
        self.viewer.scene.addPixmap(pixmap)
        self.viewer.setSceneRect(QRectF(pixmap.rect()))
        self.drawSelf.layerActive.selectByIds([self.drawSelf.featureIndex])

        self.viewer.resizeEvent([])
        self.extentbutton()
        self.infoPhoto1.setText(
            'Date: ' + self.allpicturesdates[self.drawSelf.featureIndex])
        self.infoPhoto2.setText(
            'Time: ' + self.allpicturestimes[self.drawSelf.featureIndex][0:8])
        self.infoPhoto3.setText('Layer: ' + self.drawSelf.layerActiveName)

        azimuth = self.allpicturesAzimuth[self.drawSelf.featureIndex]
        if type(azimuth) is str:
            try:
                azimuth = float(azimuth)
            except:
                pass
        if type(azimuth) is float:
            if azimuth > 0:
                self.rotate_azimuth.setEnabled(True)
                return
        self.rotate_azimuth.setEnabled(False)

    def rotatebutton(self):
        self.viewer.rotate(90)
        self.viewer.rotate_value = self.viewer.rotate_value + 90
        if self.viewer.rotate_value == 360:
            self.viewer.rotate_value = 0

    def rotate_azimuthbutton(self):
        if self.viewer.rotate_azimuth_value == 0:
            azimuth = self.allpicturesAzimuth[self.drawSelf.featureIndex]
            if type(azimuth) is str:
                azimuth = float(azimuth)
            self.viewer.rotate(azimuth)
            self.viewer.rotate_azimuth_value = azimuth
            return
        if self.viewer.rotate_azimuth_value > 0:
            self.viewer.rotate(-self.viewer.rotate_azimuth_value)
            self.viewer.rotate_azimuth_value = 0

    def zoom_to_selectbutton(self):
        self.drawSelf.iface.actionZoomToSelected().trigger()

    def panbutton(self):
        self.viewer.panSelect = True
        self.viewer.zoomSelect = False
        self.viewer.setCursor(Qt.OpenHandCursor)
        self.viewer.setDragMode(QGraphicsView.ScrollHandDrag)

    def zoombutton(self):
        self.viewer.panSelect = False
        self.viewer.zoomSelect = True
        self.viewer.setCursor(Qt.CrossCursor)
        self.viewer.setDragMode(QGraphicsView.RubberBandDrag)

    def extentbutton(self):
        self.viewer.zoom_data = []
        self.viewer.fitInView(self.viewer.sceneRect(), Qt.KeepAspectRatio)
        self.viewer.panSelect = False
        self.viewer.zoomSelect = False
        self.viewer.setCursor(Qt.ArrowCursor)
        self.viewer.setDragMode(QGraphicsView.NoDrag)