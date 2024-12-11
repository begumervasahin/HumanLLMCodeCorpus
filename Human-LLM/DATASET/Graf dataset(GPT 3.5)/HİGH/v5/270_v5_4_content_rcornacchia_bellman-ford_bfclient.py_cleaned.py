import sys
import socket
import select
import thread
import time
from collections import namedtuple
b1 = namedtuple('b1', ['ip', 'port'])
b2 = socket.gethostbyname(socket.gethostname())
b3 = int(sys.argv[1])
b4 = int(sys.argv[2])
b5 = {}
b6 = {}
b7 = {}
b8 = {}
b9 = {}
b10 = {}
b11 = {}
b12 = {}
b13 = {}
b14 = time.time()
if len(sys.argv[3:]) % 3 != 0:
    print("Incorrect usage. Neighbors should be listed as: ip address, port, weight")
    exit()
a1 = 3
while a1 / 3 <= len(sys.argv[3:]) / 3:
    b15 = sys.argv[a1]
    b16 = int(sys.argv[a1 + 1])
    b17 = int(sys.argv[a1 + 2])
    b18 = b1(b15, b16)
    b5[b18] = int(b17)
    b8[b18] = int(b17)
    b6[b18] = b18
    b10[b18] = b18
    b7[b18] = time.time()
    a1 += 3
b9 = b8
def fonk1():
    for b18 in b7:
        b19 = f"ROUTE_UPDATE {b2} {b3} {b8.get(b18, float('inf'))} "
        for v in b5:
            b19 += f"{v.ip} {v.port} {b5[v]} "
        b19 += "EOT"
        b23.sendto(b19, (b18.ip, b18.port))
        b14 = time.time()
def fonk2(b32):
    print("Sending LINKDOWN")
    b19 = f"LINKDOWN {b2} {b3} "
    b23.sendto(b19, (b32.ip, b32.port))
def fonk3(b32):
    print("Sending LINKUP")
    b19 = f"LINKUP {b2} {b3} "
    b23.sendto(b19, (b32.ip, b32.port))
def fonk4():
    b20 = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print(f"{b20}\tDistance vector list is: ")
    for b32 in b5:
        print(f"b21 = {b32.ip}:{b32.port}\tCost={b5[b32]}\t\tLink:{b6[b32]}")
def fonk5(broken_node, target_node):
    print("LINK DESTROYED")
    b19 = f"LINK_DESTROYED {b2} {b3} {broken_node.ip} {broken_node.port} "
    b23.sendto(b19, (target_node.ip, target_node.port))
def fonk6(delay):
    b14 = time.time()
    while b33:
        b20 = time.time()
        b22 = []
        for b18 in b7:
            if b20 - b7[b18] > b4 * 2:
                print("Removing deactivated b18")
                b13[b18] = b8.get(b18, float('inf'))
                b22.append(b18)
        for inactive_node in b22:
            if inactive_node in b7:
                b5[inactive_node] = float("inf")
                del b7[inactive_node]
            for key in b6:
                if b6[key] == inactive_node:
                    if key in b7:
                        b5[key] = b8.get(key, float('inf'))
                    else:
                        b5[inactive_node] = float("inf")
                        b5[key] = float("inf")
                        b6[key] = "no link exists"
            fonk1()
        if b20 - b14 > b4:
            b14 = time.time()
            fonk1()
        time.sleep(1)
thread.start_new_thread(run, ("thread1", 2,))
b23 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b24 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b24.bind((b2, b3))
b25 = [b24, sys.stdin]
b26 = [sys.stdin]
time.sleep(1)
while b33:
    try:
        inputready, outputready, b27 = select.select(b25, [], [])
        for b28 in inputready:
            if b28 = = sys.stdin:
                b29 = sys.stdin.readline()
                b29 = b29.split()
                if b29[0] == "LINKDOWN" and len(b29) > 2:
                    b30 = b29[1]
                    b31 = int(b29[2])
                    b32 = b1(b30, b31)
                    if b32 in b7:
                        b5[b32] = float("inf")
                        b12[b32] = b5[b32]
                    else:
                        print("b1 is not a b18, can't Linkdown")
                    for b32 in b12:
                        if b32 in b7:
                            del b7[b32]
                            fonk2(b32)
                            fonk1()
                elif b29[0] == "LINKUP" and len(b29) > 2:
                    b32 = b1(b30, b31)
                    if b32 not in b7:
                        b7[b32] = time.time()
                        if b32 in b5:
                            b5[b32] = int(b8[b32])
                            fonk3(b32)
                elif b29[0] == "CLOSE":
                    print("b1 shutting down")
                    b33 = False
                elif b29[0] == "SHOW_RT":
                    fonk4()
                else:
                    print(f"{b29[0]} Command