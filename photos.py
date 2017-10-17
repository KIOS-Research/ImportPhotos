# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photos.ui'
#
# Created: Mon Oct 09 12:30:08 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_importPhotos(object):
    def setupUi(self, importPhotos):
        importPhotos.setObjectName(_fromUtf8("importPhotos"))
        importPhotos.setWindowModality(QtCore.Qt.NonModal)
        importPhotos.resize(1010, 758)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(importPhotos.sizePolicy().hasHeightForWidth())
        importPhotos.setSizePolicy(sizePolicy)
        importPhotos.setMinimumSize(QtCore.QSize(1010, 758))
        importPhotos.setMaximumSize(QtCore.QSize(1010, 758))
        importPhotos.setAcceptDrops(True)
        importPhotos.setSizeGripEnabled(False)
        importPhotos.setModal(True)
        self.webView = QtWebKit.QWebView(importPhotos)
        self.webView.setGeometry(QtCore.QRect(0, 0, 1011, 841))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(1011, 841))
        self.webView.setMaximumSize(QtCore.QSize(1011, 841))
        self.webView.setSizeIncrement(QtCore.QSize(0, 0))
        self.webView.setMouseTracking(True)
        self.webView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.webView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.webView.setAcceptDrops(False)
        self.webView.setToolTip(_fromUtf8(""))
        self.webView.setWhatsThis(_fromUtf8(""))
        self.webView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.webView.setAutoFillBackground(True)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("c:\\Users\\mkiria01\\Desktop\\test2\\DJI_0243.JPG")))
        self.webView.setZoomFactor(1.0)
        self.webView.setObjectName(_fromUtf8("webView"))
        self.infoPhoto1 = QtGui.QLineEdit(importPhotos)
        self.infoPhoto1.setGeometry(QtCore.QRect(0, 0, 113, 20))
        self.infoPhoto1.setFrame(False)
        self.infoPhoto1.setReadOnly(True)
        self.infoPhoto1.setObjectName(_fromUtf8("infoPhoto1"))
        self.infoPhoto2 = QtGui.QLineEdit(importPhotos)
        self.infoPhoto2.setGeometry(QtCore.QRect(0, 20, 113, 20))
        self.infoPhoto2.setFrame(False)
        self.infoPhoto2.setReadOnly(True)
        self.infoPhoto2.setObjectName(_fromUtf8("infoPhoto2"))
        self.infoPhoto3 = QtGui.QLineEdit(importPhotos)
        self.infoPhoto3.setGeometry(QtCore.QRect(0, 40, 113, 20))
        self.infoPhoto3.setFrame(False)
        self.infoPhoto3.setReadOnly(True)
        self.infoPhoto3.setObjectName(_fromUtf8("infoPhoto3"))

        self.retranslateUi(importPhotos)
        QtCore.QMetaObject.connectSlotsByName(importPhotos)

    def retranslateUi(self, importPhotos):
        importPhotos.setWindowTitle(_translate("importPhotos", "Photos", None))

from PyQt4 import QtWebKit
