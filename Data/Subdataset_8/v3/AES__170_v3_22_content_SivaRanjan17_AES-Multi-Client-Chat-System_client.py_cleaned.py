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
def receive_messages():
    while True:
        try:
            encrypted_msg = client_socket.recv(buffer_size).decode('utf-8')
            message = decrypt_message(encryption_key, encrypted_msg)
            message_list.insert(tkinter.END, message)
        except OSError:
            break
def send_message(event=None):
    message = user_message.get()
    user_message.set("")
    encrypted_msg = encrypt_message(encryption_key, message)
    client_socket.send(encrypted_msg.encode('utf-8'))
    if message == "{quit}":
        client_socket.close()
        top.quit()
def on_window_close(event=None):
    user_message.set("{quit}")
    send_message()
def setup_gui():
    top.title("Chat Room")
    messages_frame = tkinter.Frame(top)
    global user_message
    user_message = tkinter.StringVar()
    user_message.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)
    global message_list
    message_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    message_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    message_list.pack()
    messages_frame.pack()
    entry_field = tkinter.Entry(top, textvariable=user_message)
    entry_field.bind("<Return>", send_message)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send_message)
    send_button.pack()
    top.protocol("WM_DELETE_WINDOW", on_window_close)
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
if __name__ == "__main__":
    top = tkinter.Tk()
    encryption_key = get_random_bytes(16)
    buffer_size = 1024
    setup_gui()
    setup_network()
    receive_thread = Thread(target=receive_messages)
    receive_thread.start()
    tkinter.mainloop()