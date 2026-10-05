import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
def fonk1(key, plaintext):
    b1 = AES.new(key, AES.MODE_CBC)
    b2 = b1.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    b3 = base64.b64encode(b1.b3).decode('utf-8')
    b4 = base64.b64encode(b2).decode('utf-8')
    return b3 + b4
def fonk2(key, ciphertext):
    b3, b4 = ciphertext[:24], ciphertext[24:]
    b3 = base64.b64decode(b3)
    b4 = base64.b64decode(b4)
    b1 = AES.new(key, AES.MODE_CBC, b3)
    b5 = unpad(b1.decrypt(b4), AES.block_size)
    return b5.decode('utf-8')
def fonk3():
    while True:
        try:
            b6 = b19.recv(a1).decode('utf-8')
            b7 = fonk2(b22, b6)
            b12.insert(tkinter.END, b7)
        except OSError:
            break
def fonk4(b8 = None):
    b7 = b10.get()
    b10.set("")
    b6 = fonk1(b22, b7)
    b19.send(b6.encode('utf-8'))
    if b7 = = "{quit}":
        b19.close()
        b21.quit()
def fonk5(b8 = None):
    b10.set("{quit}")
    fonk4()
def fonk6():
    b21.title("Chat Room")
    b9 = tkinter.Frame(b21)
    global b10
    b10 = tkinter.StringVar()
    b10.set("Type your messages here.")
    b11 = tkinter.Scrollbar(b9)
    global b12
    b12 = tkinter.Listbox(b9, height=15, width=50, yscrollcommand=b11.set)
    b11.pack(b13 = tkinter.RIGHT, fill=tkinter.Y)
    b12.pack(b13 = tkinter.LEFT, fill=tkinter.BOTH)
    b12.pack()
    b9.pack()
    b14 = tkinter.Entry(b21, textvariable=b10)
    b14.bind("<Return>", send_message)
    b14.pack()
    b15 = tkinter.Button(b21, text="Send", command=send_message)
    b15.pack()
    b21.protocol("WM_DELETE_WINDOW", on_window_close)
def fonk7():
    global b19
    b16 = input('Enter host: ')
    b17 = input('Enter port: ')
    if not b17:
        b17 = 33000
    else:
        b17 = int(b17)
    b18 = (b16, b17)
    b19 = socket(AF_INET, SOCK_STREAM)
    b19.connect(b18)
if b20 = = "__main__":
    b21 = tkinter.Tk()
    b22 = get_random_bytes(16)
    a1 = 1024
    fonk6()
    fonk7()
    b23 = Thread(target=receive_messages)
    b23.start()
    tkinter.mainloop()