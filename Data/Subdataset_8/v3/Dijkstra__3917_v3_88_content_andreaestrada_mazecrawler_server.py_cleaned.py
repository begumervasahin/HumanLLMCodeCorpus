import socket
import threading
from queue import Queue
HOST = ""
PORT = 12345
BACKLOG = 2
def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(BACKLOG)
    print("Waiting for players...")
    def handle_client(client, server_channel, client_id, clientele):
        client.setblocking(1)
        message_buffer = ""
        while True:
            try:
                message_buffer += client.recv(1024).decode("UTF-8")
                commands = message_buffer.split("\n")
                while len(commands) > 1:
                    ready_message = commands[0]
                    message_buffer = "\n".join(commands[1:])
                    server_channel.put(f"{client_id} {ready_message}")
                    commands = message_buffer.split("\n")
            except:
                return
    def server_thread(clientele, server_channel):
        while True:
            message = server_channel.get(True, None)
            parts = message.split(" ")
            sender_id = parts[0]
            instruction = parts[1]
            details = " ".join(parts[2:])
            if details:
                for client_id, client_socket in clientele.items():
                    if client_id != sender_id:
                        send_message = f"{instruction} {sender_id} {details}\n"
                        client_socket.send(send_message.encode())
            server_channel.task_done()
    clientele = {}
    player_num = 0
    server_channel = Queue(100)
    threading.Thread(target=server_thread, args=(clientele, server_channel)).start()
    player_names = ["Player1", "Player2"]
    while True:
        try:
            client_socket, client_address = server.accept()
            current_player_id = player_names[player_num]
            for existing_client_id, existing_client_socket in clientele.items():
                existing_client_socket.send(f"PlayerJoined {current_player_id}\n".encode())
                client_socket.send(f"PlayerJoined {existing_client_id}\n".encode())
            clientele[current_player_id] = client_socket
            client_socket.send(f"MyIDis {current_player_id}\n".encode())
            print(f"Connection received from {current_player_id}")
            threading.Thread(target=handle_client, args=(client_socket, server_channel, current_player_id, clientele)).start()
            player_num += 1
        except:
            print("Max players reached")
if __name__ == '__main__':
    run_server()