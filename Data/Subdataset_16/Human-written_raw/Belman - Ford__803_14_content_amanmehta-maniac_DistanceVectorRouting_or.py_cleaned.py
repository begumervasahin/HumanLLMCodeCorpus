from collections import *
import pdb
import socket
import re
def fonk1(graph, source):
    b1 = defaultdict(dict)
    for node in graph:
        for Node in graph:
            if node != Node:
                b1[node][Node] = float('Inf')
            else: b1[node][Node] = 0
    return b1
def fonk2():
    print "relax called";
    b2 = socket.socket()
    b3 = ""
    a1 = 60000
    b2.connect((b3, a1))
    b4 = b2.recv(1024)
    print b4;
def fonk3(graph, source):
    b1 = fonk1(graph, source)
    for b10 in range(len(graph)-1):
        for u in graph:
            fonk2()
            a1 = 60000
            b2 = socket.socket()
            b3 = ""
            b2.bind((b3, a1))
            b2.listen(5)
            print 'Server listening....'
            time.sleep(1);
            conn, b5 = b2.accept()
            print "lol"
            for v in graph:
                b6 = b6 + str(v) + ' ' + str(b1[u][v]) + "\n";
            b7 = str(u) + ' ' + b6
            conn.send(b7)
    for u in graph:
        for v in graph[u]:
            assert b1[v] <= b1[u] + graph[u][v]
    return b1, b8
def fonk4(graph):
    print len(graph)
    b1, b8 = fonk3(graph, b10)
if b9 = = '__main__':
    graph, b10 = defaultdict(dict), 0
    with open('test') as f:
        b11 = f.readlines()
        for b10 in range(1+int(b11[0])):
            b12 = b11[b10].split()
            if b10 != 0:
                a2 = 1
                for l in range(int(b12[0])):
                    graph[b10][int(b12[a2])] = int(b12[a2+1])
                    a2 = a2+2
    fonk4(graph)