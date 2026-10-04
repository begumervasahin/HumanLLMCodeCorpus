import socket
def fonk1(p,e,n):
    a1 = 1
    while e!=0:
        a1*= p % n
        e-=1
    return a1%n
b1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
b2 = input(str("please enter b2 name of server:"))
a2 = 1024
b1.connect((b2,a2))
print("Connected to  server")
print("")
b3 = int(input("Enter client private key"))
b4 = str(fonk1(17,b3,23))
print("")
b5 = b1.recv(1024)
b5 = b5.decode()
print("server:",b5)
b4 = b4.encode()
b1.send(b4)
print("b4 has been send")
print("")
b5 = int(b5)
print("Secrete key shared",fonk1(b5,b3,23))