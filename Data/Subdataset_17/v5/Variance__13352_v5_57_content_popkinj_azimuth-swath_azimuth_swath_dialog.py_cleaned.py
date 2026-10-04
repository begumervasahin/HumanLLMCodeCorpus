
import os
from PyQt4 import QtGui, uic
ui_file_path = os.path.join(os.path.dirname(__file__), 'azimuth_swath_dialog_base.ui')
FORM_CLASS, _ = uic.loadUiType(ui_file_path)
class AzimuthSwathDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(AzimuthSwathDialog, self).__init__(parent)
        self.setupUi(self)