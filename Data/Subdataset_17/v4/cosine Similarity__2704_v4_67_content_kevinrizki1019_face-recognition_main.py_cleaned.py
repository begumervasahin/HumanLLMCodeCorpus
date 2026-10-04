from tkinter import *
from tkinter import ttk, filedialog
from pageone import PageOne
LARGE_FONT = ("Verdana", 16)
class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("KetokMagicHalal")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        self.current_frame = None
        self._initialize_frames(container)
        self.show_frame(PageOne)
        self.current_frame.load_db(db_path)
    def _initialize_frames(self, container):
        for FrameClass in (PageOne,):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.pack_forget()
    def show_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_class]
        self.current_frame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)
if __name__ == '__main__':
    db_path = 'path/to/your/database'
    app = MainApp()
    app.geometry("800x600")
    app.mainloop()