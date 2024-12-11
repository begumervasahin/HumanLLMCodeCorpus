import random
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from graph import *
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, graph):
        b1 = []
        self.a1 = len(graph)
        for i in range(self.a1):
            b2 = []
            for j in range(self.a1):
                b2.append(0)
            b1.append(b2)
        for i in range(0, self.a1):
            for j in range(0, self.a1):
                b1[i][j] = graph[i][j]
        for k in range(0, self.a1):
            for i in range(0, self.a1):
                for j in range(0, self.a1):
                    if float(b1[i][k] + b1[k][j]) < b1[i][j]:
                        b1[i][j] = float(b1[i][k] + b1[k][j])
        self.fonk3(b1)
    def fonk3(self, farness):
        for i in range(0, self.a1):
            for j in range(0, self.a1):
                if farness[i][j] == float('infinity'):
                    print("INF\b15", b3 = '')
                else:
                    print(str(farness[i][j]) + "\b15", b3 = '')
            print()
        print()
    def fonk4(self, b6, b7, b5):
        b4 = sys.maxsize
        a2 = 0
        for a1 in range(0, b5):
            if (b7[a1] == False and b6[a1] <= b4):
                b4 = b6[a1]
                a2 = a1
        return a2
    def fonk5(self,froom, b6, b5):
        print('Distance from :',froom)
        print('Vertex\tDistance from source')
        for i in range(0, b5):
            print(str(i) + '\b15\b15\b15' + str(b6[i]))
    def fonk6(self, graph):
        b5 = len(graph)
        a3 = 0
        for source in range(0, b5):
            b6 = [sys.maxsize] * b5
            b7 = [False] * b5
            b6[source] = 0
            for count in range(0, b5 - 1):
                b8 = self.fonk4(b6, b7, b5)
                b7[b8] = True
                for a1 in range(0, b5):
                    if b7[a1] == False and (
                            bool(graph[b8][a1]) and
                            b6[b8] != sys.maxsize and
                            b6[b8] + graph[b8][a1] < b6[a1]):
                        b6[a1] = b6[b8] + graph[b8][a1]
            self.fonk5(a3,b6, b5)
            a3+=1
b9 = []
b10 = []
b11 = []
b12 = []
for ip in range(5):
    print('                                                                                                    :', ip)
    while True:
        a1 = random.randint(4,8)
        if a1 not in b9:
            b9.append(a1)
            break
    b13 = nx.DiGraph()
    b14 = [[random.randint(1, 1000) for x in range(a1)]for y in range(a1)]
    print(a1)
    for b15 in range(a1):
        for b8 in range(a1):
            if b15 = = b8:
                b14[b15][b8] = 0
    for b15 in range(a1):
        for b8 in range(a1):
            if b14[b15][b8] != 0:
                b13.add_edges_from([(b15, b8)], b16 = b14[b15][b8])
    b17 = len(b13.edges)/1.1
    print(b17)
    for i in range(int(b17)):
        b18 = random.randint(0, a1 - 1)
        b19 = random.randint(0, a1 - 1)
        if b13.has_edge(b18,b19):
            b13.remove_edge(b18,b19)
    print('Total Remaning Edges :',len(b13.edges))
    b20 = dict([((b8, a1,), d['b16'])
                        for b8, a1, d in b13.edges(b14 = True)])
    b21 = nx.spring_layout(b13)
    nx.draw_networkx_edge_labels(b13, b21, b20 = b20)
    nx.draw(b13, b21, b22 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
    b23 = class1()
    b24 = time.time()
    b23.fonk2(b14)
    b25 = time.time() - b24
    b10.append(b25)
    b26 = time.time()
    b23.fonk6(b14)
    b27 = time.time() - b26
    b11.append(b27)
    print("Floyd : ", b25)
    print("Dijkstra : ", b27)
    plt.show()
b11.sort()
b10.sort()
b9.sort()
b28 = interp1d(b9, b10)
b29 = interp1d(b9, b11)
b30 = interp1d(b9, b10, kind='cubic')
b31 = interp1d(b9, b11, kind='cubic')
plt.plot(b9, b10, 'o', b9, b28(b9), '-', b9, b30(b9), '-')
plt.plot(b9, b11, 'o', b9, b29(b9), '-', b9, b31(b9), '-')
plt.legend(['Floyd','','Floyd Line','Dijkstra','','Dijkstra Line'], b32 = 'best')
plt.show()