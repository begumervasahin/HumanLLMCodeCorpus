import random
import sys
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
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
    def fonk4(self, b4, b5):
        b3 = sys.maxsize
        a2 = -1
        for a1 in range(self.a1):
            if not b5[a1] and b4[a1] <= b3:
                b3 = b4[a1]
                a2 = a1
        return a2
    def fonk5(self, source, b4):
        print(f"Distance from vertex {source}:")
        print("Vertex\tDistance from source")
        for i in range(self.a1):
            print(f"{i}\t\t{b4[i]}")
        print()
    def fonk6(self, graph):
        self.a1 = len(graph)
        for source in range(self.a1):
            b4 = [sys.maxsize] * self.a1
            b5 = [False] * self.a1
            b4[source] = 0
            for _ in range(self.a1 - 1):
                b6 = self.fonk4(b4, b5)
                b5[b6] = True
                for a1 in range(self.a1):
                    if (not b5[a1] and graph[b6][a1] and b4[b6] != sys.maxsize
                            and b4[b6] + graph[b6][a1] < b4[a1]):
                        b4[a1] = b4[b6] + graph[b6][a1]
            self.fonk5(source, b4)
def fonk7(a1):
    return [[random.randint(1, 1000) if i != j else 0 for j in range(a1)] for i in range(a1)]
def fonk8(b12, b17, b7):
    nx.draw_networkx_edge_labels(b12, b17, b7 = b7)
    nx.draw(b12, b17, b8 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
    plt.show()
def fonk9():
    b9 = []
    b10 = []
    b11 = []
    for ip in range(5):
        print(f"Graph {ip + 1}")
        while True:
            a1 = random.randint(4, 8)
            if a1 not in b9:
                b9.append(a1)
                break
        b12 = nx.DiGraph()
        b13 = fonk7(a1)
        for i in range(a1):
            for j in range(a1):
                if b13[i][j] != 0:
                    b12.add_edge(i, j, b14 = b13[i][j])
        b15 = int(len(b12.edges) / 1.1)
        for _ in range(b15):
            b16 = random.choice(list(b12.edges))
            b12.remove_edge(*b16)
        print(f"Total remaining edges: {len(b12.edges)}")
        b17 = nx.spring_layout(b12)
        b7 = {(b6, a1): d['b14'] for b6, a1, d in b12.edges(b13=True)}
        fonk8(b12, b17, b7)
        b18 = class1()
        b19 = time.time()
        b18.fonk2(b13)
        b10.append(time.time() - b19)
        b19 = time.time()
        b18.fonk6(b13)
        b11.append(time.time() - b19)
        print(f"Floyd-Warshall time: {b10[-1]:.6f} seconds")
        print(f"Dijkstra time: {b11[-1]:.6f} seconds")
    b9.sort()
    b10.sort()
    b11.sort()
    b20 = interp1d(b9, b10)
    b21 = interp1d(b9, b11)
    b22 = interp1d(b9, b10, kind='cubic')
    b23 = interp1d(b9, b11, kind='cubic')
    plt.plot(b9, b10, 'o', b9, b20(b9), '-', b9, b22(b9), '-')
    plt.plot(b9, b11, 'o', b9, b21(b9), '-', b9, b23(b9), '-')
    plt.legend(['Floyd-Warshall', '', 'Floyd-Warshall (Cubic)', 'Dijkstra', '', 'Dijkstra (Cubic)'], b24 = 'best')
    plt.show()
if b25 = = "__main__":
    fonk9()