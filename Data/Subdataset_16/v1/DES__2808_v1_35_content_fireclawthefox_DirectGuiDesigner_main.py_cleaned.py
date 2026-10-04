from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
loadPrcFileData(
    "",
)
log_filepath, b1 = setupLog("DirectGuiDesigner")
class class1(ShowBase):
    def fonk1(self):
        ShowBase.fonk1(self)
        self.accept("request_dirty_name", self.set_dirty_name)
        self.accept("request_clean_name", self.set_clean_name)
        self.b2 = DirectGuiDesigner(self.pixel2d)
        self.b2.b3 = log_filepath
        self.b2.b1 = b1
    def fonk2(self):
        b4 = WindowProperties()
        b4.setTitle("*DirectGUI Designer")
        self.win.requestProperties(b4)
    def fonk3(self):
        b4 = WindowProperties()
        b4.setTitle("DirectGUI Designer")
        self.win.requestProperties(b4)
b5 = class1()
b5.run()