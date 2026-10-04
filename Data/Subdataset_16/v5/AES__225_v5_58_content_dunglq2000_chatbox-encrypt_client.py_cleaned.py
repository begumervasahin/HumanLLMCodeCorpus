import socket
import sys
import random
import tkinter as tk
from threading import Thread
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
def fonk1():
    if len(sys.argv) != 2:
        print("Usage: python client.py <b1>")
        sys.exit()
    b1 = sys.argv[1]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((b1, 12345))
        b2 = []
        E, b3 = generate_curve()
        p, a, b4 = E.p(), E.a(), E.b4()
        Gx, b5 = b3.x(), b3.y()
        b6 = f"{p} {a} {b4} {Gx} {b5}"
        sock.send(b6.encode('utf-8'))
        b7 = random.random() * 100000
        b8 = sock.recv(1024).decode("utf-8").split()
        F, b9 = gen_curve(int(b8[0]), int(b8[1]))
        b10 = b7 * b9
        b11 = b7 * b3
        Qx, b12 = b11.x(), b11.y()
        b13 = f"{Qx} {b12}"
        sock.send(b13.encode('utf-8'))
        b14 = str(b10.x() * b10.y())
        while len(b14) < 16:
            b14 += "0"
        b15 = b14[:16].encode('utf-8')
        b2.append(b15)
        def fonk2(b16 = None):
            b17 = b23.get()
            b23.set("")
            if b17.lower() == "quit":
                sock.close()
                b21.quit()
            else:
                b18 = encrypt(b17.encode('utf-8'), b15)
                sock.send(b18)
        def fonk3():
            while True:
                b19 = sock.recv(1024)
                if not b19:
                    break
                b20 = decrypt(b19, b2[0])
                b25.insert(tk.END, b20.decode('utf-8'))
        b21 = tk.Tk()
        b21.title("Chatter")
        b22 = tk.Frame(b21)
        b23 = tk.StringVar()
        b23.set("Type your messages here.")
        b24 = tk.Scrollbar(b22)
        b25 = tk.Listbox(b22, height=15, width=50, yscrollcommand=b24.set)
        b24.pack(b26 = tk.RIGHT, fill=tk.Y)
        b25.pack(b26 = tk.LEFT, fill=tk.BOTH, expand=True)
        b22.pack()
        b27 = tk.Entry(b21, textvariable=b23)
        b27.bind("<Return>", send_msg)
        b27.pack()
        b28 = tk.Button(b21, text="Send", command=send_msg)
        b28.pack()
        b29 = Thread(target=listen_msg)
        b29.start()
        tk.mainloop()
if b30 = = "__main__":
    fonk1()