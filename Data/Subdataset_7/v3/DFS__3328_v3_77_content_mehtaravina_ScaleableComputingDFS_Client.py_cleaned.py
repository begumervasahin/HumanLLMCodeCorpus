import socket
import pickle
b1 = 'localhost'
a1 = 5001
a2 = 5003
a3 = 6002
a4 = 5009
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2.bind((b1, a1))
b2.listen(5)
b3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b3.bind((b1, a2))
b3.listen(5)
b4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b4.bind((b1, a3))
b4.listen(5)
b5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b5.bind((b1, a4))
b5.listen(5)
print("Server started. Listening for connections...")
b6 = {'user1': 'password1', 'user2': 'password2'}
b7 = {}
def fonk1(conn):
    b8 = conn.recv(1024).decode()
    conn.sendall(b8.encode())
    b9 = conn.recv(1024).decode()
    conn.sendall(b9.encode())
    b10 = conn.recv(1024).decode()
    conn.sendall(b10.encode())
    print(b9, b10, b8)
    if b9 in b6:
        if b6[b9] == b10:
            conn.sendall('true'.encode())
            return b9
        else:
            conn.sendall('false'.encode())
            return None
    else:
        b6[b9] = b10
        conn.sendall('exists'.encode())
        return None
def fonk2(conn):
    b11 = conn.recv(1024).decode()
    conn.sendall(b11.encode())
    if b11 = = '1':
        b12 = conn.recv(1024).decode()
        conn.sendall(b12.encode())
        b13 = conn.recv(1024).decode()
        conn.sendall(b13.encode())
        b7[b12] = b13
        b14 = pickle.dumps(list(b7.keys()))
        conn.sendall(b14)
    elif b11 = = '2':
        b15 = pickle.dumps(list(b7.keys()))
        conn.sendall(b15)
        b16 = conn.recv(1024).decode()
        if b16 in b7:
            conn.sendall(b7[b16].encode())
        else:
            conn.sendall("File not found.".encode())
def fonk3(conn):
    b16 = conn.recv(1024).decode()
    if b16 in b7:
        conn.sendall('locked'.encode())
    else:
        conn.sendall('unlocked'.encode())
def fonk4(conn):
    while True:
        b17 = conn.recv(1024).decode()
        if not b17:
            break
        if b17 = = '1':
            fonk2(conn)
        elif b17 = = '2':
            fonk3(conn)
def fonk5():
    while True:
        conn, b18 = b5.accept()
        print('Connected by', b18)
        b9 = fonk1(conn)
        if b9:
            print('User authenticated:', b9)
            fonk4(conn)
        else:
            print('Authentication failed. Closing connection.')
        conn.close()
if b19 = = '__main__':
    fonk5()