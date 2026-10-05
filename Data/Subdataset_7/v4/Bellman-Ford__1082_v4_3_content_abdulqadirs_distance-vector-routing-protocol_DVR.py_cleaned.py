import sys
import time
import socket
import pickle
import threading
b1 = time.clock()
b2 = {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}}
b3 = {}
b4 = {}
def fonk1(b22):
    while True:
        fonk2()
        time.sleep(3)
        if time.clock() - b1 < 20:
            fonk3(b22)
        fonk4()
        fonk5()
def fonk2():
    for node in b2:
        b3[node], b4[node] = float('inf'), None
    b3[router_id] = 0
def fonk3(b22):
    for b16 in b2:
        b2[b16] = b22[b16]
        for neighbor in b22[b16]:
            b2[b16][neighbor] = b22[b16][neighbor]
            b2[neighbor][b16] = b22[b16][neighbor]
def fonk4():
    for _ in range(len(b2) - 1):
        for u in b2:
            for v in b2[u]:
                if b3[v] >= b3[u] + b2[u][v]:
                    b3[v], b4[v] = b3[u] + b2[u][v], u
def fonk5():
    for node, dist in b3.items():
        print("Distance to {}: {}".format(node, dist))
    print()
def fonk6(port_numbers, b22):
    b5 = "127.0.0.1"
    while True:
        try:
            b6 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except:
            print("Socket creation failed")
        a1 = 0
        while a1 < len(port_numbers):
            time.sleep(4)
            b7 = {router_id: b2[router_id]}
            b6.sendto(pickle.dumps(b7), (b5, int(port_numbers[a1])))
            a1 += 1
def fonk7(port_number):
    b8 = "127.0.0.1"
    b9 = port_number
    b10 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b10.bind((b8, b9))
    print("Server setup")
    b11 = {neighbor: time.clock() for neighbor in b24}
    while True:
        b10.settimeout(20)
        try:
            b7, b12 = b10.recvfrom(2048)
            b7 = pickle.loads(b7)
        except:
            print("Message not received from all neighbors")
            for neighbor in b24:
                b2[router_id][neighbor] = float('inf')
            continue
        if 'updated' in b7:
            fonk8(b7)
        else:
            fonk9(b7, b11)
def fonk8(b7):
    b13 = 'updated'
    b14 = b7[b13]
    b15 = list(b14.keys())[0]
    b22[router_id][b15] = b14[b15]
def fonk9(b7, b11):
    b16 = list(b7.keys())[0]
    b17 = b7[b16]
    for neighbor, value in b17.items():
        b2[neighbor][b16] = value
        b2[b16][neighbor] = value
    b11[b16] = time.clock()
    fonk10(b11)
def fonk10(b11):
    for neighbor in b24:
        if time.clock() - b11[neighbor] > 15:
            b18 = neighbor
            b2[router_id][b18] = float('inf')
            b2[b18][router_id] = float('inf')
if b19 = = '__main__':
    _, router_id, port_no, b20 = sys.argv
    print("I am Router " + router_id)
    print("My b25 number is " + port_no)
    with open(b20) as f:
        b21 = int(f.readline().strip())
        print("Number of routers connected: " + str(b21))
        b22 = {router_id: {}}
        b23 = []
        global b24
        b24 = []
        for _ in range(b21):
            neighbor, distance_val, b25 = f.readline().strip().split()
            b24.append(neighbor)
            b23.append(b25)
            b22[router_id][neighbor] = float(distance_val)
        print(b24)
    threading.Thread(b26 = server, args=(int(port_no),)).start()
    time.sleep(4)
    threading.Thread(b26 = client, args=(b23, b22)).start()
    threading.Thread(b26 = bellman_ford, args=(b22,)).start()
    while True:
        pass