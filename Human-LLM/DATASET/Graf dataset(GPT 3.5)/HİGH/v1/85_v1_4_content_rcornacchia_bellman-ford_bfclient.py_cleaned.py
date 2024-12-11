import sys
import socket
import select
import time
from collections import defaultdict
class class1:
    def fonk1(self, b2, b3, b1 = float('inf')):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
class class2:
    def fonk2(self):
        self.b4 = defaultdict(lambda: float('inf'))
        self.b5 = {}
        self.b6 = {}
        self.b7 = {}
        self.b8 = {}
        self.b9 = {}
        self.b10 = {}
        self.b11 = {}
        self.b12 = {}
def fonk3():
    if len(sys.argv) < 4 or len(sys.argv[3:]) % 3 != 0:
        print("Usage: python script.py <b3> <b13> <neighbor1_ip> <neighbor1_port> <neighbor1_weight> ...")
        return
    b3 = int(sys.argv[1])
    b13 = int(sys.argv[2])
    b14 = True
    b15 = class2()
    def fonk4():
        for neighbor, b1 in b15.b7.items():
            if b1 != float('inf'):
                b16 = f"ROUTE_UPDATE {my_ip} {my_port} {b1} "
                for dest, w in b15.b4.items():
                    b16 += f"{dest.b2} {dest.b3} {w} "
                b16 += "EOT"
                b26.sendto(b16, (neighbor.b2, neighbor.b3))
    def fonk5(b25):
        b16 = f"LINKDOWN {my_ip} {my_port} "
        b26.sendto(b16, (b25.b2, b25.b3))
    def fonk6(b25):
        b16 = f"LINKUP {my_ip} {my_port} "
        b26.sendto(b16, (b25.b2, b25.b3))
    def fonk7():
        b17 = time.strftime("%H:%M:%S", time.localtime(time.time()))
        print(f"{b17}\tDistance vector list is:")
        for dest, w in b15.b4.items():
            print(f"b18 = {dest.b2}:{dest.b3}\tCost={w}\t\tLink:{b15.b5[dest]}")
    def fonk8(broken_node, target_node):
        b16 = f"LINK_DESTROYED {my_ip} {my_port} {broken_node.b2} {broken_node.b3} "
        b26.sendto(b16, (target_node.b2, target_node.b3))
    def fonk9(delay):
        b19 = time.time()
        while b14:
            b17 = time.time()
            b20 = []
            for neighbor, last_seen in b15.b6.items():
                if b17 - last_seen > b13 * 2:
                    b15.b12[neighbor] = b15.b7[neighbor]
                    b20.append(neighbor)
            for inactive_node in b20:
                if inactive_node in b15.b6:
                    b15.b4[inactive_node] = float("inf")
                    del b15.b6[inactive_node]
                for key, b21 in b15.b5.items():
                    if b21 = = inactive_node:
                        if key in b15.b6:
                            b15.b4[key] = b15.b7[key]
                        else:
                            b15.b4[inactive_node] = float("inf")
                            b15.b4[key] = float("inf")
                            b15.b5[key] = "no link exists"
                fonk4()
            if b17 - b19 > b13:
                b19 = time.time()
                fonk4()
            time.sleep(1)
    def fonk10(b22):
        b22 = b22.split()
        if b22[0] == "LINKDOWN" and len(b22) > 2:
            b23 = b22[1]
            b24 = int(b22[2])
            b25 = class1(b23, b24)
            if b25 in b15.b6:
                b15.b4[b25] = float("inf")
                b15.b11[b25] = b15.b4[b25]
            else:
                print("class1 is not a neighbor, can't Linkdown")
            for b25 in b15.b11:
                if b25 in b15.b6:
                    del b15.b6[b25]
                    fonk5(b25)
                    fonk4()
        elif b22[0] == "LINKUP" and len(b22) > 2:
            b25 = class1(b23, b24)
            if b25 not in b15.b6:
                b15.b6[b25] = time.time()
                if b25 in b15.b4:
                    b15.b4[b25] = int(b15.b7[b25])
                    fonk6(b25)
        elif b22[0] == "CLOSE":
            print("class1 shutting down")
            b14 = False
        elif b22[0] == "SHOW_RT":
            fonk7()
        else:
            print(b22[0] + "Command not recognized")
    thread.start_new_thread(run, (2,))
    b26 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b27 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b27.bind((my_ip, my_port))
    b28 = [b27, sys.stdin]
    while b14:
        try:
            inputready, b29, b29 = select.select(b28, [], [])
            for b30 in inputready:
                if b30 = = sys.stdin:
                    b22 = sys.stdin.readline()
                    fonk10(b22)
                else:
                    b31, b29 = b30.recvfrom(1024)
                    b31 = b31.split()
                    if b31[0] == "ROUTE_UPDATE":
                        b32 = b31[1]
                        b33 = int(b31[2])
                        if b31[3] == "inf":
                            b34 = float("inf")
                        else:
                            b34 = int(b31[3])
                        b35 = class1(b32, b33)
                        if b35 not in b15.b12:
                            if b35 in b15.b6:
                                b15.b6[b35] = time.time()
                                if b35 in b15.b7:
                                    if b15.b7[b35] > b34:
                                        b15.b7[b35] = b34
                                        b15.b4[b35] = b34
                                else:
                                    print("don't have neighbor in neighbor distance for some reason")
                            else:
                                b15.b6[b35] = time.time()
                                b15.b7[b35] = b34
                                b15.b4[b35] = b34
                                b15.b5[b35] = b35
                                b15.b9 = b35
                            b36 = False
                            a1 = 4
                            b37 = {}
                            while not b36:
                                if b31[a1+2] == "inf":
                                    b1 = float("inf")
                                else:
                                    b1 = int(b31[a1+2])
                                b37[class1(b31[a1], int(b31[a1+1]))] = b1
                                a1 += 3
