'''
Author: keqin
Time: 2019-06-11
Leader_server:
There is only one leader_server in a program.
The leader_server can connect with b3 and b2.
The leader_server assign b6 and follower_server_id to b3 and b2
when a new connection is created.
It also needs to response to preempt/release request of b3 or b2.
And it response to check request of b3.
When b5 changes, it broadcast new b5 to all b2 to ensure
the b10 consistency of system.
'''
from socket import *
import threading
from threading import Thread
class class1():
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = []
    def fonk2(self,b8):
        '''
        Creating b6 for b3 connected with leader_server.
        The first client'b14 id which connected with leader_server is 1001 and the second is 1002,
        and so on.
        :param b8:
        :return: b6
        '''
        b6 = len(self.b3) + 1001
        self.b3.append({'b6':b6,'socket':b8})
        return b6
    def fonk3(self,b8):
        '''
        Creating b7 for b2. The first id is 2 and the second is 3, and so on.
        The first client'b14 id which connected with follower_server_2 is 2001 and the second is 2002, and so on.
        :param b8:
        :return: b7
        '''
        b7 = len(self.b2) +2
        self.b2.append({'b7':b7,'socket':b8})
        return b7
    def fonk4(self,lock_name,b6):
        if self.b5 != None:
            for lock in self.b5:
                if lock['name'] == lock_name:
                    return {'result':False}
        self.b5.append({'name': lock_name, 'client': b6})
        self.fonk5(lock_name,b6)
        return {'result':True}
    def fonk5(self,lock_name,b6):
        print('broadcast new b5')
        for follower in self.b2:
            b8 = follower['socket']
            b9 = "UpdateLockmap:%b14:%d"%(lock_name,int(b6))
            b8.sendall(b9.encode())
    def fonk6(self,lock_name,b6):
        if self.b5 != None:
            for lock in self.b5:
                if lock['name'] == lock_name and lock['client'] == b6:
                    self.b5.remove({"name":lock_name,"client":b6})
                    self.fonk7(lock_name,b6)
                    return {'result':True}
        return {'result':False}
    def fonk7(self,lock_name,b6):
        print("broadcast to remove b5")
        for follower in self.b2:
            b8 = follower['socket']
            b9 = "RemoveLockmap:%b14:%d"%(lock_name,int(b6))
            b8.sendall(b9.encode())
    def fonk8(self,b8):
        while True:
            b10 = b8.recv(1024).decode('utf-8')
            if not b10:
                continue
            if b10 = = 'NewClient':
                b6 = self.fonk2(b8)
                b8.sendall(("ClientId:%d"%(b6)).encode())
                continue
            if b10 = = 'NewFollower':
                b7 = self.fonk3(b8)
                b8.sendall(("FollowerId:%d"%(b7)).encode())
                continue
            b11 = b10.split(":")
            if b11[0] == 'PreemptLock':
                b12 = self.fonk4(b11[1], b11[2])
                if b12['result']:
                    b8.sendall(("PreemptLock Success:%d"%(int(b11[2]))).encode())
                else:
                    b8.sendall(("PreemptLock Failed:%d"%(int(b11[2]))).encode())
                continue
            if b11[0] == "ReleaseLock":
                b12 = self.fonk6(b11[1],b11[2])
                if b12['result']:
                    b8.sendall(("ReleaseLock Success:%d"%(int(b11[2]))).encode())
                else:
                    b8.sendall(("ReleaseLock Failed:%d"%(int(b11[2]))).encode())
                continue
            if b11[0] == "CheckLock":
                if self.b5:
                    for lock in self.b5:
                        if lock['name'] == b11[1]:
                            b6 = lock['client']
                            break
                    b8.sendall(("CheckLock:Lock:%d"%(int(b6))).encode())
                else:
                    b8.sendall(("there is no locks in server").encode())
    def fonk9(self):
        b13 = '127.0.0.1'
        b1 = self.b1
        b14 = socket(AF_INET, SOCK_STREAM)
        b14.bind((b13, b1))
        b14.listen(5)
        print(b14)
        while True:
            conn_socket, b15 = b14.accept()
            print("Connect from", b15)
            self.b4.append(conn_socket)
            b16 = threading.Thread(target=self._responce_msg, args=(conn_socket,))
            b16.setDaemon(True)
            b16.start()
            print("active threads:")
            print(threading.active_count())
b17 = class1(9000)
b17.fonk9()