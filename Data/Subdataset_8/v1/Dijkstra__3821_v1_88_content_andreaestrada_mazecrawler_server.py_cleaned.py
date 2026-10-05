import socket
import threading
from queue import Queue
HOST = ""
PORT = 12345
def run_server():
    BACKLOG = 2
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(BACKLOG)
    print("Waiting for players...")
    def handle_client(client, server_channel, c_id, clientele):
        client.setblocking(1)
        msg = ""
        while True:
            try:
                msg += client.recv(10).decode("UTF-8")
                command = msg.split("\n")
                while len(command) > 1:
                    ready_msg = command[0]
                    msg = "\n".join(command[1:])
                    server_channel.put(str(c_id) + " " + ready_msg)
                    command = msg.split("\n")
            except:
                return
    def server_thread(clientele, server_channel):
        while True:
            msg = server_channel.get(True, None)
            msg_list = msg.split(" ")
            sender_id = msg_list[0]
            instruction = msg_list[1]
            details = " ".join(msg_list[2:])
            if details != "":
                for c_id in clientele:
                    if c_id != sender_id:
                        send_msg = instruction + " " + sender_id + " " + details + "\n"
                        clientele[c_id].send(send_msg.encode())
            server_channel.task_done()
    clientele = dict()
    player_num = 0
    server_channel = Queue(100)
    threading.Thread(target=server_thread, args=(clientele, server_channel)).start()
    names = ["Player1", "Player2"]
    while True:
        try:
            client, address = server.accept()
            my_id = names[player_num]
            for c_id in clientele:
                clientele[c_id].send(("PlayerJoined %s\n" % my_id).encode())
                client.send(("PlayerJoined %s\n" % c_id).encode())
            clientele[my_id] = client
            client.send(("MyIDis %s \n" % my_id).encode())
            print("Connection received from %s" % my_id)
            threading.Thread(target=handle_client, args=(client, server_channel, my_id, clientele)).start()
            player_num += 1
        except:
            print("Max players reached")
if __name__ == '__main__':
    run_server()