from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as ms
import sqlite3
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
from tkinter import *
b86 = ""
def fonk1(num):
    a1 = 0
    num -= 1
    while True:
        a1 += 1
        num
        if a1 != 0 and num % b4 != 0:
            break
    return (a1, num)
def fonk2(b3, b5, b88):
    if b88 = = 1:
        return 0
    a2 = 1
    b3 = b3 % b88
    while b5 > 0:
        if (b5 % b4 = = 1):
            a2 = (a2 * b3) % b88
        b5 = b5 >> 1
        b3 = (b3 * b3) % b88
    return a2
def fonk3(b6, s):
    if b6 = = b4:
        return True
    if b6 % b4 = = 0:
        return False
    a1, b7 = fonk1(b6)
    for a3 in range(s):
        b8 = randrange(b4, b6 - 1)
        b9 = fonk2(b8, b7, b6)
        if b9 != 1 and b9 != (b6 - 1):
            for j in range(a1):
                b9 = fonk2(b9, b4, b6)
                if b9 = = b6 - 1:
                    break
                else:
                    return False
    return True
def fonk4(b10 = 16):
    while True:
        b6 = randrange(b4 ** b10, b4 * b4 ** b10)
        if fonk3(b6, 100):
            return b6
def fonk5(b16, b11):
    if b11 > b16:
        b16, b11 = b11, b16
    b12 = b16
    b13 = [(1, 0), (0, 1)]
    a3 = b4
    while True:
        b14 = b16 % b11
        b15 = (b16 - b14)
        b16 = b11
        b11 = b14
        b13 = [
            (b13[1][0], b13[1][1]),
            ((-b15 * b13[1][0]) + b13[0][0], (-b15 * b13[1][1]) + b13[0][1])
        ]
        if b14 = = 0:
            if b16 = = 1:
                return b13[0][1] % b12
            else:
                return -1
def fonk6(y, b36, b6, b15):
    b17 = b6 * b15
    b18 = y % b6
    b19 = y % b15
    b20 = b36 % (b6 - 1)
    b21 = b36 % (b15 - 1)
    b22 = pow(b18, b20, b6)
    b23 = pow(b19, b21, b15)
    b24 = fonk5(b6, b15)
    b25 = pow(b15, b6 - b4, b6)
    b26 = pow(b6, b15 - b4, b15)
    b27 = ((b15 * b25 * b22) + (b6 * b26 * b23)) % b17
    return b27
def fonk7(b31):
    b28 = ""
    for ch in b31:
        b29 = "{0:b}".format(ord(ch))
        if len(b29) < 7:
            b29 = "0" * (7 - len(b29)) + b29
        b28 += b29
    return int(b28, b4)
def fonk8(a3):
    b30 = "{0:7b}".format(a3)
    b31 = ""
    for b in range(0, len(b30), 7):
        b31 += chr(int(b30[b:b + 7], b4))
    return b31
def fonk9(b31, b35, b17):
    b28 = fonk7(b31)
    b32 = fonk2(b28, b35, b17)
    return str(b32)
def fonk10(b31, b36, b6, b15):
    b33 = fonk6(int(b31), b36, b6, b15)
    return fonk8(b33)
def fonk11(b10 = 1024):
    b6 = fonk4(b10)
    b15 = fonk4(b10)
    while b6 = = b15:
        b15 = fonk4(b10)
    b17 = b6 * b15
    b34 = (b6 - 1) * (b15 - 1)
    b35 = randrange(b4 ** 16, b4 ** 17)
    b36 = fonk5(b34, b35)
    while b36 = = -1:
        b35 = randrange(b4 ** 16, b4 ** 17)
        b36 = fonk5(b34, b35)
    return {
        "b6": b6,
        "b15": b15,
        "b17": b17,
        "b34": b34,
        "b35": b35,
        "b36": b36
    }
