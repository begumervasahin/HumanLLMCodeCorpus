from tkinter import *
from tkinter import ttk, filedialog
from pageone import PageOne
b1 = ("Verdana", 16)
class class1(Tk):
    def fonk1(self, *args, **kwargs):
        super().fonk1(*args, **kwargs)
        self.title("KetokMagicHalal")
        b2 = Frame(self)
        b2.pack(b3 = "top", fill="both", expand=True)
        self.b4 = {}
        self.b5 = None
        self.fonk2(b2)
        self.fonk3(PageOne)
    def fonk2(self, b2):
        for FrameClass in (PageOne,):
            b6 = FrameClass(b2, self)
            self.b4[FrameClass] = b6
            b6.pack_forget()
    def fonk3(self, frame_class):
        if self.b5 is not None:
            self.b5.pack_forget()
        self.b5 = self.b4[frame_class]
        self.b5.pack(b3 = TOP, fill=BOTH, expand=True, padx=20, pady=20)
        self.b5.load_db(b8)
if b7 = = '__main__':
    b8 = 'path/to/your/database'
