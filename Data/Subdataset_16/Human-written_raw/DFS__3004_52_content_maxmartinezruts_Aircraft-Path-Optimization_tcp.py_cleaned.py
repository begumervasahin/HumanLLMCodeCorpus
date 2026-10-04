import socket
b1 = '52.43.121.77'
a1 = 2329
a2 = 1024
b2 = "Hello, World!"
b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b3.connect((b1, a1))
print('connected')
b3.send(b2.encode())
b4 = b3.recv(a2)
b3.close()
print("received b4:", b4)