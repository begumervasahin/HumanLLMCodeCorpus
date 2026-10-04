from direct.showbase.ShowBase import ShowBase
from panda3d.core import loadPrcFileData, WindowProperties
from editorLogHandler import setupLog
from DirectGuiDesigner.DirectGuiDesigner import DirectGuiDesigner
loadPrcFileData(
    "",
)
log_filepath, config_file = setupLog("DirectGuiDesigner")
class DirectGUIDesignerApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.setup_direct_gui_designer()
        self.setup_event_handlers()
    def setup_direct_gui_designer(self):
        self.dgd = DirectGuiDesigner(self.pixel2d)
        self.dgd.log_file = log_filepath
        self.dgd.config_file = config_file
    def setup_event_handlers(self):
        self.accept("request_dirty_name", self.set_dirty_name)
        self.accept("request_clean_name", self.set_clean_name)
    def set_dirty_name(self):
        """
        Set the window title to indicate a "dirty" state.
        """
        self.set_window_title("*DirectGUI Designer")
    def set_clean_name(self):
        """
        Set the window title to indicate a "clean" state.
        """
        self.set_window_title("DirectGUI Designer")
    def set_window_title(self, title):
        wp = WindowProperties()
        wp.setTitle(title)
        self.win.requestProperties(wp)
def main():
    app = DirectGUIDesignerApp()
    app.run()
if __name__ == "__main__":
    main()