import tkinter
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import AES
AES_KEY = b'master key'
BUFSIZ = 1024
def receive_messages():
    while True:
        try:
            encrypted_msg = client_socket.recv(BUFSIZ)
            decrypted_msg = AES.decrypt(AES_KEY, encrypted_msg).decode("utf-8")
            msg_list.insert(tkinter.END, decrypted_msg)
        except OSError:
            break
def send_message(event=None):
    msg = message_var.get()
    message_var.set("")
    encrypted_msg = AES.encrypt(AES_KEY, msg.encode('UTF-8'))
    client_socket.send(encrypted_msg)
    if msg == "{quit}":
        client_socket.close()
        top.destroy()
def on_window_close(event=None):
    message_var.set("{quit}")
    send_message()
    top.destroy()
def setup_gui():
    top.title("Chat Room")
    messages_frame = tkinter.Frame(top)
    global message_var
    message_var = tkinter.StringVar()
    message_var.set("Type your messages here.")
    scrollbar = tkinter.Scrollbar(messages_frame)
    global msg_list
    msg_list = tkinter.Listbox(messages_frame, height=15, width=60, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msg_list.pack()
    messages_frame.pack()
    entry_field = tkinter.Entry(top, textvariable=message_var)
    entry_field.bind("<Return>", send_message)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send_message)
    send_button.pack()
    top.protocol("WM_DELETE_WINDOW", on_window_close)
def connect_to_server():
    host = input('Enter host: ')
    port = input('Enter port: ')
    if not port:
        port = 33000
    else:
        port = int(port)
    addr = (host, port)
    client_socket.connect(addr)
top = tkinter.Tk()
client_socket = socket(AF_INET, SOCK_STREAM)
setup_gui()
connect_to_server()
Thread(target=receive_messages).start()
tkinter.mainloop()