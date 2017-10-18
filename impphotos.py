# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impphotos.ui'
#
# Created: Wed Oct 18 16:58:14 2017
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

class Ui_photosImp(object):
    def setupUi(self, photosImp):
        photosImp.setObjectName(_fromUtf8("photosImp"))
        photosImp.setWindowModality(QtCore.Qt.ApplicationModal)
        photosImp.resize(377, 164)
        photosImp.setWhatsThis(_fromUtf8(""))
        photosImp.setSizeGripEnabled(False)
        self.label = QtGui.QLabel(photosImp)
        self.label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(photosImp)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.imp = QtGui.QLineEdit(photosImp)
        self.imp.setGeometry(QtCore.QRect(100, 20, 190, 20))
        self.imp.setObjectName(_fromUtf8("imp"))
        self.toolButtonImport = QtGui.QToolButton(photosImp)
        self.toolButtonImport.setGeometry(QtCore.QRect(300, 20, 60, 19))
        self.toolButtonImport.setObjectName(_fromUtf8("toolButtonImport"))
        self.out = QtGui.QLineEdit(photosImp)
        self.out.setGeometry(QtCore.QRect(100, 50, 190, 20))
        self.out.setObjectName(_fromUtf8("out"))
        self.toolButtonOut = QtGui.QToolButton(photosImp)
        self.toolButtonOut.setGeometry(QtCore.QRect(300, 50, 60, 19))
        self.toolButtonOut.setObjectName(_fromUtf8("toolButtonOut"))
        self.progressBar = QtGui.QProgressBar(photosImp)
        self.progressBar.setGeometry(QtCore.QRect(10, 90, 351, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.ok = QtGui.QPushButton(photosImp)
        self.ok.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.closebutton = QtGui.QPushButton(photosImp)
        self.closebutton.setGeometry(QtCore.QRect(290, 130, 75, 23))
        self.closebutton.setObjectName(_fromUtf8("closebutton"))

        self.retranslateUi(photosImp)
        QtCore.QMetaObject.connectSlotsByName(photosImp)

    def retranslateUi(self, photosImp):
        photosImp.setWindowTitle(_translate("photosImp", "ImportPhotos", None))
        self.label.setText(_translate("photosImp", "Import directory", None))
        self.label_2.setText(_translate("photosImp", "Output shapefile", None))
        self.toolButtonImport.setText(_translate("photosImp", "Browse...", None))
        self.toolButtonOut.setText(_translate("photosImp", "Browse...", None))
        self.ok.setText(_translate("photosImp", "OK", None))
        self.closebutton.setText(_translate("photosImp", "Close", None))

