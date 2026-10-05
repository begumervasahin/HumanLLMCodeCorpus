import sys
import time
import socket
import pickle
import threading
b1 = time.clock()
b2 = {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}}
b3 = {}
b4 = {}
def fonk1(b21):
    while True:
        fonk2()
        time.sleep(3)
        if time.clock() - b1 < 20:
            fonk3(b21)
        fonk4()
        fonk5()
def fonk2():
    for node in b2:
        b3[node], b4[node] = float('inf'), None
    b3[router_id] = 0
def fonk3(b21):
    for b16 in b2:
        b2[b16] = b21[b16]
        for neighbor in b21[b16]:
            b2[b16][neighbor] = b21[b16][neighbor]
            b2[neighbor][b16] = b21[b16][neighbor]
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
def fonk6(port_numbers, b21):
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
    b11 = {neighbor: time.clock() for neighbor in b23}
    while True:
        b10.settimeout(20)
        try:
            b7, b12 = b10.recvfrom(2048)
            b7 = pickle.loads(b7)
        except:
            print("Message not received from all neighbors")
            fonk12()
            continue
        if 'updated' in b7:
            fonk8(b7)
        else:
            fonk9(b7, b11)
def fonk8(b7):
    b13 = 'updated'
    b14 = b7[b13]
    b15 = list(b14.keys())[0]
    b21[router_id][b15] = b14[b15]
def fonk9(b7, b11):
    b16 = list(b7.keys())[0]
    b17 = b7[b16]
    for neighbor, value in b17.items():
        b2[neighbor][b16] = value
        b2[b16][neighbor] = value
    b11[b16] = time.clock()
    fonk10(b11)
def fonk10(b11):
    for neighbor in b23:
        if time.clock() - b11[neighbor] > 15:
            fonk11(neighbor)
def fonk11(neighbor):
    b2[router_id][neighbor] = float('inf')
    b2[neighbor][router_id] = float('inf')
def fonk12():
    for neighbor in b23:
        fonk11(neighbor)
if b18 = = '__main__':
    _, router_id, port_no, b19 = sys.argv
    print("I am Router " + router_id)
    print("My b24 number is " + port_no)
    with open(b19) as f:
        b20 = int(f.readline().strip())
        print("Number of routers connected: " + str(b20))
        b21 = {router_id: {}}
        b22 = []
        global b23
        b23 = []
        for _ in range(b20):
            neighbor, distance_val, b24 = f.readline().strip().split()
            b23.append(neighbor)
            b22.append(b24)
            b21[router_id][neighbor] = float(distance_val)
        print(b23)
    threading.Thread(b25 = server, args=(int(port_no),)).start()
    time.sleep(4)
    threading.Thread(b25 = client, args=(b22, b21)).start()
    threading.Thread(b25 = bellman_ford, args=(b21,)).start()
    while True:
        pass