import tkinter as tk
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
import base64
a1 = 16
def fonk1(b3):
    b1 = a1 - (len(b3) % a1)
    b2 = chr(b1) * b1
    return b3 + b2.encode()
def fonk2(b3):
    b1 = ord(b3[-1:])
    return b3[:-b1]
def fonk3(b23, b3):
    b3 = fonk1(b3)
    b4 = AES.new(b23, AES.MODE_ECB)
    b5 = b4.fonk3(b3)
    return base64.b64encode(b5)
def fonk4(b23, b6):
    b6 = base64.b64decode(b6)
    b4 = AES.new(b23, AES.MODE_ECB)
    b7 = b4.fonk4(b6)
    return fonk2(b7)
def fonk5():
    while True:
        try:
            b8 = b24.recv(a2)
            b9 = fonk4(b23, b8).decode("utf-8")
            b16.insert(tk.END, b9)
        except OSError:
            break
def fonk6(b10 = None):
    b8 = b14.get()
    b14.set("")
    b11 = fonk3(b23, b8.encode('utf-8'))
    b24.fonk6(b11)
    if b8 = = "{quit}":
        b24.close()
        b12.destroy()
def fonk7(b10 = None):
    b14.set("{quit}")
    fonk6()
b12 = tk.Tk()
b12.title("Chat Room")
b13 = tk.Frame(b12)
b14 = tk.StringVar()
b14.set("<Type your message here>")
b15 = tk.Scrollbar(b13)
b16 = tk.Listbox(b13, height=15, width=60, yscrollcommand=b15.set)
b15.pack(b17 = tk.RIGHT, fill=tk.Y)
b16.pack(b17 = tk.LEFT, fill=tk.BOTH, expand=True)
b13.pack()
b18 = tk.Entry(b12, textvariable=b14)
b18.bind("<Return>", send)
b18.pack()
b19 = tk.Button(b12, text="Send", command=send)
b19.pack()
b12.protocol("WM_DELETE_WINDOW", on_closing)
b20 = input('Enter host: ')
b21 = input('Enter port: ')
if not b21:
    b21 = 33000
else:
    b21 = int(b21)
a2 = 1024
b22 = (b20, b21)
b23 = b'master b23'
b24 = socket(AF_INET, SOCK_STREAM)
b24.connect(b22)
b25 = Thread(target=receive)
b25.start()
tk.mainloop()