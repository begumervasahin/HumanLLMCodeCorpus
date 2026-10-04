
import socket
from tkinter import *
from Crypto.Cipher import AES
class DecryptorApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.master.title("DECRYPTOR")
        Label(self, text="Port").grid(row=0, column=0, padx=10, pady=5)
        self.port_entry = Entry(self)
        self.port_entry.grid(row=0, column=1, padx=10, pady=5)
        Button(self, text="Start Server", command=self.start_server).grid(row=1, column=1, padx=10, pady=5)
        self.listen_label = None
        self.message_label = None
        self.decryption_key_entry = None
        self.decrypt_btn = None
        self.decrypted_message_label = None
    def start_server(self):
        port = int(self.port_entry.get())
        if self.listen_label:
            self.listen_label.destroy()
        self.listen_label = Label(self, text=f"Listening on port: {port}")
        self.listen_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        server_socket = socket.socket()
        server_socket.bind(('', port))
        server_socket.listen(5)
        client_socket, _ = server_socket.accept()
        self.cipher_text = client_socket.recv(1024)
        self.iv = client_socket.recv(1024)
        if self.message_label:
            self.message_label.destroy()
        self.message_label = Label(self, text=f"Incoming encrypted message: {self.cipher_text}")
        self.message_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
        Label(self, text="Enter decryption key").grid(row=6, column=0, padx=10, pady=5)
        self.decryption_key_entry = Entry(self)
        self.decryption_key_entry.grid(row=6, column=1, padx=10, pady=5)
        if self.decrypt_btn:
            self.decrypt_btn.destroy()
        self.decrypt_btn = Button(self, text="Decrypt", command=self.decrypt_message)
        self.decrypt_btn.grid(row=7, column=1, padx=10, pady=5)
    def decrypt_message(self):
        key = self.decryption_key_entry.get()
        key = (key + (16 - len(key) % 16) * 'X').encode('utf-8')
        decryption_suite = AES.new(key, AES.MODE_CFB, self.iv)
        plain_text = decryption_suite.decrypt(self.cipher_text).decode('utf-8')
        if self.decrypted_message_label:
            self.decrypted_message_label.destroy()
        self.decrypted_message_label = Label(self, text=f"Your decrypted message is: {plain_text}")
        self.decrypted_message_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
if __name__ == "__main__":
    root = Tk()
    root.geometry("600x300")
    app = DecryptorApp(master=root)
    root.mainloop()