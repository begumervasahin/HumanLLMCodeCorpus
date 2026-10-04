import socket
import threading
from queue import Queue
import spec
HOST = spec.host
PORT = int(spec.port)
BACKLOG = 2
def handle_client(client_socket, server_queue, client_id, all_clients):
    client_socket.setblocking(True)
    buffer = ""
    while True:
        try:
            buffer += client_socket.recv(1024).decode("UTF-8")
            messages = buffer.split("\n")
            while len(messages) > 1:
                message = messages[0]
                buffer = "\n".join(messages[1:])
                server_queue.put(f"{client_id} {message}")
                messages = buffer.split("\n")
        except Exception as e:
            print(f"Error handling client {client_id}: {e}")
            break
def server_thread(all_clients, server_queue):
    while True:
        message = server_queue.get(True, None)
        sender_id, instruction, *details = message.split(" ")
        details = " ".join(details)
        if details:
            for client_id, client_socket in all_clients.items():
                if client_id != sender_id:
                    broadcast_message = f"{instruction} {sender_id} {details}\n"
                    client_socket.send(broadcast_message.encode())
        server_queue.task_done()
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(BACKLOG)
    print("Server is waiting for players...")
    all_clients = {}
    player_names = ["Player1", "Player2"]
    server_queue = Queue(100)
    threading.Thread(target=server_thread, args=(all_clients, server_queue), daemon=True).start()
    while True:
        try:
            client_socket, _ = server_socket.accept()
            if len(all_clients) >= len(player_names):
                print("Max players reached. Rejecting new connection.")
                client_socket.send("Max players reached. Try again later.\n".encode())
                client_socket.close()
                continue
            player_id = player_names[len(all_clients)]
            for c_id in all_clients:
                all_clients[c_id].send(f"PlayerJoined {player_id}\n".encode())
                client_socket.send(f"PlayerJoined {c_id}\n".encode())
            all_clients[player_id] = client_socket
            client_socket.send(f"MyIDis {player_id}\n".encode())
            print(f"Connection established with {player_id}")
            threading.Thread(target=handle_client, args=(client_socket, server_queue, player_id, all_clients), daemon=True).start()
        except Exception as e:
            print(f"Server error: {e}")
if __name__ == '__main__':
    run_server()