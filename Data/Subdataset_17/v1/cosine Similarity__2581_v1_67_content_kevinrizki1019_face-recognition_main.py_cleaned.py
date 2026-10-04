from tkinter import *
from tkinter import ttk, filedialog
from pageone import PageOne
LARGE_FONT = ("Verdana", 16)
class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("KetokMagicHalal")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        self.currentFrame = None
        for F in (PageOne,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.pack_forget()
        self.show_frame(PageOne)
    def show_frame(self, cont):
        if self.currentFrame is not None:
            self.currentFrame.pack_forget()
        self.currentFrame = self.frames[cont]
        self.currentFrame.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)
        self.currentFrame.load_db(db_path)
if __name__ == '__main__':
    db_path = 'path/to/your/database'
    app = MainApp()
    app.geometry("800x600")
    app.mainloop()