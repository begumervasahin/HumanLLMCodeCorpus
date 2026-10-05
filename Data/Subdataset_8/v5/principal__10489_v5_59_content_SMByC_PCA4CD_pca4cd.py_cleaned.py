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
class PCA4CDPlugin:
    dialog = None
    temporary_directory = None
    is_plugin_active = False
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
        self.menu_name_plugin = self.translate("PCA4CD - PCA for Change Detection")
        self.about_dialog = AboutDialog()
    def translate(self, message):
        return QCoreApplication.translate('PCA4CD', message)
    def initialize_gui(self):
        self.add_tool_bar_icon()
        self.add_menu_actions()
    def add_tool_bar_icon(self):
        icon_path = ':/plugins/pca4cd/icons/pca4cd.svg'
        self.dockable_action = QAction(QIcon(icon_path), "PCA4CD", self.iface.mainWindow())
        self.dockable_action.triggered.connect(self.run_plugin)
        self.iface.addToolBarIcon(self.dockable_action)
    def add_menu_actions(self):
        icon_path = ':/plugins/pca4cd/icons/about.svg'
        self.about_action = QAction(QIcon(icon_path), self.translate('About'), self.iface.mainWindow())
        self.about_action.triggered.connect(self.show_about_dialog)
        self.iface.addPluginToMenu(self.menu_name_plugin, self.about_action)
    def show_about_dialog(self):
        self.about_dialog.show()
    def run_plugin(self):
        if not self.is_plugin_active:
            self.is_plugin_active = True
            if self.dialog is None:
                self.dialog = PCA4CDDialog()
            self.temporary_directory = Path(tempfile.mkdtemp())
            self.dialog.closingPlugin.connect(self.on_close_plugin)
            self.dialog.show()
            result = self.dialog.exec_()
            if result:
                pass
        else:
            self.activate_plugin_dialog()
    def activate_plugin_dialog(self):
        if hasattr(self.dialog, "main_analysis_dialog") and self.dialog.main_analysis_dialog:
            self.dialog.main_analysis_dialog.setWindowState(
                self.dialog.main_analysis_dialog.windowState() & ~Qt.WindowMinimized | Qt.WindowActive
            )
            self.dialog.main_analysis_dialog.raise_()
            self.dialog.main_analysis_dialog.activateWindow()
        else:
            self.dialog.setWindowState(
                self.dialog.windowState() & ~Qt.WindowMinimized | Qt.WindowActive
            )
            self.dialog.raise_()
            self.dialog.activateWindow()
    def on_close_plugin(self):
        self.remove_temporary_files()
        self.dialog.closingPlugin.disconnect(self.on_close_plugin)
        self.dialog.close()
        self.dialog = None
        self.is_plugin_active = False
        from qgis.utils import reloadPlugin
        reloadPlugin("PCA4CD - PCA for Change Detection")
    def unload(self):
        self.remove_temporary_files()
        self.remove_menu_actions()
        self.remove_tool_bar_icon()
        if self.dialog:
            self.dialog.close()
    def remove_menu_actions(self):
        self.iface.removePluginMenu(self.menu_name_plugin, self.dockable_action)
        self.iface.removePluginMenu(self.menu_name_plugin, self.about_action)
    def remove_tool_bar_icon(self):
        self.iface.removeToolBarIcon(self.dockable_action)
    def remove_temporary_files(self):
        if not self.dialog:
            return
        if self.temporary_directory and self.temporary_directory.is_dir():
            for file_tmp in self.temporary_directory.glob("*"):
                unload_layer(file_tmp)
        if self.temporary_directory and os.path.isdir(self.temporary_directory):
            shutil.rmtree(self.temporary_directory, ignore_errors=True)
        self.temporary_directory = None
        iface.mapCanvas().clearCache()
        iface.mapCanvas().refresh()