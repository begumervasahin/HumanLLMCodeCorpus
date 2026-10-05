import sys
import socket
import select
import datetime
import copy
import cPickle as pickle
a1 = 1
a2 = 4096
b1 = float("inf")
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
def fonk1(b17):
    b8.sendto('DOWN', b17)
def fonk2(b17, weight):
    b2[b17] = float(weight)
    b3[b17] = time()
    b4[b17] = 1
    b5[b6][b17] = [b17, float(weight)]
    b5[b17] = {b17: [b17, 0]}
def fonk3(b17, vector):
    b5[b17] = vector
    b5[b6][b17] = [b17, b5[b17][b6][1]]
    b2[b17] = float(b5[b17][b6][1])
def fonk4():
    global b7
    if a1:
        print("Distance Vector (b6):", b5[b6])
        print("Uplink:", b4)
    for neighbor, vector in b5.items():
        if neighbor is not b6 and b4[neighbor] == 1:
            if a1:
                print("Broadcasting to:", neighbor)
            b10 = copy.deepcopy(b5[b6])
            for dest, b12 in b5[b6].items():
                if b12[0] == neighbor and dest != neighbor:
                    b10[dest][1] = b1
            if a1:
                print("Poisoned message to", neighbor, ":", b10)
            b8.sendto(pickle.dumps(b10), neighbor)
    b7 = time()
def fonk5():
    print(f"{datetime.datetime.now()}, Current Distance Vector is:")
    for dest, b12 in b5[b6].items():
        if dest is not b6:
            print(f"b11 = {dest[0]}:{dest[1]}, Cost={float(b12[1]):.1f}, Link=({b12[0][0]}:{b12[0][1]})")
def fonk6():
    a3 = 0
    for dest, cost in b5[b6].items():
        b12 = cost[0]
        try:
            b5[b6][dest][1] = b5[b6][b12][1] + b5[b12][dest][1]
        except KeyError:
            b5[b6][dest][1] = b1
    for dest, cost in b5[b6].items():
        if dest is not b6:
            try:
                if b5[cost[0]][b6][1] + b5[cost[0]][dest][1] > b5[b6][dest][1]:
                    b5[b6][dest] = [dest, b5[cost[0]][b6][1] + b5[cost[0]][dest][1]]
            except KeyError:
                pass
        b13 = b5[b6][dest][1]
        b14 = b1
        for neighbor, links in b5.items():
            if b4[neighbor] and neighbor != b6:
                try:
                    b15 = b5[neighbor][dest][1]
                except KeyError:
                    b15 = b1
                if neighbor != dest:
                    b16 = b5[b6][neighbor][1]
                else:
                    b16 = b2[neighbor]
                if b16 + b15 < b14:
                    b14 = b16 + b15
                    b12 = neighbor
        if b13 != b14:
            a3 = 1
            b5[b6][dest] = [b12, b14]
    return a3
def fonk7(client_input):
    b17 = client_input
    if b17[0] == 'localhost' or b17[0][:3] == '127':
        b17 = (b9, client_input[1])
    b4[b17] = 0
    b2[b17] = b5[b6][b17][1]
    b5[b6][b17][1] = b1
    try:
        b5[b17][b6][1] = b1
    except KeyError:
        pass
    for dest, b12 in b5[b6].items():
        if b12[1] == b17:
            b5[b6][dest] = [("ALSO DOWN", 0), b1]
    fonk6()
    fonk1(b17)
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk8(client_input):
    b17 = client_input
    if b17[0] == 'localhost' or b17[0][:3] == '127':
        b17 = (b9, client_input[1])
    b4[b17] = 1
    b5[b6][b17] = [b17, b2[b17]]
    b5[b17][b6] = [b6, b2[b17]]
    fonk6()
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk9(packet):
    if packet[1][0][:3] == '127':
        b18 = (b9, packet[1][1])
    else:
        b18 = packet[1]
    if packet[0] == 'DOWN':
        b2[b18] = b5[b6][b18][1]
        b5[b6][b18][1] = b1
        try:
            b5[b18][b6][1] = b1
        except:
            pass
        b4[b18] = 0
        fonk6()
        fonk4()
    else:
        a3 = 0
        b19 = pickle.loads(packet[0])
        b3[b18] = time()
        if b18 not in b5.keys():
            fonk3(b18, b19)
            b4[b18] = 1
            for dest, b12 in b5[b18].items():
                if dest not in b5[b6].keys():
                    b5[b6][dest] = [("UNKNOWN", 0), b1]
                    a3 = 1
            b2[b18] = b5[b18][b6][