
from tkinter import *
import socket
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
        Button(self, b2 = "Start Server", command=self.start_server).grid(b4=1, column=1, padx=10, pady=5)
        self.b5 = None
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = None
    def fonk3(self):
        b10 = int(self.b3.get())
        self.fonk5(self.b5, f"Listening on b10: {b10}", b4 = 2, column=0, columnspan=2)
        b11 = socket.socket()
        b11.bind(('', b10))
        b11.listen(5)
        client_socket, b12 = b11.accept()
        self.b13 = client_socket.recv(1024)
        self.b14 = client_socket.recv(1024)
        self.fonk5(self.b6, f"Incoming encrypted message: {self.b13}", b4 = 4, column=0, columnspan=2)
        Label(self, b2 = "Enter decryption b15").grid(b4=6, column=0, padx=10, pady=5)
        self.b7 = Entry(self)
        self.b7.grid(b4 = 6, column=1, padx=10, pady=5)
        if self.b8:
            self.b8.destroy()
        self.b8 = Button(self, b2="Decrypt", command=self.decrypt_message)
        self.b8.grid(b4 = 7, column=1, padx=10, pady=5)
    def fonk4(self):
        b15 = self.b7.get()
        b15 = (b15 + (16 - len(b15) % 16) * 'X').encode('utf-8')
        b16 = AES.new(b15, AES.MODE_CFB, self.b14)
        b17 = b16.decrypt(self.b13).decode('utf-8')
        self.fonk5(self.b9, f"Your decrypted message is: {b17}", b4 = 8, column=0, columnspan=2)
    def fonk5(self, b18, b2, **grid_options):
        if b18:
            b18.destroy()
        b18 = Label(self, b2=b2)
        b18.grid(**grid_options)
        return b18
if b19 = = "__main__":
    b20 = Tk()
    b20.geometry("600x300")
    b21 = class1(b1=b20)
    b20.mainloop()