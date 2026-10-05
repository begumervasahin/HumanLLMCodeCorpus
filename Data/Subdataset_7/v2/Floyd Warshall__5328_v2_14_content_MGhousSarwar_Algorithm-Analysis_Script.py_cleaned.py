import random
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from b1 import Graph, Algorithms
def fonk1(b9):
    b1 = nx.DiGraph()
    b2 = [[random.randint(1, 1000) for _ in range(b9)] for _ in range(b9)]
    for i in range(b9):
        b2[i][i] = 0
    for i in range(b9):
        for j in range(b9):
            if b2[i][j] != 0:
                b1.add_edges_from([(i, j)], b3 = b2[i][j])
    return b1, b2
def fonk2(b1, factor):
    b4 = int(len(b1.edges) / factor)
    for _ in range(b4):
        b5 = random.choice(list(b1.edges()))
        b1.remove_edge(*b5)
def fonk3():
    b6 = []
    b7 = []
    b8 = []
    for graph_index in range(5):
        while True:
            b9 = random.randint(4, 8)
            if b9 not in b6:
                b6.append(b9)
                break
        b1, b2 = fonk1(b9)
        fonk2(b1, random.uniform(1.0, 1.1))
        print('Total Remaining Edges for Graph {}: {}'.format(graph_index, len(b1.edges)))
        b10 = dict([((u, v), d['b3']) for u, v, d in b1.edges(data=True)])
        b11 = nx.spring_layout(b1)
        nx.draw_networkx_edge_labels(b1, b11, b10 = b10)
        nx.draw(b1, b11, b12 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
        plt.show()
        b13 = Algorithms()
        b14 = time.time()
        b13.floydWarshal(b2)
        b15 = time.time() - b14
        b7.append(b15)
        b16 = time.time()
        b13.dijkstra(b2)
        b17 = time.time() - b16
        b8.append(b17)
        print("Floyd Execution Time:", b15)
        print("Dijkstra Execution Time:", b17)
    b7.sort()
    b8.sort()
    b6.sort()
    b18 = interp1d(b6, b7)
    b19 = interp1d(b6, b8)
    b20 = interp1d(b6, b7, kind='cubic')
    b21 = interp1d(b6, b8, kind='cubic')
    plt.plot(b6, b7, 'o', b6, b18(b6), '-', b6, b20(b6), '-')
    plt.plot(b6, b8, 'o', b6, b19(b6), '-', b6, b21(b6), '-')
    plt.legend(['Floyd', '', 'Floyd Interpolated', 'Dijkstra', '', 'Dijkstra Interpolated'], b22 = 'best')
    plt.show()
if b23 = = "__main__":
    fonk3()