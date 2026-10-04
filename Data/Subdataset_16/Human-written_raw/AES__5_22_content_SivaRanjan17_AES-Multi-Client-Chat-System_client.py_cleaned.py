
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
import AES
b1 = b'master b1'
def fonk1():
    while True:
        try:
            b2 = b18.recv(a1)
            b3 = AES.decrypt(b1, b2).decode("utf-8")
            b11.insert(tkinter.END, b3)
        except OSError:
            break
def fonk2(b4 = None):
    b5 = b9.get()
    b9.set("")
    b3 = b5.encode('UTF-8')
    b6 = AES.encrypt(b1, b3)
    b18.fonk2(b6)
    if b5 = = "{quit}":
        b18.close()
        b7.destroy()
def fonk3(b4 = None):
    b9.set("{quit}")
    fonk2()
    b7.destroy()
b7 = tkinter.Tk()
b7.title("Chat Room")
b8 = tkinter.Frame(b7)
b9 = tkinter.StringVar()
b9.set("<messages here>")
b10 = tkinter.Scrollbar(b8)
b11 = tkinter.Listbox(b8, height=15, width=60, yscrollcommand=b10.set)
b10.pack(b12 = tkinter.RIGHT, fill=tkinter.Y)
b11.pack(b12 = tkinter.LEFT, fill=tkinter.BOTH)
b11.pack()
b8.pack()
b13 = tkinter.Entry(b7, textvariable=b9)
b13.bind("<Return>", send)
b13.pack()
b14 = tkinter.Button(b7, text="Send", command=send)
b14.pack()
b7.protocol("WM_DELETE_WINDOW", on_closing)
b15 = input('Enter host: ')
b16 = input('Enter port: ')
if not b16:
    b16 = 33000
else:
    b16 = int(b16)
a1 = 1024
b17 = (b15, b16)
b18 = socket(AF_INET, SOCK_STREAM)
b18.connect(b17)
b19 = Thread(target=receive)
b19.start()
tkinter.mainloop()