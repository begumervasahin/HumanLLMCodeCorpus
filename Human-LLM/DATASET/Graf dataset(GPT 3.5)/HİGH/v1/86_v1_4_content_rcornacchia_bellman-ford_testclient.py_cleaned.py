import socket
b1 = socket.gethostbyname(socket.gethostname())
a1 = 5005
b2 = "Hello, World!"
print("UDP target IP:", b1)
print("UDP target port:", a1)
print("message:", b2)
b3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b3.sendto(bytes(b2, 'utf-8'), (b1, a1))