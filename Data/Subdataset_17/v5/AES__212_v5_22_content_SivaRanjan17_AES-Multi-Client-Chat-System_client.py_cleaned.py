
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter as tk
from Crypto.Cipher import AES
import base64
BLOCK_SIZE = 16
BUFSIZ = 1024
KEY = b'master key'
def pad(data):
    padding_length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    padding = chr(padding_length) * padding_length
    return data + padding.encode()
def unpad(data):
    padding_length = ord(data[-1:])
    return data[:-padding_length]
def encrypt(key, data):
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(data)
    return base64.b64encode(encrypted_data)
def decrypt(key, enc_data):
    enc_data = base64.b64decode(enc_data)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(enc_data)
    return unpad(decrypted_data)
def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ)
            message = decrypt(KEY, msg).decode("utf-8")
            msg_list.insert(tk.END, message)
        except OSError:
            break
def send(event=None):
    message = my_msg.get()
    my_msg.set("")
    encrypted_message = encrypt(KEY, message.encode('utf-8'))
    client_socket.send(encrypted_message)
    if message == "{quit}":
        client_socket.close()
        top.destroy()
def on_closing(event=None):
    my_msg.set("{quit}")
    send()
def setup_gui():
    global msg_list, my_msg, top
    top = tk.Tk()
    top.title("Chat Room")
    messages_frame = tk.Frame(top)
    my_msg = tk.StringVar()
    my_msg.set("<Type your message here>")
    scrollbar = tk.Scrollbar(messages_frame)
    msg_list = tk.Listbox(messages_frame, height=15, width=60, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    messages_frame.pack()
    entry_field = tk.Entry(top, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tk.Button(top, text="Send", command=send)
    send_button.pack()
    top.protocol("WM_DELETE_WINDOW", on_closing)
def setup_network():
    global client_socket
    HOST = input('Enter host: ')
    PORT = input('Enter port: ')
    if not PORT:
        PORT = 33000
    else:
        PORT = int(PORT)
    ADDR = (HOST, PORT)
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(ADDR)
    receive_thread = Thread(target=receive)
    receive_thread.start()
if __name__ == "__main__":
    setup_gui()
    setup_network()
    tk.mainloop()