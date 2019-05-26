from PyQt5.QtWidgets import *

from windows.StringReplacer import Ui_Dialog

import string


class StringReplacerWindow(QDialog, Ui_Dialog):

    default_string = "abc"

    def __init__(self, *args, **kwargs):
        super(StringReplacerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.replaceButton.clicked.connect(self.string_replace)

        self.exec_()

    def string_replace(self):
        StringReplacerWindow.default_string = "replaced"
        



