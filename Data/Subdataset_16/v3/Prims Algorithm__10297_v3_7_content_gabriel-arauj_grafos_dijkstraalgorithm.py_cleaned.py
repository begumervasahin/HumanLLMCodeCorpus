import time
import networkx as nx
import heapq
import sys
def fonk1(b7, b8, b9):
    for b6 in b7:
        b7.nodes[b6]['distance'] = sys.maxsize
        b7.nodes[b6]['labelled'] = False
    b7.nodes[b8]['distance'] = 0
    b1 = [(0, b8)]
    heapq.heapify(b1)
    while b1:
        current_distance, b2 = heapq.heappop(b1)
        if b7.nodes[b2]['labelled']:
            continue
        b7.nodes[b2]['labelled'] = True
        for neighbor in b7.successors(b2):
            if not b7.nodes[neighbor]['labelled']:
                b3 = current_distance + b7.edges[b2, neighbor]['weight']
                if b3 < b7.nodes[neighbor]['distance']:
                    b7.nodes[neighbor]['distance'] = b3
                    b7.nodes[neighbor]['precedent'] = b2
                    heapq.heappush(b1, (b3, neighbor))
    b4 = b7.nodes[b9]['distance']
    b5 = [{'weight': b4}]
    b6 = b9
    while b6 != b8:
        b5.append(b6)
        b6 = b7.nodes[b6].get('precedent', b8)
    b5.append(b8)
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
    return b7
def fonk3():
    try:
        b8 = int(input("Enter the b8 vertex: "))
        b9 = int(input("Enter the b9 vertex: "))
        return b8, b9
    except ValueError:
        print("The vertices must be integers.")
        return None, None
def fonk4():
    b7 = fonk2()
    print("Nodes\n", b7.nodes())
    print("Edges\n", b7.edges(b10 = True))
    b8, b9 = fonk3()
    if b8 is None or b9 is None:
        return
    if b8 in b7 and b9 in b7:
        b11 = time.time()
        b12 = fonk1(b7, b8, b9)
        b13 = time.time() - b11
        print(f"Dijkstra's algorithm executed in {b13:.6f} seconds.")
        print("Shortest Path: ", b12)
    else:
        print("The b8 or b9 vertex is not in the graph")
if b14 = = "__main__":
    fonk4()