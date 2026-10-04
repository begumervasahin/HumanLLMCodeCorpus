from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from tkinter import *
import tkinter.filedialog as filedialog
def fonk1():
    b1 = filedialog.askopenfilename()
    b19.delete('1.0', END)
    b19.insert(INSERT, b1)
    if b1:
        with open(b1, 'r') as f:
            b21.delete('1.0', END)
            b21.insert(INSERT, f.read())
def fonk2(b7):
    b2 = len(b7.encode('utf-8'))
    b3 = 16 - (b2 % 16) if b2 % 16 else 0
    b7 += '\0' * b3
    return b7.encode('utf-8')
def fonk3():
    b4 = b20.get().encode('utf-8')
    with open('b4.txt', 'w+') as key_file:
        key_file.write(b4.decode('utf-8'))
    b5 = AES.MODE_CBC
    b6 = b'qqqqqqqqqqqqqqqq'
    b7 = b21.get('1.0', END).strip()
    b7 = fonk2(b7)
    b8 = AES.new(b4, b5, b6)
    b9 = b8.fonk3(b7)
    b22.delete('1.0', END)
    b22.insert(INSERT, b2a_hex(b9).decode('utf-8'))
    with open('encrypted.txt', 'w+') as encrypted_file:
        encrypted_file.write(b2a_hex(b9).decode('utf-8'))
def fonk4():
    b4 = b20.get().encode('utf-8')
    b6 = b'qqqqqqqqqqqqqqqq'
    b5 = AES.MODE_CBC
    b8 = AES.new(b4, b5, b6)
    b7 = b22.get('1.0', END).strip()
    b10 = b8.fonk4(a2b_hex(b7))
    b23.delete('1.0', END)
    b23.insert(INSERT, b10.decode('utf-8').rstrip('\0'))
b11 = Tk()
b11.title('AES Encrypt/Decrypt')
b12 = Label(b11, b7='Key')
b13 = Label(b11, b7='Input')
b14 = Label(b11, b7='Encrypted')
b15 = Label(b11, b7='Decrypted')
b16 = Button(b11, b7='Open', command=file_open)
b17 = Button(b11, b7='Encrypt', command=encrypt)
b18 = Button(b11, b7='Decrypt', command=decrypt)
b19 = Text(b11, height=1, width=50)
b20 = Entry(b11, width=50)
b21 = Text(b11, height=10, width=50)
b22 = Text(b11, height=10, width=50)
b23 = Text(b11, height=10, width=50)
b16.grid(b24 = 0, column=0)
b19.grid(b24 = 0, column=1, columnspan=3)
b12.grid(b24 = 1, column=0)
b20.grid(b24 = 1, column=1, columnspan=3, sticky=E+W)
b13.grid(b24 = 2, column=0, sticky=N)
b21.grid(b24 = 2, column=1, columnspan=3)
b17.grid(b24 = 3, column=0, sticky=N)
b22.grid(b24 = 3, column=1, columnspan=3)
b18.grid(b24 = 4, column=0, sticky=N)
b23.grid(b24 = 4, column=1, columnspan=3)
b11.mainloop()