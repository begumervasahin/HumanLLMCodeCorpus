import socket
from threading import Thread
import sys
from aes import *
import threading
from ec import *
import random
import tkinter
if len(sys.argv) == 1:
	exit
b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b1.connect((sys.argv[1], 12345))
b2 = []
E, b3 = generate_curve()
b4 = E.b4()
b5 = E.b5()
b6 = E.b6()
b7 = b3.x()
b8 = b3.y()
b9 = str(b4) + " " + str(b5) + " " + str(b6) + " " + str(b7) + " " + str(b8)
b1.send(bytes(b9, "utf-8"))
b10 = random.random() * 100000
b11 = b1.recv(1024).decode("utf-8").split(" ")
F, b12 = gen_curve(int(b11[0]), int(b11[1]))
b13 = b10 * b12
b14 = b10 * b3
b15 = b14.x()
b16 = b14.y()
b17 = str(b15) + " " + str(b16)
b1.send(bytes(b17, "utf-8"))
b18 = str(b13.x() * b13.y())
a1 = 0
while len(b18[a1:]) != 16:
	a1 += 1
b19 = bytes(b18[a1:], "utf-8")
print(b19)
b2.append(b19)
def fonk1(b20 = None):
		b21 = b27.get()
		b27.set("")
		b22 = bytes(b21, "utf-8")
		if b22 = = b6"quit":
			b1.close()
			b25.quit()
			return
		else:
			b23 = encrypt(b22, b19)
			b1.send(bytes(b23, "utf-8"))
def fonk2():
	b13 = str(1234567812345678)
	while True:
		b22 = b1.recv(1024)
		b24 = decrypt(b22.decode("utf-8"), b2[0])
		if not b22:
			break
		b29.insert(tkinter.END, bytes(b24, "utf-8"))
b25 = tkinter.Tk()
b25.title("Chatter")
b26 = tkinter.Frame(b25)
b27 = tkinter.StringVar()
b27.set("Type your messages here.")
b28 = tkinter.Scrollbar(b26)
b29 = tkinter.Listbox(b26, height=15, width=50, yscrollcommand=b28.set)
b28.pack(b30 = tkinter.RIGHT, fill=tkinter.Y)
b29.pack(b30 = tkinter.LEFT, fill=tkinter.BOTH)
b29.pack()
b26.pack()
b31 = tkinter.Entry(b25, textvariable=b27)
b31.bind("<Return>", sendMsg)
b31.pack()
b32 = tkinter.Button(b25, text="Send", command=sendMsg)
b32.pack()
b33 = Thread(target=listenMsg)
b33.start()
tkinter.mainloop()
b1.close()