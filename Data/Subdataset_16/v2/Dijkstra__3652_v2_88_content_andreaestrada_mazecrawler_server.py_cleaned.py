import socket
import threading
from queue import Queue
import spec
b1 = spec.host
b2 = int(spec.port)
a1 = 2
def fonk1(client_socket, b11, client_id, b9):
    client_socket.setblocking(True)
    b3 = ""
    while True:
        try:
            b3 += client_socket.recv(1024).decode("UTF-8")
            b4 = b3.split("\n")
            while len(b4) > 1:
                b5 = b4[0]
                b3 = "\n".join(b4[1:])
                b11.put(f"{client_id} {b5}")
                b4 = b3.split("\n")
        except Exception as e:
            print(f"Error handling client {client_id}: {e}")
            break
def fonk2(b9, b11):
    while True:
        b5 = b11.get(True, None)
        sender_id, instruction, *b6 = b5.split(" ")
        b6 = " ".join(b6)
        if b6:
            for client_id, client_socket in b9.items():
                if client_id != sender_id:
                    b7 = f"{instruction} {sender_id} {b6}\n"
                    client_socket.send(b7.encode())
        b11.task_done()
def fonk3():
    b8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b8.bind((b1, b2))
    b8.listen(a1)
    print("Server is waiting for players...")
    b9 = {}
    b10 = ["Player1", "Player2"]
    b11 = Queue(100)
    threading.Thread(b12 = server_thread, args=(b9, b11), daemon=True).start()
    while True:
        try:
            client_socket, b13 = b8.accept()
            if len(b9) >= len(b10):
                print("Max players reached. Rejecting new connection.")
                client_socket.send("Max players reached. Try again later.\n".encode())
                client_socket.close()
                continue
            b14 = b10[len(b9)]
            for c_id in b9:
                b9[c_id].send(f"PlayerJoined {b14}\n".encode())
                client_socket.send(f"PlayerJoined {c_id}\n".encode())
            b9[b14] = client_socket
            client_socket.send(f"MyIDis {b14}\n".encode())
            print(f"Connection established with {b14}")
            threading.Thread(b12 = handle_client, args=(client_socket, b11, b14, b9), daemon=True).start()
        except Exception as e:
            print(f"Server error: {e}")
if b15 = = '__main__':
    fonk3()