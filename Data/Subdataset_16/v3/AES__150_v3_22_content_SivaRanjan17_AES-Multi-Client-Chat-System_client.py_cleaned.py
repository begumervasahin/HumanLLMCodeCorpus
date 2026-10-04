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
def fonk3(b21, b3):
    b3 = fonk1(b3)
    b4 = AES.new(b21, AES.MODE_ECB)
    b5 = b4.fonk3(b3)
    return base64.b64encode(b5)
def fonk4(b21, b6):
    b6 = base64.b64decode(b6)
    b4 = AES.new(b21, AES.MODE_ECB)
    b7 = b4.fonk4(b6)
    return fonk2(b7)
def fonk5():
    while True:
        try:
            b8 = b22.recv(a2)
            b9 = fonk4(b21, b8).decode("utf-8")
            b14.insert(tk.END, b9)
        except OSError:
            break
def fonk6(b10 = None):
    b8 = b25.get()
    b25.set("")
    b11 = fonk3(b21, b8.encode('utf-8'))
    b22.fonk6(b11)
    if b8 = = "{quit}":
        b22.close()
        b24.destroy()
def fonk7(b10 = None):
    b25.set("{quit}")
    fonk6()
def fonk8():
    b24.title("Chat Room")
    b12 = tk.Frame(b24)
    b13 = tk.Scrollbar(b12)
    global b14
    b14 = tk.Listbox(b12, height=15, width=60, yscrollcommand=b13.set)
    b13.pack(b15 = tk.RIGHT, fill=tk.Y)
    b14.pack(b15 = tk.LEFT, fill=tk.BOTH, expand=True)
    b12.pack()
    b16 = tk.Entry(b24, textvariable=b25)
    b16.bind("<Return>", send)
    b16.pack()
    b17 = tk.Button(b24, text="Send", command=send)
    b17.pack()
    b24.protocol("WM_DELETE_WINDOW", on_closing)
def fonk9():
    global b22, a2, b20, b21
    b18 = input('Enter host: ')
    b19 = input('Enter port: ')
    if not b19:
        b19 = 33000
    else:
        b19 = int(b19)
    a2 = 1024
    b20 = (b18, b19)
    b21 = b'master b21'
    b22 = socket(AF_INET, SOCK_STREAM)
    b22.connect(b20)
    b23 = Thread(target=receive)
    b23.start()
b24 = tk.Tk()
b25 = tk.StringVar()
b25.set("<Type your message here>")
fonk8()
fonk9()
tk.mainloop()