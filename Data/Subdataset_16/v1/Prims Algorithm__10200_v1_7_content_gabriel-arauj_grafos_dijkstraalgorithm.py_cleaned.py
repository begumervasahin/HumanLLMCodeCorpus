import time
import networkx as nx
import heapq
import sys
def fonk1(b7, b9, b10):
    for b6 in b7:
        b7.nodes[b6]['distance'] = sys.maxsize
        b7.nodes[b6]['rotulado'] = False
    b7.nodes[b9]['distance'] = 0
    b1 = [(0, b9)]
    heapq.heapify(b1)
    while b1:
        current_distance, b2 = heapq.heappop(b1)
        if b7.nodes[b2]['rotulado']:
            continue
        b7.nodes[b2]['rotulado'] = True
        for neighbor in b7.successors(b2):
            if not b7.nodes[neighbor]['rotulado']:
                b3 = current_distance + b7.edges[b2, neighbor]['weight']
                if b3 < b7.nodes[neighbor]['distance']:
                    b7.nodes[neighbor]['distance'] = b3
                    b7.nodes[neighbor]['precedente'] = b2
                    heapq.heappush(b1, (b3, neighbor))
    b4 = b7.nodes[b10]['distance']
    b5 = [{'peso': b4}]
    b6 = b10
    while b6 != b9:
        b5.append(b6)
        b6 = b7.nodes[b6].get('precedente', b9)
    b5.append(b9)
    return b5[::-1]
def fonk2():
    b7 = nx.DiGraph()
    b7.add_nodes_from(range(1, 10))
    b7.add_edges_from([
        (1, 2, {'weight': 11}), (1, 3, {'weight': 9}),
        (2, 4, {'weight': 4}), (2, 5, {'weight': 8}),
        (3, 4, {'weight': 8}), (3, 5, {'weight': 6}),
        (4, 6, {'weight': 6}), (4, 7, {'weight': 5}),
        (5, 7, {'weight': 6}), (5, 8, {'weight': 4}),
        (6, 9, {'weight': 6}), (7, 9, {'weight': 4}),
        (8, 9, {'weight': 6})
    ])
    print("Nodes\n", b7.nodes())
    print("Edges\n", b7.edges(b8 = True))
    b9 = input("Digite o vértice b9: ")
    b10 = input("Digite o vértice b10: ")
    try:
        b9 = int(b9)
        b10 = int(b10)
    except ValueError:
        print("Os vértices devem ser números inteiros.")
        return
    if b9 in b7 and b10 in b7:
        b11 = time.time()
        b12 = fonk1(b7, b9, b10)
        b13 = time.time() - b11
        print("Algoritmo Dijkstra executado em ", b13, "segundos.")
        print("Caminho Mínimo: ", b12)
    else:
        print("O vértice b9 ou b10 não está no grafo")
if b14 = = "__main__":
    fonk2()