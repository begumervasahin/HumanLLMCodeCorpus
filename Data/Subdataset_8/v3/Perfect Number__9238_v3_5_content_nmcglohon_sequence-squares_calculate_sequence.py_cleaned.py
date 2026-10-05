import sys
import networkx as nx
import time
from random import shuffle
perfect_squares = set()
def hamiltonian_path_recursive(graph, path, position, randomize):
    assert isinstance(graph, nx.Graph)
    if position == graph.number_of_nodes():
        print(graph.number_of_nodes(), path)
        return True
    nodes = list(graph.nodes())
    if randomize:
        shuffle(nodes)
    for node in nodes:
        if node not in path:
            if len(path) == 0 or graph.has_edge(path[-1], node):
                path.append(node)
                if hamiltonian_path_recursive(graph, path, position + 1, randomize):
                    return True
                path.remove(node)
    return False
def is_square(num):
    assert num > 0
    x = num
    seen = set([x])
    while x * x != num:
        x = (x + (num
        if x in seen:
            return False
        seen.add(x)
    return True
def is_sum_to_perfect_square(a, b):
    if a + b in perfect_squares:
        return True
    elif is_square(a + b):
        perfect_squares.add(a + b)
        return True
    else:
        return False
def main():
    end = int(sys.argv[1])
    randomize = int(sys.argv[2])
    has_hamiltonian_path = set()
    graph = nx.Graph()
    for i in range(1, end + 1):
        graph.add_node(i)
        for node in graph.nodes():
            if is_sum_to_perfect_square(i, node):
                graph.add_edge(i, node)
        start_time = time.time()
        if hamiltonian_path_recursive(graph.copy(), [], 0, randomize):
            has_hamiltonian_path.add(i)
            print("%d: %.2f Seconds" % (i, (time.time() - start_time)))
    for i in range(1, end + 1):
        if i in has_hamiltonian_path:
            print("%d: Yes" % i)
        else:
            print("%d: No" % i)
if __name__ == '__main__':
    main()