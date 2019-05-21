# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Void\Desktop\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(775, 563)
        MainWindow.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.appTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.appTitle.setFont(font)
        self.appTitle.setObjectName("appTitle")
        self.verticalLayout_3.addWidget(self.appTitle, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_1.setSpacing(50)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.stringButton = QtWidgets.QPushButton(self.centralwidget)
        self.stringButton.setObjectName("stringButton")
        self.horizontalLayout_1.addWidget(self.stringButton)
        self.feature_2 = QtWidgets.QPushButton(self.centralwidget)
        self.feature_2.setObjectName("feature_2")
        self.horizontalLayout_1.addWidget(self.feature_2)
        self.feature_3 = QtWidgets.QPushButton(self.centralwidget)
        self.feature_3.setObjectName("feature_3")
        self.horizontalLayout_1.addWidget(self.feature_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appTitle.setText(_translate("MainWindow", "Welcome to ESolver"))
        self.stringButton.setText(_translate("MainWindow", "Strings"))
        self.feature_2.setText(_translate("MainWindow", "Feature 2"))
        self.feature_3.setText(_translate("MainWindow", "Feature 3"))

    def printMessage(self):
        print("Hello")



