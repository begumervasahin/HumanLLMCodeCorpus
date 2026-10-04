from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from tkinter import *
import tkinter.filedialog as filedialog
def fonk1():
    b1 = filedialog.askopenfilename()
    b20.delete('1.0', END)
    b20.insert(INSERT, b1)
    if b1:
        with open(b1, 'r') as f:
            b22.delete('1.0', END)
            b22.insert(INSERT, f.read())
def fonk2(b7):
    b2 = len(b7.encode('utf-8'))
    b3 = 16 - (b2 % 16) if b2 % 16 else 0
    b7 += '\0' * b3
    return b7.encode('utf-8')
def fonk3():
    b4 = b21.get().encode('utf-8')
    with open('b4.txt', 'w') as key_file:
        key_file.write(b4.decode('utf-8'))
    b5 = AES.MODE_CBC
    b6 = b'qqqqqqqqqqqqqqqq'
    b7 = b22.get('1.0', END).strip()
    b7 = fonk2(b7)
    b8 = AES.new(b4, b5, b6)
    b9 = b8.fonk3(b7)
    b23.delete('1.0', END)
    b23.insert(INSERT, b2a_hex(b9).decode('utf-8'))
    with open('encrypted.txt', 'w') as encrypted_file:
        encrypted_file.write(b2a_hex(b9).decode('utf-8'))
def fonk4():
    b4 = b21.get().encode('utf-8')
    b6 = b'qqqqqqqqqqqqqqqq'
    b5 = AES.MODE_CBC
    b8 = AES.new(b4, b5, b6)
    b10 = b23.get('1.0', END).strip()
    b11 = b8.fonk4(a2b_hex(b10))
    b24.delete('1.0', END)
    b24.insert(INSERT, b11.decode('utf-8').rstrip('\0'))
b12 = Tk()
b12.title('AES Encrypt/Decrypt')
b13 = Label(b12, b7='Key')
b14 = Label(b12, b7='Input')
b15 = Label(b12, b7='Encrypted')
b16 = Label(b12, b7='Decrypted')
b17 = Button(b12, b7='Open', command=file_open)
b18 = Button(b12, b7='Encrypt', command=encrypt)
b19 = Button(b12, b7='Decrypt', command=decrypt)
b20 = Text(b12, height=1, width=50)
b21 = Entry(b12, width=50)
b22 = Text(b12, height=10, width=50)
b23 = Text(b12, height=10, width=50)
b24 = Text(b12, height=10, width=50)
b17.grid(b25 = 0, column=0)
b20.grid(b25 = 0, column=1, columnspan=3)
b13.grid(b25 = 1, column=0)
b21.grid(b25 = 1, column=1, columnspan=3, sticky=E+W)
b14.grid(b25 = 2, column=0, sticky=N)
b22.grid(b25 = 2, column=1, columnspan=3)
b18.grid(b25 = 3, column=0, sticky=N)
b23.grid(b25 = 3, column=1, columnspan=3)
b19.grid(b25 = 4, column=0, sticky=N)
b24.grid(b25 = 4, column=1, columnspan=3)
b12.mainloop()