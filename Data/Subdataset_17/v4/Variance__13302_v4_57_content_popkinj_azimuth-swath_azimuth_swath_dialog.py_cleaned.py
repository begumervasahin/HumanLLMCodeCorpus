
import os
from PyQt4 import QtGui, uic
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui'))
class AzimuthSwathDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(AzimuthSwathDialog, self).__init__(parent)
        self.setupUi(self)