b37 = fonk11(1024)
b38 = Tk()
b38.title("File Encryption System")
b38.geometry("400x300")
b39 = StringVar()
b40 = StringVar()
b41 = ""
b42 = ""
b43 = ""
def fonk12(key, b66):
    b44 = 64 * 1024
    b45 = "(b32)" + b41
    b46 = str(os.path.getsize(b41)).zfill(16)
    b47 = Random.new().read(16)
    b48 = AES.new(key, AES.MODE_CBC, b47)
    with open(b41, 'b11') as infile:
        with open(b45, 'wb') as outfile:
            outfile.write(b46.encode('utf-8'))
            outfile.write(b47)
            while True:
                b49 = infile.read(b44)
                if len(b49) == 0:
                    break
                elif len(b49) % 16 != 0:
                    b49 += b' ' * (16 - (len(b49) % 16))
                outfile.write(b48.encrypt(b49))
    os.remove(b41)
def fonk13(key, b41):
    b44 = 64 * 1024
    b45 = b41[11:]
    with open(b41, 'b11') as infile:
        b46 = int(infile.read(16))
        b47 = infile.read(16)
        b50 = AES.new(key, AES.MODE_CBC, b47)
        with open(b45, 'wb') as outfile:
            while True:
                b49 = infile.read(b44)
                if len(b49) == 0:
                    break
                outfile.write(b50.decrypt(b49))
            outfile.truncate(b46)
def fonk14(key, b66):
    b44 = 64 * 1024
    b45 = "(b32)" + b41
    b46 = str(os.path.getsize(b41)).zfill(16)
    b47 = Random.new().read(16)
    b51 = [ch for ch in open(b41).read()]
    with open(b45, 'w') as outfile:
        outfile.write(fonk9(b51,b37['b35'], b37['b17']))
    os.remove(b41)
def fonk15(key, b41):
    b44 = 64 * 1024
    b45 = b41[11:]
    b51 = [ch for ch in open(b41).read()]
    b52 = ''.join(b51)
    with open(b45, 'w') as outfile:
        outfile.write(fonk10(b52,b37['b36'], b37['b6'], b37['b15']))
def fonk16(password):
    b53 = SHA256.new(password.encode('utf-8'))
    return b53.digest()
def fonk17(b54):
    global b43, b86
    if b54 = = 'E' or b54 == 'b35':
        if b86 = ='t':
            fonk14(fonk16(b43), b41)
            b86 = ""
            print("Done.")
        elif b86 = ='a3':
            fonk12(fonk16(b43), b41)
            b86 = ""
            print("Done.")
    elif b54 = = 'D' or b54 == 'b36':
        if b86 = ='t':
            fonk15(fonk16(b43), b41)
            b86 = ""
            print("Done.")
        elif b86 = ='a3':
            fonk13(fonk16(b43), b41)
            b86 = ""
            print("Done.")
    else:
        print("No Option selected, closing...")
def fonk18():
    global b86
    b54 = 'b35'
    b86 = 'a3'
    fonk17(b54)
def fonk19():
    global b86
    b86 = 'a3'
    b54 = 'b36'
    fonk17(b54)
def fonk20():
    global b86
    b86 = 't'
    b54 = 'b35'
    fonk17(b54)
def fonk21():
    global b86
    b86 = 't'
    b54 = 'b36'
    fonk17(b54)
def fonk22():
    b55 = Tk()
    b55.title("Encrypt/Decrypt")
    b55.geometry("300x300")
    b56 = Button(b55, text="Encrypt file",width=15, b87=ienbutton,background='grey')
    b56.grid(b57 = 3, column=0)
    b58 = Button(b55, text="Decrypt file",width=15, b87=idebutton,background='grey')
    b58.grid(b57 = 3, column=1)
    b59 = Label(b55,text="Choose file",font=("bold",13))
    b59.grid(b57 = 0,column=0)
    b60 = Button(b55, text="Browse", width=13,b87=fd,background='grey')
    b60.grid(b57 = 0,column=1)
