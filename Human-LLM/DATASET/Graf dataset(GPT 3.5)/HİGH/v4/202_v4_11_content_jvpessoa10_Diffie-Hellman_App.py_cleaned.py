import socket
import threading
from DHCalculator import DHCalculator
from getIp import get_lan_ip
b1 = ""
b2 = False
a1 = 0
a2 = 0
a3 = 0
class class1(threading.Thread):
    def fonk1(self, local_host, b14):
        threading.Thread.fonk4(self, b3 = "messenger_receiver")
        self.b4 = local_host
        self.b5 = b14
        self.b6 = ""
    def fonk2(self):
        global b2, a1, a2
        b7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b7.bind((self.b4, self.b5))
        b7.fonk2(10)
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
                            a1 = self.b6[0]
                            a2 = self.b6[1]
                            print("Transported a2 and a1:", a1, a2)
                        break
            finally:
                connection.shutdown(2)
                connection.close()
    def fonk3(self):
        self.fonk2()
class class2(threading.Thread):
    def fonk4(self, b15, b16):
        threading.Thread.fonk4(self, b3 = "messenger_sender")
        self.b4 = b15
        self.b5 = b16
    def fonk5(self):
        b11 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        global b2, a1, a2
        while True:
            try:
                b11.connect((self.b4, self.b5))
            except Exception:
                b2 = True
                a1 = calculator.generateGP()
                a2 = calculator.generateGP()
            else:
                print("Global a2 and a1:", a2, a1)
                if (a2 and a1) != 0:
                    print("Global a2 and a1:", a2, a1)
                    break
                b12 = str(a1) + "," + str(a2)
                b11.send(b12.encode("utf-8"))
                b11.shutdown(2)
                b11.close()
def fonk6():
    global b1
    b13 = int(input("Type your local key:\n>> "))
    calculator.setA(b13)
    b14 = int(input("Local PORT:"))
    b15 = input("Remote IP:")
    b16 = int(input("Remote PORT:"))
    print("Waiting for another peer")
    b17 = class1(b1, b14)
    b18 = class2(b15, b16)
    b19 = [b18.start(), b17.start()]
def fonk7():
    global b1
    b1 = get_lan_ip()
    b20 = input("Your IP is: " + b1 + "? (y/n)\n>>")
    if b20 = = "y":
        fonk6()
    elif b20 = = "n":
        b1 = input("Local IP:\n>>")
        fonk6()
    else:
        print("Invalid input!")
        fonk7()
if b21 = = "__main__":
    fonk7()