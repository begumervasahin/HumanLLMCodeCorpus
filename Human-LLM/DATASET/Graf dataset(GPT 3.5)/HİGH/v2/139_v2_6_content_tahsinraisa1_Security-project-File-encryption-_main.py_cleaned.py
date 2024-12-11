import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
def fonk1(num):
    a1 = 0
    num -= 1
    while True:
        a1 += 1
        num
        if a1 != 0 and num % b3 != 0:
            break
    return (a1, num)
def fonk2(b88, b4, b86):
    if b86 = = 1:
        return 0
    a2 = 1
    b88 = b88 % b86
    while b4 > 0:
        if (b4 % b3 = = 1):
            a2 = (a2 * b88) % b86
        b4 = b4 >> 1
        b88 = (b88 * b88) % b86
    return a2
def fonk3(b5, s):
    if b5 = = b3:
        return True
    if b5 % b3 = = 0:
        return False
    a1, b6 = fonk1(b5)
    for a3 in range(s):
        b7 = randrange(b3, b5 - 1)
        b8 = fonk2(b7, b6, b5)
        if b8 != 1 and b8 != (b5 - 1):
            for j in range(a1):
                b8 = fonk2(b8, b3, b5)
                if b8 = = b5 - 1:
                    break
                else:
                    return False
    return True
def fonk4(b9 = 16):
    while True:
        b5 = randrange(b3 ** b9, b3 * b3 ** b9)
        if fonk3(b5, 100):
            return b5
def fonk5(b15, b10):
    if b10 > b15:
        b15, b10 = b10, b15
    b11 = b15
    b12 = [(1, 0), (0, 1)]
    a3 = b3
    while True:
        b13 = b15 % b10
        b14 = (b15 - b13)
        b15 = b10
        b10 = b13
        b12 = [
            (b12[1][0], b12[1][1]),
            ((-b14 * b12[1][0]) + b12[0][0], (-b14 * b12[1][1]) + b12[0][1])
        ]
        if b13 = = 0:
            if b15 = = 1:
                return b12[0][1] % b11
            else:
                return -1
def fonk6(y, b35, b5, b14):
    b16 = b5 * b14
    b17 = y % b5
    b18 = y % b14
    b19 = b35 % (b5 - 1)
    b20 = b35 % (b14 - 1)
    b21 = pow(b17, b19, b5)
    b22 = pow(b18, b20, b14)
    b23 = fonk5(b5, b14)
    b24 = pow(b14, b5 - b3, b5)
    b25 = pow(b5, b14 - b3, b14)
    b26 = ((b14 * b24 * b21) + (b5 * b25 * b22)) % b16
    return b26
def fonk7(b30):
    b27 = ""
    for ch in b30:
        b28 = "{0:b}".format(ord(ch))
        if len(b28) < 7:
            b28 = "0" * (7 - len(b28)) + b28
        b27 += b28
    return int(b27, b3)
def fonk8(a3):
    b29 = "{0:7b}".format(a3)
    b30 = ""
    for b in range(0, len(b29), 7):
        b30 += chr(int(b29[b:b + 7], b3))
    return b30
def fonk9(b30, b34, b16):
    b27 = fonk7(b30)
    b31 = fonk2(b27, b34, b16)
    return str(b31)
def fonk10(b30, b35, b5, b14):
    b32 = fonk6(int(b30), b35, b5, b14)
    return fonk8(b32)
def fonk11(b9 = 1024):
    b5 = fonk4(b9)
    b14 = fonk4(b9)
    while b5 = = b14:
        b14 = fonk4(b9)
    b16 = b5 * b14
    b33 = (b5 - 1) * (b14 - 1)
    b34 = randrange(b3 ** 16, b3 ** 17)
    b35 = fonk5(b33, b34)
    while b35 = = -1:
        b34 = randrange(b3 ** 16, b3 ** 17)
        b35 = fonk5(b33, b34)
    return {
        "b5": b5,
        "b14": b14,
        "b16": b16,
        "b33": b33,
        "b34": b34,
        "b35": b35
    }
