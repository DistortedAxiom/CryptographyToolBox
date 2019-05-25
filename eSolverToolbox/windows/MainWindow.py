# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Void\Desktop\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(967, 685)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setStyleSheet("background-color: rgb(214, 107, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout.setObjectName("gridLayout")
        self.stringButton = QtWidgets.QPushButton(self.page_1)
        self.stringButton.setObjectName("stringButton")
        self.gridLayout.addWidget(self.stringButton, 2, 1, 1, 1)
        self.appTitle = QtWidgets.QLabel(self.page_1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.appTitle.setFont(font)
        self.appTitle.setObjectName("appTitle")
        self.gridLayout.addWidget(self.appTitle, 2, 0, 1, 1)
        self.feature_2 = QtWidgets.QPushButton(self.page_1)
        self.feature_2.setObjectName("feature_2")
        self.gridLayout.addWidget(self.feature_2, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(360, 90, 211, 61))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.stackedWidget.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.stringButton.setText(_translate("Form", "Strings"))
        self.appTitle.setText(_translate("Form", "Welcome to ESolver"))
        self.feature_2.setText(_translate("Form", "Feature 2"))
        self.label_2.setText(_translate("Form", "Second Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