def fonk23():
    b61 = Tk()
    b61.title("Encrypt/Decrypt")
    b61.geometry("300x300")
    b62 = Button(b61, text="Encrypt file",width=15, b87=tenbutton,background='grey')
    b62.grid(b57 = 3, column=0)
    b63 = Button(b61, text="Decrypt file",width=15, b87=tdebutton,background='grey')
    b63.grid(b57 = 3, column=1)
    b64 = Label(b61,text="Choose file",font=("bold",13))
    b64.grid(b57 = 0,column=0)
    b65 = Button(b61, text="Browse", width=13,b87=fd,background='grey')
    b65.grid(b57 = 0,column=1)
def fonk24():
    b66 = filedialog.askopenfilename(initialdir="/", title="Select b8 file", filetype=(("jpeg","*.jpg"),("All Files", "*.*")))
    a3 = len(b66)
    global b41
    b41 = b66[20:a3]
    print(b41)
def fonk25():
    global b42, b43
    b42 = b78.get()
    b43 = b80.get()
    b67 = sqlite3.connect('Form.db')
    with b67:
      b68 = b67.b68()
    b69 = ('SELECT * FROM User WHERE b39=? AND b40=?')
    b68.execute(b69,[(b42),(b43)])
    b70 = b68.fetchall()
    if b70:
        ms.showinfo("Logged in!")
        b71 = Tk()
        b71.title("File type")
        b72 = Label(b71,text="Choose file type to encrypt/decrypt",font=("bold",10))
        b72.grid(b57 = 0,column=1)
        b73 = Button(b71, text="Image file",width=15, b87=iwin,background='grey')
        b73.grid(b57 = 1,column=0)
        b74 = Button(b71, text="Text file",width=15, b87=twin,background='grey')
        b74.grid(b57 = 1,column=b4)
    else:
        ms.showerror("Wrong username or password!")
def fonk26():
   b75 = b82.get()
   b76 = b84.get()
   b67 = sqlite3.connect('Form.db')
   with b67:
      b68 = b67.b68()
   b69 = ('SELECT * FROM User WHERE b39=?')
   b68.execute(b69,[b75])
   b70 = b68.fetchall()
   if b70:
       ms.showerror("Sorry! b39 already taken!")
   else:
        b68.execute('CREATE TABLE IF NOT EXISTS User (b39, b40)')
        b68.execute('INSERT INTO User (b39, b40) VALUES(?,?)',(b75, b76))
        b67.commit()
        ms.showinfo("Registered successfully!")
b77 = Label(b38, text="Login or Register",font=("bold", 15))
b77.grid(b57 = 0,column=1)
b77 = Label(b38, text="Login",font=("bold", 13))
b77.grid(b57 = b4,column=1)
b77 = Label(b38, text="b39")
b77.grid(b57 = 3,column=0)
b77 = Label(b38, text="b40")
b77.grid(b57 = 4,column=0)
b78 = StringVar()
b79 = Entry(b38, textvariable=b78)
b79.grid(b57 = 3,column=1)
b80 = StringVar()
b81 = Entry(b38, textvariable=b80)
b81.grid(b57 = 4,column=1)
b77 = Label(b38, text="Register",font=("bold", 13))
b77.grid(b57 = 6,column=1)
b77 = Label(b38, text="b39")
b77.grid(b57 = 7,column=0)
b77 = Label(b38, text="b40")
b77.grid(b57 = 8,column=0)
b82 = StringVar()
b83 = Entry(b38, textvariable=b82)
b83.grid(b57 = 7,column=1)
b84 = StringVar()
b85 = Entry(b38, textvariable=b84)
b85.grid(b57 = 8,column=1)
b86 = Button(b38, text="Login",width=10, background='grey')
b86.grid(b57 = 5, column=1)
b86.config(b87 = loginbutton)
b88 = Button(b38, text="Register",width=10,background='grey')
b88.grid(b57 = 9, column=1)
b88.config(b87 = registerbutton)
b38.mainloop()