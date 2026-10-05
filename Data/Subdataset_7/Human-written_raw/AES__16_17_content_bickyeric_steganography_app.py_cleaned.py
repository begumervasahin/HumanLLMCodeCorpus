import cv2
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
from lsb import LSB
from aes import AESCipher
class class1:
  b1 = tk.Tk()
  b2 = None
  b3 = None
  b4 = None
  b5 = None
  b6 = "./dst.png"
  def fonk1(self):
    self.b1.title('AES + Steganography')
    self.b2 = np.zeros(shape=[100, 100, 3], dtype=np.uint8)
    self.fonk2()
    b7 = tk.Button(self.b1, b15 = 'Open', command = self.openImage)
    b7.pack()
    b8 = tk.Frame(self.b1)
    b8.pack()
    b9 = tk.Button(b8, b15 = 'Encode', command = self.encode)
    b9.pack(b10 = tk.LEFT)
    b11 = tk.Button(b8, b15 = 'Decode', command = self.decode)
    b11.pack(b10 = tk.LEFT)
    b12 = tk.Frame(self.b1)
    b12.pack()
    b13 = tk.Button(b12, b15 = 'Save Image', command = self.saveImage)
    b13.pack(b10 = tk.LEFT)
    b14 = tk.Button(b12, b15 = 'Save Value', command = self.saveValue)
    b14.pack(b10 = tk.LEFT)
    tk.Label(self.b1, b15 = 'Key').pack()
    self.b4 = tk.Entry(self.b1)
    self.b4.pack()
    tk.Label(self.b1, b15 = 'Secret Message').pack()
    self.b5 = tk.Text(self.b1, height=10, width=60)
    self.b5.pack()
  def fonk2(self):
    b2 = cv2.cvtColor(self.b2, cv2.COLOR_BGR2RGB)
    b2 = Image.fromarray(b2)
    b2 = ImageTk.PhotoImage(b2)
    if self.b3 = = None:
      self.b3 = tk.Label(b2=b2)
      self.b3.b2 = b2
      self.b3.pack(b10 = "top", padx=10, pady=10)
    else:
      self.b3.configure(b2 = b2)
      self.b3.b2 = b2
  def fonk3(self):
    b16 = self.b4.get()
    if len(b16) != 16:
      messagebox.showwarning("Warning","Key must be 16 character")
      return
    return AESCipher(self.b4.get())
  def fonk4(self):
    b17 = self.b5.get("1.0",'end-1c')
    if len(b17)%16 != 0:
      b17 += (" " * (16-len(b17)%16))
    b18 = self.fonk3()
    if b18 = = None:
      return
    b19 = b18.encrypt(b17)
    b20 = LSB(self.b2)
    b20.embed(b19)
    self.b5.delete(1.0, tk.END)
    self.b2 = b20.b2
    self.fonk2()
    messagebox.showinfo("Info", "Encoded")
  def fonk5(self):
    b18 = self.fonk3()
    if b18 = = None:
      return
    b20 = LSB(self.b2)
    b19 = b20.extract()
    b21 = b18.decrypt(b19)
    self.b5.delete(1.0, tk.END)
    self.b5.insert(tk.INSERT, b21)
  def fonk6(self):
    b6 = askopenfilename()
    if not isinstance(b6, str):
      return
    self.b2 = cv2.imread(b6)
    self.fonk2()
  def fonk7(self):
    b6 = asksaveasfilename(title = "Select file")
    if b6 = = '':
      return
    np.savetxt(b6+'_blue.csv', self.b2[:, :, 0], b22 = ',', fmt='%d')
    np.savetxt(b6+'_green.csv', self.b2[:, :, 1], b22 = ',', fmt='%d')
    np.savetxt(b6+'_red.csv', self.b2[:, :, 2], b22 = ',', fmt='%d')
    messagebox.showinfo("Info", "Saved")
  def fonk8(self):
    b6 = asksaveasfilename(title = "Select file",filetypes=[("png files", "*.png")])
    if b6 = = '':
      return
    if ".png" not in b6:
      b6 = b6 + ".png"
    b20 = LSB(self.b2)
    b20.save(b6)
    messagebox.showinfo("Info", "Saved")
  def fonk9(self):
    self.b1.mainloop()
if b23 = = "__main__":
  b24 = class1()
  b24.fonk9()