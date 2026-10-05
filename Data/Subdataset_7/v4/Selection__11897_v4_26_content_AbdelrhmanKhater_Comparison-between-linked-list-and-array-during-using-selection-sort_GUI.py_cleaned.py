from tkinter import *
from main import automatic, Selection_Sort_Array, Linkedlist
class class1(Tk):
    def fonk1(self):
        Tk.fonk1(self)
        self.wm_title("Comparison")
        self.geometry("300x300")
        self.fonk2()
    def fonk2(self):
        self.b1 = Button(self, bg="blue", text="Automatic", command=automatic)
        self.b1.place(b2 = 60, y=140)
        self.b3 = Button(self, text="Manual", bg="blue", command=self.open_manual)
        self.b3.place(b2 = 180, y=140)
    def fonk3(self):
        self.b4 = Tk()
        self.b4.geometry("250x250")
        self.b4.wm_title("Manual")
        self.fonk4()
    def fonk4(self):
        self.b5 = Label(self.b4, fg="white", bd=5, bg="black", text="Size")
        self.b5.place(b2 = 50, y=90)
        self.b6 = Entry(self.b4, bd=5)
        self.b6.place(b2 = 110, y=90)
        self.b7 = Label(self.b4, fg="white", bd=5, bg="black", text="Inputs")
        self.b7.place(b2 = 50, y=125)
        self.b8 = Entry(self.b4, bd=5)
        self.b8.place(b2 = 110, y=125)
        self.b9 = Button(self.b4, text="Compare", bg="blue", command=self.compare_manual)
        self.b9.place(b2 = 110, y=160)
        self.b10 = Entry(self.b4, bd=5)
        self.b10.place(b2 = 75, y=190)
    def fonk5(self):
        b11 = int(self.b6.get())
        b12 = self.b8.get().split()
        b13 = [int(num) for num in b12]
        b14 = Selection_Sort_Array(b13)
        b15 = " ".join(str(num) for num in b14)
        self.b10.insert(0, b15)
b16 = class1()
b16.mainloop()