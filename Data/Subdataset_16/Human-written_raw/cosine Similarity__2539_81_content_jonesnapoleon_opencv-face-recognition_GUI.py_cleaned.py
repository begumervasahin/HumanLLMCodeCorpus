import tkinter as tk
from tkinter import filedialog
class class1(tk.Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.pack()
        self.fonk2()
    def fonk2(self):
        self.b2 = tk.Button(self, text="Insert Photo", command=self.take_input)
        self.b2.pack(b3 = tk.TOP)
        self.b4 = tk.Label(self, text="Choose one system", pady=20).pack()
        self.b5 = tk.Radiobutton(self, text="Cosinus", padx=20, value=1)
        self.b5.pack(b3 = tk.LEFT)
        self.b6 = tk.Radiobutton(self, text="Euclidean distance", padx=20, value=2)
        self.b6.pack(b3 = tk.LEFT)
        self.b7 = tk.Button(self, text="Next", fg="blue", command=self.b7)
        self.b7.pack(b3 = tk.BOTTOM)
        self.b8 = tk.Button(self, text="Quit", fg="red", command=self.destroy)
        self.b8.pack(b3 = tk.BOTTOM)
    def fonk3(self):
        print('thankyou b7')
    def fonk4(self):
        print('TAKE INPUT')
        pass