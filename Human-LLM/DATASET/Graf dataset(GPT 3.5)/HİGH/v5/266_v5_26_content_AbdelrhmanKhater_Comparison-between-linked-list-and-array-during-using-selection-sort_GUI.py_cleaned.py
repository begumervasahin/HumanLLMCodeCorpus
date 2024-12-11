from tkinter import Tk, Button, Label, Entry
from main import automatic, Selection_Sort_Array
class class1(Tk):
    def fonk1(self):
        super().fonk1()
        self.title("Comparison")
        self.geometry("300x300")
        self.fonk2()
    def fonk2(self):
        self.b1 = Button(self, text="Automatic", bg="blue", command=automatic)
        self.b1.place(b2 = 60, y=140)
        self.b3 = Button(self, text="Manual", bg="blue", command=self.open_manual)
        self.b3.place(b2 = 180, y=140)
    def fonk3(self):
        self.b4 = Tk()
        self.b4.geometry("250x250")
        self.b4.title("Manual")
        self.fonk4()
    def fonk4(self):
        self.b5 = Label(self.b4, text="Size", fg="white", bd=5, bg="black")
        self.b5.place(b2 = 50, y=90)
        self.b6 = Entry(self.b4, bd=5)
        self.b6.place(b2 = 110, y=90)
        self.b7 = Label(self.b4, text="Inputs", fg="white", bd=5, bg="black")
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
        b15 = " ".join(map(str, b14))
        self.b10.insert(0, b15)
b16 = class1()
b16.mainloop()