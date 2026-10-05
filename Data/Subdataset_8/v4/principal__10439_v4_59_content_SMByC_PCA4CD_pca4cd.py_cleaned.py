import os.path
import shutil
import tempfile
from pathlib import Path
from qgis.PyQt.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtGui import QIcon
from qgis.utils import iface
from .resources import *
from pca4cd.gui.pca4cd_dialog import PCA4CDDialog
from pca4cd.gui.about_dialog import AboutDialog
from pca4cd.utils.qgis_utils import unload_layer
class PCA4CD:
    dialog = None
    tmp_dir = None
    pluginIsActive = False
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = Path(self.plugin_dir, 'i18n', f'PCA4CD_{locale}.qm')
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.menu_name_plugin = self.tr("PCA4CD - PCA for Change Detection")
        self.about_dialog = AboutDialog()
    def tr(self, message):
        return QCoreApplication.translate('PCA4CD', message)
    def initGui(self):
        icon_path = ':/plugins/pca4cd/icons/pca4cd.svg'
        self.dockable_action = QAction(QIcon(icon_path), "PCA4CD", self.iface.mainWindow())
        self.dockable_action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.dockable_action)
        self.iface.addPluginToMenu(self.menu_name_plugin, self.dockable_action)
        icon_path = ':/plugins/pca4cd/icons/about.svg'
        self.about_action = QAction(QIcon(icon_path), self.tr('About'), self.iface.mainWindow())
        self.about_action.triggered.connect(self.about)
        self.iface.addPluginToMenu(self.menu_name_plugin, self.about_action)
    def about(self):
        self.about_dialog.show()
    def run(self):
        if not self.pluginIsActive:
            self.pluginIsActive = True
            if PCA4CD.dialog is None:
                PCA4CD.dialog = PCA4CDDialog()
            PCA4CD.tmp_dir = Path(tempfile.mkdtemp())
            PCA4CD.dialog.closingPlugin.connect(self.onClosePlugin)
            PCA4CD.dialog.show()
            result = PCA4CD.dialog.exec_()
            if result:
                pass
        else:
            if hasattr(PCA4CD.dialog, "main_analysis_dialog") and PCA4CD.dialog.main_analysis_dialog:
                PCA4CD.dialog.main_analysis_dialog.setWindowState(PCA4CD.dialog.main_analysis_dialog.windowState()
                                                                  & ~Qt.WindowMinimized | Qt.WindowActive)
                PCA4CD.dialog.main_analysis_dialog.raise_()
                PCA4CD.dialog.main_analysis_dialog.activateWindow()
            else:
                PCA4CD.dialog.setWindowState(PCA4CD.dialog.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
                PCA4CD.dialog.raise_()
                PCA4CD.dialog.activateWindow()
    def onClosePlugin(self):
        self.removes_temporary_files()
        PCA4CD.dialog.closingPlugin.disconnect(self.onClosePlugin)
        PCA4CD.dialog.close()
        PCA4CD.dialog = None
        self.pluginIsActive = False
        from qgis.utils import reloadPlugin
        reloadPlugin("PCA4CD - PCA for Change Detection")
    def unload(self):
        self.removes_temporary_files()
        self.iface.removePluginMenu(self.menu_name_plugin, self.dockable_action)
        self.iface.removePluginMenu(self.menu_name_plugin, self.about_action)
        self.iface.removeToolBarIcon(self.dockable_action)
        if PCA4CD.dialog:
            PCA4CD.dialog.close()
    @staticmethod
    def removes_temporary_files():
        if not PCA4CD.dialog:
            return
        if PCA4CD.tmp_dir and PCA4CD.tmp_dir.is_dir():
            for file_tmp in PCA4CD.tmp_dir.glob("*"):
                unload_layer(file_tmp)
        if PCA4CD.tmp_dir and os.path.isdir(PCA4CD.tmp_dir):
            shutil.rmtree(PCA4CD.tmp_dir, ignore_errors=True)
        PCA4CD.tmp_dir = None
        iface.mapCanvas().clearCache()
        iface.mapCanvas().refresh()