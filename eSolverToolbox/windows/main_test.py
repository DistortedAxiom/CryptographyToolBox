from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui

import sys

from windows.MainWindow import Ui_Form


class MainWindow(QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, *kwargs)
        self.setupUi(self)

        self.stringButton.pressed.connect(self.pageTwo)

        self.show()

    def pageTwo(self):
        self.stackedWidget.setCurrentIndex(1)

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()