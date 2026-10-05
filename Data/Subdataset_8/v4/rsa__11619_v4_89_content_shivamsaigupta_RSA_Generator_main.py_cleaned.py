import tkinter
from tkinter import *
import random
import sys
from GUI_gen import GUIGen
from GUI_decrypt import GUID
from GUI_encrypt import GUIE
sys.setrecursionlimit(1000000)
class GUI:
    def generate_rsa_keys(self):
        self.rsa_key_generator = GUIGen()
    def encrypt_message(self):
        self.message_encrypter = GUIE()
    def decrypt_message(self):
        self.message_decrypter = GUID()
    def __init__(self):
        self.root = Tk()
        self.frame = Frame(self.root)
        self.label = Label(self.root, text="RSA Program by Shivam Sai Gupta for Discrete Maths, Prof. Mahavir Jhawar")
        self.generate_button = Button(self.root, text="Generate", command=self.generate_rsa_keys)
        self.encrypt_button = Button(self.root, text="Encrypt", command=self.encrypt_message)
        self.decrypt_button = Button(self.root, text="Decrypt", command=self.decrypt_message)
        self.label.pack()
        self.generate_button.pack()
        self.encrypt_button.pack()
        self.decrypt_button.pack()
        self.root.title("RSA Key Generator by Shivam Sai Gupta")
        self.root.mainloop()
my_gui = GUI()