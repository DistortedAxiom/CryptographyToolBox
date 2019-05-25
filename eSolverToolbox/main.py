from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui

import sys

from windows.MainWindow import Ui_Form
from windows.StringReplacer import Ui_Dialog

string_text = "abc"


class StringReplacerWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(StringReplacerWindow, self).__init__(*args, *kwargs)
        self.setupUi(self)


class MainWindow(QWidget, Ui_Form):

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
        text = self.textEdit.toPlainText()
        print(string_text)

    def open_dialog(self):
        string_replace_window = StringReplacerWindow()
        string_replace_window.exec()

    def feature_two_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.backBtn3.click.connect(self.back_button)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
