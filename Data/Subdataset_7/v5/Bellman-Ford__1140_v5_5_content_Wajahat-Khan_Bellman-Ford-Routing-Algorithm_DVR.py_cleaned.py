import sys
import socket
import json
import threading
import time
import os
b1 = sys.argv[1]
b2 = int(sys.argv[2])
b3 = sys.argv[3]
b4 = {}
b5 = {}
b6 = threading.Lock()
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b7 = {}
        self.b8 = []
        self.fonk2(b3)
    def fonk2(self, config_file):
        with open(config_file, "r") as fo:
            b9 = fo.read()
            b10 = b9.split()
            b11 = b10[0]
            a1 = 1
            while a1 < len(b10):
                d[b10[a1]] = [float(0), int(b10[a1 + 2])]
                a1 += 3
            for key, value in d.items():
                self.b7[key] = value[0]
                if key != self.b1:
                    self.b8.append(key)
            b4[self.b1] = self.b7.copy()
def fonk3():
    b12 = "localhost"
    b13 = b2
    b14 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b14.bind((b12, b13))
    while True:
        message, b15 = b14.recvfrom(2048)
        b16 = json.loads(message)
        for key, val in b16.items():
            b17 = key.encode('ascii', 'ignore')
            for b18, v in b16[b17].items():
                b18 = b18.encode('ascii', 'ignore')
                b4[b18] = v
        threading.Thread(b19 = bellman_ford).start()
    b14.close()
def fonk4():
    while True:
        b20 = [value[1][1] for value in d.items()]
        b21 = "localhost"
        b22 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b23 = json.dumps(b4)
        for item in b20:
            if int(item) != b2:
                b22.sendto(b23.encode(), (b21, int(item)))
        time.sleep(5)
        b22.close()
def fonk5():
    b24 = [node for node in b4 if node in b27.b8]
    b25 = set([b17 for node in b4 for b17 in b4[node]])
    for node in b4:
        for router in b25:
            if router not in b4[node]:
                b4[node][router] = float('inf')
    for router in b25:
        for b17 in b24:
            if b4[b1][router] > b4[b17][router] + b4[b1][b17]:
                b26 = b4[b17][router] + b4[b1][b17]
                b4[b1][router] = b26
                if router in b24 and b27.b7[router] <= b26:
                    b4[b1][router] = b27.b7[router]
                    b5[router] = 'direct'
                else:
                    b5[router] = b17
            elif len(b5) != len(b25):
                b5[router] = 'direct'
            elif router in b24 and b27.b7[router] <= b4[b1][router]:
                b4[b1][router] = b27.b7[router]
                b5[router] = 'direct'
    fonk6()
def fonk6():
    with b6:
        os.system("cls")
        print(f"\nI am Router {b1}\n")
        for node in b4[b1]:
            print(f"Least cost path to router {node}: through {b5[node]} with cost {b4[b1][node]:.1f}\n")
b27 = class1(b1, b2, b3)
threading.Thread(b19 = send).start()
threading.Thread(b19 = receive).start()