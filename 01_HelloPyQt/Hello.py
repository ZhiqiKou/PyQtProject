# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hello(object):
    def setupUi(self, Hello):
        Hello.setObjectName("Hello")
        Hello.resize(348, 140)
        self.centralwidget = QtWidgets.QWidget(Hello)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 241, 71))
        self.textEdit.setObjectName("textEdit")
        Hello.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hello)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 23))
        self.menubar.setObjectName("menubar")
        Hello.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hello)
        self.statusbar.setObjectName("statusbar")
        Hello.setStatusBar(self.statusbar)

        self.retranslateUi(Hello)
        QtCore.QMetaObject.connectSlotsByName(Hello)

    def retranslateUi(self, Hello):
        _translate = QtCore.QCoreApplication.translate
        Hello.setWindowTitle(_translate("Hello", "HelloPyqt"))
        self.textEdit.setHtml(_translate("Hello", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; color:#ff0000;\">hello Pyqt</span></p></body></html>"))

