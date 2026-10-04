import time
import networkx as nx
from filaprioritaria import PriorityQueue
import sys
def dijkstra(digraph, source, target):
    for node in digraph:
        digraph.nodes[node]['distance'] = sys.maxsize
        digraph.nodes[node]['labeled'] = False
    digraph.nodes[source]['distance'] = 0
    pq = PriorityQueue()
    for node in digraph:
        pq.insert((digraph.nodes[node]['distance'], node))
    while pq.getTamanho() != 0:
        u = pq.remove_min()
        k = u[1]
        digraph.nodes[k]['labeled'] = True
        for successor in digraph.successors(k):
            if not digraph.nodes[successor]['labeled']:
                new_cost = digraph.nodes[k]['distance'] + digraph.edges[k, successor]['weight']
                if new_cost < digraph.nodes[successor]['distance']:
                    digraph.nodes[successor]['distance'] = new_cost
                    digraph.nodes[successor]['precedent'] = k
                    pq.increase_key(successor, new_cost)
    distance = digraph.nodes[target]['distance']
    path = [{'weight': distance}]
    current_node = target
    while True:
        try:
            path.append(current_node)
            current_node = digraph.nodes[current_node]['precedent']
        except KeyError:
            break
    return path[::-1]
def teste():
    digraph = nx.DiGraph()
    digraph.add_nodes_from(range(1, 10))
    digraph.add_edges_from([
        (1, 2, {'weight': 11}), (1, 3, {'weight': 9}), (2, 4, {'weight': 4}),
        (2, 5, {'weight': 8}), (3, 4, {'weight': 8}), (3, 5, {'weight': 6}),
        (4, 6, {'weight': 6}), (4, 7, {'weight': 5}), (5, 7, {'weight': 6}),
        (5, 8, {'weight': 4}), (6, 9, {'weight': 6}), (7, 9, {'weight': 4}), (8, 9, {'weight': 6})
    ])
    print("Nodes\n", digraph.nodes())
    print("Edges\n", digraph.edges(data=True))
    source = input("Digite o vértice fonte: ")
    try:
        source = int(source)
    except ValueError:
        pass
    target = input("Digite o vértice destino: ")
    try:
        target = int(target)
    except ValueError:
        pass
    if source in digraph:
        if target in digraph:
            start_time = time.time()
            minimum_path = dijkstra(digraph, source, target)
            elapsed_time = time.time() - start_time
            print(f"Algoritmo Dijkstra executado em {elapsed_time} segundos.")
            print("Caminho Mínimo: ", minimum_path)
        else:
            print("O vértice destino não está no grafo.")
    else:
        print("O vértice fonte não está no grafo.")
if __name__ == "__main__":
    teste()