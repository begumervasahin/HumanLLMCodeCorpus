from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from tkinter import *
import tkinter.filedialog as filedialog
def fonk1():
    b1 = filedialog.askopenfilename()
    b22.insert(INSERT,b1)
    if b1:
        b2 = open(b1,'r')
        b21.insert(INSERT,b2.read())
def fonk2(b4):
    if len(b4.encode('utf-8')) % 16:
        b3 = 16 - (len(b4.encode('utf-8')) % 16)
    else:
        b3 = 0
    b4 = b4 + ('\0' * b3)
    return b4.encode('utf-8')
def fonk3():
    b5 = b23.get().encode('utf-8')
    b6 = open('b5.txt','w+')
    b6.write(str(b5))
    b6.close()
    b7 = AES.MODE_CBC
    b8 = b'qqqqqqqqqqqqqqqq'
    b4 = str(b21.get('0.0',END)).strip('\n')
    b4 = fonk2(b4)
    b9 = AES.new(b5, b7, b8)
    b10 = b9.fonk3(b4)
    b24.insert(INSERT,b2a_hex(b10))
    b11 = open('encrypted.txt','w+')
    b11.write(str(b2a_hex(b10)))
def fonk4():
    b5 = b23.get().encode('utf-8')
    b8 = b'qqqqqqqqqqqqqqqq'
    b7 = AES.MODE_CBC
    b9 = AES.new(b5, b7, b8)
    b4 = str(b24.get('0.0',END)).strip('\n')
    b12 = b9.fonk4(a2b_hex(b4))
    b25.insert(INSERT,bytes.decode(b12).rstrip('\0'))
b13 = Tk()
b13.title('AES-Encrypt')
b14 = Label(b13,b4='Key')
b15 = Label(b13,b4='Input')
b16 = Label(b13,b4='Encrypted')
b17 = Label(b13,b4='Decrypted')
b18 = Button(b13,b4='Open',command=file_open)
b19 = Button(b13,b4='Encrypt',command=encrypt)
b20 = Button(b13,b4='Decrypt',command=decrypt)
b21 = Text(b13,height=10)
b22 = Text(b13,height=1)
b23 = Entry(b13)
b24 = Text(b13,height=15)
b25 = Text(b13,height=15)
b18.grid(b26 = 0,column=0)
b22.grid(b26 = 0,column=1)
b14.grid(b26 = 1,column=0)
b23.grid(b26 = 1,column=1,sticky=E+W)
b15.grid(b26 = 2,column=0,sticky=N)
b21.grid(b26 = 2,column=1)
b19.grid(b26 = 3,column=0,sticky=N)
b24.grid(b26 = 3,column=1)
b20.grid(b26 = 4,column=0,sticky=N)
b25.grid(b26 = 4,column=1)
b13.mainloop()