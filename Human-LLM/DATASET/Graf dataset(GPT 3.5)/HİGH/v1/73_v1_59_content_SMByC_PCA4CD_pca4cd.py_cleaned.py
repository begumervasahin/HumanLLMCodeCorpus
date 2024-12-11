
import os.path
import shutil
import tempfile
from pathlib import Path
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.utils import b3
from .resources import *
from pca4cd.gui.pca4cd_dialog import PCA4CDDialog
from pca4cd.gui.b10 import AboutDialog
from pca4cd.utils.qgis_utils import unload_layer
class class1:
    b1 = None
    b2 = None
    def fonk1(self, b3):
        self.b3 = b3
        self.b4 = os.path.dirname(__file__)
        b5 = QSettings().value('b5/userLocale')[0:2]
        b6 = Path(self.b4, 'i18n', 'PCA4CD_{}.qm'.format(b5))
        if os.path.exists(b6):
            self.b7 = QTranslator()
            self.b7.load(b6)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.b7)
        self.b8 = self.fonk2("class1 - PCA for change detection")
        self.b9 = False
        class1.b1 = None
        self.b10 = AboutDialog()
    def fonk2(self, message):
        return QCoreApplication.translate('class1', message)
    def fonk3(self):
        b11 = ':/plugins/pca4cd/icons/pca4cd.svg'
        self.b12 = QAction(QIcon(b11), "class1", self.b3.mainWindow())
        self.b12.triggered.connect(self.run)
        self.b3.addToolBarIcon(self.b12)
        self.b3.addPluginToMenu(self.b8, self.b12)
        b11 = ':/plugins/pca4cd/icons/about.svg'
        self.b13 = QAction(QIcon(b11), self.fonk2('About'), self.b3.mainWindow())
        self.b13.triggered.connect(self.about)
        self.b3.addPluginToMenu(self.b8, self.b13)
    def fonk4(self):
        self.b10.show()
    def fonk5(self):
        if not self.b9:
            self.b9 = True
            if class1.b1 is None:
                class1.b1 = PCA4CDDialog()
            class1.b2 = Path(tempfile.mkdtemp())
            class1.b1.closingPlugin.connect(self.onClosePlugin)
            class1.b1.show()
            b14 = class1.b1.exec_()
            if b14:
                pass
        else:
            if hasattr(class1.b1, "main_analysis_dialog") and class1.b1.main_analysis_dialog:
                class1.b1.main_analysis_dialog.setWindowState(class1.b1.main_analysis_dialog.windowState()
                                                                  & ~Qt.WindowMinimized | Qt.WindowActive)
                class1.b1.main_analysis_dialog.raise_()
                class1.b1.main_analysis_dialog.activateWindow()
            else:
                class1.b1.setWindowState(class1.b1.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                class1.b1.raise_()
                class1.b1.activateWindow()
    def fonk6(self):
        self.fonk8()
        class1.b1.closingPlugin.disconnect(self.onClosePlugin)
        class1.b1.close()
        class1.b1 = None
        self.b9 = False
        from qgis.utils import reloadPlugin
        reloadPlugin("class1 - PCA for change detection")
    def fonk7(self):
        self.fonk8()
        self.b3.removePluginMenu(self.b8, self.b12)
        self.b3.removePluginMenu(self.b8, self.b13)
        self.b3.removeToolBarIcon(self.b12)
        if class1.b1:
            class1.b1.close()
    @staticmethod
    def fonk8():
        if not class1.b1:
            return
        if class1.b2 and class1.b2.is_dir():
            for file_tmp in class1.b2.glob("*"):
                unload_layer(file_tmp)
        if class1.b2 and os.path.isdir(class1.b2):
            shutil.rmtree(class1.b2, b15 = True)
        class1.b2 = None
        b3.mapCanvas().clearCache()
        b3.mapCanvas().refresh()