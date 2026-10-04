import socket
def fonk1():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def fonk2(sock, ip, port):
    sock.connect((ip, port))
    print(f'Connected to {ip} on port {port}')
def fonk3(sock, message):
    sock.sendall(message.encode())
def fonk4(sock, buffer_size):
    b1 = sock.recv(buffer_size)
    return b1.decode()
def fonk5():
    b2 = '52.43.121.77'
    a1 = 2329
    a2 = 1024
    b3 = "Hello, World!"
    try:
        with fonk1() as sock:
            fonk2(sock, b2, a1)
            fonk3(sock, b3)
            b1 = fonk4(sock, a2)
            print("Received b1:", b1)
    except Exception as e:
        print(f"An error occurred: {e}")
if b4 = = "__main__":
    fonk5()