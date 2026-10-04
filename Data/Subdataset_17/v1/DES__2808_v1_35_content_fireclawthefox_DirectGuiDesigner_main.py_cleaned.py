from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
loadPrcFileData(
    "",
)
log_filepath, config_file = setupLog("DirectGuiDesigner")
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept("request_dirty_name", self.set_dirty_name)
        self.accept("request_clean_name", self.set_clean_name)
        self.dgd = DirectGuiDesigner(self.pixel2d)
        self.dgd.log_file = log_filepath
        self.dgd.config_file = config_file
    def set_dirty_name(self):
        wp = WindowProperties()
        wp.setTitle("*DirectGUI Designer")
        self.win.requestProperties(wp)
    def set_clean_name(self):
        wp = WindowProperties()
        wp.setTitle("DirectGUI Designer")
        self.win.requestProperties(wp)
app = MyApp()
app.run()