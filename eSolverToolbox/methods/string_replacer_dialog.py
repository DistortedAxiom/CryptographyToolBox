from PyQt5.QtWidgets import *

from windows.StringReplacer import Ui_Dialog
from PyQt5.QtCore import pyqtSlot

import string

class StringReplacerWindow(QDialog, Ui_Dialog):

    getter_string = ""
    getter_list = []
    replaced_string = ""

    def __init__(self, *args, **kwargs):
        super(StringReplacerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.replaceButton.clicked.connect(self.char_change)
        self.show()


    @staticmethod
    def string_replace_init(value):
        StringReplacerWindow.getter_string = value
        StringReplacerWindow.replaced_string = StringReplacerWindow.getter_string
        StringReplacerWindow.getter_list = list(StringReplacerWindow.getter_string)

    def char_change(self):
        print(StringReplacerWindow.getter_list[0:5])

    def input_getter(self):
        A = self.letterA.text()





