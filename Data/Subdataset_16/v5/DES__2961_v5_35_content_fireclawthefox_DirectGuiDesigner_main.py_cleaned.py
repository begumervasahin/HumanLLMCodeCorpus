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
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        self.b2 = DirectGuiDesigner(self.pixel2d)
        self.b2.b3 = log_filepath
        self.b2.b1 = b1
    def fonk3(self):
        self.accept("request_dirty_name", self.set_dirty_name)
        self.accept("request_clean_name", self.set_clean_name)
    def fonk4(self):
        """
        Set the window title to indicate a "dirty" state.
        """
        self.fonk6("*DirectGUI Designer")
    def fonk5(self):
        """
        Set the window title to indicate a "clean" state.
        """
        self.fonk6("DirectGUI Designer")
    def fonk6(self, title):
        b4 = WindowProperties()
        b4.setTitle(title)
        self.win.requestProperties(b4)
def fonk7():
    b5 = class1()
    b5.run()
if b6 = = "__main__":
    fonk7()