import socket
import threading
from queue import Queue
import spec
HOST = spec.host
PORT = int(spec.port)
BACKLOG = 2
def handle_client(client_socket, server_queue, client_id, clients):
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
def broadcast_messages(clients, server_queue):
    while True:
        message = server_queue.get()
        sender_id, instruction, *details = message.split(" ")
        details = " ".join(details)
        if details:
            for client_id, client_socket in clients.items():
                if client_id != sender_id:
                    broadcast_message = f"{instruction} {sender_id} {details}\n"
                    client_socket.send(broadcast_message.encode())
        server_queue.task_done()
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(BACKLOG)
        print("Waiting for players...")
        clients = {}
        player_names = ["Player1", "Player2"]
        server_queue = Queue(maxsize=100)
        threading.Thread(target=broadcast_messages, args=(clients, server_queue), daemon=True).start()
        player_count = 0
        while True:
            try:
                client_socket, _ = server_socket.accept()
                if len(clients) >= len(player_names):
                    print("Max players reached. Rejecting new connection.")
                    client_socket.send("Max players reached. Try again later.\n".encode())
                    client_socket.close()
                    continue
                player_id = player_names[player_count]
                for existing_id in clients:
                    clients[existing_id].send(f"PlayerJoined {player_id}\n".encode())
                    client_socket.send(f"PlayerJoined {existing_id}\n".encode())
                clients[player_id] = client_socket
                client_socket.send(f"MyIDis {player_id}\n".encode())
                print(f"Connection received from {player_id}")
                threading.Thread(target=handle_client, args=(client_socket, server_queue, player_id, clients), daemon=True).start()
                player_count += 1
            except Exception as e:
                print(f"Server error: {e}")
if __name__ == '__main__':
    run_server()