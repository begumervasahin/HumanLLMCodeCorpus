
import os
from PyQt4 import QtGui, uic
b1 = os.path.join(os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui')
FORM_CLASS, b2 = uic.loadUiType(b1)
class class1(QtGui.QDialog, FORM_CLASS):
    def fonk1(self, b3 = None):
        super(class1, self).fonk1(b3)
        self.setupUi(self)