import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from aes import AESCipher
from lsb import LSB
class SteganographyApp:
    def __init__(self, master):
        self.master = master
        self.master.title('AES + Steganography')
        self.setup_ui()
    def setup_ui(self):
        tk.Button(self.master, text='Open', command=self.open_image).pack()
        frame = tk.Frame(self.master)
        tk.Button(frame, text='Encode', command=self.encode).pack(side=tk.LEFT)
        tk.Button(frame, text='Decode', command=self.decode).pack(side=tk.LEFT)
        frame.pack()
        save_frame = tk.Frame(self.master)
        tk.Button(save_frame, text='Save Image', command=self.save_image).pack(side=tk.LEFT)
        tk.Button(save_frame, text='Save Value', command=self.save_value).pack(side=tk.LEFT)
        save_frame.pack()
        tk.Label(self.master, text='Key').pack()
        self.key_input = tk.Entry(self.master)
        self.key_input.pack()
        tk.Label(self.master, text='Secret Message').pack()
        self.message_input = tk.Text(self.master, height=10, width=50)
        self.message_input.pack()
        self.image = np.zeros((100, 100, 3), dtype=np.uint8)
        self.update_image()
    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.update_image()
    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            cv2.imwrite(file_path, self.image)
            messagebox.showinfo("Success", "Image saved successfully!")
    def save_value(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            np.savetxt(f"{file_path}_blue.csv", self.image[:, :, 0], delimiter=',', fmt='%d')
            np.savetxt(f"{file_path}_green.csv", self.image[:, :, 1], delimiter=',', fmt='%d')
            np.savetxt(f"{file_path}_red.csv", self.image[:, :, 2], delimiter=',', fmt='%d')
            messagebox.showinfo("Success", "Values saved successfully!")
    def encode(self):
        key = self.key_input.get()
        message = self.message_input.get("1.0", tk.END).strip()
        if not key or not message:
            messagebox.showwarning("Warning", "Key and message cannot be empty.")
            return
        cipher = AESCipher(key)
        lsb = LSB(self.image)
        encrypted_message = cipher.encrypt(message)
        lsb.embed(encrypted_message)
        self.image = lsb.image
        self.update_image()
        messagebox.showinfo("Success", "Message encoded successfully!")
    def decode(self):
        key = self.key_input.get()
        if not key:
            messagebox.showwarning("Warning", "Key cannot be empty.")
            return
        cipher = AESCipher(key)
        lsb = LSB(self.image)
        encrypted_message = lsb.extract()
        message = cipher.decrypt(encrypted_message)
        self.message_input.delete(1.0, tk.END)
        self.message_input.insert(tk.END, message)
        messagebox.showinfo("Success", "Message decoded successfully!")
    def update_image(self):
        img = Image.fromarray(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        img_tk = ImageTk.PhotoImage(img)
        img_label = tk.Label(self.master, image=img_tk)
        img_label.image = img_tk
        img_label.pack(side="top", padx=10, pady=10)
def main():
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()