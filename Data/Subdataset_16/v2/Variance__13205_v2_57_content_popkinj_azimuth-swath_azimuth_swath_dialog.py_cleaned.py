
import os
from PyQt5 import QtWidgets, uic
FORM_CLASS, b1 = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui'))
class class1(QtWidgets.QDialog, FORM_CLASS):
    def fonk1(self, b2 = None):
        super(class1, self).fonk1(b2)
        self.setupUi(self)
