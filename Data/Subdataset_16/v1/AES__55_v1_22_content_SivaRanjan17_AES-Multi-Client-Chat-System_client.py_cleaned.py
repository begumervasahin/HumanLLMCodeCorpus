from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from Crypto.Cipher import AES
import base64
a1 = 16
def fonk1(b2):
    b1 = a1 - (len(b2) % a1)
    return b2 + (chr(b1) * b1).encode()
def fonk2(b2):
    return b2[:-ord(b2[len(b2)-1:])]
def fonk3(b21, b2):
    b2 = fonk1(b2)
    b3 = AES.new(b21, AES.MODE_ECB)
    return base64.b64encode(b3.fonk3(b2))
def fonk4(b21, b4):
    b4 = base64.b64decode(b4)
    b3 = AES.new(b21, AES.MODE_ECB)
    return fonk2(b3.fonk4(b4))
def fonk5():
    while True:
        try:
            b5 = b22.recv(a2)
            b6 = fonk4(b21, b5).decode("utf-8")
            b14.insert(tk.END, b6)
        except OSError:
            break
def fonk6(b7 = None):
    b8 = b12.get()
    b12.set("")
    b6 = b8.encode('UTF-8')
    b9 = fonk3(b21, b6)
    b22.fonk6(b9)
    if b8 = = "{quit}":
        b22.close()
        b10.destroy()
def fonk7(b7 = None):
    b12.set("{quit}")
    fonk6()
    b10.destroy()
b10 = tk.Tk()
b10.title("Chat Room")
b11 = tk.Frame(b10)
b12 = tk.StringVar()
b12.set("<messages here>")
b13 = tk.Scrollbar(b11)
b14 = tk.Listbox(b11, height=15, width=60, yscrollcommand=b13.set)
b13.pack(b15 = tk.RIGHT, fill=tk.Y)
b14.pack(b15 = tk.LEFT, fill=tk.BOTH)
b14.pack()
b11.pack()
b16 = tk.Entry(b10, textvariable=b12)
b16.bind("<Return>", send)
b16.pack()
b17 = tk.Button(b10, text="Send", command=send)
b17.pack()
b10.protocol("WM_DELETE_WINDOW", on_closing)
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
tk.mainloop()