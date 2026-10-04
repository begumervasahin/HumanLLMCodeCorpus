from collections import defaultdict
import socket
import time
def fonk1(b8, a2):
    b1 = defaultdict(dict)
    for node in b8:
        for target in b8:
            b1[node][target] = float('Inf') if node != target else 0
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
            fonk2()
            a1 = 60000
            with socket.socket() as s:
                b2 = "127.0.0.1"
                s.bind((b2, a1))
                s.listen(5)
                print('Server listening...')
                time.sleep(1)
                conn, b4 = s.accept()
                with conn:
                    print(f"Connected by {b4}")
                    b5 = ""
                    for v in b8:
                        b5 += f"{v} {b1[u][v]}\n"
                    b6 = f"{u} {b5}"
                    conn.sendall(b6.encode('utf-8'))
    for u in b8:
        for v in b8[u]:
            assert b1[v] <= b1[u] + b8[u][v]
    return b1
def fonk4(b8):
    a2 = 0
    b1 = fonk3(b8, a2)
    print("Distances from a2:")
    for node in b1:
        print(f"Node {node}: {b1[node]}")
if b7 = = '__main__':
    b8 = defaultdict(dict)
    with open('test') as f:
        b9 = f.readlines()
        for i in range(1, int(b9[0]) + 1):
            b10 = b9[i].split()
            for k in range(1, len(b10), 2):
                b8[i][int(b10[k])] = int(b10[k + 1])
    fonk4(b8)