import socket
import threading
import sys
HOST = '127.0.0.1'
PORT = 50007
MAX_CONNECTIONS = 2
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((HOST, PORT))
except socket.error as e:
    print(f"Failed to bind the server socket: {e}")
    sys.exit()
print("Server is running on port", PORT)
print("Waiting for connections...")
server_socket.listen(MAX_CONNECTIONS)
clients = []
while len(clients) < MAX_CONNECTIONS:
    try:
        conn, addr = server_socket.accept()
        print(f"Client connected: IP {addr[0]}, Port {addr[1]}")
        clients.append((conn, addr))
    except Exception as e:
        print("An error occurred while accepting connections:", e)
        break
class ClientHandler(threading.Thread):
    def __init__(self, client_from, client_to):
        super().__init__()
        self.client_from = client_from[0]
        self.client_to = client_to[0]
    def run(self):
        while True:
            try:
                msg = self.client_from.recv(1024)
                if not msg:
                    print("Client disconnected.")
                    break
                self.client_to.send(msg)
            except ConnectionResetError:
                print("A client disconnected unexpectedly.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break
handler1 = ClientHandler(clients[0], clients[1])
handler2 = ClientHandler(clients[1], clients[0])
handler1.start()
handler2.start()
handler1.join()
handler2.join()
print("Both clients have disconnected. Server shutting down.")
server_socket.close()