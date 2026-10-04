
from tkinter import *
import socket
from Crypto.Cipher import AES
class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("DECRYPTOR")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="Port").grid(row=0, column=0)
        self.port_entry = Entry(self)
        self.port_entry.grid(row=0, column=1)
        Button(self, text="Start Server", command=self.start_server).grid(row=1, column=1)
    def start_server(self):
        port = int(self.port_entry.get())
        Label(self, text=f"Listening on port: {port}").grid(row=2, column=0, columnspan=3)
        server_socket = socket.socket()
        server_socket.bind(('', port))
        server_socket.listen(5)
        client_socket, addr = server_socket.accept()
        cipher_text = client_socket.recv(1024)
        iv = client_socket.recv(1024)
        Label(self, text=f"Incoming encrypted message: {cipher_text}").grid(row=4, column=0, columnspan=3, rowspan=2)
        Label(self, text="Enter decryption key").grid(row=6, column=0)
        self.key_entry = Entry(self)
        self.key_entry.grid(row=6, column=1)
        Button(self, text="Decrypt", command=lambda: self.decrypt(cipher_text, iv)).grid(row=7, column=1)
    def decrypt(self, cipher_text, iv):
        key = self.key_entry.get()
        key = (key + (16 - len(key) % 16) * 'X').encode('utf-8')
        decryption_suite = AES.new(key, AES.MODE_CFB, iv)
        plain_text = decryption_suite.decrypt(cipher_text).decode('utf-8')
        Label(self, text=f"Your decrypted message is: {plain_text}").grid(row=8, column=0, columnspan=3, rowspan=2)
root = Tk()
root.geometry("600x300")
app = Window(root)
root.mainloop()