from kruskal import Algoritimo_kruskal as kr
import networkx as nx
import random
import time
import matplotlib.pyplot as plt
import prim_graph as prim
def gerar_graficos_grafo_completo():
    k = kr()
    lista_vertices = []
    lista_media_tempo_kruskal = []
    lista_media_tempo_prim = []
    total = 2011
    tempo_total = time.time()
    for num_vertices in range(10, total, 100):
        print('Número de Vértices:', num_vertices)
        G = nx.complete_graph(num_vertices)
        a = G.edges()
        matriz = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in a:
            n = random.randint(10, 100)
            matriz[v1][v2] = n
            matriz[v2][v1] = n
            G.edges[v1, v2]['weight'] = n
        A = prim.Graph(num_vertices)
        A.graph = matriz
        soma_kruskal = 0.
        soma_prim = 0.
        for _ in range(1, 11):
            start = time.time()
            mst = k.kruskal(G)
            tempo = time.time() - start
            soma_kruskal += tempo
            start = time.time()
            parent = A.primMST()
            tempo = time.time() - start
            soma_prim += tempo
        print("Tempo execução (média) Kruskal:", soma_kruskal/10, "seconds")
        print("Tempo execução (média) Prim:", soma_prim/10, "seconds")
        lista_vertices.append(num_vertices)
        lista_media_tempo_kruskal.append(soma_kruskal/10)
        lista_media_tempo_prim.append(soma_prim/10)
    print("Total Time:", time.time() - tempo_total)
    plt.plot(lista_vertices, lista_media_tempo_prim, label="Prim's algorithm")
    plt.plot(lista_vertices, lista_media_tempo_kruskal, label="Kruskal's algorithm")
    plt.legend()
    plt.axis([0, total + 10, 0, max(lista_media_tempo_kruskal) * 2])
    plt.ylabel('Tempo de execução (Segundos)')
    plt.xlabel('Número de Vértices')
    plt.title("Comparação de desempenho: Kruskal x Prim (Grafo Completo)")
    plt.savefig('Kruskal x Prim - Grafos completos.png')
    plt.show()
    print("Lista de vértices:", lista_vertices)
    print("Tempo médio Kruskal:", lista_media_tempo_kruskal)
    print("Tempo médio Prim:", lista_media_tempo_prim)
def gerar_graficos_grafo_nao_completo():
    k = kr()
    lista_vertices = []
    lista_media_tempo_kruskal = []
    lista_media_tempo_prim = []
    total = 2011
    tempo_total = time.time()
    for num_vertices in range(10, total, 100):
        print('Número de Vértices:', num_vertices)
        G = nx.connected_watts_strogatz_graph(num_vertices, int(num_vertices/2), 1)
        a = G.edges()
        matriz = [[0] * num_vertices for _ in range(num_vertices)]
        for v1, v2 in a:
            n = random.randint(10, 100)
            matriz[v1][v2] = n
            matriz[v2][v1] = n
            G.edges[v1, v2]['weight'] = n
        A = prim.Graph(num_vertices)
        A.graph = matriz
        soma_kruskal = 0.
        soma_prim = 0.
        for _ in range(1, 11):
            start = time.time()
            mst = k.kruskal(G)
            tempo = time.time() - start
            soma_kruskal += tempo
            start = time.time()
            parent = A.primMST()
            tempo = time.time() - start
            soma_prim += tempo
        print("Tempo execução (média) Kruskal:", soma_kruskal/10, "seconds")
        print("Tempo execução (média) Prim:", soma_prim/10, "seconds")
        lista_vertices.append(num_vertices)
        lista_media_tempo_kruskal.append(soma_kruskal/10)
        lista_media_tempo_prim.append(soma_prim/10)
    print("Total Time:", time.time() - tempo_total)
    plt.plot(lista_vertices, lista_media_tempo_prim, label="Prim's algorithm")
    plt.plot(lista_vertices, lista_media_tempo_kruskal, label="Kruskal's algorithm")
    plt.legend()
    plt.axis([0, total + 10, 0, max(lista_media_tempo_kruskal) * 2])
    plt.ylabel('Tempo de execução (Segundos)')
    plt.xlabel('Número de Vértices')
    plt.title("Comparação de desempenho: Kruskal x Prim (Grafos não completos)")
    plt.savefig('Kruskal x Prim - Grafos não completos.png')
    plt.show()
    print("Lista de vértices:", lista_vertices)
    print("Tempo médio Kruskal:", lista_media_tempo_kruskal)
    print("Tempo médio Prim:", lista_media_tempo_prim)
def gerar_grafo(num_vertices):
    G = nx.connected_watts_strogatz_graph(num_vertices, 25, 0.5)
    a = G.edges()
    matriz = [[0] * num_vertices for _ in range(num_vertices)]
    for v1, v2 in a:
        n = random.randint(10, 100)
        matriz[v1][v2] = n
        matriz[v2][v1] = n
        G.edges[v1, v2]['weight'] = n
    k = kr()
    A = prim.Graph(num_vertices)
    A.graph = matriz
    mst = k.kruskal(G)
    mst_prim = A.primMST()
    plt.show()
    nx.draw(G, node_size=5, alpha=1, node_color="black", edge_color="red")
    plt.axis('equal')
    plt.savefig('Grafo.png')
    plt.show()
    plt.figure(figsize=(8, 8))
    nx.draw(mst_prim, node_size=5, alpha=1, node_color="black", edge_color="blue")
    plt.axis('equal')
    plt.savefig('mst_prim.png')
    plt.show()
    nx.draw(mst, node_size=5, alpha=1, node_color="black", edge_color="green")
    plt.axis('equal')
    plt.savefig('mst_kruskal.png')
    plt.show()
gerar_grafo(500)
gerar_graficos_grafo_nao_completo()
gerar_graficos_grafo_completo()