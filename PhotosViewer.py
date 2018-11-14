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
try:
    from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QVBoxLayout, QHBoxLayout, QWidget, \
        QLineEdit, QLabel, QSizePolicy, QPushButton, QFrame
    from PyQt5.QtCore import Qt, pyqtSignal, QRectF
    from PyQt5.QtGui import QPainterPath, QIcon, QPixmap, QImage
except:
    from PyQt4.QtCore import Qt, pyqtSignal, QRect, QFrame
    from PyQt4.QtGui import QGraphicsView, QGraphicsScene, QPainterPath, \
        QVBoxLayout, QWidget, QLineEdit, QLabel, QSizePolicy, QIcon, QHBoxLayout, QPushButton, QPixmap, QImage
import os.path

try:
    # qgis 3
    from qgis.utils import Qgis
except:
    # qgis 2
    try:
        from qgis.utils import QGis as Qgis  #  for QGIS 2
    except:
        from qgis.utils import Qgis # QGIS 3

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

        self.zoom_data = []
        self.scene = QGraphicsScene()
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
            self.selfwindow.close()

        if e.key() == Qt.Key_F11:
            if self.selfwindow.isFullScreen():
                self.selfwindow.showMaximized()
            else:
                self.selfwindow.showFullScreen()

class PhotoWindow(QWidget):
    def __init__(self, drawSelf):
        super(PhotoWindow, self).__init__()
        self.drawSelf = drawSelf
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.viewer = PhotosViewer(self)

        ## Update for photo
        self.allpictures = []
        self.allpicturesdates = []
        self.allpicturestimes = []
        self.allpicturesImpath= []
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
            self.allpictures.append(f.attributes()[f.fieldNameIndex('Name')])
            self.allpicturesdates.append(dateTrue)
            self.allpicturestimes.append(timeTrue)
            self.allpicturesImpath.append(imPath)
        ######################################################################################

        self.setWindowTitle('Photo')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
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
        self.extent.setCheckable(True)
        self.extent.setChecked(True)
        self.extent.setIcon(QIcon(self.path + '//svg//mActionZoomFullExtent.svg'))
        self.extent.clicked.connect(self.extentbutton)

        self.zoom = QPushButton(self)
        self.zoom.setSizePolicy(sizePolicy)
        self.zoom.setCheckable(True)
        self.zoom.setChecked(False)
        self.zoom.setIcon(QIcon(self.path + '//svg//mActionZoomToSelected.svg'))
        self.zoom.clicked.connect(self.zoombutton)

        self.pan = QPushButton(self)
        self.pan.setSizePolicy(sizePolicy)
        self.pan.setCheckable(True)
        self.pan.setChecked(False)
        self.pan.setIcon(QIcon(self.path + '//svg//mActionPan.svg'))
        self.pan.clicked.connect(self.panbutton)

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.rightClick = QPushButton(self)
        self.rightClick.setSizePolicy(sizePolicy)
        self.rightClick.setIcon(QIcon(self.path+'//svg//arrowRight.png'))
        self.rightClick.clicked.connect(self.rightClickButton)

        self.leftClick = QPushButton(self)
        self.leftClick.setSizePolicy(sizePolicy)
        self.leftClick.setIcon(QIcon(self.path+'//svg//arrowLeft.png'))
        self.leftClick.clicked.connect(self.leftClickButton)

        # Arrange layout
        VBlayout = QVBoxLayout(self)
        HBlayout = QHBoxLayout()
        HBlayout2 = QHBoxLayout()
        HBlayout2.addWidget(self.leftClick)
        HBlayout2.addWidget(self.viewer)
        HBlayout2.addWidget(self.rightClick)
        HBlayout.setAlignment(Qt.AlignCenter)
        HBlayout.addWidget(self.infoPhoto1)
        HBlayout.addWidget(self.infoPhoto2)
        HBlayout.addWidget(self.infoPhoto3)
        HBlayout.addWidget(self.extent)
        HBlayout.addWidget(self.zoom)
        HBlayout.addWidget(self.pan)

        VBlayout.addLayout(HBlayout2)
        VBlayout.addLayout(HBlayout)

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
        self.viewer.scene.clear()
        pixmap = QPixmap.fromImage(QImage(imPath))
        self.viewer.scene.addPixmap(pixmap)
        if Qgis.QGIS_VERSION >= '3.0':
            self.viewer.setSceneRect(QRectF(pixmap.rect()))
            self.drawSelf.layerActive.selectByIds([self.drawSelf.featureIndex])
        else:
            self.viewer.setSceneRect(QRect(pixmap.rect()))
            self.drawSelf.layerActive.setSelectedFeatures([self.drawSelf.featureIndex])

        self.viewer.resizeEvent([])
        self.extentbutton()
        self.infoPhoto1.setText(
            'Date: ' + self.allpicturesdates[self.drawSelf.featureIndex])
        self.infoPhoto2.setText(
            'Time: ' + self.allpicturestimes[self.drawSelf.featureIndex])

    def panbutton(self):
        self.viewer.panSelect = True
        self.viewer.zoomSelect = False
        self.viewer.setCursor(Qt.OpenHandCursor)
        self.viewer.setDragMode(QGraphicsView.ScrollHandDrag)
        self.pan.setChecked(True)
        self.zoom.setChecked(False)
        self.extent.setChecked(False)

    def zoombutton(self):
        self.viewer.panSelect = False
        self.viewer.zoomSelect = True
        self.viewer.setCursor(Qt.CrossCursor)
        self.viewer.setDragMode(QGraphicsView.RubberBandDrag)
        self.extent.setChecked(False)
        self.zoom.setChecked(True)
        self.pan.setChecked(False)

    def extentbutton(self):
        self.viewer.zoom_data = []
        self.viewer.fitInView(self.viewer.sceneRect(), Qt.KeepAspectRatio)

        self.viewer.panSelect = False
        self.viewer.zoomSelect = False
        self.viewer.setCursor(Qt.ArrowCursor)
        self.viewer.setDragMode(QGraphicsView.NoDrag)
        self.extent.setChecked(True)
        self.zoom.setChecked(False)
        self.pan.setChecked(False)