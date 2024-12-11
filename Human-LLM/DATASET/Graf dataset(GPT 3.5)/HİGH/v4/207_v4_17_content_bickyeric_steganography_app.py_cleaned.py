import cv2
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
from lsb import LSB
from aes import AESCipher
class class1:
    def fonk1(self):
        self.b1 = tk.Tk()
        self.b1.title('AES + Steganography')
        self.b2 = np.zeros(shape=[100, 100, 3], dtype=np.uint8)
        self.b3 = None
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        b4 = tk.Button(self.b1, b12='Open', command=self.open_image)
        b4.pack()
        b5 = tk.Frame(self.b1)
        b5.pack()
        b6 = tk.Button(b5, b12='Encode', command=self.encode)
        b6.pack(b7 = tk.LEFT)
        b8 = tk.Button(b5, b12='Decode', command=self.decode)
        b8.pack(b7 = tk.LEFT)
        b9 = tk.Frame(self.b1)
        b9.pack()
        b10 = tk.Button(b9, b12='Save Image', command=self.save_image)
        b10.pack(b7 = tk.LEFT)
        b11 = tk.Button(b9, b12='Save Value', command=self.save_value)
        b11.pack(b7 = tk.LEFT)
        tk.Label(self.b1, b12 = 'Key').pack()
        self.b13 = tk.Entry(self.b1)
        self.b13.pack()
        tk.Label(self.b1, b12 = 'Secret Message').pack()
        self.b14 = tk.Text(self.b1, height=10, width=60)
        self.b14.pack()
    def fonk3(self):
        b2 = cv2.cvtColor(self.b2, cv2.COLOR_BGR2RGB)
        b2 = Image.fromarray(b2)
        b2 = ImageTk.PhotoImage(b2)
        if self.b3 is None:
            self.b3 = tk.Label(b2=b2)
            self.b3.b2 = b2
            self.b3.pack(b7 = "top", padx=10, pady=10)
        else:
            self.b3.configure(b2 = b2)
            self.b3.b2 = b2
    def fonk4(self):
        b15 = self.b13.get()
        if len(b15) != 16:
            messagebox.showwarning("Warning", "Key must be 16 characters long")
            return None
        return AESCipher(b15)
    def fonk5(self):
        b16 = self.b14.get("1.0", 'end-1c')
        if len(b16) % 16 != 0:
            b16 += (" " * (16 - len(b16) % 16))
        b17 = self.fonk4()
        if b17 is None:
            return
        b18 = b17.encrypt(b16)
        b19 = LSB(self.b2)
        b19.embed(b18)
        self.b14.delete(1.0, tk.END)
        self.b2 = b19.b2
        self.fonk3()
        messagebox.showinfo("Info", "Message encoded successfully!")
    def fonk6(self):
        b17 = self.fonk4()
        if b17 is None:
            return
        b19 = LSB(self.b2)
        b18 = b19.extract()
        b20 = b17.decrypt(b18)
        self.b14.delete(1.0, tk.END)
        self.b14.insert(tk.INSERT, b20)
    def fonk7(self):
        b21 = askopenfilename()
        if b21:
            self.b2 = cv2.imread(b21)
            self.fonk3()
    def fonk8(self):
        b21 = asksaveasfilename(title="Select file")
        if b21:
            np.savetxt(f'{b21}_blue.csv', self.b2[:, :, 0], b22 = ',', fmt='%d')
            np.savetxt(f'{b21}_green.csv', self.b2[:, :, 1], b22 = ',', fmt='%d')
            np.savetxt(f'{b21}_red.csv', self.b2[:, :, 2], b22 = ',', fmt='%d')
            messagebox.showinfo("Info", "RGB values saved successfully!")
    def fonk9(self):
        b21 = asksaveasfilename(title="Select file", filetypes=[("PNG files", "*.png")])
        if b21:
            if not b21.endswith(".png"):
                b21 += ".png"
            cv2.imwrite(b21, self.b2)
            messagebox.showinfo("Info", "Image saved successfully!")
    def fonk10(self):
        self.b1.mainloop()
if b23 = = "__main__":
    b24 = class1()
    b24.fonk10()