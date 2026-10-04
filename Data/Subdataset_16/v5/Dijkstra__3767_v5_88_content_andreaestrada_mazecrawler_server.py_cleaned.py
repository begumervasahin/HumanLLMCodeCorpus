import socket
import threading
from queue import Queue
import spec
b1 = spec.host
b2 = int(spec.port)
a1 = 2
def fonk1(client_socket, b10, client_id, b8):
    client_socket.setblocking(True)
    b3 = ""
    while True:
        try:
            b3 += client_socket.recv(1024).decode("UTF-8")
            b4 = b3.split("\n")
            while len(b4) > 1:
                b5 = b4[0]
                b3 = "\n".join(b4[1:])
                b10.put(f"{client_id} {b5}")
                b4 = b3.split("\n")
        except Exception as e:
            print(f"Error handling client {client_id}: {e}")
            break
def fonk2(b8, b10):
    while True:
        b5 = b10.get()
        sender_id, instruction, *b6 = b5.split(" ")
        b6 = " ".join(b6)
        if b6:
            for client_id, client_socket in b8.items():
                if client_id != sender_id:
                    b7 = f"{instruction} {sender_id} {b6}\n"
                    client_socket.send(b7.encode())
        b10.task_done()
def fonk3():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((b1, b2))
        server_socket.listen(a1)
        print("Waiting for players...")
        b8 = {}
        b9 = ["Player1", "Player2"]
        b10 = Queue(maxsize=100)
        threading.Thread(b11 = broadcast_messages, args=(b8, b10), daemon=True).start()
        a2 = 0
        while True:
            try:
                client_socket, b12 = server_socket.accept()
                if len(b8) >= len(b9):
                    print("Max players reached. Rejecting new connection.")
                    client_socket.send("Max players reached. Try again later.\n".encode())
                    client_socket.close()
                    continue
                b13 = b9[a2]
                for existing_id in b8:
                    b8[existing_id].send(f"PlayerJoined {b13}\n".encode())
                    client_socket.send(f"PlayerJoined {existing_id}\n".encode())
                b8[b13] = client_socket
                client_socket.send(f"MyIDis {b13}\n".encode())
                print(f"Connection received from {b13}")
                threading.Thread(b11 = handle_client, args=(client_socket, b10, b13, b8), daemon=True).start()
                a2 += 1
            except Exception as e:
                print(f"Server error: {e}")
if b14 = = '__main__':
    fonk3()