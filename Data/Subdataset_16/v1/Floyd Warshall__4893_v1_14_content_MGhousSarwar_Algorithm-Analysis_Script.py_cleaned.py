import random
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from graph import Graph
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, graph):
        self.a1 = len(graph)
        b1 = [[graph[i][j] for j in range(self.a1)] for i in range(self.a1)]
        for k in range(self.a1):
            for i in range(self.a1):
                for j in range(self.a1):
                    if b1[i][k] + b1[k][j] < b1[i][j]:
                        b1[i][j] = b1[i][k] + b1[k][j]
        self.fonk3(b1)
    def fonk3(self, b1):
        for i in range(self.a1):
            for j in range(self.a1):
                if b1[i][j] == float('inf'):
                    print("INF", b2 = "\t")
                else:
                    print(f"{b1[i][j]:.2f}", b2 = "\t")
            print()
        print()
    def fonk4(self, b5, b6, b4):
        b3 = sys.maxsize
        a2 = -1
        for a1 in range(b4):
            if not b6[a1] and b5[a1] <= b3:
                b3 = b5[a1]
                a2 = a1
        return a2
    def fonk5(self, source, b5, b4):
        print(f"Distance from vertex {source}:")
        print("Vertex\tDistance from source")
        for i in range(b4):
            print(f"{i}\t\t{b5[i]}")
        print()
    def fonk6(self, graph):
        b4 = len(graph)
 for source in range(b4):
            b5 = [sys.maxsize] * b4
            b6 = [False] * b4
            b5[source] = 0
            for _ in range(b4 - 1):
                b7 = self.fonk4(b5, b6, b4)
                b6[b7] = True
                for a1 in range(b4):
                    if (not b6[a1] and graph[b7][a1] and b5[b7] != sys.maxsize
                            and b5[b7] + graph[b7][a1] < b5[a1]):
                        b5[a1] = b5[b7] + graph[b7][a1]
            self.fonk5(source, b5, b4)
def fonk7(a1):
    b8 = [[random.randint(1, 1000) if i != j else 0 for j in range(a1)] for i in range(a1)]
    return b8
def fonk8(b14, b18, b9):
    nx.draw_networkx_edge_labels(b14, b18, b9 = b9)
    nx.draw(b14, b18, b10 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
    plt.show()
def fonk9():
    b11 = []
    b12 = []
    b13 = []
    for ip in range(5):
        print(f"Graph {ip+1}")
        while True:
            a1 = random.randint(4, 8)
            if a1 not in b11:
                b11.append(a1)
                break
        b14 = nx.DiGraph()
        b8 = fonk7(a1)
        for i in range(a1):
            for j in range(a1):
                if b8[i][j] != 0:
                    b14.add_edge(i, j, b15 = b8[i][j])
        b16 = len(b14.edges)
        for _ in range(int(b16)):
            b17 = random.choice(list(b14.edges))
            b14.remove_edge(*b17)
        print(f"Total remaining edges: {len(b14.edges)}")
        b18 = nx.spring_layout(b14)
        b9 = {(b7, a1): d['b15'] for b7, a1, d in b14.edges(b8=True)}
        fonk8(b14, b18, b9)
        b19 = class1()
        b20 = time.time()
        b19.fonk2(b8)
        b12.append(time.time() - b20)
        b20 = time.time()
        b19.fonk6(b8)
        b13.append(time.time() - b20)
        print(f"Floyd-Warshall time: {b12[-1]:.6f} seconds")
        print(f"Dijkstra time: {b13[-1]:.6f} seconds")
    b11.sort()
    b12.sort()
    b13.sort()
    b21 = interp1d(b11, b12)
    b22 = interp1d(b11, b13)
    b23 = interp1d(b11, b12, kind='cubic')
    b24 = interp1d(b11, b13, kind='cubic')
    plt.plot(b11, b12, 'o', b11, b21(b11), '-', b11, b23(b11), '-')
    plt.plot(b11, b13, 'o', b11, b22(b11), '-', b11, b24(b11), '-')
    plt.legend(['Floyd-Warshall', '', 'Floyd-Warshall (Cubic)', 'Dijkstra', '', 'Dijkstra (Cubic)'], b25 = 'best')
    plt.show()
if b26 = = "__main__":
    fonk9()q