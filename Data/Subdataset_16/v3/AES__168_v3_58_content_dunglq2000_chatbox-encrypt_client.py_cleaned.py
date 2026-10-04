import socket
from threading import Thread
import sys
import random
import tkinter as tk
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
def fonk1():
    if len(sys.argv) != 2:
        print("Usage: python client.py <b1>")
        sys.exit()
    b1 = sys.argv[1]
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.connect((b1, 12345))
    b3 = []
    E, b4 = generate_curve()
    p, a, b5 = E.p(), E.a(), E.b5()
    Gx, b6 = b4.x(), b4.y()
    b7 = f"{p} {a} {b5} {Gx} {b6}"
    b2.send(b7.encode('utf-8'))
    b8 = random.random() * 100000
    b9 = b2.recv(1024).decode("utf-8").split(" ")
    F, b10 = gen_curve(int(b9[0]), int(b9[1]))
    b11 = b8 * b10
    b12 = b8 * b4
    Qx, b13 = b12.x(), b12.y()
    b14 = f"{Qx} {b13}"
    b2.send(b14.encode('utf-8'))
    b15 = str(b11.x() * b11.y())[:16]
    b16 = b15.encode('utf-8')
    b3.append(b16)
    def fonk2(b17 = None):
        b18 = b24.get()
        b24.set("")
        if b18 = = "quit":
            b2.close()
            b22.quit()
        else:
            b19 = encrypt(b18.encode('utf-8'), b16)
            b2.send(b19)
    def fonk3():
        while True:
            b20 = b2.recv(1024)
            if not b20:
                break
            b21 = decrypt(b20, b3[0])
            b26.insert(tk.END, b21.decode('utf-8'))
    b22 = tk.Tk()
    b22.title("Chatter")
    b23 = tk.Frame(b22)
    b24 = tk.StringVar()
    b24.set("Type your messages here.")
    b25 = tk.Scrollbar(b23)
    b26 = tk.Listbox(b23, height=15, width=50, yscrollcommand=b25.set)
    b25.pack(b27 = tk.RIGHT, fill=tk.Y)
    b26.pack(b27 = tk.LEFT, fill=tk.BOTH)
    b23.pack()
    b28 = tk.Entry(b22, textvariable=b24)
    b28.bind("<Return>", send_msg)
    b28.pack()
    b29 = tk.Button(b22, text="Send", command=send_msg)
    b29.pack()
    b30 = Thread(target=listen_msg)
    b30.start()
    tk.mainloop()
    b2.close()
if b31 = = "__main__":
    fonk1()