import cv2
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox
from PIL import Image, ImageTk
from lsb import LSB
from aes import AESCipher
class SteganographyApp:
    def __init__(self):
        self.master = tk.Tk()
        self.setup_window()
        self.setup_ui()
    def setup_window(self):
        self.master.title('AES + Steganography')
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.imgPanel = None
    def setup_ui(self):
        tk.Button(self.master, text='Open Image', command=self.open_image).pack()
        frame = tk.Frame(self.master)
        tk.Button(frame, text='Encode', command=self.encode).pack(side=tk.LEFT)
        tk.Button(frame, text='Decode', command=self.decode).pack(side=tk.LEFT)
        frame.pack()
        frame_save = tk.Frame(self.master)
        tk.Button(frame_save, text='Save Image', command=self.save_image).pack(side=tk.LEFT)
        tk.Button(frame_save, text='Save Values', command=self.save_values).pack(side=tk.LEFT)
        frame_save.pack()
        tk.Label(self.master, text='Key').pack()
        self.keyInput = tk.Entry(self.master)
        self.keyInput.pack()
        tk.Label(self.master, text='Secret Message').pack()
        self.messageInput = tk.Text(self.master, height=10, width=60)
        self.messageInput.pack()
        self.update_image_display()
    def update_image_display(self):
        img_to_display = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        imgtk = ImageTk.PhotoImage(image=img_to_display)
        if self.imgPanel is None:
            self.imgPanel = tk.Label(self.master, image=imgtk)
            self.imgPanel.image = imgtk
            self.imgPanel.pack(side="top", padx=10, pady=10)
        else:
            self.imgPanel.configure(image=imgtk)
            self.imgPanel.image = imgtk
    def get_cipher(self):
        key = self.keyInput.get()
        if len(key) != 16:
            messagebox.showwarning("Warning", "Key must be 16 characters long")
            return None
        return AESCipher(key)
    def encode(self):
        message = self.messageInput.get("1.0", 'end-1c')
        message += " " * ((16 - len(message) % 16) % 16)
        cipher = self.get_cipher()
        if not cipher:
            return
        cipher_text = cipher.encrypt(message)
        lsb = LSB(self.image)
        lsb.embed(cipher_text)
        self.image = lsb.image
        self.messageInput.delete(1.0, tk.END)
        self.update_image_display()
        messagebox.showinfo("Info", "Message encoded successfully!")
    def decode(self):
        cipher = self.get_cipher()
        if not cipher:
            return
        lsb = LSB(self.image)
        cipher_text = lsb.extract()
        message = cipher.decrypt(cipher_text)
        self.messageInput.delete(1.0, tk.END)
        self.messageInput.insert(tk.INSERT, message)
    def open_image(self):
        path = askopenfilename()
        if path:
            self.image = cv2.imread(path)
            self.update_image_display()
    def save_values(self):
        path = asksaveasfilename(title="Select file")
        if path:
            for color, name in zip(range(3), ['blue', 'green', 'red']):
                np.savetxt(f'{path}_{name}.csv', self.image[:, :, color], delimiter=',', fmt='%d')
            messagebox.showinfo("Info", "RGB values saved successfully!")
    def save_image(self):
        path = asksaveasfilename(title="Select file", filetypes=[("PNG files", "*.png")])
        if path:
            if not path.endswith(".png"):
                path += ".png"
            cv2.imwrite(path, self.image)
            messagebox.showinfo("Info", "Image saved successfully!")
    def run(self):
        self.master.mainloop()
if __name__ == "__main__":
    app = SteganographyApp()
    app.run()