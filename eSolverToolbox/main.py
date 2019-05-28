from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

import sys

from windows.MainWindow import Ui_Form
from methods.string_replacer_dialog import *

string_text = "default text"

class MainWindow(QWidget, Ui_Form):

    string_text_trigger = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)
        self.setupUi(self)

        self.stringButton.clicked.connect(self.string_page)
        self.feature_2.clicked.connect(self.feature_two_page)

    def back_button(self):
        self.stackedWidget.setCurrentIndex(0)

    def string_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.backBtn2.clicked.connect(self.back_button)
        self.pushButton.clicked.connect(self.string_btn_handler)
        self.pushButton.clicked.connect(self.open_dialog)

    def string_btn_handler(self):
        global string_text
        string_text = self.textEdit.toPlainText()
        return string_text

    def open_dialog(self):
        s_window = StringReplacerWindow()
        s_window.string_replace_init(string_text)
        s_window.exec_()
        self.textEdit_2.setText(s_window.replaced_string)

    def feature_two_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.backBtn3.clicked.connect(self.back_button)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
