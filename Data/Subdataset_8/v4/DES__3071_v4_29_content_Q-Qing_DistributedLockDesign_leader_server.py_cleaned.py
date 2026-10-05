from socket import *
import threading
class LeaderServer:
    def __init__(self, port):
        self.port = port
        self.follower_servers = []
        self.clients = []
        self.connections = []
        self.lock_map = []
    def create_new_client_id(self, client_socket):
        client_id = len(self.clients) + 1001
        self.clients.append({'client_id': client_id, 'socket': client_socket})
        return client_id
    def create_new_follower_id(self, follower_socket):
        follower_id = len(self.follower_servers) + 2
        self.follower_servers.append({'follower_id': follower_id, 'socket': follower_socket})
        return follower_id
    def preempt_lock(self, lock_name, client_id):
        if any(lock['name'] == lock_name for lock in self.lock_map):
            return {'result': False}
        self.lock_map.append({'name': lock_name, 'client': client_id})
        self.broadcast_lock_update(lock_name, client_id)
        return {'result': True}
    def broadcast_lock_update(self, lock_name, client_id):
        print('Broadcasting new lock_map')
        for follower in self.follower_servers:
            follower_socket = follower['socket']
            update_message = f"UpdateLockmap:{lock_name}:{client_id}"
            follower_socket.sendall(update_message.encode())
    def release_lock(self, lock_name, client_id):
        for lock in self.lock_map:
            if lock['name'] == lock_name and lock['client'] == client_id:
                self.lock_map.remove(lock)
                self.broadcast_lock_removal(lock_name, client_id)
                return {'result': True}
        return {'result': False}
    def broadcast_lock_removal(self, lock_name, client_id):
        print("Broadcasting removal of lock_map")
        for follower in self.follower_servers:
            follower_socket = follower['socket']
            removal_message = f"RemoveLockmap:{lock_name}:{client_id}"
            follower_socket.sendall(removal_message.encode())
    def respond_to_message(self, client_socket):
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                continue
            if data == 'NewClient':
                client_id = self.create_new_client_id(client_socket)
                client_socket.sendall(f"ClientId:{client_id}".encode())
            elif data == 'NewFollower':
                follower_id = self.create_new_follower_id(client_socket)
                client_socket.sendall(f"FollowerId:{follower_id}".encode())
            else:
                message_parts = data.split(":")
                if message_parts[0] == 'PreemptLock':
                    response = self.preempt_lock(message_parts[1], message_parts[2])
                    msg = f"PreemptLock Success:{message_parts[2]}" if response['result'] else f"PreemptLock Failed:{message_parts[2]}"
                    client_socket.sendall(msg.encode())
                elif message_parts[0] == "ReleaseLock":
                    response = self.release_lock(message_parts[1], message_parts[2])
                    msg = f"ReleaseLock Success:{message_parts[2]}" if response['result'] else f"ReleaseLock Failed:{message_parts[2]}"
                    client_socket.sendall(msg.encode())
                elif message_parts[0] == "CheckLock":
                    if self.lock_map:
                        for lock in self.lock_map:
                            if lock['name'] == message_parts[1]:
                                client_id = lock['client']
                                client_socket.sendall(f"CheckLock:Lock:{client_id}".encode())
                                break
                    else:
                        client_socket.sendall("There are no locks in the server".encode())
    def run_server(self):
        host = '127.0.0.1'
        port = self.port
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server is listening on port {port}")
        while True:
            client_socket, client_addr = server_socket.accept()
            print(f"Connected from {client_addr}")
            self.connections.append(client_socket)
            response_thread = threading.Thread(target=self.respond_to_message, args=(client_socket,))
            response_thread.setDaemon(True)
            response_thread.start()
            print("Active threads:", threading.active_count())
if __name__ == "__main__":
    leader_server = LeaderServer(9000)
    leader_server.run_server()