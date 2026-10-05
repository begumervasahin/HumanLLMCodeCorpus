import socket
from threading import Thread
import tkinter
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
import random
import sys
def send_message(event=None):
    message = message_entry.get()
    message_entry.delete(0, tkinter.END)
    if message == "quit":
        send_quit_signal()
    else:
        encrypted_msg = encrypt(message.encode(), encryption_key)
        sock.send(encrypted_msg)
def receive_messages():
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            decrypted_msg = decrypt(msg, keys[0])
            msg_list.insert(tkinter.END, decrypted_msg.decode())
        except ConnectionAbortedError:
            break
def send_quit_signal():
    sock.send(b"quit")
    sock.close()
    top.quit()
if len(sys.argv) == 1:
    sys.exit()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((sys.argv[1], 12345))
E, G = generate_curve()
p, a, b = E.p(), E.a(), E.b()
Gx, Gy = G.x(), G.y()
public_key = f"{p} {a} {b} {Gx} {Gy}"
sock.send(public_key.encode())
exchanged_key = sock.recv(1024).decode().split()
F, Q = gen_curve(int(exchanged_key[0]), int(exchanged_key[1]))
n_client = random.random() * 100000
key = n_client * Q
p_client = n_client * G
Qx, Qy = p_client.x(), p_client.y()
key_client = f"{Qx} {Qy}"
sock.send(key_client.encode())
aes_key = str(key.x() * key.y())
padding = 16 - len(aes_key) % 16
aes_key += " " * padding
encryption_key = aes_key.encode()
top = tkinter.Tk()
top.title("Chatter")
messages_frame = tkinter.Frame(top)
message_entry = tkinter.Entry(top)
msg_list = tkinter.Listbox(messages_frame, height=15, width=50)
scrollbar = tkinter.Scrollbar(messages_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
message_entry.pack()
messages_frame.pack()
send_button = tkinter.Button(top, text="Send", command=send_message)
send_button.pack()
receive_thread = Thread(target=receive_messages)
receive_thread.start()
top.mainloop()
sock.close()