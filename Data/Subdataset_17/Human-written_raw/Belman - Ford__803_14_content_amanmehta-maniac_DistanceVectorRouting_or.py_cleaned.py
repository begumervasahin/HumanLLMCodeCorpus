from collections import *
import pdb
import socket
import re
def initialize(graph, source):
    d = defaultdict(dict)
    for node in graph:
        for Node in graph:
            if node != Node:
                d[node][Node] = float('Inf')
            else: d[node][Node] = 0
    return d
def relax():
    print "relax called";
    s = socket.socket()
    host = ""
    port = 60000
    s.connect((host, port))
    data = s.recv(1024)
    print data;
def bellman_ford(graph, source):
    d = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            relax()
            port = 60000
            s = socket.socket()
            host = ""
            s.bind((host, port))
            s.listen(5)
            print 'Server listening....'
            time.sleep(1);
            conn, addr = s.accept()
            print "lol"
            for v in graph:
                tosend = tosend + str(v) + ' ' + str(d[u][v]) + "\n";
            forwd_table_u = str(u) + ' ' + tosend
            conn.send(forwd_table_u)
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p
def test(graph):
    print len(graph)
    d, p = bellman_ford(graph, i)
if __name__ == '__main__':
    graph, i = defaultdict(dict), 0
    with open('test') as f:
        lines = f.readlines()
        for i in range(1+int(lines[0])):
            gf = lines[i].split()
            if i != 0:
                k=1
                for l in range(int(gf[0])):
                    graph[i][int(gf[k])] = int(gf[k+1])
                    k=k+2
    test(graph)