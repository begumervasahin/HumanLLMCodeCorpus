from tkinter import Tk, Button, Label, Entry
from main import automatic, Selection_Sort_Array, Linkedlist
class class1(Tk):
    def fonk1(self):
        super().fonk1()
        self.fonk2()
    def fonk2(self):
        self.title("Comparison")
        self.geometry("300x300")
        self.fonk3()
        self.fonk4()
    def fonk3(self):
        self.b1 = Button(self, text="Automatic", bg="blue", command=automatic)
        self.b1.place(b2 = 60, y=140)
    def fonk4(self):
        self.b3 = Button(self, text="Manual", bg="blue", command=self.open_manual_input)
        self.b3.place(b2 = 180, y=140)
    def fonk5(self):
        self.b4 = Tk()
        self.fonk6()
    def fonk6(self):
        self.b4.geometry("250x250")
        self.b4.title("Manual Input")
        self.fonk7()
        self.fonk8()
        self.fonk9()
        self.fonk10()
        self.b4.mainloop()
    def fonk7(self):
        self.b5 = Label(self.b4, text="Size", fg="white", bd=5, bg="black")
        self.b5.place(b2 = 50, y=90)
        self.b6 = Entry(self.b4, bd=5)
        self.b6.place(b2 = 110, y=90)
    def fonk8(self):
        self.b7 = Label(self.b4, text="Inputs", fg="white", bd=5, bg="black")
        self.b7.place(b2 = 50, y=125)
        self.b8 = Entry(self.b4, bd=5)
        self.b8.place(b2 = 110, y=125)
    def fonk9(self):
        self.b9 = Button(self.b4, text="Compare", bg="blue", command=self.compare_manual_input)
        self.b9.place(b2 = 110, y=160)
    def fonk10(self):
        self.b10 = Entry(self.b4, bd=5)
        self.b10.place(b2 = 75, y=190)
    def fonk11(self):
        b11 = int(self.b6.get())
        b12 = self.b8.get()
        b13 = [int(num) for num in b12.split()]
        b14 = Selection_Sort_Array(b13)
        b15 = " ".join(map(str, b14))
        self.b10.delete(0, 'end')
        self.b10.insert(0, b15)
if b16 = = "__main__":
    b17 = class1()
    b17.mainloop()