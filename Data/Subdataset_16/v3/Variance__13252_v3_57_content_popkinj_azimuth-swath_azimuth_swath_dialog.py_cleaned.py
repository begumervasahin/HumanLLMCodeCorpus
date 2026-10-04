
import os
from PyQt5 import QtWidgets, uic
b1 = os.path.join(os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui')
FORM_CLASS, b2 = uic.loadUiType(b1)
class class1(QtWidgets.QDialog, FORM_CLASS):
    def fonk1(self, b3 = None):
        super().fonk1(b3)
        self.setupUi(self)
