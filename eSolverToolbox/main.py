from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui

import sys

from windows.MainWindow import Ui_Form


class MainWindow(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)
        self.setupUi(self)

        self.stringButton.pressed.connect(self.string_page)
        self.feature_2.pressed.connect(self.feature_two_page)

        self.show()

    def back_button(self):
        self.stackedWidget.setCurrentIndex(0)

    def string_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.backBtn2.pressed.connect(self.back_button)

    def feature_two_page(self):
        self.stackedWidget.setCurrentIndex(2)
        self.backBtn3.pressed.connect(self.back_button)


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
