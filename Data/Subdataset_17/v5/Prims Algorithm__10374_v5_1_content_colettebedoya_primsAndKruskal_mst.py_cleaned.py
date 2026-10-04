import sys
import heapq
from DisjointSet import DisjointSet
def parse_input_file(input_file):
    adjacency = {}
    nodes = set()
    with open(input_file) as graph:
        for line in graph:
            vertex1, vertex2, weight = line.split()
            weight = int(weight)
            if vertex1 not in adjacency:
                adjacency[vertex1] = []
            if vertex2 not in adjacency:
                adjacency[vertex2] = []
            adjacency[vertex1].append((vertex2, weight))
            adjacency[vertex2].append((vertex1, weight))
            nodes.update([vertex1, vertex2])
    return adjacency, list(nodes)
def prims(input_file):
    adjacency, nodes = parse_input_file(input_file)
    for vertex, neighbors in adjacency.items():
        print(f"{vertex}: {neighbors}")
    start_node = nodes[0]
    min_heap = [(0, start_node)]
    visited = set()
    mst_cost = 0
    mst_edges = []
    while min_heap:
        weight, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        mst_cost += weight
        if weight != 0:
            mst_edges.append((previous_node, current_node, weight))
        for neighbor, edge_weight in adjacency[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
                previous_node = current_node
    print(f"Prim's total cost: {mst_cost} with edges:")
    return mst_edges
def kruskals(input_file):
    edges = []
    nodes = {}
    count = 0
    with open(input_file) as graph:
        for line in graph:
            vertex1, vertex2, weight = line.split()
            weight = int(weight)
            edges.append((weight, vertex1, vertex2))
            if vertex1 not in nodes:
                nodes[vertex1] = count
                count += 1
            if vertex2 not in nodes:
                nodes[vertex2] = count
                count += 1
    disjoint_set = DisjointSet(len(nodes))
    edges.sort()
    mst_cost = 0
    mst_edges = []
    for weight, vertex1, vertex2 in edges:
        if disjoint_set.find(nodes[vertex1]) != disjoint_set.find(nodes[vertex2]):
            disjoint_set.union(nodes[vertex1], nodes[vertex2])
            mst_edges.append((weight, vertex1, vertex2))
            mst_cost += weight
    return mst_cost, mst_edges
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python mst.py [input file] [prims | kruskals]")
        sys.exit(1)
    input_file = sys.argv[1]
    algorithm = sys.argv[2]
    if algorithm == 'prims':
        result = prims(input_file)
        for edge in result:
            print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")
    elif algorithm == 'kruskals':
        total_cost, result = kruskals(input_file)
        print(f"Kruskal's total cost: {total_cost} with edges:")
        for edge in result:
            print(f"Edge from {edge[1]} to {edge[2]} with weight {edge[0]}")
    else:
        print("Illegal algorithm. Must be either 'prims' or 'kruskals'.")
        sys.exit(1)