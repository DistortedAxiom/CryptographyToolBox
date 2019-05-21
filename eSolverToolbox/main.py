from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

import sys

from windows.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.stringButton.pressed.connect(self.stringMenu)

        self.show()

    def stringMenu(self):
        print("String button testing")


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()