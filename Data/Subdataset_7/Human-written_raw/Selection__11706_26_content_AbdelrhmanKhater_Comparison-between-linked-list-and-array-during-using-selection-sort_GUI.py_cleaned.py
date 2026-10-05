from tkinter import *
from main import *
class class1(Tk):
    def fonk1(self):
        Tk.fonk1(self)
        self.wm_title("Comparison")
        self.geometry("300x300")
        self.b1 = Button(self,bg = "blue", text = "Automatic", command = automatic)
        self.b1.place(b2 = 60, y = 140)
        self.b3 = Button(self, text = "Manual", bg = "blue", command = self.helper)
        self.b3.place(b2 = 180, y = 140)
    def fonk2(self):
        self.b4 = Tk()
        self.b4.geometry("250x250")
        self.b4.wm_title("Manual")
        self.b5 = Label(self.b4, fg = "white" , bd = 5, bg = "black", text= "Size    ")
        self.b5.place(b2 = 50, y = 90)
        self.b6 = Entry(self.b4, bd = 5)
        self.b6.place(b2 = 110, y = 90)
        self.b7 = Label(self.b4, fg = "white", bd = 5, bg = "black", text = "Inputs")
        self.b7.place(b2 = 50, y = 125)
        self.b8 = Entry(self.b4, bd = 5)
        self.b8.place(b2 = 110, y = 125)
        self.b9 = Button(self.b4, text = "Compare", bg = "blue", command = self.manual)
        self.b9.place(b2 = 110, y = 160)
        self.b10 = Entry(self.b4, bd = 5)
        self.b10.place(b2 = 75, y = 190)
        self.b4.mainloop()
    def fonk3(self):
        self.b11 = int(self.b6.get())
        self.b12 = self.b8.get()
        self.b13 = self.b12.split()
        self.b14 = Linkedlist()
        self.b15 = []
        self.b16 = []
        for i in range(0, self.b11):
            self.b15.append(int(self.b13[i]))
            self.b16.append(int(self.b13[i]))
            self.b14.add(int(self.b13[i]))
        self.b15 = Selection_Sort_Array(self.b15)
        self.b17 = ""
        for i in range(len(self.b15)):
            self.b17 += str(self.b15[i]) + " "
        self.b10.insert(0, self.b17)
"""
b18 = Tk()
b18.wm_title("Comparison")
b18.geometry("300x300")
b1 = Button(b18,bg = "blue", text = "Automatic", command = automatic)
b1.place(b2 = 60, y = 140)
b3 = Button(b18, text = "Manual", bg = "blue", command = helper)
b3.place(b2 = 180, y = 140)
b18.mainloop()
"""
b19 = class1()
b19.mainloop()