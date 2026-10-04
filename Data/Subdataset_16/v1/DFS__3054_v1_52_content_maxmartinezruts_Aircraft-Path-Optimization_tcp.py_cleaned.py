import socket
def fonk1():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def fonk2(b4, ip, port):
    b4.connect((ip, port))
    print('Connected to {} on port {}'.format(ip, port))
def fonk3(b4, message):
    b4.sendall(message.encode())
def fonk4(b4, buffer_size):
    b1 = b4.recv(buffer_size)
    return b1.decode()
def fonk5():
    b2 = '52.43.121.77'
    a1 = 2329
    a2 = 1024
    b3 = "Hello, World!"
    b4 = fonk1()
    fonk2(b4, b2, a1)
    fonk3(b4, b3)
    b1 = fonk4(b4, a2)
    b4.close()
    print("Received b1:", b1)
if b5 = = "__main__":
    fonk5()