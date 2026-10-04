'''
decryptor.py
This code runs a GUI for decrypting a message sent over localhost.
@author  Dhruv Panchal
@version 1.0, 04/04/19
'''
from tkinter import *
import socket
from Crypto.Cipher import AES
from Crypto import Random
class class1(Frame):
    def fonk1(self, b1 = None):
        Frame.fonk1(self, b1)
        self.b1 = b1
        self.fonk2()
    def fonk2(self):
        self.b1.title("DECRYPTOR")
        self.pack(b2 = BOTH, expand=1)
        b3 = Label(self, text="Port")
        b3.grid(b4 = 0,column=0)
        b5 = Entry(self)
        b5.grid(b4 = 0,column=1)
        def fonk3():
            b6 = b5.get()
            b7 = int(b6)
            b8 = Label(self, text="Listening on b5: "+str(b7))
            b8.grid(b4 = 2, column=0, columnspan=3)
            b9 = socket.socket()
            b9.bind(('', b7))
            b9.listen(5)
            c, b10 = b9.accept()
            b11 = c.recv(1024)
            b12 = c.recv(9999)
            print(b12)
            b13 = Label(self, text ="Incoming ecnryted message: "+str(b11))
            b13.grid(b4 = 4, column=0, columnspan=3,rowspan=2)
            b14 = Label(self, text = "Enter decryption b16").grid(b4=6, column=0)
            b15 = Entry(self)
            b15.grid(b4 = 6, column=1)
            def fonk4():
                b16 = b15.get()
                b16 += ((16 - len(b16) % 16)*'X')
                b17 = AES.new(b16, AES.MODE_CFB, b12)
                b18 = b17.fonk4(b11)
                b19 = Label(self, text = ("Your decrypted message is "+str(b18)))
                b19.grid(b4 = 8, column=0, columnspan=3, rowspan=2)
            b20 = Button(self, text="Decrypt", command=decrypt).grid(b4=7, column=1)
        b21 = Button(self, text = "Start server", command = start_server).grid(b4=1, column=1)
b22 = Tk()
b22.geometry("600x300")
b23 = class1(b22)
b22.mainloop()