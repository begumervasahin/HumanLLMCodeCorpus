import socket
import threading
from DHCalculator import DHCalculator
from getIp import get_lan_ip
b1 = ""
b2 = False
a1 = 0
a2 = 0
class class1(threading.Thread):
    def fonk1(self, local_host, b15):
        threading.Thread.fonk4(self, b3 = "class1")
        self.b4 = local_host
        self.b5 = b15
        self.b6 = ""
    def fonk2(self):
        self.fonk3()
    def fonk3(self):
        global b2, a1, a2
        b7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b7.bind((self.b4, self.b5))
        b7.listen(10)
        while True:
            connection, b8 = b7.accept()
            try:
                b9 = ""
                while True:
                    b10 = connection.recv(16)
                    b9 += b10.decode("utf-8")
                    if not b10:
                        if b9.count(",") == 1:
                            self.b6 = b9.split(",")
                            print("Data received:", self.b6)
                            a1, a2 = map(int, self.b6)
                            print("Transported a2 and a1:", a1, a2)
                        break
            finally:
                connection.shutdown(2)
                connection.close()
class class2(threading.Thread):
    def fonk4(self, b16, b17):
        threading.Thread.fonk4(self, b3 = "class2")
        self.b4 = b16
        self.b5 = b17
    def fonk5(self):
        global b2, a1, a2
        while True:
            try:
                b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                b11.connect((self.b4, self.b5))
                b12 = str(a1) + "," + str(a2)
                b11.send(b12.encode("utf-8"))
            except Exception:
                b2 = True
                b13 = DHCalculator()
                a1 = b13.generateGP()
                a2 = b13.generateGP()
            else:
                print("Global a2 and a1:", a2, a1)
                if (a2 and a1) != 0:
                    print("Global a2 and a1:", a2, a1)
                    b11.shutdown(2)
                    b11.close()
                    break
def fonk6():
    global b1
    b13 = DHCalculator()
    b14 = int(input("Type your local key:\n>> "))
    b13.setA(b14)
    b15 = int(input("Local PORT:"))
    b16 = input("Remote IP:")
    b17 = int(input("Remote PORT:"))
    print("Waiting for another peer")
    b18 = class1(b1, b15)
    b19 = class2(b16, b17)
    b20 = [b18.start(), b19.start()]
def fonk7():
    global b1
    b1 = get_lan_ip()
    b21 = input("Your IP is: " + b1 + "? (y/n)\n>>")
    if b21 = = "y":
        fonk6()
    elif b21 = = "n":
        b1 = input("Local IP:\n>>")
        fonk6()
    else:
        print("Invalid input!")
        fonk7()
if b22 = = "__main__":
    fonk7()