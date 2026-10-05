from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
b1 = loadPrcFileData("", b1)
log_filepath, b2 = setupLog("DirectGuiDesigner")
b3 = ShowBase()
def fonk1():
    fonk3("*DirectGUI Designer")
def fonk2():
    fonk3("DirectGUI Designer")
def fonk3(title):
    b4 = WindowProperties()
    b4.setTitle(title)
    b3.win.requestProperties(b4)
b3.accept("request_dirty_name", set_dirty_name)
b3.accept("request_clean_name", set_clean_name)
b5 = DirectGuiDesigner(b3.pixel2d)
b5.b6 = log_filepath
b5.b2 = b2
b3.b5 = b5
b3.run()