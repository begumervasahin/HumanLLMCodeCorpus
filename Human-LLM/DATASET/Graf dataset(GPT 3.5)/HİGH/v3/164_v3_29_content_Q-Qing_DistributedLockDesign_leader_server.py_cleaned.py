from socket import *
import threading
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = []
    def fonk2(self, client_socket):
        b6 = len(self.b3) + 1001
        self.b3.append({'b6': b6, 'socket': client_socket})
        return b6
    def fonk3(self, follower_socket):
        b7 = len(self.b2) + 2
        self.b2.append({'b7': b7, 'socket': follower_socket})
        return b7
    def fonk4(self, lock_name, b6):
        if any(lock['name'] == lock_name for lock in self.b5):
            return {'result': False}
        self.b5.append({'name': lock_name, 'client': b6})
        self.fonk5(lock_name, b6)
        return {'result': True}
    def fonk5(self, lock_name, b6):
        print('Broadcasting new b5')
        b8 = f"UpdateLockmap:{lock_name}:{b6}"
        for follower in self.b2:
            follower['socket'].sendall(b8.encode())
    def fonk6(self, lock_name, b6):
        for lock in self.b5:
            if lock['name'] == lock_name and lock['client'] == b6:
                self.b5.remove(lock)
                self.fonk7(lock_name, b6)
                return {'result': True}
        return {'result': False}
    def fonk7(self, lock_name, b6):
        print("Broadcasting removal of b5")
        b9 = f"RemoveLockmap:{lock_name}:{b6}"
        for follower in self.b2:
            follower['socket'].sendall(b9.encode())
    def fonk8(self, client_socket):
        while True:
            b10 = client_socket.recv(1024).decode('utf-8')
            if not b10:
                continue
            if b10 = = 'NewClient':
                b6 = self.fonk2(client_socket)
                client_socket.sendall(f"ClientId:{b6}".encode())
            elif b10 = = 'NewFollower':
                b7 = self.fonk3(client_socket)
                client_socket.sendall(f"FollowerId:{b7}".encode())
            else:
                b11 = b10.split(":")
                if b11[0] == 'PreemptLock':
                    b12 = self.fonk4(b11[1], b11[2])
                    b13 = f"PreemptLock Success:{b11[2]}" if b12['result'] else f"PreemptLock Failed:{b11[2]}"
                    client_socket.sendall(b13.encode())
                elif b11[0] == "ReleaseLock":
                    b12 = self.fonk6(b11[1], b11[2])
                    b13 = f"ReleaseLock Success:{b11[2]}" if b12['result'] else f"ReleaseLock Failed:{b11[2]}"
                    client_socket.sendall(b13.encode())
                elif b11[0] == "CheckLock":
                    if self.b5:
                        for lock in self.b5:
                            if lock['name'] == b11[1]:
                                b6 = lock['client']
                                client_socket.sendall(f"CheckLock:Lock:{b6}".encode())
                                break
                    else:
                        client_socket.sendall("There are no locks in the server".encode())
    def fonk9(self):
        b14 = '127.0.0.1'
        b1 = self.b1
        b15 = socket(AF_INET, SOCK_STREAM)
        b15.bind((b14, b1))
        b15.listen(5)
        print(f"Server is listening on b1 {b1}")
        while True:
            client_socket, b16 = b15.accept()
            print(f"Connected from {b16}")
            self.b4.append(client_socket)
            b17 = threading.Thread(target=self.respond_to_message, args=(client_socket,))
            b17.setDaemon(True)
            b17.start()
            print("Active threads:", threading.active_count())
if b18 = = "__main__":
    b19 = class1(9000)
    b19.fonk9()