from PyQt4.QtCore import Qt, pyqtSignal, QRect
from PyQt4.QtGui import QGraphicsView, QGraphicsScene, QPainterPath, \
    QVBoxLayout, QWidget, QLineEdit, QSizePolicy, QIcon, QHBoxLayout


class PhotosViewer(QGraphicsView):
    afterLeftClick = pyqtSignal(float, float)
    afterLeftClickReleased = pyqtSignal(float, float)
    afterDoubleClick = pyqtSignal(float, float)
    
    def __init__(self):
        QGraphicsView.__init__(self)

        self.zoom_data = []
        self.zoom = True
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setMouseTracking(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setDragMode(QGraphicsView.NoDrag)
        self.setCursor(Qt.CrossCursor)

    def mousePressEvent(self, event):
        sc_pos = self.mapToScene(event.pos())
        if self.zoom:
            self.setDragMode(QGraphicsView.RubberBandDrag)
        self.afterLeftClick.emit(sc_pos.x(), sc_pos.y())
        QGraphicsView.mousePressEvent(self, event)

    def mouseDoubleClickEvent(self, event):
        sc_pos = self.mapToScene(event.pos())
        if self.zoom:
            self.zoom_data = []
            self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        self.afterDoubleClick.emit(sc_pos.x(), sc_pos.y())
        QGraphicsView.mouseDoubleClickEvent(self, event)

    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)
        sc_pos = self.mapToScene(event.pos())
        if self.zoom:
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
        self.viewer = PhotosViewer()

        self.setWindowTitle('Photo')
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon("icon.png"))

        rect = QRect(0, 0, 113, 20)
        self.infoPhoto1 = QLineEdit(self)
        self.infoPhoto1.setGeometry(rect)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.infoPhoto1.setSizePolicy(sizePolicy)
        self.infoPhoto1.setFrame(True)
        self.infoPhoto1.setReadOnly(True)

        self.infoPhoto2 = QLineEdit(self)
        self.infoPhoto2.setGeometry(rect)
        self.infoPhoto2.setSizePolicy(sizePolicy)
        self.infoPhoto2.setFrame(True)
        self.infoPhoto2.setReadOnly(True)

        self.infoPhoto3 = QLineEdit(self)
        self.infoPhoto3.setGeometry(rect)
        self.infoPhoto3.setSizePolicy(sizePolicy)
        self.infoPhoto3.setFrame(True)
        self.infoPhoto3.setReadOnly(True)

        # Arrange layout
        VBlayout = QVBoxLayout(self)
        HBlayout = QHBoxLayout()
        VBlayout.addWidget(self.viewer)
        HBlayout.setAlignment(Qt.AlignCenter)
        HBlayout.addWidget(self.infoPhoto1)
        HBlayout.addWidget(self.infoPhoto2)
        HBlayout.addWidget(self.infoPhoto3)

        VBlayout.addLayout(HBlayout)
