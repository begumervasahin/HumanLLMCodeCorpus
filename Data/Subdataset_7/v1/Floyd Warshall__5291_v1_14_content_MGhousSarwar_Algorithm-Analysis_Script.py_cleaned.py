import random
import time
import matplotlib.pyplot as plt
import networkx as nx
from scipy.interpolate import interp1d
from graph import Graph, Algorithms
def fonk1(b10):
    b1 = nx.DiGraph()
    b2 = [[random.randint(1, 1000) for _ in range(b10)] for _ in range(b10)]
    for b3 in range(b10):
        for u in range(b10):
            if b3 = = u:
                b2[b3][u] = 0
    for b3 in range(b10):
        for u in range(b10):
            if b2[b3][u] != 0:
                b1.add_edges_from([(b3, u)], b4 = b2[b3][u])
    return b1, b2
def fonk2(b1, b11):
    b5 = int(len(b1.edges) / b11)
    for _ in range(b5):
        b6 = random.choice(list(b1.edges()))
        b1.remove_edge(*b6)
def fonk3():
    b7 = []
    b8 = []
    b9 = []
    for ip in range(5):
        while True:
            b10 = random.randint(4, 8)
            if b10 not in b7:
                b7.append(b10)
                break
        b1, b2 = fonk1(b10)
        b11 = random.uniform(1.0, 1.1)
        fonk2(b1, b11)
        print('Total Remaining Edges for Graph {}: {}'.format(ip, len(b1.edges)))
        b12 = dict([((u, b10,), d['b4']) for u, b10, d in b1.edges(b2=True)])
        b13 = nx.spring_layout(b1)
        nx.draw_networkx_edge_labels(b1, b13, b12 = b12)
        nx.draw(b1, b13, b14 = True, node_size=1500, edge_color='black', edge_cmap=plt.cm.Reds)
        plt.show()
        b15 = Algorithms()
        b16 = time.time()
        b15.floydWarshal(b2)
        b17 = time.time() - b16
        b8.append(b17)
        b18 = time.time()
        b15.dijkstra(b2)
        b19 = time.time() - b18
        b9.append(b19)
        print("Floyd:", b17)
        print("Dijkstra:", b19)
    b9.sort()
    b8.sort()
    b7.sort()
    b20 = interp1d(b7, b8)
    b21 = interp1d(b7, b9)
    b22 = interp1d(b7, b8, kind='cubic')
    b23 = interp1d(b7, b9, kind='cubic')
    plt.plot(b7, b8, 'o', b7, b20(b7), '-', b7, b22(b7), '-')
    plt.plot(b7, b9, 'o', b7, b21(b7), '-', b7, b23(b7), '-')
    plt.legend(['Floyd', '', 'Floyd Line', 'Dijkstra', '', 'Dijkstra Line'], b24 = 'best')
    plt.show()
if b25 = = "__main__":
    fonk3()