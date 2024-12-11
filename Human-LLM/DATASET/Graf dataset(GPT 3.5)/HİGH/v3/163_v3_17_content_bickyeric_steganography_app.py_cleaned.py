import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from aes import AESCipher
from b13 import LSB
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b1.title('AES + Steganography')
        self.fonk2()
    def fonk2(self):
        self.fonk3()
        self.fonk4()
        self.fonk5()
        self.fonk6()
        self.fonk7()
        self.fonk8()
    def fonk3(self):
        tk.Button(self.b1, b2 = 'Open', command=self.open_image).pack()
    def fonk4(self):
        b3 = tk.Frame(self.b1)
        tk.Button(b3, b2 = 'Encode', command=self.encode).pack(b18=tk.LEFT)
        tk.Button(b3, b2 = 'Decode', command=self.decode).pack(b18=tk.LEFT)
        b3.pack()
    def fonk5(self):
        b4 = tk.Frame(self.b1)
        tk.Button(b4, b2 = 'Save Image', command=self.save_image).pack(b18=tk.LEFT)
        tk.Button(b4, b2 = 'Save Value', command=self.save_value).pack(b18=tk.LEFT)
        b4.pack()
    def fonk6(self):
        tk.Label(self.b1, b2 = 'Key').pack()
        self.b5 = tk.Entry(self.b1)
        self.b5.pack()
    def fonk7(self):
        tk.Label(self.b1, b2 = 'Secret Message').pack()
        self.b6 = tk.Text(self.b1, height=10, width=50)
        self.b6.pack()
    def fonk8(self):
        self.b7 = np.zeros((100, 100, 3), dtype=np.uint8)
        self.fonk14()
    def fonk9(self):
        b8 = filedialog.askopenfilename()
        if b8:
            self.b7 = cv2.imread(b8)
            self.fonk14()
    def fonk10(self):
        b8 = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if b8:
            cv2.imwrite(b8, self.b7)
            messagebox.showinfo("Success", "Image saved successfully!")
    def fonk11(self):
        b8 = filedialog.asksaveasfilename()
        if b8:
            np.savetxt(f"{b8}_blue.csv", self.b7[:, :, 0], b9 = ',', fmt='%d')
            np.savetxt(f"{b8}_green.csv", self.b7[:, :, 1], b9 = ',', fmt='%d')
            np.savetxt(f"{b8}_red.csv", self.b7[:, :, 2], b9 = ',', fmt='%d')
            messagebox.showinfo("Success", "Values saved successfully!")
    def fonk12(self):
        b10 = self.b5.get()
        b11 = self.b6.get("1.0", tk.END).strip()
        if not b10 or not b11:
            messagebox.showwarning("Warning", "Key and b11 cannot be empty.")
            return
        b12 = AESCipher(b10)
        b13 = LSB(self.b7)
        b14 = b12.encrypt(b11)
        b13.embed(b14)
        self.b7 = b13.b7
        self.fonk14()
        messagebox.showinfo("Success", "Message encoded successfully!")
    def fonk13(self):
        b10 = self.b5.get()
        if not b10:
            messagebox.showwarning("Warning", "Key cannot be empty.")
            return
        b12 = AESCipher(b10)
        b13 = LSB(self.b7)
        b14 = b13.extract()
        b11 = b12.decrypt(b14)
        self.b6.delete(1.0, tk.END)
        self.b6.insert(tk.END, b11)
        messagebox.showinfo("Success", "Message decoded successfully!")
    def fonk14(self):
        b15 = Image.fromarray(cv2.cvtColor(self.b7, cv2.COLOR_BGR2RGB))
        b16 = ImageTk.PhotoImage(b15)
        b17 = tk.Label(self.b1, b7=b16)
        b17.b7 = b16
        b17.pack(b18 = "top", padx=10, pady=10)
def fonk15():
    b19 = tk.Tk()
    class1(b19)
    b19.mainloop()
if b20 = = "__main__":
    fonk15()