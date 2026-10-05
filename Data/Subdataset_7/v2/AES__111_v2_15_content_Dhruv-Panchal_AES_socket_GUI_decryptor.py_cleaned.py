import socket
from Crypto.Cipher import AES
from Crypto import Random
from tkinter import *
class class1(Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.b1 = b1
        self.fonk2()
    def fonk2(self):
        self.b1.title("DECRYPTOR")
        self.pack(b2 = BOTH, expand=True)
        b3 = Label(self, b13="Port")
        b3.grid(b4 = 0, column=0)
        self.b5 = Entry(self)
        self.b5.grid(b4 = 0, column=1)
        b6 = Button(self, b13="Start server", command=self.start_server)
        b6.grid(b4 = 1, column=1)
        self.b7 = Label(self, b13="")
        self.b7.grid(b4 = 2, column=0, columnspan=3)
        self.b8 = Label(self, b13="")
        self.b8.grid(b4 = 4, column=0, columnspan=3, rowspan=2)
        self.b9 = Label(self, b13="Enter decryption b19")
        self.b9.grid(b4 = 6, column=0)
        self.b10 = Entry(self)
        self.b10.grid(b4 = 6, column=1)
        b11 = Button(self, b13="Decrypt", command=self.decrypt)
        b11.grid(b4 = 7, column=1)
    def fonk3(self):
        b12 = int(self.b5.get())
        self.b7.config(b13 = "Listening on b12: " + str(b12))
        b14 = socket.socket()
        b14.bind(('', b12))
        b14.listen(5)
        client_socket, b15 = b14.accept()
        b16 = client_socket.recv(1024)
        b17 = client_socket.recv(9999)
        self.b8.config(b13 = "Incoming encrypted message: " + str(b16))
        self.b18 = AES.new(self.b10.get().ljust(16, 'X'), AES.MODE_CFB, b17)
    def fonk4(self):
        b19 = self.b10.get().ljust(16, 'X')
        b20 = self.b18.fonk4(b16)
        b21 = Label(self, b13="Your decrypted message is " + str(b20))
        b21.grid(b4 = 8, column=0, columnspan=3, rowspan=2)
b22 = Tk()
b22.geometry("600x300")
b23 = class1(b22)
b22.mainloop()