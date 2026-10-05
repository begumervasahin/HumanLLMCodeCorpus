from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
loadPrcFileData(
    "",
)
log_filepath, config_file = setupLog("DirectGuiDesigner")
base = ShowBase()
def set_dirty_name():
    window_properties = WindowProperties()
    window_properties.setTitle("*DirectGUI Designer")
    base.win.requestProperties(window_properties)
def set_clean_name():
    window_properties = WindowProperties()
    window_properties.setTitle("DirectGUI Designer")
    base.win.requestProperties(window_properties)
base.accept("request_dirty_name", set_dirty_name)
base.accept("request_clean_name", set_clean_name)
direct_gui_designer = DirectGuiDesigner(base.pixel2d)
direct_gui_designer.log_file = log_filepath
direct_gui_designer.config_file = config_file
base.direct_gui_designer = direct_gui_designer
base.run()