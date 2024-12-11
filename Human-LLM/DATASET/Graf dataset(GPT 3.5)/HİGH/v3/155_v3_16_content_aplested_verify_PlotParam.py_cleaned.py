import sys
import tkinter as tk
from tkinter import simpledialog
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        self.title('Enter new plot parameters...')
        b1 = ['Min X:', 'Max X:', 'Bin width:', 'Max Y:']
        self.b2 = []
        for b6, label_text in enumerate(b1):
            b3 = tk.Label(master, text=label_text)
            b3.grid(b4 = b6, column=0, sticky=tk.W)
            b5 = tk.Entry(master, justify=tk.CENTER)
            b5.grid(b4 = b6, column=1)
            b5.insert(tk.END, '0' if b6 = = 0 else '10' if b6 == 1 else '1' if b6 == 2 else '1000')
            self.b2.append(b5)
        return self.b2[0]
    def fonk2(self):
        self.b7 = int(self.b2[0].get())
        self.b8 = int(self.b2[1].get())
        self.b9 = int(self.b2[2].get())
        self.b10 = int(self.b2[3].get())
if b11 = = "__main__":
    b12 = tk.Tk()
    b13 = class1(b12)
    print("Min X:", b13.b7)
    print("Max X:", b13.b8)
    print("Bin width:", b13.b9)
    print("Max Y:", b13.b10)
    b12.mainloop()