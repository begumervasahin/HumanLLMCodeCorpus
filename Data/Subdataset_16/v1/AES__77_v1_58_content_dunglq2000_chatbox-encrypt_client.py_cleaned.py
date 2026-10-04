import socket
from threading import Thread
import sys
import random
import tkinter
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
def fonk1():
    if len(sys.argv) != 2:
        print("Usage: python client.py <b1>")
        exit()
    b1 = sys.argv[1]
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.connect((b1, 12345))
    b3 = []
    E, b4 = generate_curve()
    b5 = E.b5()
    b6 = E.b6()
    b7 = E.b7()
    b8 = b4.x()
    b9 = b4.y()
    b10 = f"{b5} {b6} {b7} {b8} {b9}"
    b2.send(bytes(b10, "utf-8"))
    b11 = random.random() * 100000
    b12 = b2.recv(1024).decode("utf-8").split(" ")
    F, b13 = gen_curve(int(b12[0]), int(b12[1]))
    b14 = b11 * b13
    b15 = b11 * b4
    b16 = b15.x()
    b17 = b15.y()
    b18 = f"{b16} {b17}"
    b2.send(bytes(b18, "utf-8"))
    b19 = str(b14.x() * b14.y())
    a1 = 0
    while len(b19[a1:]) < 16:
        a1 += 1
    b20 = bytes(b19[a1:], "utf-8")
    b3.append(b20)
    def fonk2(b21 = None):
        b22 = b28.get()
        b28.set("")
        if b22 = = "quit":
            b2.close()
            b26.quit()
        else:
            b23 = encrypt(bytes(b22, "utf-8"), b20)
            b2.send(bytes(b23, "utf-8"))
    def fonk3():
        while True:
            b24 = b2.recv(1024)
            if not b24:
                break
            b25 = decrypt(b24.decode("utf-8"), b3[0])
            b30.insert(tkinter.END, b25)
    b26 = tkinter.Tk()
    b26.title("Chatter")
    b27 = tkinter.Frame(b26)
    b28 = tkinter.StringVar()
    b28.set("Type your messages here.")
    b29 = tkinter.Scrollbar(b27)
    b30 = tkinter.Listbox(b27, height=15, width=50, yscrollcommand=b29.set)
    b29.pack(b31 = tkinter.RIGHT, fill=tkinter.Y)
    b30.pack(b31 = tkinter.LEFT, fill=tkinter.BOTH)
    b30.pack()
    b27.pack()
    b32 = tkinter.Entry(b26, textvariable=b28)
    b32.bind("<Return>", send_msg)
    b32.pack()
    b33 = tkinter.Button(b26, text="Send", command=send_msg)
    b33.pack()
    b34 = Thread(target=listen_msg)
    b34.start()
    tkinter.mainloop()
    b2.close()
if b35 = = "__main__":
    fonk1()