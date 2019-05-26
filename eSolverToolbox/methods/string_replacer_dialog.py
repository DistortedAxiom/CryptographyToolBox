from PyQt5.QtWidgets import *

from windows.StringReplacer import Ui_Dialog
from PyQt5.QtCore import pyqtSlot

import string

class StringReplacerWindow(QDialog, Ui_Dialog):

    default_string = "abc"

    def __init__(self, *args, **kwargs):
        super(StringReplacerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.replaceButton.clicked.connect(self.string_replace)


    def string_replace(self, value):
        StringReplacerWindow.default_string = value




