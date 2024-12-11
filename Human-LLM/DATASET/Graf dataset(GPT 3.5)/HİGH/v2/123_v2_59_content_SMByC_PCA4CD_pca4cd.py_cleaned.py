
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
from pca4cd.gui.b7 import AboutDialog
from pca4cd.utils.qgis_utils import unload_layer
class class1:
    b1 = None
    b2 = None
    def fonk1(self, b3):
        self.b3 = b3
        self.b4 = os.path.dirname(__file__)
        self.fonk2()
        self.b5 = self.fonk3("class1 - PCA for change detection")
        self.b6 = False
        class1.b1 = None
        self.b7 = AboutDialog()
    def fonk2(self):
        b8 = QSettings().value('b8/userLocale')[0:2]
        b9 = Path(self.b4, 'i18n', f'PCA4CD_{b8}.qm')
        if os.path.exists(b9):
            self.b10 = QTranslator()
            self.b10.load(b9)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.b10)
    def fonk3(self, message):
        return QCoreApplication.translate('class1', message)
    def fonk4(self):
        self.fonk5()
        self.fonk6()
    def fonk5(self):
        b11 = ':/plugins/pca4cd/icons/pca4cd.svg'
        self.b12 = QAction(QIcon(b11), "class1", self.b3.mainWindow())
        self.b12.triggered.connect(self.run)
        self.b3.addToolBarIcon(self.b12)
    def fonk6(self):
        self.b13 = QAction(QIcon(':/plugins/pca4cd/icons/about.svg'), self.fonk3('About'), self.b3.mainWindow())
        self.b13.triggered.connect(self.about)
        self.b3.addPluginToMenu(self.b5, self.b12)
        self.b3.addPluginToMenu(self.b5, self.b13)
    def fonk7(self):
        self.b7.show()
    def fonk8(self):
        if not self.b6:
            self.fonk9()
        else:
            self.fonk10()
    def fonk9(self):
        self.b6 = True
        if class1.b1 is None:
            class1.b1 = PCA4CDDialog()
        class1.b2 = Path(tempfile.mkdtemp())
        class1.b1.closingPlugin.connect(self.onClosePlugin)
        class1.b1.show()
        b14 = class1.b1.exec_()
        if b14:
            pass
    def fonk10(self):
        if hasattr(class1.b1, "main_analysis_dialog") and class1.b1.main_analysis_dialog:
            b1 = class1.b1.main_analysis_dialog
        else:
            b1 = class1.b1
        b1.setWindowState(b1.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
        b1.raise_()
        b1.activateWindow()
    def fonk11(self):
        self.fonk12()
        from qgis.utils import reloadPlugin
        reloadPlugin("class1 - PCA for change detection")
    def fonk12(self):
        self.fonk13()
        class1.b1.closingPlugin.disconnect(self.onClosePlugin)
        class1.b1.close()
        class1.b1 = None
        self.b6 = False
    def fonk13(self):
        if class1.b1:
            if class1.b2 and class1.b2.is_dir():
                for file_tmp in class1.b2.glob("*"):
                    unload_layer(file_tmp)
            if class1.b2 and os.path.isdir(class1.b2):
                shutil.rmtree(class1.b2, b15 = True)
            class1.b2 = None
            b3.mapCanvas().clearCache()
            b3.mapCanvas().refresh()