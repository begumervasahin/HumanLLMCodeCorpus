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
        super().fonk1()
        self.b2 = DirectGuiDesigner(self.pixel2d)
        self.b2.b3 = log_filepath
        self.b2.b1 = b1
        self.accept("request_dirty_name", self.set_dirty_name)
        self.accept("request_clean_name", self.set_clean_name)
    def fonk2(self):
        """
        Set the window title to indicate a "dirty" state.
        """
        b4 = WindowProperties()
        b4.setTitle("*DirectGUI Designer")
        self.win.requestProperties(b4)
    def fonk3(self):
        """
        Set the window title to indicate a "clean" state.
        """
        b4 = WindowProperties()
        b4.setTitle("DirectGUI Designer")
        self.win.requestProperties(b4)
if b5 = = "__main__":
    b6 = class1()
    b6.run()