import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master b1'
def fonk1():
    while True:
        try:
            b2 = b17.recv(a1)
            b3 = AES.decrypt(b1, b2).decode("utf-8")
            b10.insert(tkinter.END, b3)
        except OSError:
            break
def fonk2(b4 = None):
    b5 = b8.get()
    b8.set("")
    b2 = AES.encrypt(b1, b5.encode('UTF-8'))
    b17.fonk2(b2)
    if b5 = = "{quit}":
        b17.close()
        b6.destroy()
def fonk3(b4 = None):
    b8.set("{quit}")
    fonk2()
    b6.destroy()
b6 = tkinter.Tk()
b6.title("Chat Room")
b7 = tkinter.Frame(b6)
b8 = tkinter.StringVar()
b8.set("Type your messages here.")
b9 = tkinter.Scrollbar(b7)
b10 = tkinter.Listbox(b7, height=15, width=60, yscrollcommand=b9.set)
b9.pack(b11 = tkinter.RIGHT, fill=tkinter.Y)
b10.pack(b11 = tkinter.LEFT, fill=tkinter.BOTH)
b10.pack()
b7.pack()
b12 = tkinter.Entry(b6, textvariable=b8)
b12.bind("<Return>", send)
b12.pack()
b13 = tkinter.Button(b6, text="Send", command=send)
b13.pack()
b6.protocol("WM_DELETE_WINDOW", on_closing)
b14 = input('Enter host: ')
b15 = input('Enter port: ')
if not b15:
    b15 = 33000
else:
    b15 = int(b15)
a1 = 1024
b16 = (b14, b15)
b17 = socket(AF_INET, SOCK_STREAM)
b17.connect(b16)
b18 = Thread(target=receive)
b18.start()
tkinter.mainloop()