import socket
from threading import Thread
import sys
import random
import tkinter as tk
from aes import encrypt, decrypt
from ec import generate_curve, gen_curve
def main():
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_ip>")
        sys.exit()
    server_ip = sys.argv[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, 12345))
    keys = []
    E, G = generate_curve()
    p, a, b = E.p(), E.a(), E.b()
    Gx, Gy = G.x(), G.y()
    public_key = f"{p} {a} {b} {Gx} {Gy}"
    sock.send(public_key.encode('utf-8'))
    n_client = random.random() * 100000
    exchanged_key = sock.recv(1024).decode("utf-8").split(" ")
    F, Q = gen_curve(int(exchanged_key[0]), int(exchanged_key[1]))
    key = n_client * Q
    p_client = n_client * G
    Qx, Qy = p_client.x(), p_client.y()
    key_client = f"{Qx} {Qy}"
    sock.send(key_client.encode('utf-8'))
    aes_key = str(key.x() * key.y())[:16]
    ex_key = aes_key.encode('utf-8')
    keys.append(ex_key)
    def send_msg(event=None):
        message = my_msg.get()
        my_msg.set("")
        if message == "quit":
            sock.close()
            root.quit()
        else:
            encrypted_msg = encrypt(message.encode('utf-8'), ex_key)
            sock.send(encrypted_msg)
    def listen_msg():
        while True:
            msg = sock.recv(1024)
            if not msg:
                break
            decrypted_msg = decrypt(msg, keys[0])
            msg_list.insert(tk.END, decrypted_msg.decode('utf-8'))
    root = tk.Tk()
    root.title("Chatter")
    messages_frame = tk.Frame(root)
    my_msg = tk.StringVar()
    my_msg.set("Type your messages here.")
    scrollbar = tk.Scrollbar(messages_frame)
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    messages_frame.pack()
    entry_field = tk.Entry(root, textvariable=my_msg)
    entry_field.bind("<Return>", send_msg)
    entry_field.pack()
    send_button = tk.Button(root, text="Send", command=send_msg)
    send_button.pack()
    receive_thread = Thread(target=listen_msg)
    receive_thread.start()
    tk.mainloop()
    sock.close()
if __name__ == "__main__":
    main()