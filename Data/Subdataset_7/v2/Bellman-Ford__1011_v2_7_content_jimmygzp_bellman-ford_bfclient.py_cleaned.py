import sys
import socket
import select
import pickle
from time import time, sleep
import datetime
import copy
a1 = 1
b1 = a1
a2 = 4096
b2 = {}
b3 = {}
b4 = {}
b5 = {}
b6 = (0, 0)
b7 = time()
b8 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b8.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b8.setblocking(0)
b9 = socket.gethostbyname(socket.gethostname())
if b9[:3] == '127':
    b9 = '127.0.0.1'
b10 = float("inf")
def fonk1(b18):
    b8.sendto('DOWN', b18)
def fonk2(b18, weight):
    b2[b18] = float(weight)
    b3[b18] = time()
    b4[b18] = 1
    b5[b6][b18] = [b18, float(weight)]
    b5[b18] = {}
    b5[b18][b18] = [b18, 0]
def fonk3(b18, vector):
    b5[b18] = vector
    b5[b6][b18] = [b18, b5[b18][b6][1]]
    b2[b18] = float(b5[b18][b6][1])
def fonk4():
    global b7
    if a1:
        print("Distance Vector (b6):", b5[b6])
        print("Uplink:", b4)
    for neighbor, vector in b5.items():
        if neighbor is not b6:
            if b4[neighbor] == 1:
                if a1:
                    print("Broadcasting to:", neighbor)
                b11 = copy.deepcopy(b5[b6])
                for dest, b13 in b5[b6].items():
                    if b13[0] == neighbor and dest != neighbor:
                        b11[dest][1] = b10
                if a1:
                    print("Poisoned message to", neighbor, ":", b11)
                b8.sendto(pickle.dumps(b11), neighbor)
    b7 = time()
def fonk5():
    print(str(datetime.datetime.now()) + ", Current Distance Vector is:")
    for dest, b13 in b5[b6].items():
        if dest is not b6:
            print(f"b12 = {dest[0]}:{dest[1]}, Cost={float(b13[1]):.1f}, Link=({b13[0][0]}:{b13[0][1]})")
def fonk6():
    a3 = 0
    for dest, cost in b5[b6].items():
        b13 = cost[0]
        try:
            b5[b6][dest][1] = b5[b6][b13][1] + b5[b13][dest][1]
        except:
            b5[b6][dest][1] = b10
    b13 = ("UNREACHABLE", 0)
    for dest, cost in b5[b6].items():
        if dest is not b6:
            try:
                if b5[cost[0]][b6][1] + b5[cost[0]][dest][1] > b5[b6][dest][1]:
                    b5[b6][dest] = [dest, b5[cost[0]][b6][1] + b5[cost[0]][dest][1]]
            except:
                pass
        b14 = b5[b6][dest][1]
        b15 = b10
        for neighbor, links in b5.items():
            if b4[neighbor] and neighbor != b6:
                try:
                    b16 = b5[neighbor][dest][1]
                except:
                    b16 = b10
                if neighbor != dest:
                    b17 = b5[b6][neighbor][1]
                else:
                    b17 = b2[neighbor]
                if b17 + b16 < b15:
                    b15 = b17 + b16
                    b13 = neighbor
        if b14 != b15:
            a3 = 1
            b5[b6][dest] = [b13, b15]
    return a3
def fonk7(client_input):
    b18 = client_input
    if b18[0] == 'localhost' or b18[0][:3] == '127':
        b18 = (b9, client_input[1])
    b4[b18] = 0
    b2[b18] = b5[b6][b18][1]
    b5[b6][b18][1] = b10
    try:
        b5[b18][b6][1] = b10
    except:
        pass
    for dest, b13 in b5[b6].items():
        if b13[1] == b18:
            b5[b6][dest] = [("ALSO DOWN", 0), b10]
    fonk6()
    fonk1(b18)
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk8(client_input):
    b18 = client_input
    if b18[0] == 'localhost' or b18[0][:3] == '127':
        b18 = (b9, client_input[1])
    b4[b18] = 1
    b5[b6][b18] = [b18, b2[b18]]
    b5[b18][b6] = [b6, b2[b18]]
    fonk6()
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk9(packet):
    if packet[1][0][:3] == '127':
        b19 = (b9, packet[1][1])
    else:
        b19 = packet[1]
    if packet[0] == 'DOWN':
        b2[b19] = b5[b6][b19][1]
        b5[b6][b19][1] = b10
        try:
            b5[b19][b6][1] = b10
        except:
            pass
        b4[b19] = 0
        fonk6()
        fonk4()
    else:
        a3 = 0
        b20 = pickle.loads(packet[0])
        b3[b19] = time()
        if b19 not in b5.keys():
            fonk3(b19, b20)
            b4[b19] = 1
            for dest, b13 in b5[b19].items():
                if dest not in b5[b6].keys():
                    b5[b6][dest] = [("UNKNOWN", 0), b10]
                    a3 = 1
            b2[b19] = b5[b19][b6][1]
            b5[b6][b19] = [b19, b2[b19]]
            if fonk6():
                a3 = 1
        else:
            b5[b19] = b20
            for