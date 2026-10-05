import tkinter as tk
from tkinter import *
import sys
from GUI_gen import GUIGen
from GUI_decrypt import GUID
from GUI_encrypt import GUIE
sys.setrecursionlimit(1000000)
class class1:
    def fonk1(self):
        self.b1 = tk.Tk()
        self.fonk2()
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.fonk5()
        self.b1.mainloop()
    def fonk3(self):
        self.b2 = tk.Label(self.b1, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        self.b3 = tk.Button(self.b1, text="Generate", command=self.generate_rsa_keys)
        self.b4 = tk.Button(self.b1, text="Encrypt", command=self.encrypt_message)
        self.b5 = tk.Button(self.b1, text="Decrypt", command=self.decrypt_message)
    def fonk4(self):
        self.b2.pack()
        self.b3.pack()
        self.b4.pack()
        self.b5.pack()
    def fonk5(self):
        self.b1.title("RSA Key Generator by Shivam Sai Gupta")
    def fonk6(self):
        b6 = GUIGen()
    def fonk7(self):
        b7 = GUIE()
    def fonk8(self):
        b8 = GUID()
b9 = class1()