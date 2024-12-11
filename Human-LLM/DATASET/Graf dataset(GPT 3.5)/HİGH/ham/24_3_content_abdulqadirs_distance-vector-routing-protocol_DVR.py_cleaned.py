from sys import argv
import thread
import time
import socket
import pickle
b1 = time.clock()
b2 = {
            'A':{},
            'B':{},
            'C':{},
            'D':{},
            'E':{},
            'F':{},
        }
distance, b3 = dict(), dict()
def fonk1(b23):
    while 1:
        for node in b2:
            distance[node], b3[node] = float('inf'), None
        distance[routerid] = 0
        time.sleep(3)
        if time.clock()-b1<20:
            for a1 in range(len(b23)):
                b4 = (b23.keys()[a1])
                b2[b4]=b23[b4]
                for j in b23[b4]:
                    b2[b4][j]=b23[b4][j]
                    b2[j][b4]=b23[b4][j]
        for _ in range(len(b2)-1):
            for u in b2:
                for v in b2[u]:
                    if distance[v] >=distance[u] + b2[u][v]:
                        distance[v], b3[v] = distance[u] + b2[u][v],u
        for a1 in range(len(b2)):
            b4 = b2.keys()[a1]
            if distance[b4]==float('inf'):
                b3[b4]=None
        b5 = distance.keys()
        for a1 in range(len(distance)):
            print "Distance to %s: %f" %(b5[a1], distance[b5[a1]])
        print '\n'
def fonk2(portno, b23):
    b6 = "127.0.0.1"
    while 1:
        try:
            b7 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except:
            print "Socket cannot be bound"
        a1 = 0
        while a1 < len(portno):
            time.sleep(4)
            b8 = {routerid:b2[routerid]}
            b7.sendto(pickle.dumps(b8),(b6,int(portno[a1])))
            a1+=1
def fonk3(portno):
    b9 = "127.0.0.1"
    b10 = portno
    b11 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    b11.bind((b9,b10))
    print "Server setup"
    b12 = dict()
    for a1 in range(len(b25)):
        b12[b25[a1]] = time.clock()
    while 1:
        b11.settimeout(20)
        try:
            b14,b13 = b11.recvfrom(2048)
            b14 = pickle.loads(b14)
        except:
            print("b14 not received from all neighbors")
            for a1 in range(len(b25)):
                b2[routerid][b25[a1]]=float('inf')
            continue
        if b14.keys()[0] == 'updated':
            b15 = (b14.keys()[0])
            b16 = b14[b15]
            b17 = b16.keys()[0]
            b23[routerid][b17] = b16[b17]
        else:
            b4 = (b14.keys()[0])
            b18 = b14[b4]
            for a1 in b18:
                b2[a1][b4]=b18[a1]
                b2[b4][a1]=b18[a1]
            b12[b4] = time.clock()
        for a1 in range(len(b25)):
            if time.clock() - b12[b25[a1]] > 15:
                b19 = b25[a1]
                b2[routerid][b19]=float('inf')
                b2[b19][routerid]=float('inf')
script, routerid, portno, b20 = argv
print "I am Router " + routerid
print "My port number is " + portno
b21 = open(b20)
b22 = b21.readline()
print "Number of routers connected: " + b22
b22 = int(b22)
b23 = {}
b23[routerid] = {}
b24 = []
b25 = []
while b22 > 0:
    b26 = b21.readline()
    b27 = b26.split()
    b25.append(b27[0])
    b24.append(b27[2])
    b23[routerid][b27[0]] = float(b27[1])
    b22 = b22 - 1
print b25
thread.start_new_thread(server, (int(portno), ))
time.sleep(4)
thread.start_new_thread(client, (b24, b23))
thread.start_new_thread(bellmanford, (b23, ))
while 1:
    pass