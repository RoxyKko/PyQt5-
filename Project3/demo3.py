# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_child2(QMainWindow):
    def setupUi(self, child2):
        child2.setObjectName("child2")
        child2.resize(390, 110)
        self.centralwidget = QtWidgets.QWidget(child2)
        self.centralwidget.setObjectName("centralwidget")
        child2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(child2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 23))
        self.menubar.setObjectName("menubar")
        child2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(child2)
        self.statusbar.setObjectName("statusbar")
        child2.setStatusBar(self.statusbar)

        self.retranslateUi(child2)
        QtCore.QMetaObject.connectSlotsByName(child2)

    def retranslateUi(self, child2):
        _translate = QtCore.QCoreApplication.translate
        child2.setWindowTitle(_translate("child2", "子窗口2"))

