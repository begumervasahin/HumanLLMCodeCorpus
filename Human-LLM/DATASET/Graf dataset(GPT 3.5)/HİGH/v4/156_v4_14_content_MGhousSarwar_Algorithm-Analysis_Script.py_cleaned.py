import random
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from b7 import Graph, class1
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, b7):
        self.a1 = len(b7)
        b1 = [[0] * self.a1 for _ in range(self.a1)]
        for i in range(self.a1):
            for j in range(self.a1):
                b1[i][j] = b7[i][j]
        for k in range(self.a1):
            for i in range(self.a1):
                for j in range(self.a1):
                    if b1[i][k] + b1[k][j] < b1[i][j]:
                        b1[i][j] = b1[i][k] + b1[k][j]
        self.fonk3(b1)
    def fonk3(self, b4):
        for i in range(self.a1):
            for j in range(self.a1):
                if b4[i][j] == float('inf'):
                    print("INF\t", b2 = '')
                else:
                    print(str(b4[i][j]) + "\t", b2 = '')
            print()
        print()
    def fonk4(self, b4, b5):
        b3 = sys.maxsize
        a2 = 0
        for v in range(self.a1):
            if not b5[v] and b4[v] <= b3:
                b3 = b4[v]
                a2 = v
        return a2
    def fonk5(self, from_vertex, b4):
        print('Distance from:', from_vertex)
        print('Vertex\tDistance from source')
        for i in range(self.a1):
            print(str(i) + '\t\t' + str(b4[i]))
    def fonk6(self, b7):
        self.a1 = len(b7)
        for source in range(self.a1):
            b4 = [sys.maxsize] * self.a1
            b5 = [False] * self.a1
            b4[source] = 0
            for _ in range(self.a1 - 1):
                b6 = self.fonk4(b4, b5)
                b5[b6] = True
                for v in range(self.a1):
                    if not b5[v] and b7[b6][v] and b4[b6] != sys.maxsize \
                            and b4[b6] + b7[b6][v] < b4[v]:
                        b4[v] = b4[b6] + b7[b6][v]
            self.fonk5(source, b4)
def fonk7(b15):
    b7 = nx.DiGraph()
    b8 = [[random.randint(1, 1000) for _ in range(b15)] for _ in range(b15)]
    for i in range(b15):
        b8[i][i] = 0
    for i in range(b15):
        for j in range(b15):
            if b8[i][j] != 0:
                b7.add_edges_from([(i, j)], b9 = b8[i][j])
    return b7, b8
def fonk8(b7, reduction_factor):
    b10 = int(len(b7.edges) / reduction_factor)
    for _ in range(b10):
        b11 = random.choice(list(b7.edges()))
        b7.remove_edge(*b11)
def fonk9():
    b12 = []
    b13 = []
    b14 = []
    for graph_index in range(5):
        while True:
            b15 = random.randint(4, 8)
            if b15 not in b12:
                b12.append(b15)
                break
        b7, b8 = fonk7(b15)
        fonk8(b7, random.uniform(1.0, 1.1))
        print('Total Remaining Edges for Graph {}: {}'.format(graph_index, len(b7.edges)))
        b16 = class1()
        b17 = time.time()
        b16.fonk2(b8)
        b18 = time.time() - b17
        b13.append(b18)
        b19 = time.time()
        b16.fonk6(b8)
        b20 = time.time() - b19
        b14.append(b20)
        print("Floyd Execution Time:", b18)
        print("Dijkstra Execution Time:", b20)
    b13.sort()
    b14.sort()
    b12.sort()
    b21 = interp1d(b12, b13)
    b22 = interp1d(b12, b14)
    b23 = interp1d(b12, b13, kind='cubic')
    b24 = interp1d(b12, b14, kind='cubic')
    plt.plot(b12, b13, 'o', b12, b21(b12), '-', b12, b23(b12), '-')
    plt.plot(b12, b14, 'o', b12, b22(b12), '-', b12, b24(b12), '-')
    plt.legend(['Floyd', '', 'Floyd Line', 'Dijkstra', '', 'Dijkstra Line'], b25 = 'best')
    plt.show()
if b26 = = "__main__":
    fonk9()