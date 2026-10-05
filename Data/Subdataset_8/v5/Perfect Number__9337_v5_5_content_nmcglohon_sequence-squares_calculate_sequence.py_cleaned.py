import sys
import networkx as nx
from random import shuffle
import time
perfect_squares = set()
def find_hamiltonian_path(G, path, pos, randomize):
    assert isinstance(G, nx.Graph)
    if pos == G.number_of_nodes():
        print(G.number_of_nodes(), path)
        return True
    nodes = list(G.nodes())
    if randomize:
        shuffle(nodes)
    for v in nodes:
        if v not in path:
            if len(path) == 0 or G.has_edge(path[-1], v):
                path.append(v)
                if find_hamiltonian_path(G, path, pos+1, randomize):
                    return True
                path.remove(v)
    return False
def is_square(a):
    assert a > 0
    x = a
    seen = set([x])
    while x * x != a:
        x = (x + (a
        if x in seen:
            return False
        seen.add(x)
    return True
def is_sum_to_perfect_square(a, b):
    if (a + b) in perfect_squares:
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
    G = nx.Graph()
    for i in range(1, end + 1):
        G.add_node(i)
        for node in G.nodes():
            if is_sum_to_perfect_square(i, node):
                G.add_edge(i, node)
        start = time.time()
        if find_hamiltonian_path(G.copy(), [], 0, randomize):
            has_hamiltonian_path.add(i)
            print("%d: %.2f Seconds" % (i, (time.time() - start)))
    for i in range(1, end + 1):
        if i in has_hamiltonian_path:
            print("%d: Yes" % i)
        else:
            print("%d: No" % i)
if __name__ == '__main__':
    main()