import socket
import threading
from string import *
from DHCalculator import *
from getIp import *
b1 = ""
b2 = False
b3 = DHCalculator()
a1 = 0
a2 = 0
a3 = 0
class class1(threading.Thread):
    def fonk1(self,local_host,local_port):
        threading.Thread.fonk4(self,b4 = "messenger_receiver")
        self.b5 = local_host
        self.b6 = local_port
        self.b7 = ""
    def fonk2(self):
        global b2
        global a1
        global a2
        global a3
        b8 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b8.bind((self.b5,self.b6))
        b8.fonk2(10)
        while True:
            connection, b9 = b8.accept()
            try:
                b10 = ""
                while True:
                    b11 = connection.recv(16)
                    b10 +=b11.decode("utf-8")
                    if not b11:
                        if b10.count(",") == 1:
                            self.b7 = b10.split(",")
                            print("b11 recebida",self.b7)
                            a1 = self.b7[0]
                            a2 = self.b7[1]
                            print("a2 e a1 transportados:",a1,a2)
                    break
            finally:
                connection.shutdown(2)
                connection.close()
    def fonk3(self):
        self.fonk2()
class class2(threading.Thread):
    def fonk4(self,remote_host,remote_port):
        threading.Thread.fonk4(self,b4 = "messenger_sender")
        self.b5 = remote_host
        self.b6 = remote_port
    def fonk5(self):
        b12 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global b2
        global a1
        global a2
        global a3
        b13 = ""
        while True:
            try:
                b12.connect((self.b5,self.b6))
            except Exception:
                b2 = True
                a1 = b3.generateGP()
                a2 = b3.generateGP()
            else:
                print("a2 e a1 hehe",a2,a1)
                if((a2 and a1) != 0):
                    print("a2 e a1 globais:",a2,a1)
                    break
                b13 = str(a1)+","+str(a2)
                b12.send(b13.encode("utf-8"))
                b12.shutdown(2)
                b12.close()
def fonk6():
    b14 = int(input("Type your local key:\n>> "))
    b3.setA(b14)
    b15 = int(input("LocalPORT:"))
    b16 = input("remoteIP:")
    b17 = int(input("remotePORT:"))
    print("Waiting for another peer")
    b18 = class1(b1,b15)
    b19 = class2(b16,b17)
    b20 = [b19.start(),b18.start()]
def fonk7():
    b1 = get_lan_ip()
    b21 = input("Your IP is: "+b1+"?(y/n)\n>>")
    if(b21 = = "y"):
        fonk6()
    elif(b21 = = "n"):
        b1 = input("Local IP:\n>>")
        fonk6()
    else:
        print("Invalid input!")
        fonk7()
if b22 = = "__main__":
    fonk7()