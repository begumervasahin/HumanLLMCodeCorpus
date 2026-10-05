from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
loadPrcFileData(
    "",
)
log_filepath, b1 = setupLog("DirectGuiDesigner")
b2 = ShowBase()
def fonk1():
    b3 = WindowProperties()
    b3.setTitle("*DirectGUI Designer")
    b2.win.requestProperties(b3)
def fonk2():
    b3 = WindowProperties()
    b3.setTitle("DirectGUI Designer")
    b2.win.requestProperties(b3)
b2.accept("request_dirty_name", set_dirty_name)
b2.accept("request_clean_name", set_clean_name)
b4 = DirectGuiDesigner(b2.pixel2d)
b4.b5 = log_filepath
b4.b1 = b1
b2.b4 = b4
b2.run()