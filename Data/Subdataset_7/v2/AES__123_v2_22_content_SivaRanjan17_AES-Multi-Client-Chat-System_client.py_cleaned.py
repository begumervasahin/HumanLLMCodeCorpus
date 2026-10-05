import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
def fonk1(b6, plaintext):
    b1 = AES.new(b6, AES.MODE_CBC)
    b2 = b1.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    b3 = base64.b64encode(b1.b3).decode('utf-8')
    b4 = base64.b64encode(b2).decode('utf-8')
    return b3 + b4
def fonk2(b6, ciphertext):
    b3, b4 = ciphertext[:24], ciphertext[24:]
    b3 = base64.b64decode(b3)
    b4 = base64.b64decode(b4)
    b1 = AES.new(b6, AES.MODE_CBC, b3)
    b5 = unpad(b1.decrypt(b4), AES.block_size)
    return b5.decode('utf-8')
b6 = get_random_bytes(16)
def fonk3():
    while True:
        try:
            b7 = b23.recv(a1).decode('utf-8')
            b8 = fonk2(b6, b7)
            b16.insert(tkinter.END, b8)
        except OSError:
            break
def fonk4(b9 = None):
    b10 = b14.get()
    b14.set("")
    b11 = fonk1(b6, b10)
    b23.fonk4(b11.encode('utf-8'))
    if b10 = = "{quit}":
        b23.close()
        b12.quit()
def fonk5(b9 = None):
    b14.set("{quit}")
    fonk4()
b12 = tkinter.Tk()
b12.title("Chat Room")
b13 = tkinter.Frame(b12)
b14 = tkinter.StringVar()
b14.set("Type your messages here.")
b15 = tkinter.Scrollbar(b13)
b16 = tkinter.Listbox(b13, height=15, width=50, yscrollcommand=b15.set)
b15.pack(b17 = tkinter.RIGHT, fill=tkinter.Y)
b16.pack(b17 = tkinter.LEFT, fill=tkinter.BOTH)
b16.pack()
b13.pack()
b18 = tkinter.Entry(b12, textvariable=b14)
b18.bind("<Return>", send)
b18.pack()
b19 = tkinter.Button(b12, text="Send", command=send)
b19.pack()
b12.protocol("WM_DELETE_WINDOW", on_closing)
b20 = input('Enter host: ')
b21 = input('Enter port: ')
if not b21:
    b21 = 33000
else:
    b21 = int(b21)
a1 = 1024
b22 = (b20, b21)
b23 = socket(AF_INET, SOCK_STREAM)
b23.connect(b22)
b24 = Thread(target=receive)
b24.start()
tkinter.mainloop()
