import random
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from b1 import Graph, Algorithms
def fonk1(b12):
    b1 = nx.DiGraph()
    b2 = [[random.randint(1, 1000) for _ in range(b12)] for _ in range(b12)]
    for i in range(b12):
        b2[i][i] = 0
    for i in range(b12):
        for j in range(b12):
            if b2[i][j] != 0:
                b1.add_edge(i, j, b3 = b2[i][j])
    return b1, b2
def fonk2(b1, reduction_factor):
    b4 = int(len(b1.edges) / reduction_factor)
    for _ in range(b4):
        b5 = random.choice(list(b1.edges()))
        b1.remove_edge(*b5)
def fonk3(b1):
    b6 = {(u, v): d['b3'] for u, v, d in b1.edges(data=True)}
    b7 = nx.spring_layout(b1)
    nx.draw_networkx_edge_labels(b1, b7, b6 = b6)
    nx.draw(b1, b7, b8 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
    plt.show()
def fonk4():
    b9 = []
    b10 = []
    b11 = []
    for graph_index in range(5):
        while True:
            b12 = random.randint(4, 8)
            if b12 not in b9:
                b9.append(b12)
                break
        b1, b2 = fonk1(b12)
        fonk2(b1, random.uniform(1.0, 1.1))
        print('Total Remaining Edges for Graph {}: {}'.format(graph_index, len(b1.edges)))
        fonk3(b1)
        b13 = Algorithms()
        b14 = time.time()
        b13.floydWarshal(b2)
        b15 = time.time() - b14
        b10.append(b15)
        b16 = time.time()
        b13.dijkstra(b2)
        b17 = time.time() - b16
        b11.append(b17)
        print("Floyd Execution Time:", b15)
        print("Dijkstra Execution Time:", b17)
    b10.sort()
    b11.sort()
    b9.sort()
    b18 = interp1d(b9, b10)
    b19 = interp1d(b9, b11)
    b20 = interp1d(b9, b10, kind='cubic')
    b21 = interp1d(b9, b11, kind='cubic')
    plt.plot(b9, b10, 'o', b9, b18(b9), '-', b9, b20(b9), '-')
    plt.plot(b9, b11, 'o', b9, b19(b9), '-', b9, b21(b9), '-')
    plt.legend(['Floyd', '', 'Floyd Interpolated', 'Dijkstra', '', 'Dijkstra Interpolated'], b22 = 'best')
    plt.show()
if b23 = = "__main__":
    fonk4()