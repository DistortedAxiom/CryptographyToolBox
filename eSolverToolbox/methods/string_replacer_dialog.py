from PyQt5.QtWidgets import *

from windows.StringReplacer import Ui_Dialog
from PyQt5.QtCore import pyqtSlot

import string

class StringReplacerWindow(QDialog, Ui_Dialog):

    getter_string = ""
    getter_list = []
    replaced_string = ""
    letter_dict = {}
    key_value_pair = {}


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
        print(StringReplacerWindow.getter_list[0:10])

    def input_getter(self):
        pass


#We can iterate from list, IE: list_item: self.letter*(wild_card).text()
    def recursion_tester(self):
        pass

    def key_value_pair_init(self):
        StringReplacerWindow.key_value_pair = {
            "A": self.letterA.text(),
            "B": self.letterB.text(),
            "C": self.letterC.text(),
            "D": self.lettetD.text(),
        }







