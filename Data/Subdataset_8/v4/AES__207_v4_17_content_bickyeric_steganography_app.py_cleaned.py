import cv2
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
from lsb import LSB
from aes import AESCipher
class Activity:
    def __init__(self):
        self.master = tk.Tk()
        self.master.title('AES + Steganography')
        self.image = np.zeros(shape=[100, 100, 3], dtype=np.uint8)
        self.imgPanel = None
        self.initialize_ui()
        self.update_image()
    def initialize_ui(self):
        openBtn = tk.Button(self.master, text='Open', command=self.open_image)
        openBtn.pack()
        btnFrame = tk.Frame(self.master)
        btnFrame.pack()
        encodeBtn = tk.Button(btnFrame, text='Encode', command=self.encode)
        encodeBtn.pack(side=tk.LEFT)
        decodeBtn = tk.Button(btnFrame, text='Decode', command=self.decode)
        decodeBtn.pack(side=tk.LEFT)
        savebtnFrame = tk.Frame(self.master)
        savebtnFrame.pack()
        saveBtn = tk.Button(savebtnFrame, text='Save Image', command=self.save_image)
        saveBtn.pack(side=tk.LEFT)
        saveValueBtn = tk.Button(savebtnFrame, text='Save Value', command=self.save_value)
        saveValueBtn.pack(side=tk.LEFT)
        tk.Label(self.master, text='Key').pack()
        self.keyInput = tk.Entry(self.master)
        self.keyInput.pack()
        tk.Label(self.master, text='Secret Message').pack()
        self.messageInput = tk.Text(self.master, height=10, width=60)
        self.messageInput.pack()
    def update_image(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
        if self.imgPanel is None:
            self.imgPanel = tk.Label(image=image)
            self.imgPanel.image = image
            self.imgPanel.pack(side="top", padx=10, pady=10)
        else:
            self.imgPanel.configure(image=image)
            self.imgPanel.image = image
    def cipher(self):
        key = self.keyInput.get()
        if len(key) != 16:
            messagebox.showwarning("Warning", "Key must be 16 characters long")
            return None
        return AESCipher(key)
    def encode(self):
        message = self.messageInput.get("1.0", 'end-1c')
        if len(message) % 16 != 0:
            message += (" " * (16 - len(message) % 16))
        cipher = self.cipher()
        if cipher is None:
            return
        cipherText = cipher.encrypt(message)
        obj = LSB(self.image)
        obj.embed(cipherText)
        self.messageInput.delete(1.0, tk.END)
        self.image = obj.image
        self.update_image()
        messagebox.showinfo("Info", "Message encoded successfully!")
    def decode(self):
        cipher = self.cipher()
        if cipher is None:
            return
        obj = LSB(self.image)
        cipherText = obj.extract()
        msg = cipher.decrypt(cipherText)
        self.messageInput.delete(1.0, tk.END)
        self.messageInput.insert(tk.INSERT, msg)
    def open_image(self):
        path = askopenfilename()
        if path:
            self.image = cv2.imread(path)
            self.update_image()
    def save_value(self):
        path = asksaveasfilename(title="Select file")
        if path:
            np.savetxt(f'{path}_blue.csv', self.image[:, :, 0], delimiter=',', fmt='%d')
            np.savetxt(f'{path}_green.csv', self.image[:, :, 1], delimiter=',', fmt='%d')
            np.savetxt(f'{path}_red.csv', self.image[:, :, 2], delimiter=',', fmt='%d')
            messagebox.showinfo("Info", "RGB values saved successfully!")
    def save_image(self):
        path = asksaveasfilename(title="Select file", filetypes=[("PNG files", "*.png")])
        if path:
            if not path.endswith(".png"):
                path += ".png"
            cv2.imwrite(path, self.image)
            messagebox.showinfo("Info", "Image saved successfully!")
    def start_loop(self):
        self.master.mainloop()
if __name__ == "__main__":
    app = Activity()
    app.start_loop()