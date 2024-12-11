import socket
def fonk1():
    b1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return b1
def fonk2(b1):
    b1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
def fonk3(b1, host, port):
    b1.bind((host, port))
def fonk4(b1, message, b4):
    b1.sendto(message.encode(), b4)
def fonk5(b1, buffer_size):
    b5, b2 = b1.recvfrom(buffer_size)
    return b5.decode()
def fonk6(b1):
    b1.close()
def fonk7():
    b3 = fonk1()
    fonk2(b3)
    fonk3(b3, "", 8179)
    b4 = ('localhost', 8181)
    fonk4(b3, "Hello", b4)
    b5 = fonk5(b3, 4096)
    print(b5)
    fonk6(b3)
if b6 = = "__main__":
    fonk7()