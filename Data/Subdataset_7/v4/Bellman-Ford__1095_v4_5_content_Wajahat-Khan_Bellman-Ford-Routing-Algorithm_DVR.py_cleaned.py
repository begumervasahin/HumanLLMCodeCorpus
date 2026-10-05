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
b6 = {}
b7 = threading.Lock()
b8 = {}
b9 = {}
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b10 = {}
        self.b11 = []
        self.fonk2(b3)
    def fonk2(self, config_file):
        with open(config_file, "r+") as fo:
            b12 = fo.read()
            b13 = b12.split()
            b14 = b13[0]
            a1 = 1
            while a1 < len(b13):
                b4[b13[a1]] = [float(0), int(b13[a1 + 2])]
                a1 += 3
            for key, value in b4.items():
                self.b10[key] = value[0]
                if key != self.b1:
                    self.b11.append(key)
            b5[self.b1] = self.b10.copy()
def fonk3():
    b15 = "localhost"
    b16 = b2
    b17 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b17.bind((b15, b16))
    while True:
        message, b18 = b17.recvfrom(2048)
        b19 = json.loads(message)
        for key, val in b19.items():
            b20 = key.encode('ascii', 'ignore')
            for b21, v in b19[b20].items():
                b21 = b21.encode('ascii', 'ignore')
                b8[b21] = v
        threading.Thread(b22 = bellman_ford).start()
    b17.close()
def fonk4():
    while True:
        b23 = [value[1][1] for value in b4.items()]
        b24 = "localhost"
        b25 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b26 = json.dumps(b5)
        for item in b23:
            if int(item) != b2:
                b25.sendto(b26.encode(), (b24, int(item)))
        time.sleep(5)
        b25.close()
def fonk5():
    b27 = [node for node in b8 if node in b30.b11]
    b28 = set([neighbour for node in b8 for neighbour in b8[node]])
    for node in b8:
        for router in b28:
            if router not in b8[node]:
                b8[node][router] = float('inf')
    for router in b28:
        for neighbour in b27:
            if b8[b1][router] > b8[neighbour][router] + b8[b1][neighbour]:
                b29 = b8[neighbour][router] + b8[b1][neighbour]
                b8[b1][router] = b29
                if router in b27 and b30.b10[router] <= b29:
                    b8[b1][router] = b30.b10[router]
                    b6[router] = 'direct'
                else:
                    b6[router] = neighbour
            elif len(b6) != len(b28):
                b6[router] = 'direct'
            elif router in b27 and b30.b10[router] <= b8[b1][router]:
                b8[b1][router] = b30.b10[router]
                b6[router] = 'direct'
    b5[b1] = b8[b1]
    fonk6()
def fonk6():
    with b7:
        os.system("cls")
        print("\nI am Router " + b1 + '\n')
        for node in b5[b1]:
            print("Least cost path to router " + node + ": through " + b6[node] + " with cost " + str("{0:.1f}".format(b5[b1][node]) + "\n"))
b30 = class1(b1, b2, b3)
threading.Thread(b22 = sender).start()
threading.Thread(b22 = b17).start()