import time
import networkx as nx
from filaprioritaria import PriorityQueue
import sys
def fonk1(b8, b10, b11):
    for node in b8:
        b8.nodes[node]['b5'] = sys.maxsize
        b8.nodes[node]['labeled'] = False
    b8.nodes[b10]['b5'] = 0
    b1 = PriorityQueue()
    for node in b8:
        b1.insert((b8.nodes[node]['b5'], node))
    while b1.getTamanho() != 0:
        b2 = b1.remove_min()
        b3 = b2[1]
        b8.nodes[b3]['labeled'] = True
        for successor in b8.successors(b3):
            if not b8.nodes[successor]['labeled']:
                b4 = b8.nodes[b3]['b5'] + b8.edges[b3, successor]['weight']
                if b4 < b8.nodes[successor]['b5']:
                    b8.nodes[successor]['b5'] = b4
                    b8.nodes[successor]['precedent'] = b3
                    b1.increase_key(successor, b4)
    b5 = b8.nodes[b11]['b5']
    b6 = [{'weight': b5}]
    b7 = b11
    while True:
        try:
            b6.append(b7)
            b7 = b8.nodes[b7]['precedent']
        except KeyError:
            break
    return b6[::-1]
def fonk2():
    b8 = nx.DiGraph()
    b8.add_nodes_from(range(1, 10))
    b8.add_edges_from([
        (1, 2, {'weight': 11}), (1, 3, {'weight': 9}), (2, 4, {'weight': 4}),
        (2, 5, {'weight': 8}), (3, 4, {'weight': 8}), (3, 5, {'weight': 6}),
        (4, 6, {'weight': 6}), (4, 7, {'weight': 5}), (5, 7, {'weight': 6}),
        (5, 8, {'weight': 4}), (6, 9, {'weight': 6}), (7, 9, {'weight': 4}), (8, 9, {'weight': 6})
    ])
    print("Nodes\n", b8.nodes())
    print("Edges\n", b8.edges(b9 = True))
    b10 = input("Digite o vértice fonte: ")
    try:
        b10 = int(b10)
    except ValueError:
        pass
    b11 = input("Digite o vértice destino: ")
    try:
        b11 = int(b11)
    except ValueError:
        pass
    if b10 in b8:
        if b11 in b8:
            b12 = time.time()
            b13 = fonk1(b8, b10, b11)
            b14 = time.time() - b12
            print(f"Algoritmo Dijkstra executado em {b14} segundos.")
            print("Caminho Mínimo: ", b13)
        else:
            print("O vértice destino não está no grafo.")
    else:
        print("O vértice fonte não está no grafo.")
if b15 = = "__main__":
    fonk2()