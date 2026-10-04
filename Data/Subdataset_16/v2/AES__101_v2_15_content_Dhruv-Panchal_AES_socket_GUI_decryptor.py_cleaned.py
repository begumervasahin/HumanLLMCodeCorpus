
import socket
from tkinter import *
from Crypto.Cipher import AES
class class1(Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.b1 = b1
        self.grid()
        self.fonk2()
    def fonk2(self):
        self.b1.title("DECRYPTOR")
        Label(self, b2 = "Port").grid(b4=0, column=0, padx=10, pady=5)
        self.b3 = Entry(self)
        self.b3.grid(b4 = 0, column=1, padx=10, pady=5)
        self.b5 = Button(self, b2="Start Server", command=self.start_server)
        self.b5.grid(b4 = 1, column=1, padx=10, pady=5)
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
        self.b10 = None
    def fonk3(self):
        b11 = int(self.b3.get())
        if self.b6:
            self.b6.destroy()
        self.b6 = Label(self, b2=f"Listening on b11: {b11}")
        self.b6.grid(b4 = 2, column=0, columnspan=2, padx=10, pady=5)
        b12 = socket.socket()
        b12.bind(('', b11))
        b12.listen(5)
        client_socket, b13 = b12.accept()
        self.b14 = client_socket.recv(1024)
        self.b15 = client_socket.recv(1024)
        if self.b7:
            self.b7.destroy()
        self.b7 = Label(self, b2=f"Incoming encrypted message: {self.b14}")
        self.b7.grid(b4 = 4, column=0, columnspan=2, padx=10, pady=5)
        Label(self, b2 = "Enter decryption b16").grid(b4=6, column=0, padx=10, pady=5)
        self.b9 = Entry(self)
        self.b9.grid(b4 = 6, column=1, padx=10, pady=5)
        if self.b8:
            self.b8.destroy()
        self.b8 = Button(self, b2="Decrypt", command=self.decrypt_message)
        self.b8.grid(b4 = 7, column=1, padx=10, pady=5)
    def fonk4(self):
        b16 = self.b9.get()
        b16 = (b16 + (16 - len(b16) % 16) * 'X').encode('utf-8')
        b17 = AES.new(b16, AES.MODE_CFB, self.b15)
        b18 = b17.decrypt(self.b14).decode('utf-8')
        if self.b10:
            self.b10.destroy()
        self.b10 = Label(self, b2=f"Your decrypted message is: {b18}")
        self.b10.grid(b4 = 8, column=0, columnspan=2, padx=10, pady=5)
b19 = Tk()
b19.geometry("600x300")
b20 = class1(b1=b19)
b19.mainloop()