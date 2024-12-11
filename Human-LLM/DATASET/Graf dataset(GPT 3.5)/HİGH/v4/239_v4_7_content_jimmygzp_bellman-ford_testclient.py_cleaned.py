import socket
b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b1.bind(("", 8179))
b2 = ('localhost', 8181)
b1.sendto(b"Hello", b2)
response_data, b3 = b1.recvfrom(4096)
print(response_data.decode())
b1.close()