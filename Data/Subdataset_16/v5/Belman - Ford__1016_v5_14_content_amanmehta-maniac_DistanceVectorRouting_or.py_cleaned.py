from collections import defaultdict
import socket
import time
def fonk1(b8, a2):
    b1 = {b12: float('Inf') for b12 in b8}
    b1[a2] = 0
    return b1
def fonk2():
    print("Relax called")
    with socket.socket() as s:
        b2 = "127.0.0.1"
        a1 = 60000
        s.connect((b2, a1))
        b3 = s.recv(1024)
        print(b3.decode('utf-8'))
def fonk3(b8, a2):
    b1 = fonk1(b8, a2)
    for _ in range(len(b8) - 1):
        for u in b8:
            for v in b8[u]:
                b4 = b8[u][v]
                if b1[u] != float('Inf') and b1[u] + b4 < b1[v]:
                    b1[v] = b1[u] + b4
            fonk2()
            with socket.socket() as s:
                b2 = "127.0.0.1"
                a1 = 60000
                s.bind((b2, a1))
                s.listen(5)
                print('Server listening...')
                time.sleep(1)
                conn, b5 = s.accept()
                with conn:
                    print(f"Connected by {b5}")
                    b6 = "".join(f"{v} {b1[v]}\n" for v in b8)
                    b7 = f"{u} {b6}"
                    conn.sendall(b7.encode('utf-8'))
    for u in b8:
        for v in b8[u]:
            b4 = b8[u][v]
            if b1[u] != float('Inf') and b1[u] + b4 < b1[v]:
                print("Graph contains a negative b4 cycle")
                return
    return b1
def fonk4(b8):
    a2 = 0
    b1 = fonk3(b8, a2)
    print("Distances from a2:")
    for b12 in b1:
        print(f"Node {b12}: {b1[b12]}")
def fonk5(filename):
    b8 = defaultdict(dict)
    with open(filename) as f:
        b9 = f.readlines()
        b10 = int(b9[0])
        for i in range(1, b10 + 1):
            b11 = b9[i].split()
            b12 = int(b11[0])
            for k in range(1, len(b11), 2):
                b8[b12][int(b11[k])] = int(b11[k + 1])
    return b8
if b13 = = '__main__':
    b8 = fonk5('test')
    fonk4(b8)