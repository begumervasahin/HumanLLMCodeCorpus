import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv + ct
def decrypt_message(key, ciphertext):
    iv, ct = ciphertext[:24], ciphertext[24:]
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
key = get_random_bytes(16)
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode('utf-8')
            decrypted_message = decrypt_message(key, msg)
            msg_list.insert(tkinter.END, decrypted_message)
        except OSError:
            break
def send(event=None):
    message = my_msg.get()
    my_msg.set("")
    encrypted_message = encrypt_message(key, message)
    client_socket.send(encrypted_message.encode('utf-8'))
    if message == "{quit}":
        client_socket.close()
        top.quit()
def on_closing(event=None):
    my_msg.set("{quit}")
    send()
top = tkinter.Tk()
top.title("Chat Room")
messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()
entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
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
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
