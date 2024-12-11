import socket
from threading import Thread
import tkinter
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
import random
import sys
def fonk1(b1 = None):
    b2 = b23.get()
    b23.delete(0, tkinter.END)
    if b2 = = "quit":
        fonk3()
    else:
        b3 = encrypt(b2.encode(), b20)
        b6.send(b3)
def fonk2():
    while True:
        try:
            b4 = b6.recv(1024)
            if not b4:
                break
            b5 = decrypt(b4, keys[0])
            b24.insert(tkinter.END, b5.decode())
        except ConnectionAbortedError:
            break
def fonk3():
    b6.send(b8"quit")
    b6.close()
    b21.quit()
if len(sys.argv) == 1:
    sys.exit()
b6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b6.connect((sys.argv[1], 12345))
E, b7 = generate_curve()
p, a, b8 = E.p(), E.a(), E.b8()
Gx, b9 = b7.x(), b7.y()
b10 = f"{p} {a} {b8} {Gx} {b9}"
b6.send(b10.encode())
b11 = b6.recv(1024).decode().split()
F, b12 = gen_curve(int(b11[0]), int(b11[1]))
b13 = random.random() * 100000
b14 = b13 * b12
b15 = b13 * b7
Qx, b16 = b15.x(), b15.y()
b17 = f"{Qx} {b16}"
b6.send(b17.encode())
b18 = str(b14.x() * b14.y())
b19 = 16 - len(b18) % 16
b18 += " " * b19
b20 = b18.encode()
b21 = tkinter.Tk()
b21.title("Chatter")
b22 = tkinter.Frame(b21)
b23 = tkinter.Entry(b21)
b24 = tkinter.Listbox(b22, height=15, width=50)
b25 = tkinter.Scrollbar(b22)
b25.pack(b26 = tkinter.RIGHT, fill=tkinter.Y)
b24.pack(b26 = tkinter.LEFT, fill=tkinter.BOTH)
b23.pack()
b22.pack()
b27 = tkinter.Button(b21, text="Send", command=send_message)
b27.pack()
b28 = Thread(target=receive_messages)
b28.start()
b21.mainloop()
b6.close()