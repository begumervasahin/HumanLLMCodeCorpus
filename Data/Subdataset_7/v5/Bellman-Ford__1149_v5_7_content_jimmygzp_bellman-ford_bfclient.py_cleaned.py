import sys
import socket
import select
import datetime
import copy
import cPickle as pickle
b1 = True
a1 = 4096
b2 = float("inf")
b3 = {}
b4 = {}
b5 = {}
b6 = {}
b7 = (0, 0)
b8 = time()
b9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b9.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
b9.setblocking(0)
b10 = socket.gethostbyname(socket.gethostname())
if b10[:3] == '127':
    b10 = '127.0.0.1'
def fonk1(b18):
    b9.sendto('DOWN', b18)
def fonk2(b18, weight):
    b3[b18] = float(weight)
    b4[b18] = time()
    b5[b18] = 1
    b6[b7][b18] = [b18, float(weight)]
    b6[b18] = {b18: [b18, 0]}
def fonk3(b18, vector):
    b6[b18] = vector
    b6[b7][b18] = [b18, b6[b18][b7][1]]
    b3[b18] = float(b6[b18][b7][1])
def fonk4():
    global b8
    if b1:
        print("Distance Vector (b7):", b6[b7])
        print("Uplink:", b5)
    for neighbor, vector in b6.items():
        if neighbor is not b7 and b5[neighbor] == 1:
            if b1:
                print("Broadcasting to:", neighbor)
            b11 = copy.deepcopy(b6[b7])
            for dest, b13 in b6[b7].items():
                if b13[0] == neighbor and dest != neighbor:
                    b11[dest][1] = b2
            if b1:
                print("Poisoned message to", neighbor, ":", b11)
            b9.sendto(pickle.dumps(b11), neighbor)
    b8 = time()
def fonk5():
    print(f"{datetime.datetime.now()}, Current Distance Vector is:")
    for dest, b13 in b6[b7].items():
        if dest is not b7:
            print(f"b12 = {dest[0]}:{dest[1]}, Cost={float(b13[1]):.1f}, Link=({b13[0][0]}:{b13[0][1]})")
def fonk6():
    a2 = 0
    for dest, cost in b6[b7].items():
        b13 = cost[0]
        try:
            b6[b7][dest][1] = b6[b7][b13][1] + b6[b13][dest][1]
        except KeyError:
            b6[b7][dest][1] = b2
    for dest, cost in b6[b7].items():
        if dest is not b7:
            try:
                if b6[cost[0]][b7][1] + b6[cost[0]][dest][1] > b6[b7][dest][1]:
                    b6[b7][dest] = [dest, b6[cost[0]][b7][1] + b6[cost[0]][dest][1]]
            except KeyError:
                pass
        b14 = b6[b7][dest][1]
        b15 = b2
        for neighbor, links in b6.items():
            if b5[neighbor] and neighbor != b7:
                try:
                    b16 = b6[neighbor][dest][1]
                except KeyError:
                    b16 = b2
                if neighbor != dest:
                    b17 = b6[b7][neighbor][1]
                else:
                    b17 = b3[neighbor]
                if b17 + b16 < b15:
                    b15 = b17 + b16
                    b13 = neighbor
        if b14 != b15:
            a2 = 1
            b6[b7][dest] = [b13, b15]
    return a2
def fonk7(client_input):
    b18 = client_input
    if b18[0] == 'localhost' or b18[0][:3] == '127':
        b18 = (b10, client_input[1])
    b5[b18] = 0
    b3[b18] = b6[b7][b18][1]
    b6[b7][b18][1] = b2
    try:
        b6[b18][b7][1] = b2
    except KeyError:
        pass
    for dest, b13 in b6[b7].items():
        if b13[1] == b18:
            b6[b7][dest] = [("ALSO DOWN", 0), b2]
    fonk6()
    fonk1(b18)
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk8(client_input):
    b18 = client_input
    if b18[0] == 'localhost' or b18[0][:3] == '127':
        b18 = (b10, client_input[1])
    b5[b18] = 1
    b6[b7][b18] = [b18, b3[b18]]
    b6[b18][b7] = [b7, b3[b18]]
    fonk6()
    for _ in range(5):
        fonk4()
        sleep(0.2)
def fonk9(packet):
    if packet[1][0][:3] == '127':
        b19 = (b10, packet[1][1])
    else:
        b19 = packet[1]
    if packet[0] == 'DOWN':
        b3[b19] = b6[b7][b19][1]
        b6[b7][b19][1] = b2
        try:
            b6[b19][b7][1] = b2
        except:
            pass
        b5[b19] = 0
        fonk6()
        fonk4()
    else:
        a2 = 0
        b20 = pickle.loads(packet[0])
        b4[b19] = time()
        if b19 not in b6.keys():
            fonk3(b19, b20)
            b5[b19] = 1
            for dest, b13 in b6[b19].items():
                if dest not in b6[b7].keys():
                    b6[b7][dest] = [("UNKNOWN", 0), b2]
                    a2 = 1
            b3[b19] = b6[b19][b7][1]
        else:
            b6[b19] = b20
            for dest, b13 in b6[b19].items():
                if dest not in b6[b7].keys():
                    b6[b7][