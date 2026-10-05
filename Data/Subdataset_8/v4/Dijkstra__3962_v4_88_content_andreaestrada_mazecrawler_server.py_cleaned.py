import socket
import threading
from queue import Queue
import spec
HOST = spec.host
PORT = int(spec.port)
BACKLOG = 2
def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(BACKLOG)
    print("Waiting for players...")
    def handle_client(client, server_channel, client_id, clientele):
        client.setblocking(1)
        msg_buffer = ""
        while True:
            try:
                msg_buffer += client.recv(1024).decode("UTF-8")
                commands = msg_buffer.split("\n")
                while len(commands) > 1:
                    ready_msg = commands[0]
                    msg_buffer = "\n".join(commands[1:])
                    server_channel.put(f"{client_id} {ready_msg}")
                    commands = msg_buffer.split("\n")
            except:
                return
    def server_thread(clientele, server_channel):
        while True:
            msg = server_channel.get(True, None)
            msg_parts = msg.split(" ")
            sender_id = msg_parts[0]
            instruction = msg_parts[1]
            details = " ".join(msg_parts[2:])
            if details:
                for c_id in clientele:
                    if c_id != sender_id:
                        send_msg = f"{instruction} {sender_id} {details}\n"
                        clientele[c_id].send(send_msg.encode())
            server_channel.task_done()
    clientele = {}
    player_num = 0
    server_channel = Queue(100)
    threading.Thread(target=server_thread, args=(clientele, server_channel)).start()
    player_names = ["Player1", "Player2"]
    while True:
        try:
            client_socket, address = server.accept()
            my_id = player_names[player_num]
            for existing_client_id in clientele:
                clientele[existing_client_id].send(f"PlayerJoined {my_id}\n".encode())
                client_socket.send(f"PlayerJoined {existing_client_id}\n".encode())
            clientele[my_id] = client_socket
            client_socket.send(f"MyIDis {my_id}\n".encode())
            print(f"Connection received from {my_id}")
            threading.Thread(target=handle_client, args=(client_socket, server_channel, my_id, clientele)).start()
            player_num += 1
        except:
            print("Max players reached")
if __name__ == '__main__':
    run_server()