b36 = fonk11(1024)
def fonk12(key, b60):
    b37 = 64 * 1024
    b38 = "(b31)" + b60
    b39 = str(os.path.getsize(b60)).zfill(16)
    b40 = Random.new().read(16)
    b41 = AES.new(key, AES.MODE_CBC, b40)
    with open(b60, 'b10') as infile:
        with open(b38, 'wb') as outfile:
            outfile.write(b39.encode('utf-8'))
            outfile.write(b40)
            while True:
                b42 = infile.read(b37)
                if len(b42) == 0:
                    break
                elif len(b42) % 16 != 0:
                    b42 += b' ' * (16 - (len(b42) % 16))
                outfile.write(b41.encrypt(b42))
    os.remove(b60)
def fonk13(key, b60):
    b37 = 64 * 1024
    b38 = b60[11:]
    with open(b60, 'b10') as infile:
        b39 = int(infile.read(16))
        b40 = infile.read(16)
        b43 = AES.new(key, AES.MODE_CBC, b40)
        with open(b38, 'wb') as outfile:
            while True:
                b42 = infile.read(b37)
                if len(b42) == 0:
                    break
                outfile.write(b43.decrypt(b42))
            outfile.truncate(b39)
def fonk14(key, b60):
    b37 = 64 * 1024
    b38 = "(b31)" + b60
    b39 = str(os.path.getsize(b60)).zfill(16)
    b40 = Random.new().read(16)
    b44 = [ch for ch in open(b60).read()]
    with open(b38, 'w') as outfile:
        outfile.write(fonk9(b44, b36['b34'], b36['b16']))
    os.remove(b60)
def fonk15(key, b60):
    b37 = 64 * 1024
    b38 = b60[11:]
    b44 = [ch for ch in open(b60).read()]
    b45 = ''.join(b44)
    with open(b38, 'w') as outfile:
        outfile.write(fonk10(b45, b36['b35'], b36['b5'], b36['b14']))
def fonk16(password):
    b46 = SHA256.new(password.encode('utf-8'))
    return b46.digest()
def fonk17(b47):
    global b63, b48, b61
    if b47 = = 'E' or b47 == 'b34':
        if b48 = = 't':
            fonk14(fonk16(b63), b61)
            b48 = ""
            print("Done.")
        elif b48 = = 'a3':
            fonk12(fonk16(b63), b61)
            b48 = ""
            print("Done.")
    elif b47 = = 'D' or b47 == 'b35':
        if b48 = = 't':
            fonk15(fonk16(b63), b61)
            b48 = ""
            print("Done.")
        elif b48 = = 'a3':
            fonk13(fonk16(b63), b61)
            b48 = ""
            print("Done.")
    else:
        print("No Option selected, closing...")
def fonk18():
    global b48
    b47 = 'b34'
    b48 = 'a3'
    fonk17(b47)
def fonk19():
    global b48
    b48 = 'a3'
    b47 = 'b35'
    fonk17(b47)
def fonk20():
    global b48
    b48 = 't'
    b47 = 'b34'
    fonk17(b47)
def fonk21():
    global b48
    b48 = 't'
    b47 = 'b35'
    fonk17(b47)
def fonk22():
    b49 = tk.Tk()
    b49.title("Encrypt/Decrypt")
    b49.geometry("300x300")
    b50 = ttk.Button(b49, text="Encrypt file", width=15, b87=ienbutton)
    b50.grid(b51 = 3, column=0)
    b52 = ttk.Button(b49, text="Decrypt file", width=15, b87=idebutton)
    b52.grid(b51 = 3, column=1)
    b53 = tk.Label(b49, text="Choose file", font=("bold", 13))
    b53.grid(b51 = 0, column=0)
    b54 = ttk.Button(b49, text="Browse", width=13, b87=fd)
    b54.grid(b51 = 0, column=1)
