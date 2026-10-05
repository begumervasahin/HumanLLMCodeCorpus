import socket
from threading import Thread
import sys
import tkinter
from ec import *
from aes import *
def fonk1(b1 = None):
    b2 = b23.get()
    b23.set("")
    if b2 = = "quit":
        b6.send(b9"quit")
        b6.close()
        b21.quit()
        return
    else:
        b3 = encrypt(b2, b20)
        b6.send(bytes(b3, "utf-8"))
def fonk2():
    while True:
        try:
            b4 = b6.recv(1024)
            if not b4:
                break
            b5 = decrypt(b4.decode("utf-8"), b20)
            b25.insert(tkinter.END, b5)
        except ConnectionAbortedError:
            break
if len(sys.argv) == 1:
    sys.exit()
b6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b6.connect((sys.argv[1], 12345))
b7 = []
E, b8 = generate_curve()
p, a, b9 = E.p(), E.a(), E.b9()
Gx, b10 = b8.x(), b8.y()
b11 = f"{p} {a} {b9} {Gx} {b10}"
b6.send(bytes(b11, "utf-8"))
b12 = b6.recv(1024).decode("utf-8").split(" ")
F, b13 = gen_curve(int(b12[0]), int(b12[1]))
b14 = random.random() * 100000
b15 = b14 * b13
b16 = b14 * b8
Qx, b17 = b16.x(), b16.y()
b18 = f"{Qx} {b17}"
b6.send(bytes(b18, "utf-8"))
b19 = str(b15.x() * b15.y())
b19 += " " * (16 - len(b19) % 16)
b20 = bytes(b19, "utf-8")
b7.append(b20)
b21 = tkinter.Tk()
b21.title("Chatter")
b22 = tkinter.Frame(b21)
b23 = tkinter.StringVar()
b23.set("Type your messages here.")
b24 = tkinter.Scrollbar(b22)
b25 = tkinter.Listbox(b22, height=15, width=50, yscrollcommand=b24.set)
b24.pack(b26 = tkinter.RIGHT, fill=tkinter.Y)
b25.pack(b26 = tkinter.LEFT, fill=tkinter.BOTH)
b25.pack()
b22.pack()
b27 = tkinter.Entry(b21, textvariable=b23)
b27.bind("<Return>", send_message)
b27.pack()
b28 = tkinter.Button(b21, text="Send", command=send_message)
b28.pack()
b29 = Thread(target=receive_messages)
b29.start()
tkinter.mainloop()
b6.close()