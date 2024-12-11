
from b1 import Algoritimo_kruskal as kr
import networkx as nx
import random
import time
import matplotlib.pyplot as plt
import b10 as prim
def fonk1():
    b1 = kr()
    b2 = []
    b3 = []
    b4 = []
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10, a1, 100):
        print('Number of Vertices:', num_vertices)
        b6 = nx.complete_graph(num_vertices)
        b7 = b6.b7()
        b8 = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in b7:
            b9 = random.randint(10, 100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.b7[v1, v2]['b9'] = b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0
        a3 = 0
        for _ in range(10):
            b12 = time.time()
            b13 = b1.b1(b6)
            b14 = time.time() - b12
            a2 += b14
            b12 = time.time()
            b15 = b10.primMST()
            b16 = time.time() - b12
            a3 += b16
        print("Average Execution Time (Kruskal):", a2 / 10, "seconds")
        print("Average Execution Time (Prim):", a3 / 10, "seconds")
        b2.append(num_vertices)
        b3.append(a2 / 10)
        b4.append(a3 / 10)
    print("Total Time:", time.time() - b5)
    plt.plot(b2, b4, b17 = "Prim's Algorithm")
    plt.plot(b2, b3, b17 = "Kruskal's Algorithm")
    plt.legend()
    plt.axis([0, a1 + 10, 0, max(b3) * 2])
    plt.ylabel('Execution Time (Seconds)')
    plt.xlabel('Number of Vertices')
    plt.title("Performance Comparison: Kruskal vs Prim (Complete Graphs)")
    plt.savefig('Kruskal_vs_Prim_Complete_Graphs.png')
    plt.show()
    print("Vertices List:")
    print(b2)
    print("Average Kruskal Times:")
    print(b3)
    print("Average Prim Times:")
    print(b4)
def fonk2():
    b1 = kr()
    b2 = []
    b3 = []
    b4 = []
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10, a1, 100):
        print('Number of Vertices:', num_vertices)
        b6 = nx.connected_watts_strogatz_graph(num_vertices, int(num_vertices / 2), 1)
        b7 = b6.b7()
        b8 = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in b7:
            b9 = random.randint(10, 100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.b7[v1, v2]['b9'] = b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0
        a3 = 0
        for _ in range(10):
            b12 = time.time()
            b13 = b1.b1(b6)
            b14 = time.time() - b12
            a2 += b14
            b12 = time.time()
            b15 = b10.primMST()
            b16 = time.time() - b12
            a3 += b16
        print("Average Execution Time (Kruskal):", a2 / 10, "seconds")
        print("Average Execution Time (Prim):", a3 / 10, "seconds")
        b2.append(num_vertices)
        b3.append(a2 / 10)
        b4.append(a3 / 10)
    print("Total Time:", time.time() - b5)
    plt.plot(b2, b4, b17 = "Prim's Algorithm")
    plt.plot(b2, b3, b17 = "Kruskal's Algorithm")
    plt.legend()
    plt.axis([0, a1 + 10, 0, max(b3) * 2])
    plt.ylabel('Execution Time (Seconds)')
    plt.xlabel('Number of Vertices')
    plt.title("Performance Comparison: Kruskal vs Prim (Incomplete Graphs)")
    plt.savefig('Kruskal_vs_Prim_Incomplete_Graphs.png')
    plt.show()
    print("Vertices List:")
    print(b2)
    print("Average Kruskal Times:")
    print(b3)
    print("Average Prim Times:")
    print(b4)
def fonk3(num_vertices):
    b6 = nx.connected_watts_strogatz_graph(num_vertices, 25, 0.5)
    b7 = b6.b7()
    b8 = [[0] * num_vertices for _ in range(num_vertices)]
    for v1, v2 in b7:
        b9 = random.randint(10, 100)
        b8[v1][v2] = b9
        b8[v2][v1] = b9
        b6.b7[v1, v2]['b9'] = b9
    b1 = kr()
    b10 = prim.Graph(num_vertices)
    b10.b11 = b8
    b13 = b1.b1(b6)
    b15 = b10.primMST()
    plt.show()
    nx.draw(b6, b18 = 5, alpha=1, node_color="black", edge_color="blue")
    plt.axis('equal')
    plt.savefig('Graph.png')
    plt.show()
    plt.figure(b19 = (8, 8))
    nx.draw(b15, b18 = 5, alpha=1, node_color="black", edge_color="red")
    plt.axis('equal')
    plt.savefig('Prim_MST.png')
    plt.show()
    plt.figure(b19 = (8, 8))
    nx.draw(b13, b18 = 5, alpha=1, node_color="black", edge_color="green")
    plt.axis('equal')
    plt.savefig('Kruskal_MST.png')
    plt.show()
fonk3(500)
fonk2()
fonk1()