def fonk23():
    b55 = tk.Tk()
    b55.title("Encrypt/Decrypt")
    b55.geometry("300x300")
    b56 = ttk.Button(b55, text="Encrypt file", width=15, b87=tenbutton)
    b56.grid(b51 = 3, column=0)
    b57 = ttk.Button(b55, text="Decrypt file", width=15, b87=tdebutton)
    b57.grid(b51 = 3, column=1)
    b58 = tk.Label(b55, text="Choose file", font=("bold", 13))
    b58.grid(b51 = 0, column=0)
    b59 = ttk.Button(b55, text="Browse", width=13, b87=fd)
    b59.grid(b51 = 0, column=1)
def fonk24():
    b60 = filedialog.askopenfilename(initialdir="/", title="Select b7 file", filetype=(("jpeg", "*.jpg"), ("All Files", "*.*")))
    a3 = len(b60)
    global b61
    b61 = b60[20:a3]
    print(b61)
def fonk25():
    global b62, b63
    b62 = b78.get()
    b63 = b80.get()
    b64 = sqlite3.connect('Form.db')
    with b64:
        b65 = b64.b65()
    b66 = ('SELECT * FROM User WHERE b75=? AND b76=?')
    b65.execute(b66, [(b62), (b63)])
    b67 = b65.fetchall()
    if b67:
        messagebox.showinfo("Logged in!")
        b68 = tk.Tk()
        b68.title("File type")
        b69 = tk.Label(b68, text="Choose file type to encrypt/decrypt", font=("bold", 10))
        b69.grid(b51 = 0, column=1)
        b70 = ttk.Button(b68, text="Image file", width=15, b87=iwin)
        b70.grid(b51 = 1, column=0)
        b71 = ttk.Button(b68, text="Text file", width=15, b87=twin)
        b71.grid(b51 = 1, column=b3)
    else:
        messagebox.showerror("Wrong username or password!")
def fonk26():
    b72 = b82.get()
    b73 = b84.get()
    b64 = sqlite3.connect('Form.db')
    with b64:
        b65 = b64.b65()
    b66 = ('SELECT * FROM User WHERE b75=?')
    b65.execute(b66, [b72])
    b67 = b65.fetchall()
    if b67:
        messagebox.showerror("Sorry! b75 already taken!")
    else:
        b65.execute('CREATE TABLE IF NOT EXISTS User (b75, b76)')
        b65.execute('INSERT INTO User (b75, b76) VALUES(?,?)', (b72, b73))
        b64.commit()
        messagebox.showinfo("Registered successfully!")
b74 = tk.Tk()
b74.title("File Encryption System")
b74.geometry("400x300")
b75 = tk.StringVar()
b76 = tk.StringVar()
b61 = ""
b77 = tk.Label(b74, text="Login or Register", font=("bold", 15))
b77.grid(b51 = 0, column=1)
b77 = tk.Label(b74, text="Login", font=("bold", 13))
b77.grid(b51 = b3, column=1)
b77 = tk.Label(b74, text="b75")
b77.grid(b51 = 3, column=0)
b77 = tk.Label(b74, text="b76")
b77.grid(b51 = 4, column=0)
b78 = tk.StringVar()
b79 = tk.Entry(b74, textvariable=b78)
b79.grid(b51 = 3, column=1)
b80 = tk.StringVar()
b81 = tk.Entry(b74, textvariable=b80)
b81.grid(b51 = 4, column=1)
b77 = tk.Label(b74, text="Register", font=("bold", 13))
b77.grid(b51 = 6, column=1)
b77 = tk.Label(b74, text="b75")
b77.grid(b51 = 7, column=0)
b77 = tk.Label(b74, text="b76")
b77.grid(b51 = 8, column=0)
b82 = tk.StringVar()
b83 = tk.Entry(b74, textvariable=b82)
b83.grid(b51 = 7, column=1)
b84 = tk.StringVar()
b85 = tk.Entry(b74, textvariable=b84)
b85.grid(b51 = 8, column=1)
b86 = tk.Button(b74, text="Login", width=10)
b86.grid(b51 = 5, column=1)
b86.config(b87 = loginbutton)
b88 = tk.Button(b74, text="Register", width=10)
b88.grid(b51 = 9, column=1)
b88.config(b87 = registerbutton)
b74.mainloop()