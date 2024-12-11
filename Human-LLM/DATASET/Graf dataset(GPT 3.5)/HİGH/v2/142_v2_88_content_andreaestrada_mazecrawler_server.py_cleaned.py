import socket
import threading
from queue import Queue
b1 = ""
a1 = 12345
def fonk1():
    a2 = 2
    b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2.bind((b1, a1))
    b2.listen(a2)
    print("Waiting for players...")
    def fonk2(client, b13, c_id, b12):
        client.setblocking(1)
        b3 = ""
        while True:
            try:
                b3 += client.recv(10).decode("UTF-8")
                b4 = b3.split("\n")
                while len(b4) > 1:
                    b5 = b4[0]
                    b3 = "\n".join(b4[1:])
                    b13.put(f"{c_id} {b5}")
                    b4 = b3.split("\n")
            except:
                return
    def fonk3(b12, b13):
        while True:
            b6 = b13.get(True, None)
            b7 = b6.split(" ")
            b8 = b7[0]
            b9 = b7[1]
            b10 = " ".join(b7[2:])
            if b10:
                for c_id in b12:
                    if c_id != b8:
                        b11 = f"{b9} {b8} {b10}\n"
                        b12[c_id].send(b11.encode())
            b13.task_done()
    b12 = {}
    a3 = 0
    b13 = Queue(100)
    threading.Thread(b14 = server_thread, args=(b12, b13)).start()
    b15 = ["Player1", "Player2"]
    while True:
        try:
            client, b16 = b2.accept()
            b17 = b15[a3]
            for c_id in b12:
                b12[c_id].send(f"PlayerJoined {b17}\n".encode())
                client.send(f"PlayerJoined {c_id}\n".encode())
            b12[b17] = client
            client.send(f"MyIDis {b17}\n".encode())
            print(f"Connection received from {b17}")
            threading.Thread(b14 = handle_client, args=(client, b13, b17, b12)).start()
            a3 += 1
        except:
            print("Max players reached")
if b18 = = '__main__':
    fonk1()