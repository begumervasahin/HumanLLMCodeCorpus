import socket
import threading
from queue import Queue
import spec
b1 = spec.host
b2 = int(spec.port)
a1 = 2
def fonk1():
    b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b3.bind((b1, b2))
    b3.listen(a1)
    print("Waiting for players...")
    def fonk2(client, b14, client_id, b13):
        client.setblocking(1)
        b4 = ""
        while True:
            try:
                b4 += client.recv(1024).decode("UTF-8")
                b5 = b4.split("\n")
                while len(b5) > 1:
                    b6 = b5[0]
                    b4 = "\n".join(b5[1:])
                    b14.put(f"{client_id} {b6}")
                    b5 = b4.split("\n")
            except:
                return
    def fonk3(b13, b14):
        while True:
            b7 = b14.get(True, None)
            b8 = b7.split(" ")
            b9 = b8[0]
            b10 = b8[1]
            b11 = " ".join(b8[2:])
            if b11:
                for c_id in b13:
                    if c_id != b9:
                        b12 = f"{b10} {b9} {b11}\n"
                        b13[c_id].send(b12.encode())
            b14.task_done()
    b13 = {}
    a2 = 0
    b14 = Queue(100)
    threading.Thread(b15 = server_thread, args=(b13, b14)).start()
    b16 = ["Player1", "Player2"]
    while True:
        try:
            client_socket, b17 = b3.accept()
            b18 = b16[a2]
            for existing_client_id in b13:
                b13[existing_client_id].send(f"PlayerJoined {b18}\n".encode())
                client_socket.send(f"PlayerJoined {existing_client_id}\n".encode())
            b13[b18] = client_socket
            client_socket.send(f"MyIDis {b18}\n".encode())
            print(f"Connection received from {b18}")
            threading.Thread(b15 = handle_client, args=(client_socket, b14, b18, b13)).start()
            a2 += 1
        except:
            print("Max players reached")
if b19 = = '__main__':
    fonk1()