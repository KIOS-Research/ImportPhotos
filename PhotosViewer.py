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
        QLineEdit, QSizePolicy, QPushButton
    from PyQt5.QtCore import Qt, pyqtSignal
    from PyQt5.QtGui import QPainterPath, QIcon
except:
    from PyQt4.QtCore import Qt, pyqtSignal, QRect
    from PyQt4.QtGui import QGraphicsView, QGraphicsScene, QPainterPath, \
        QVBoxLayout, QWidget, QLineEdit, QSizePolicy, QIcon, QHBoxLayout, QPushButton
import os.path

class PhotosViewer(QGraphicsView):
    afterLeftClick = pyqtSignal(float, float)
    afterLeftClickReleased = pyqtSignal(float, float)
    afterDoubleClick = pyqtSignal(float, float)
    
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


class PhotoWindow(QWidget):
    def __init__(self):
        super(PhotoWindow, self).__init__()
        self.path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.viewer = PhotosViewer(self)

        self.setWindowTitle('Photo')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(self.path + "//icon.png"))

        self.infoPhoto1 = QLineEdit(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.infoPhoto1.setSizePolicy(sizePolicy)
        self.infoPhoto1.setFrame(True)
        self.infoPhoto1.setReadOnly(True)
        self.infoPhoto1.setMouseTracking(False)

        self.infoPhoto2 = QLineEdit(self)
        self.infoPhoto2.setSizePolicy(sizePolicy)
        self.infoPhoto2.setFrame(True)
        self.infoPhoto2.setReadOnly(True)
        self.infoPhoto2.setMouseTracking(False)

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

        # Arrange layout
        VBlayout = QVBoxLayout(self)
        HBlayout = QHBoxLayout()
        VBlayout.addWidget(self.viewer)
        HBlayout.setAlignment(Qt.AlignCenter)
        HBlayout.addWidget(self.infoPhoto1)
        HBlayout.addWidget(self.infoPhoto2)
        HBlayout.addWidget(self.extent)
        HBlayout.addWidget(self.zoom)
        HBlayout.addWidget(self.pan)

        VBlayout.addLayout(HBlayout)

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