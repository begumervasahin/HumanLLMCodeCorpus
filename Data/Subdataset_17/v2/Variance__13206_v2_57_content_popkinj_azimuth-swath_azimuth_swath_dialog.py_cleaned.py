
import os
from PyQt5 import QtWidgets, uic
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui'))
class AzimuthSwathDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(AzimuthSwathDialog, self).__init__(parent)
        self.setupUi(self)
