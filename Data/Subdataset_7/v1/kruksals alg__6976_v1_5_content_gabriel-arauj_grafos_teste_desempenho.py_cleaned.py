from kruskal import Algoritimo_kruskal as kr
import networkx as nx
import random
import time
import matplotlib.pyplot as plt
import prim_graph as prim
def fonk1():
    b1 = kr()
    b2 = []
    b3 = []
    b4 = []
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10, a1, 100):
        print('Número de Vértices:', num_vertices)
        b6 = nx.complete_graph(num_vertices)
        b7 = b6.edges()
        b8 = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in b7:
            b9 = random.randint(10, 100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.edges[v1, v2]['weight'] = b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0.
        a3 = 0.
        for _ in range(1, 11):
            b12 = time.time()
            b13 = b1.kruskal(b6)
            b14 = time.time() - b12
            a2 += b14
            b12 = time.time()
            b15 = b10.primMST()
            b14 = time.time() - b12
            a3 += b14
        print("Tempo execução (média) Kruskal:", a2/10, "seconds")
        print("Tempo execução (média) Prim:", a3/10, "seconds")
        b2.append(num_vertices)
        b3.append(a2/10)
        b4.append(a3/10)
    print("Total Time:", time.time() - b5)
    plt.plot(b2, b4, b16 = "Prim's algorithm")
    plt.plot(b2, b3, b16 = "Kruskal's algorithm")
    plt.legend()
    plt.axis([0, a1 + 10, 0, max(b3) * 2])
    plt.ylabel('Tempo de execução (Segundos)')
    plt.xlabel('Número de Vértices')
    plt.title("Comparação de desempenho: Kruskal x Prim (Grafo Completo)")
    plt.savefig('Kruskal x Prim - Grafos completos.png')
    plt.show()
    print("Lista de vértices:", b2)
    print("Tempo médio Kruskal:", b3)
    print("Tempo médio Prim:", b4)
def fonk2():
    b1 = kr()
    b2 = []
    b3 = []
    b4 = []
    a1 = 2011
    b5 = time.time()
    for num_vertices in range(10, a1, 100):
        print('Número de Vértices:', num_vertices)
        b6 = nx.connected_watts_strogatz_graph(num_vertices, int(num_vertices/2), 1)
        b7 = b6.edges()
        b8 = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in b7:
            b9 = random.randint(10, 100)
            b8[v1][v2] = b9
            b8[v2][v1] = b9
            b6.edges[v1, v2]['weight'] = b9
        b10 = prim.Graph(num_vertices)
        b10.b11 = b8
        a2 = 0.
        a3 = 0.
        for _ in range(1, 11):
            b12 = time.time()
            b13 = b1.kruskal(b6)
            b14 = time.time() - b12
            a2 += b14
            b12 = time.time()
            b15 = b10.primMST()
            b14 = time.time() - b12
            a3 += b14
        print("Tempo execução (média) Kruskal:", a2/10, "seconds")
        print("Tempo execução (média) Prim:", a3/10, "seconds")
        b2.append(num_vertices)
        b3.append(a2/10)
        b4.append(a3/10)
    print("Total Time:", time.time() - b5)
    plt.plot(b2, b4, b16 = "Prim's algorithm")
    plt.plot(b2, b3, b16 = "Kruskal's algorithm")
    plt.legend()
    plt.axis([0, a1 + 10, 0, max(b3) * 2])
    plt.ylabel('Tempo de execução (Segundos)')
    plt.xlabel('Número de Vértices')
    plt.title("Comparação de desempenho: Kruskal x Prim (Grafos não completos)")
    plt.savefig('Kruskal x Prim - Grafos não completos.png')
    plt.show()
    print("Lista de vértices:", b2)
    print("Tempo médio Kruskal:", b3)
    print("Tempo médio Prim:", b4)
def fonk3(num_vertices):
    b6 = nx.connected_watts_strogatz_graph(num_vertices, 25, 0.5)
    b7 = b6.edges()
    b8 = [[0] * num_vertices for _ in range(num_vertices)]
    for v1, v2 in b7:
        b9 = random.randint(10, 100)
        b8[v1][v2] = b9
        b8[v2][v1] = b9
        b6.edges[v1, v2]['weight'] = b9
    b1 = kr()
    b10 = prim.Graph(num_vertices)
    b10.b11 = b8
    b13 = b1.kruskal(b6)
    b17 = b10.primMST()
    plt.show()
    nx.draw(b6, b18 = 5, alpha=1, node_color="black", edge_color="red")
    plt.axis('equal')
    plt.savefig('Grafo.png')
    plt.show()
    plt.figure(b19 = (8, 8))
    nx.draw(b17, b18 = 5, alpha=1, node_color="black", edge_color="blue")
    plt.axis('equal')
    plt.savefig('b17.png')
    plt.show()
    nx.draw(b13, b18 = 5, alpha=1, node_color="black", edge_color="green")
    plt.axis('equal')
    plt.savefig('mst_kruskal.png')
    plt.show()
fonk3(500)
fonk2()
fonk1()