import cv2
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
from b16 import LSB
from aes import AESCipher
class class1:
    def fonk1(self):
        self.b1 = tk.Tk()
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        self.b1.title('AES + Steganography')
        self.b2 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.b3 = None
    def fonk3(self):
        tk.Button(self.b1, b4 = 'Open Image', command=self.open_image).pack()
        b5 = tk.Frame(self.b1)
        tk.Button(b5, b4 = 'Encode', command=self.encode).pack(b11=tk.LEFT)
        tk.Button(b5, b4 = 'Decode', command=self.decode).pack(b11=tk.LEFT)
        b5.pack()
        b6 = tk.Frame(self.b1)
        tk.Button(b6, b4 = 'Save Image', command=self.save_image).pack(b11=tk.LEFT)
        tk.Button(b6, b4 = 'Save Values', command=self.save_values).pack(b11=tk.LEFT)
        b6.pack()
        tk.Label(self.b1, b4 = 'Key').pack()
        self.b7 = tk.Entry(self.b1)
        self.b7.pack()
        tk.Label(self.b1, b4 = 'Secret Message').pack()
        self.b8 = tk.Text(self.b1, height=10, width=60)
        self.b8.pack()
        self.fonk4()
    def fonk4(self):
        b9 = Image.fromarray(cv2.cvtColor(self.b2, cv2.COLOR_BGR2RGB))
        b10 = ImageTk.PhotoImage(b2=b9)
        if self.b3 is None:
            self.b3 = tk.Label(self.b1, b2=b10)
            self.b3.b2 = b10
            self.b3.pack(b11 = "top", padx=10, pady=10)
        else:
            self.b3.configure(b2 = b10)
            self.b3.b2 = b10
    def fonk5(self):
        b12 = self.b7.get()
        if len(b12) != 16:
            messagebox.showwarning("Warning", "Key must be 16 characters long")
            return None
        return AESCipher(b12)
    def fonk6(self):
        b13 = self.b8.get("1.0", 'end-1c')
        b13 += " " * ((16 - len(b13) % 16) % 16)
        b14 = self.fonk5()
        if not b14:
            return
        b15 = b14.encrypt(b13)
        b16 = LSB(self.b2)
        b16.embed(b15)
        self.b2 = b16.b2
        self.b8.delete(1.0, tk.END)
        self.fonk4()
        messagebox.showinfo("Info", "Message encoded successfully!")
    def fonk7(self):
        b14 = self.fonk5()
        if not b14:
            return
        b16 = LSB(self.b2)
        b15 = b16.extract()
        b13 = b14.decrypt(b15)
        self.b8.delete(1.0, tk.END)
        self.b8.insert(tk.INSERT, b13)
    def fonk8(self):
        b17 = askopenfilename()
        if b17:
            self.b2 = cv2.imread(b17)
            self.fonk4()
    def fonk9(self):
        b17 = asksaveasfilename(title="Select file")
        if b17:
            for color, name in zip(range(3), ['blue', 'green', 'red']):
                np.savetxt(f'{b17}_{name}.csv', self.b2[:, :, color], b18 = ',', fmt='%d')
            messagebox.showinfo("Info", "RGB values saved successfully!")
    def fonk10(self):
        b17 = asksaveasfilename(title="Select file", filetypes=[("PNG files", "*.png")])
        if b17:
            if not b17.endswith(".png"):
                b17 += ".png"
            cv2.imwrite(b17, self.b2)
            messagebox.showinfo("Info", "Image saved successfully!")
    def fonk11(self):
        self.b1.mainloop()
if b19 = = "__main__":
    b20 = class1()
    b20.fonk11()