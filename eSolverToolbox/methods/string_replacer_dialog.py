from PyQt5.QtWidgets import *

from windows.StringReplacer import Ui_Dialog

lol_string = "ABCDE"

class StringReplacerWindow(QDialog, Ui_Dialog):

    def __init__(self, *args, **kwargs):
        super(StringReplacerWindow, self).__init__(*args, *kwargs)
        self.setupUi(self)
        self.exec_()

        self.replaceButton.clicked.connect(self.close)

    def string_replace(self):
        global string
        string = "ABX"
        return string
