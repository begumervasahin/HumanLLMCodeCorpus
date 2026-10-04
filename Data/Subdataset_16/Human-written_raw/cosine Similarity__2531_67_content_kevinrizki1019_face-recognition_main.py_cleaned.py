from tkinter import  *
from tkinter import ttk, filedialog
from pageone import *
b1 = ("Verdana", 16)
class class1(Tk):
    b2 = None
    def fonk1(self, *args, **kwargs):
        global db_path
        Tk.fonk1(self, *args, **kwargs)
        Tk.wm_title(self, "KetokMagicHalal")
        b3 = Frame(self)
        b3.pack(b4 = "top", fill="both", expand = True)
        self.b5 = {}
        for F in ([PageOne]):
            b6 = F(b3, self)
            self.b5[F] = b6
            b6.pack_forget()
        self.fonk2(PageOne)
        self.b2.load_db(db_path)
    def fonk2(self, cont):
        if self.b2 is not None:
            self.b2.pack_forget()
        self.b2 = self.b5[cont]
        self.b2.pack(b4 = TOP, fill=BOTH, expand=True, padx = 20, pady= 20)
if b7 = = '__main__':
    b8 = class1()
    b8.geometry("800x600")
    b8.mainloop()