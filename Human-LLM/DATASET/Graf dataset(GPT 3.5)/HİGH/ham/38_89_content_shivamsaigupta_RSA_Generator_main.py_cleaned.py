import tkinter
from tkinter import *
import random
import sys
from GUI_gen import *
from GUI_decrypt import *
from GUI_encrypt import *
sys.setrecursionlimit(1000000)
class class1:
    def fonk1(self):
        self.b1 = GUIGen()
    def fonk2(self):
        self.b2 = GUIE()
    def fonk3(self):
        self.b3 = GUID()
    def fonk4(self):
        self.b4 = Tk()
        self.b5 = Frame(self.b4)
        self.b6 = Label(self.b4, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        self.b7 = Button(self.b4, text="Generate", command=self.gen)
        self.b8 = Button(self.b4, text="Encrypt", command=self.encrypt)
        self.b9 = Button(self.b4, text="Decrypt", command=self.decrypt)
        self.b6.pack()
        self.b7.pack()
        self.b8.pack()
        self.b9.pack()
        self.b4.title("RSA Key Generator by Shivam Sai Gupta")
        self.b4.mainloop()
b10 = class1()