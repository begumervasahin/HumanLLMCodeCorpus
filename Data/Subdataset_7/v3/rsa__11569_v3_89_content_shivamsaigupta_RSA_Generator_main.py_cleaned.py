import tkinter as tk
from tkinter import *
class class1:
    def fonk1(self):
        pass
class class2:
    def fonk2(self):
        pass
class class3:
    def fonk3(self):
        pass
class class4:
    def fonk4(self):
        self.b1 = tk.Tk()
        self.fonk5()
        self.fonk6()
        self.fonk7()
        self.fonk8()
        self.fonk9()
    def fonk5(self):
        self.b2 = Frame(self.b1)
    def fonk6(self):
        self.b3 = Label(self.b1, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        self.b4 = Button(self.b1, text="Generate", command=self.generate_rsa_keys)
        self.b5 = Button(self.b1, text="Encrypt", command=self.encrypt_message)
        self.b6 = Button(self.b1, text="Decrypt", command=self.decrypt_message)
    def fonk7(self):
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
        self.b6.pack()
    def fonk8(self):
        self.b1.title("RSA Key Generator by Shivam Sai Gupta")
    def fonk9(self):
        self.b1.mainloop()
    def fonk10(self):
        self.b7 = class1()
    def fonk11(self):
        self.b8 = class2()
    def fonk12(self):
        self.b9 = class3()
if b10 = = "__main__":
    import sys
    sys.setrecursionlimit(1000000)
    b11 = class4()