import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
b1 = b'master key'
a1 = 1024
def fonk1():
    while True:
        try:
            b2 = b17.recv(a1)
            b3 = AES.decrypt(b1, b2).decode("utf-8")
            b9.insert(tkinter.END, b3)
        except OSError:
            break
def fonk2(b4 = None):
    b5 = b7.get()
    b7.set("")
    b2 = AES.encrypt(b1, b5.encode('UTF-8'))
    b17.send(b2)
    if b5 = = "{quit}":
        b17.close()
        b16.destroy()
def fonk3(b4 = None):
    b7.set("{quit}")
    fonk2()
    b16.destroy()
def fonk4():
    b16.title("Chat Room")
    b6 = tkinter.Frame(b16)
    global b7
    b7 = tkinter.StringVar()
    b7.set("Type your messages here.")
    b8 = tkinter.Scrollbar(b6)
    global b9
    b9 = tkinter.Listbox(b6, height=15, width=60, yscrollcommand=b8.set)
    b8.pack(b10 = tkinter.RIGHT, fill=tkinter.Y)
    b9.pack(b10 = tkinter.LEFT, fill=tkinter.BOTH)
    b9.pack()
    b6.pack()
    b11 = tkinter.Entry(b16, textvariable=b7)
    b11.bind("<Return>", send_message)
    b11.pack()
    b12 = tkinter.Button(b16, text="Send", command=send_message)
    b12.pack()
    b16.protocol("WM_DELETE_WINDOW", on_window_close)
def fonk5():
    b13 = input('Enter b13: ')
    b14 = input('Enter b14: ')
    if not b14:
        b14 = 33000
    else:
        b14 = int(b14)
    b15 = (b13, b14)
    b17.connect(b15)
b16 = tkinter.Tk()
b17 = socket(AF_INET, SOCK_STREAM)
fonk4()
fonk5()
Thread(b18 = receive_messages).start()
tkinter.mainloop()