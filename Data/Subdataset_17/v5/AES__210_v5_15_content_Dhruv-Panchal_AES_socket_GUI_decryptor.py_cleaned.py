
from tkinter import *
import socket
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
        self.update_label(self.listen_label, f"Listening on port: {port}", row=2, column=0, columnspan=2)
        server_socket = socket.socket()
        server_socket.bind(('', port))
        server_socket.listen(5)
        client_socket, _ = server_socket.accept()
        self.cipher_text = client_socket.recv(1024)
        self.iv = client_socket.recv(1024)
        self.update_label(self.message_label, f"Incoming encrypted message: {self.cipher_text}", row=4, column=0, columnspan=2)
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
        self.update_label(self.decrypted_message_label, f"Your decrypted message is: {plain_text}", row=8, column=0, columnspan=2)
    def update_label(self, label, text, **grid_options):
        if label:
            label.destroy()
        label = Label(self, text=text)
        label.grid(**grid_options)
        return label
if __name__ == "__main__":
    root = Tk()
    root.geometry("600x300")
    app = DecryptorApp(master=root)
    root.mainloop()