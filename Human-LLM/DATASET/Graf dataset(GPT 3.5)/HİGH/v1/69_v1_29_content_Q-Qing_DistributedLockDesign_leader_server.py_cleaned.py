from socket import *
import threading
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = []
    def fonk2(self, b8):
        b6 = len(self.b3) + 1001
        self.b3.append({'b6': b6, 'socket': b8})
        return b6
    def fonk3(self, b8):
        b7 = len(self.b2) + 2
        self.b2.append({'b7': b7, 'socket': b8})
        return b7
    def fonk4(self, lock_name, b6):
        if any(lock['name'] == lock_name for lock in self.b5):
            return {'result': False}
        self.b5.append({'name': lock_name, 'client': b6})
        self.fonk5(lock_name, b6)
        return {'result': True}
    def fonk5(self, lock_name, b6):
        print('Broadcasting new b5')
        for follower in self.b2:
            b8 = follower['socket']
            b9 = f"UpdateLockmap:{lock_name}:{b6}"
            b8.sendall(b9.encode())
    def fonk6(self, lock_name, b6):
        for lock in self.b5:
            if lock['name'] == lock_name and lock['client'] == b6:
                self.b5.remove(lock)
                self.fonk7(lock_name, b6)
                return {'result': True}
        return {'result': False}
    def fonk7(self, lock_name, b6):
        print("Broadcasting to remove b5")
        for follower in self.b2:
            b8 = follower['socket']
            b9 = f"RemoveLockmap:{lock_name}:{b6}"
            b8.sendall(b9.encode())
    def fonk8(self, b8):
        while True:
            b10 = b8.recv(1024).decode('utf-8')
            if not b10:
                continue
            if b10 = = 'NewClient':
                b6 = self.fonk2(b8)
                b8.sendall(f"ClientId:{b6}".encode())
            elif b10 = = 'NewFollower':
                b7 = self.fonk3(b8)
                b8.sendall(f"FollowerId:{b7}".encode())
            else:
                b11 = b10.split(":")
                if b11[0] == 'PreemptLock':
                    b12 = self.fonk4(b11[1], b11[2])
                    if b12['result']:
                        b8.sendall(f"PreemptLock Success:{b11[2]}".encode())
                    else:
                        b8.sendall(f"PreemptLock Failed:{b11[2]}".encode())
                elif b11[0] == "ReleaseLock":
                    b12 = self.fonk6(b11[1], b11[2])
                    if b12['result']:
                        b8.sendall(f"ReleaseLock Success:{b11[2]}".encode())
                    else:
                        b8.sendall(f"ReleaseLock Failed:{b11[2]}".encode())
                elif b11[0] == "CheckLock":
                    if self.b5:
                        for lock in self.b5:
                            if lock['name'] == b11[1]:
                                b6 = lock['client']
                                b8.sendall(f"CheckLock:Lock:{b6}".encode())
                                break
                    else:
                        b8.sendall("There are no locks in the server".encode())
    def fonk9(self):
        b13 = '127.0.0.1'
        b1 = self.b1
        b14 = socket(AF_INET, SOCK_STREAM)
        b14.bind((b13, b1))
        b14.listen(5)
        print(f"Server listening on b1 {b1}")
        while True:
            conn_socket, b15 = b14.accept()
            print(f"Connected from {b15}")
            self.b4.append(conn_socket)
            b16 = threading.Thread(target=self._response_msg, args=(conn_socket,))
            b16.setDaemon(True)
            b16.start()
            print("Active threads:", threading.active_count())
if b17 = = "__main__":
    b18 = class1(9000)
    b18.fonk9()