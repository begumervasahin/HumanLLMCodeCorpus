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
        print("Usage: python script.py <b3> <b14> <neighbor1_ip> <neighbor1_port> <neighbor1_weight> ...")
        return
    b13 = int(sys.argv[1])
    b14 = int(sys.argv[2])
    b15 = True
    b16 = class2()
    def fonk4():
        for neighbor, b1 in b16.b7.items():
            if b1 != float('inf'):
                b17 = f"ROUTE_UPDATE {my_ip} {b13} {b1} "
                for dest, w in b16.b4.items():
                    b17 += f"{dest.b2} {dest.b3} {w} "
                b17 += "EOT"
                b27.sendto(b17, (neighbor.b2, neighbor.b3))
    def fonk5(b26):
        b17 = f"LINKDOWN {my_ip} {b13} "
        b27.sendto(b17, (b26.b2, b26.b3))
    def fonk6(b26):
        b17 = f"LINKUP {my_ip} {b13} "
        b27.sendto(b17, (b26.b2, b26.b3))
    def fonk7():
        b18 = time.strftime("%H:%M:%S", time.localtime(time.time()))
        print(f"{b18}\tDistance vector list is:")
        for dest, w in b16.b4.items():
            print(f"b19 = {dest.b2}:{dest.b3}\tCost={w}\t\tLink:{b16.b5[dest]}")
    def fonk8(broken_node, target_node):
        b17 = f"LINK_DESTROYED {my_ip} {b13} {broken_node.b2} {broken_node.b3} "
        b27.sendto(b17, (target_node.b2, target_node.b3))
    def fonk9(delay):
        b20 = time.time()
        while b15:
            b18 = time.time()
            b21 = []
            for neighbor, last_seen in b16.b6.items():
                if b18 - last_seen > b14 * 2:
                    b16.b12[neighbor] = b16.b7[neighbor]
                    b21.append(neighbor)
            for inactive_node in b21:
                if inactive_node in b16.b6:
                    b16.b4[inactive_node] = float("inf")
                    del b16.b6[inactive_node]
                for key, b22 in b16.b5.items():
                    if b22 = = inactive_node:
                        if key in b16.b6:
                            b16.b4[key] = b16.b7[key]
                        else:
                            b16.b4[inactive_node] = float("inf")
                            b16.b4[key] = float("inf")
                            b16.b5[key] = "no link exists"
                fonk4()
            if b18 - b20 > b14:
                b20 = time.time()
                fonk4()
            time.sleep(1)
    def fonk10(b23):
        b23 = b23.split()
        if b23[0] == "LINKDOWN" and len(b23) > 2:
            b24 = b23[1]
            b25 = int(b23[2])
            b26 = class1(b24, b25)
            if b26 in b16.b6:
                b16.b4[b26] = float("inf")
                b16.b11[b26] = b16.b4[b26]
            else:
                print("class1 is not a neighbor, can't Linkdown")
            for b26 in b16.b11:
                if b26 in b16.b6:
                    del b16.b6[b26]
                    fonk5(b26)
                    fonk4()
        elif b23[0] == "LINKUP" and len(b23) > 2:
            b26 = class1(b24, b25)
            if b26 not in b16.b6:
                b16.b6[b26] = time.time()
                if b26 in b16.b4:
                    b16.b4[b26] = int(b16.b7[b26])
                    fonk6(b26)
        elif b23[0] == "CLOSE":
            print("class1 shutting down")
            b15 = False
        elif b23[0] == "SHOW_RT":
            fonk7()
        else:
            print(b23[0] + "Command not recognized")
    thread.start_new_thread(run, (2,))
    b27 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b28 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b28.bind((my_ip, b13))
    b29 = [b28, sys.stdin]
    while b15:
        try:
            inputready, b30, b30 = select.select(b29, [], [])
            for b31 in inputready:
                if b31 = = sys.stdin:
                    b23 = sys.stdin.readline()
                    fonk10(b23)
                else:
                    b32, b30 = b31.recvfrom(1024)
                    b32 = b32.split()
                    if b32[0] == "ROUTE_UPDATE":
                        b33 = b32[1]
                        b34 = int(b32[2])
                        if b32[3] == "inf":
                            b35 = float("inf")
                        else:
                            b35 = int(b32[3])
                        b36 = class1(b33, b34)
                        if b36 not in b16.b12:
                            if b36 in b16.b6:
                                b16.b6[b36] = time.time()
                                if b36 in b16.b7:
                                    if b16.b7[b36] > b35:
                                        b16.b7[b36] = b35
                                        b16.b4[b36] = b35
                                else:
                                    print("don't have neighbor in neighbor distance for some reason")
                            else:
                                b16.b6[b36] = time.time()
                                b16.b7[b36] = b35
                                b16.b4[b36] = b35
                                b16.b5[b36] = b36
                                b16.b9 = b36
                            b37 = False
                            a1 = 4
                            b38 = {}
                            while not b37:
                                if b32[a1+2] == "inf":
                                    b1 = float("inf")
                                else:
                                    b1 = int(b32[a1+2])
                                b38[class1(b32[a1], int(b32[a1+1]))] = b1
                                a1 += 3
                                if b32[a1] == "EOT":
                                    b37 = True
                            for b26,