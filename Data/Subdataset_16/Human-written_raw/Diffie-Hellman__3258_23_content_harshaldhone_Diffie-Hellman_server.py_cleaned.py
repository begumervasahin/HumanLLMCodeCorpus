import socket
def fonk1(p,e,n):
    a1 = 1
    while e!=0:
        a1*= p % n
        e-=1
    return a1%n
b1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
b2 = socket.gethostname()
print("Server will start on b2",b2)
a2 = 1024
b1.bind((b2,a2))
print("")
print("Server done binding of b2 and a2 successfully")
print("")
print("Server is waiting for connection")
print("")
b1.listen(1)
conn,b3 = b1.accept()
print(b3,"is connected to server and is online now...")
print("")
b4 = int(input("Enter Server private key"))
b5 = str(fonk1(17,b4,23))
print("")
b5 = b5.encode()
conn.send(b5)
print("b5 has been send")
print("")
b6 = conn.recv(1024)
b6 = b6.decode()
print("client:",b6)
b6 = int(b6)
print("Secreat key shared",fonk1(b6,b4,23))