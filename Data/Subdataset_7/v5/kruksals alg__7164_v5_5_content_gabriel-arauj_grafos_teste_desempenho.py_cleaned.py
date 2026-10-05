import sys
import time
import random
import matplotlib.pyplot as plt
import networkx as nx
from b5 import Algoritimo_kruskal as kr
import b6 as prim
def fonk1(num_vertices, b1 = True):
    if b1:
        b2 = nx.connected_watts_strogatz_graph(num_vertices, 25, 0.5)
    else:
        b2 = nx.fast_gnp_random_graph(num_vertices, 0.1)
    for v1, v2 in b2.edges():
        b3 = random.randint(10, 100)
        b2.edges[v1, v2]['b3'] = b3
    return b2
def fonk2(b7, b4 = 10):
    b5 = kr()
    b6 = prim.Graph(b7.number_of_nodes())
    b6.b7 = nx.to_numpy_array(b7)
    a1 = 0
    a2 = 0
    for _ in range(b4):
        b8 = time.time()
        b9 = b5.b5(b7)
        a1 += time.time() - b8
        b8 = time.time()
        b10 = b6.primMST()
        a2 += time.time() - b8
    b11 = a1 / b4
    b12 = a2 / b4
    return b11, b12
def fonk3(b14, b15, b16, graph_type):
    plt.plot(b14, b16, b13 = "Prim's Algorithm")
    plt.plot(b14, b15, b13 = "Kruskal's Algorithm")
    plt.legend()
    plt.xlabel('Number of Vertices')
    plt.ylabel('Execution Time (Seconds)')
    plt.title(f"Performance Comparison: Kruskal vs Prim ({graph_type} Graphs)")
    plt.savefig(f'Kruskal_vs_Prim_{graph_type}_Graphs.png')
    plt.show()
def fonk4(b1 = True):
    b14 = []
    b15 = []
    b16 = []
    a3 = 2011
    for num_vertices in range(10, a3, 100):
        print('Number of Vertices:', num_vertices)
        b2 = fonk1(num_vertices, b1=b1)
        b11, b12 = fonk2(b2)
        b14.append(num_vertices)
        b15.append(b11)
        b16.append(b12)
        print("Average Execution Time (Kruskal):", b11, "seconds")
        print("Average Execution Time (Prim):", b12, "seconds")
    fonk3(b14, b15, b16, "Complete" if b1 else "Incomplete")
if b17 = = "__main__":
    fonk4(b1 = False)
    fonk4(b1 = True)
