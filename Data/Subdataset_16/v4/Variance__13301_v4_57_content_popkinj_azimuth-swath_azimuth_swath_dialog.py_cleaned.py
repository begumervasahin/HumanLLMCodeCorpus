
import os
from PyQt4 import QtGui, uic
FORM_CLASS, b1 = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui'))
class class1(QtGui.QDialog, FORM_CLASS):
    def fonk1(self, b2 = None):
        super(class1, self).fonk1(b2)
        self.setupUi(self)