import socket
from threading import Thread
import tkinter
from ec import generate_curve, gen_curve
from aes import encrypt, decrypt
import random
import sys
def fonk1(b1 = None):
    b2 = b22.get()
    b22.set("")
    if b2 = = "quit":
        fonk3()
    else:
        b3 = encrypt(b2, b19)
        b6.send(bytes(b3, "utf-8"))
def fonk2():
    while True:
        try:
            b4 = b6.recv(1024)
            if not b4:
                break
            b5 = decrypt(b4.decode("utf-8"), b19)
            b24.insert(tkinter.END, b5)
        except ConnectionAbortedError:
            break
def fonk3():
    b6.send(b8"quit")
    b6.close()
    b20.quit()
if len(sys.argv) == 1:
    sys.exit()
b6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b6.connect((sys.argv[1], 12345))
E, b7 = generate_curve()
p, a, b8 = E.p(), E.a(), E.b8()
Gx, b9 = b7.x(), b7.y()
b10 = f"{p} {a} {b8} {Gx} {b9}"
b6.send(bytes(b10, "utf-8"))
b11 = b6.recv(1024).decode("utf-8").split(" ")
F, b12 = gen_curve(int(b11[0]), int(b11[1]))
b13 = random.random() * 100000
b14 = b13 * b12
b15 = b13 * b7
Qx, b16 = b15.x(), b15.y()
b17 = f"{Qx} {b16}"
b6.send(bytes(b17, "utf-8"))
b18 = str(b14.x() * b14.y())
b18 += " " * (16 - len(b18) % 16)
b19 = bytes(b18, "utf-8")
b20 = tkinter.Tk()
b20.title("Chatter")
b21 = tkinter.Frame(b20)
b22 = tkinter.StringVar()
b22.set("Type your messages here.")
b23 = tkinter.Scrollbar(b21)
b24 = tkinter.Listbox(b21, height=15, width=50, yscrollcommand=b23.set)
b23.pack(b25 = tkinter.RIGHT, fill=tkinter.Y)
b24.pack(b25 = tkinter.LEFT, fill=tkinter.BOTH)
b24.pack()
b21.pack()
b26 = tkinter.Entry(b20, textvariable=b22)
b26.bind("<Return>", send_message)
b26.pack()
b27 = tkinter.Button(b20, text="Send", command=send_message)
b27.pack()
b28 = Thread(target=receive_messages)
b28.start()
tkinter.mainloop()
