from collections import defaultdict
import socket
import time
def fonk1(b5, a2):
    b1 = {b8: float('Inf') for b8 in b5}
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
def fonk3(b5, a2):
    b1 = fonk1(b5, a2)
    for _ in range(len(b5) - 1):
        for u in b5:
            for v in b5[u]:
                b4 = b5[u][v]
                if b1[u] != float('Inf') and b1[u] + b4 < b1[v]:
                    b1[v] = b1[u] + b4
            fonk2()
    for u in b5:
        for v in b5[u]:
            b4 = b5[u][v]
            if b1[u] != float('Inf') and b1[u] + b4 < b1[v]:
                print("Graph contains a negative b4 cycle")
                return
    return b1
def fonk4(b5):
    a2 = 0
    b1 = fonk3(b5, a2)
    print("Distances from a2:")
    for b8 in b1:
        print(f"Node {b8}: {b1[b8]}")
def fonk5(filename):
    b5 = defaultdict(dict)
    with open(filename) as f:
        b6 = f.readlines()
        for i in range(1, int(b6[0]) + 1):
            b7 = b6[i].split()
            b8 = int(b7[0])
            for k in range(1, len(b7), 2):
                b5[b8][int(b7[k])] = int(b7[k + 1])
    return b5
if b9 = = '__main__':
    b5 = fonk5('test')
    fonk4(b5)