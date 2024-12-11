import socket
b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b1.bind(("", 8179))
b1.sendto(b"Hello", ('localhost', 8181))
data, b2 = b1.recvfrom(4096)
print(data.decode())
b1.close()