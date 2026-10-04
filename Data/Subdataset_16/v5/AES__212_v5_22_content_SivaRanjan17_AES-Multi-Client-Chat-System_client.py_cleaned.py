
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from Crypto.Cipher import AES
import base64
a1 = 16
a2 = 1024
b1 = b'master key'
def fonk1(b4):
    b2 = a1 - (len(b4) % a1)
    b3 = chr(b2) * b2
    return b4 + b3.encode()
def fonk2(b4):
    b2 = ord(b4[-1:])
    return b4[:-b2]
def fonk3(key, b4):
    b4 = fonk1(b4)
    b5 = AES.new(key, AES.MODE_ECB)
    b6 = b5.fonk3(b4)
    return base64.b64encode(b6)
def fonk4(key, b7):
    b7 = base64.b64decode(b7)
    b5 = AES.new(key, AES.MODE_ECB)
    b8 = b5.fonk4(b7)
    return fonk2(b8)
def fonk5():
    while True:
        try:
            b9 = b24.recv(a2)
            b10 = fonk4(b1, b9).decode("utf-8")
            b17.insert(tk.END, b10)
        except OSError:
            break
def fonk6(b11 = None):
    b10 = b15.get()
    b15.set("")
    b12 = fonk3(b1, b10.encode('utf-8'))
    b24.fonk6(b12)
    if b10 = = "{quit}":
        b24.close()
        b13.destroy()
def fonk7(b11 = None):
    b15.set("{quit}")
    fonk6()
def fonk8():
    global b17, b15, b13
    b13 = tk.Tk()
    b13.title("Chat Room")
    b14 = tk.Frame(b13)
    b15 = tk.StringVar()
    b15.set("<Type your b10 here>")
    b16 = tk.Scrollbar(b14)
    b17 = tk.Listbox(b14, height=15, width=60, yscrollcommand=b16.set)
    b16.pack(b18 = tk.RIGHT, fill=tk.Y)
    b17.pack(b18 = tk.LEFT, fill=tk.BOTH, expand=True)
    b14.pack()
    b19 = tk.Entry(b13, textvariable=b15)
    b19.bind("<Return>", send)
    b19.pack()
    b20 = tk.Button(b13, text="Send", command=send)
    b20.pack()
    b13.protocol("WM_DELETE_WINDOW", on_closing)
def fonk9():
    global b24
    b21 = input('Enter host: ')
    b22 = input('Enter port: ')
    if not b22:
        b22 = 33000
    else:
        b22 = int(b22)
    b23 = (b21, b22)
    b24 = socket(AF_INET, SOCK_STREAM)
    b24.connect(b23)
    b25 = Thread(target=receive)
    b25.start()
if b26 = = "__main__":
    fonk8()
    fonk9()
    tk.mainloop()