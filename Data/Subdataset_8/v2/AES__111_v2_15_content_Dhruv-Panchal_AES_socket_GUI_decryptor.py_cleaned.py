import socket
from Crypto.Cipher import AES
from Crypto import Random
from tkinter import *
class DecryptorWindow(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("DECRYPTOR")
        self.pack(fill=BOTH, expand=True)
        port_label = Label(self, text="Port")
        port_label.grid(row=0, column=0)
        self.port_entry = Entry(self)
        self.port_entry.grid(row=0, column=1)
        start_server_button = Button(self, text="Start server", command=self.start_server)
        start_server_button.grid(row=1, column=1)
        self.listen_message_label = Label(self, text="")
        self.listen_message_label.grid(row=2, column=0, columnspan=3)
        self.message_received_label = Label(self, text="")
        self.message_received_label.grid(row=4, column=0, columnspan=3, rowspan=2)
        self.key_label = Label(self, text="Enter decryption key")
        self.key_label.grid(row=6, column=0)
        self.key_entry = Entry(self)
        self.key_entry.grid(row=6, column=1)
        decrypt_button = Button(self, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(row=7, column=1)
    def start_server(self):
        port = int(self.port_entry.get())
        self.listen_message_label.config(text="Listening on port: " + str(port))
        server_socket = socket.socket()
        server_socket.bind(('', port))
        server_socket.listen(5)
        client_socket, addr = server_socket.accept()
        cipher = client_socket.recv(1024)
        iv = client_socket.recv(9999)
        self.message_received_label.config(text="Incoming encrypted message: " + str(cipher))
        self.decryption_suite = AES.new(self.key_entry.get().ljust(16, 'X'), AES.MODE_CFB, iv)
    def decrypt(self):
        key = self.key_entry.get().ljust(16, 'X')
        plain_text = self.decryption_suite.decrypt(cipher)
        decrypt_message = Label(self, text="Your decrypted message is " + str(plain_text))
        decrypt_message.grid(row=8, column=0, columnspan=3, rowspan=2)
root = Tk()
root.geometry("600x300")
app = DecryptorWindow(root)
root.mainloop()