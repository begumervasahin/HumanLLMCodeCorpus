from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from Crypto.Cipher import AES
import base64
BLOCK_SIZE = 16
def pad(data):
    length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + (chr(length) * length).encode()
def unpad(data):
    return data[:-ord(data[len(data)-1:])]
def encrypt(key, data):
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(data))
def decrypt(key, enc_data):
    enc_data = base64.b64decode(enc_data)
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(enc_data))
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ)
            message = decrypt(key, msg).decode("utf-8")
            msg_list.insert(tk.END, message)
        except OSError:
            break
def send(event=None):
    message1 = my_msg.get()
    my_msg.set("")
    message = message1.encode('UTF-8')
    ciphertext = encrypt(key, message)
    client_socket.send(ciphertext)
    if message1 == "{quit}":
        client_socket.close()
        top.destroy()
def on_closing(event=None):
    my_msg.set("{quit}")
    send()
    top.destroy()
top = tk.Tk()
top.title("Chat Room")
messages_frame = tk.Frame(top)
my_msg = tk.StringVar()
my_msg.set("<messages here>")
scrollbar = tk.Scrollbar(messages_frame)
msg_list = tk.Listbox(messages_frame, height=15, width=60, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tk.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tk.Button(top, text="Send", command=send)
send_button.pack()
top.protocol("WM_DELETE_WINDOW", on_closing)
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)
BUFSIZ = 1024
ADDR = (HOST, PORT)
key = b'master key'
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tk.mainloop()