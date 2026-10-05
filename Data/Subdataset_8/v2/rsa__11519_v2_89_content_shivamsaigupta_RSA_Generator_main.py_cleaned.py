import tkinter as tk
from tkinter import *
import random
import sys
class GUIGen:
    def __init__(self):
        pass
class GUIE:
    def __init__(self):
        pass
class GUID:
    def __init__(self):
        pass
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = Frame(self.root)
        self.label = Label(self.root, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        self.button1 = Button(self.root, text="Generate", command=self.generate_rsa_keys)
        self.button2 = Button(self.root, text="Encrypt", command=self.encrypt_message)
        self.button3 = Button(self.root, text="Decrypt", command=self.decrypt_message)
        self.label.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.root.title("RSA Key Generator by Shivam Sai Gupta")
        self.root.mainloop()
    def generate_rsa_keys(self):
        self.rsa_key_generator = GUIGen()
    def encrypt_message(self):
        self.message_encrypter = GUIE()
    def decrypt_message(self):
        self.message_decrypter = GUID()
if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    my_gui = GUI()