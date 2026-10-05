from socket import *
import threading
class LeaderServer:
    def __init__(self, port):
        self.port = port
        self.follower_servers = []
        self.clients = []
        self.connections = []
        self.lock_map = []
    def _new_client(self, c_socket):
        client_id = len(self.clients) + 1001
        self.clients.append({'client_id': client_id, 'socket': c_socket})
        return client_id
    def _new_follower(self, c_socket):
        follower_id = len(self.follower_servers) + 2
        self.follower_servers.append({'follower_id': follower_id, 'socket': c_socket})
        return follower_id
    def _preempt_lock(self, lock_name, client_id):
        if any(lock['name'] == lock_name for lock in self.lock_map):
            return {'result': False}
        self.lock_map.append({'name': lock_name, 'client': client_id})
        self._update_map(lock_name, client_id)
        return {'result': True}
    def _update_map(self, lock_name, client_id):
        print('Broadcasting new lock_map')
        for follower in self.follower_servers:
            c_socket = follower['socket']
            send_data = f"UpdateLockmap:{lock_name}:{client_id}"
            c_socket.sendall(send_data.encode())
    def _release_lock(self, lock_name, client_id):
        for lock in self.lock_map:
            if lock['name'] == lock_name and lock['client'] == client_id:
                self.lock_map.remove(lock)
                self._remove_map(lock_name, client_id)
                return {'result': True}
        return {'result': False}
    def _remove_map(self, lock_name, client_id):
        print("Broadcasting to remove lock_map")
        for follower in self.follower_servers:
            c_socket = follower['socket']
            send_data = f"RemoveLockmap:{lock_name}:{client_id}"
            c_socket.sendall(send_data.encode())
    def _response_msg(self, c_socket):
        while True:
            data = c_socket.recv(1024).decode('utf-8')
            if not data:
                continue
            if data == 'NewClient':
                client_id = self._new_client(c_socket)
                c_socket.sendall(f"ClientId:{client_id}".encode())
            elif data == 'NewFollower':
                follower_id = self._new_follower(c_socket)
                c_socket.sendall(f"FollowerId:{follower_id}".encode())
            else:
                msg = data.split(":")
                if msg[0] == 'PreemptLock':
                    res = self._preempt_lock(msg[1], msg[2])
                    if res['result']:
                        c_socket.sendall(f"PreemptLock Success:{msg[2]}".encode())
                    else:
                        c_socket.sendall(f"PreemptLock Failed:{msg[2]}".encode())
                elif msg[0] == "ReleaseLock":
                    res = self._release_lock(msg[1], msg[2])
                    if res['result']:
                        c_socket.sendall(f"ReleaseLock Success:{msg[2]}".encode())
                    else:
                        c_socket.sendall(f"ReleaseLock Failed:{msg[2]}".encode())
                elif msg[0] == "CheckLock":
                    if self.lock_map:
                        for lock in self.lock_map:
                            if lock['name'] == msg[1]:
                                client_id = lock['client']
                                c_socket.sendall(f"CheckLock:Lock:{client_id}".encode())
                                break
                    else:
                        c_socket.sendall("There are no locks in the server".encode())
    def run(self):
        host = '127.0.0.1'
        port = self.port
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        print(f"Server listening on port {port}")
        while True:
            conn_socket, addr = s.accept()
            print(f"Connected from {addr}")
            self.connections.append(conn_socket)
            leader_server_thread = threading.Thread(target=self._response_msg, args=(conn_socket,))
            leader_server_thread.setDaemon(True)
            leader_server_thread.start()
            print("Active threads:", threading.active_count())
if __name__ == "__main__":
    l_server = LeaderServer(9000)
    l_server.run()