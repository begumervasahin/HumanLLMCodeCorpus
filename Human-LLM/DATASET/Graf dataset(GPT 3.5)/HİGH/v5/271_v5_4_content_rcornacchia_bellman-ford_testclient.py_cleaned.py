import socket
b1 = socket.gethostbyname(socket.gethostname())
a1 = 5005
b2 = "Hello, World!"
print(f"UDP target IP: {b1}")
print(f"UDP target port: {a1}")
print(f"Message: {b2}")
b3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b4 = b2.encode()
b3.sendto(b4, (b1, a1))