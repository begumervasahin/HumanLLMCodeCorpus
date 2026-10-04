from tkinter import simpledialog, Label, Entry
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        Label(master, b1 = "x:").grid(b4=0)
        Label(master, b1 = "y:").grid(b4=1)
        self.b2 = Entry(master)
        self.b3 = Entry(master)
        self.b2.grid(b4 = 0, column=1)
        self.b3.grid(b4 = 1, column=1)
    def fonk2(self):
        b5 = self.b2.get ()
        b6 = self.b3.get ()
        self.b7 = b5, b6