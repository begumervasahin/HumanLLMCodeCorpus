import socket
sendsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sendsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sendsock.bind(("localhost", 8179))
sendsock.sendto(b"Hello", ('localhost', 8181))
data, addr = sendsock.recvfrom(4096)
print(data.decode())
sendsock.close()