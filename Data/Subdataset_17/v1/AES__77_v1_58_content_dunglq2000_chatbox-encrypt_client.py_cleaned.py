import socket
from threading import Thread
import sys
import random
import tkinter
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_ip>")
        exit()
    server_ip = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, 12345))
    keys = []
    E, G = generate_curve()
    p = E.p()
    a = E.a()
    b = E.b()
    Gx = G.x()
    Gy = G.y()
    public_key = f"{p} {a} {b} {Gx} {Gy}"
    sock.send(bytes(public_key, "utf-8"))
    nClient = random.random() * 100000
    exchanged_key = sock.recv(1024).decode("utf-8").split(" ")
    F, Q = gen_curve(int(exchanged_key[0]), int(exchanged_key[1]))
    key = nClient * Q
    pClient = nClient * G
    Qx = pClient.x()
    Qy = pClient.y()
    keyClient = f"{Qx} {Qy}"
    sock.send(bytes(keyClient, "utf-8"))
    aes_key = str(key.x() * key.y())
    i = 0
    while len(aes_key[i:]) < 16:
        i += 1
    ex_key = bytes(aes_key[i:], "utf-8")
    keys.append(ex_key)
    def send_msg(event=None):
        message = my_msg.get()
        my_msg.set("")
        if message == "quit":
            sock.close()
            top.quit()
        else:
            encrypted_msg = encrypt(bytes(message, "utf-8"), ex_key)
            sock.send(bytes(encrypted_msg, "utf-8"))
    def listen_msg():
        while True:
            msg = sock.recv(1024)
            if not msg:
                break
            decrypted_msg = decrypt(msg.decode("utf-8"), keys[0])
            msg_list.insert(tkinter.END, decrypted_msg)
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
    entry_field.bind("<Return>", send_msg)
    entry_field.pack()
    send_button = tkinter.Button(top, text="Send", command=send_msg)
    send_button.pack()
    receive_thread = Thread(target=listen_msg)
    receive_thread.start()
    tkinter.mainloop()
    sock.close()
if __name__ == "__main__":
    main()