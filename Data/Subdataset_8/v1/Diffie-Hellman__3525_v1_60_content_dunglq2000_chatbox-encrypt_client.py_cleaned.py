import socket
from threading import Thread
import sys
import tkinter
from ec import *
from aes import *
def send_message(event=None):
    message = my_msg.get()
    my_msg.set("")
    if message == "quit":
        sock.send(b"quit")
        sock.close()
        top.quit()
        return
    else:
        encrypted_msg = encrypt(message, encryption_key)
        sock.send(bytes(encrypted_msg, "utf-8"))
def receive_messages():
    while True:
        try:
            received_msg = sock.recv(1024)
            if not received_msg:
                break
            decrypted_msg = decrypt(received_msg.decode("utf-8"), encryption_key)
            msg_list.insert(tkinter.END, decrypted_msg)
        except ConnectionAbortedError:
            break
if len(sys.argv) == 1:
    sys.exit()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], 12345))
keys = []
E, G = generate_curve()
p, a, b = E.p(), E.a(), E.b()
Gx, Gy = G.x(), G.y()
public_key = f"{p} {a} {b} {Gx} {Gy}"
sock.send(bytes(public_key, "utf-8"))
exchanged_key = sock.recv(1024).decode("utf-8").split(" ")
F, Q = gen_curve(int(exchanged_key[0]), int(exchanged_key[1]))
n_client = random.random() * 100000
key = n_client * Q
p_client = n_client * G
Qx, Qy = p_client.x(), p_client.y()
key_client = f"{Qx} {Qy}"
sock.send(bytes(key_client, "utf-8"))
aes_key = str(key.x() * key.y())
aes_key += " " * (16 - len(aes_key) % 16)
encryption_key = bytes(aes_key, "utf-8")
keys.append(encryption_key)
top = tkinter.Tk()
top.title("Chatter")
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
entry_field.bind("<Return>", send_message)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send_message)
send_button.pack()
receive_thread = Thread(target=receive_messages)
receive_thread.start()
tkinter.mainloop()
sock.close()