import os.path
import shutil
import tempfile
from pathlib import Path
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.utils import b4
from .resources import *
from pca4cd.gui.pca4cd_dialog import PCA4CDDialog
from pca4cd.gui.b10 import AboutDialog
from pca4cd.utils.qgis_utils import unload_layer
class class1:
    b1 = None
    b2 = None
    b3 = False
    def fonk1(self, b4):
        self.b4 = b4
        self.b5 = os.path.dirname(__file__)
        b6 = QSettings().value('b6/userLocale')[0:2]
        b7 = Path(self.b5, 'i18n', f'PCA4CD_{b6}.qm')
        if os.path.exists(b7):
            self.b8 = QTranslator()
            self.b8.load(b7)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.b8)
        self.b9 = self.fonk2("PCA4CD - PCA for Change Detection")
        self.b10 = AboutDialog()
    def fonk2(self, message):
        return QCoreApplication.fonk2('PCA4CD', message)
    def fonk3(self):
        self.fonk4()
        self.fonk5()
    def fonk4(self):
        b11 = ':/plugins/pca4cd/icons/pca4cd.svg'
        self.b12 = QAction(QIcon(b11), "PCA4CD", self.b4.mainWindow())
        self.b12.triggered.connect(self.run_plugin)
        self.b4.addToolBarIcon(self.b12)
    def fonk5(self):
        b11 = ':/plugins/pca4cd/icons/about.svg'
        self.b13 = QAction(QIcon(b11), self.fonk2('About'), self.b4.mainWindow())
        self.b13.triggered.connect(self.show_about_dialog)
        self.b4.addPluginToMenu(self.b9, self.b13)
    def fonk6(self):
        self.b10.show()
    def fonk7(self):
        if not self.b3:
            self.b3 = True
            if self.b1 is None:
                self.b1 = PCA4CDDialog()
            self.b2 = Path(tempfile.mkdtemp())
            self.b1.closingPlugin.connect(self.on_close_plugin)
            self.b1.show()
            b14 = self.b1.exec_()
            if b14:
                pass
        else:
            self.fonk8()
    def fonk8(self):
        if hasattr(self.b1, "main_analysis_dialog") and self.b1.main_analysis_dialog:
            self.b1.main_analysis_dialog.setWindowState(
                self.b1.main_analysis_dialog.windowState() & ~Qt.WindowMinimized | Qt.WindowActive
            )
            self.b1.main_analysis_dialog.raise_()
            self.b1.main_analysis_dialog.activateWindow()
        else:
            self.b1.setWindowState(
                self.b1.windowState() & ~Qt.WindowMinimized | Qt.WindowActive
            )
            self.b1.raise_()
            self.b1.activateWindow()
    def fonk9(self):
        self.fonk13()
        self.b1.closingPlugin.disconnect(self.on_close_plugin)
        self.b1.close()
        self.b1 = None
        self.b3 = False
        from qgis.utils import reloadPlugin
        reloadPlugin("PCA4CD - PCA for Change Detection")
    def fonk10(self):
        self.fonk13()
        self.fonk11()
        self.fonk12()
        if self.b1:
            self.b1.close()
    def fonk11(self):
        self.b4.removePluginMenu(self.b9, self.b12)
        self.b4.removePluginMenu(self.b9, self.b13)
    def fonk12(self):
        self.b4.removeToolBarIcon(self.b12)
    def fonk13(self):
        if not self.b1:
            return
        if self.b2 and self.b2.is_dir():
            for file_tmp in self.b2.glob("*"):
                unload_layer(file_tmp)
        if self.b2 and os.path.isdir(self.b2):
            shutil.rmtree(self.b2, b15 = True)
        self.b2 = None
        b4.mapCanvas().clearCache()
        b4.mapCanvas().refresh()