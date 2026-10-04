
from tkinter import *
import socket
from Crypto.Cipher import AES
class class1(Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.b1 = b1
        self.fonk2()
    def fonk2(self):
        self.b1.title("DECRYPTOR")
        self.pack(b2 = BOTH, expand=1)
        Label(self, b3 = "Port").grid(b5=0, column=0)
        self.b4 = Entry(self)
        self.b4.grid(b5 = 0, column=1)
        Button(self, b3 = "Start Server", command=self.start_server).grid(b5=1, column=1)
    def fonk3(self):
        b6 = int(self.b4.get())
        Label(self, b3 = f"Listening on b6: {b6}").grid(b5=2, column=0, columnspan=3)
        b7 = socket.socket()
        b7.bind(('', b6))
        b7.listen(5)
        client_socket, b8 = b7.accept()
        b9 = client_socket.recv(1024)
        b10 = client_socket.recv(1024)
        Label(self, b3 = f"Incoming encrypted message: {b9}").grid(b5=4, column=0, columnspan=3, rowspan=2)
        Label(self, b3 = "Enter decryption b12").grid(b5=6, column=0)
        self.b11 = Entry(self)
        self.b11.grid(b5 = 6, column=1)
        Button(self, b3 = "Decrypt", command=lambda: self.fonk4(b9, b10)).grid(b5=7, column=1)
    def fonk4(self, b9, b10):
        b12 = self.b11.get()
        b12 = (b12 + (16 - len(b12) % 16) * 'X').encode('utf-8')
        b13 = AES.new(b12, AES.MODE_CFB, b10)
        b14 = b13.fonk4(b9).decode('utf-8')
        Label(self, b3 = f"Your decrypted message is: {b14}").grid(b5=8, column=0, columnspan=3, rowspan=2)
b15 = Tk()
b15.geometry("600x300")
b16 = class1(b15)
b15.mainloop()