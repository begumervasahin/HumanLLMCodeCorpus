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
        self.b4 = tk.Label(self, text="Choose one system", pady=20)
        self.b4.pack()
        self.b5 = tk.Radiobutton(self, text="Cosine", padx=20, value=1)
        self.b5.pack(b3 = tk.LEFT)
        self.b6 = tk.Radiobutton(self, text="Euclidean distance", padx=20, value=2)
        self.b6.pack(b3 = tk.LEFT)
        self.b7 = tk.Button(self, text="Next", fg="blue", command=self.next_step)
        self.b7.pack(b3 = tk.BOTTOM)
        self.b8 = tk.Button(self, text="Quit", fg="red", command=self.b1.destroy)
        self.b8.pack(b3 = tk.BOTTOM)
    def fonk3(self):
        print('Thank you, b7')
    def fonk4(self):
        b9 = filedialog.askopenfilename(title="Select a photo", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
        if b9:
            print(f'Selected file: {b9}')
        else:
            print('No file selected')
if b10 = = '__main__':
    b11 = tk.Tk()
    b12 = class1(b1=b11)
    b12.mainloop()