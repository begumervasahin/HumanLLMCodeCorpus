
import os
from PyQt5 import QtWidgets, uic
UI_FILE = os.path.join(os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui')
FORM_CLASS, _ = uic.loadUiType(UI_FILE)
class AzimuthSwathDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
