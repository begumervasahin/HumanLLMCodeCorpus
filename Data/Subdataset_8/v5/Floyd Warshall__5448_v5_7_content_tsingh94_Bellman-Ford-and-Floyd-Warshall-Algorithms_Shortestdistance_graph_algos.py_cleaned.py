import os
import re
import sys
import time
GRAPH_REGEX = re.compile(r"(\d+)\s(\d+)")
EDGE_REGEX = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def change_edge_matrix(edges):
    for v in range(len(edges)):
        for e in range(len(edges[v])):
            if isinstance(edges[v][e], str):
                edges[v][e] = int(edges[v][e])
    return edges
def bellman_ford(G):
    path_pairs = []
    edges = change_edge_matrix(G[1])
    infinity_val = edges[0][0]
    for n in range(len(G[0])):
        one_node_to_rest = [infinity_val if m != n else 0 for m in range(len(G[0]))]
        for _ in range(len(G[0])):
            new_row = []
            for i in range(len(edges)):
                val_assign = one_node_to_rest[i]
                for k in range(len(edges[i])):
                    check_node_weight = edges[k][i]
                    check_node_weight_prev_val = one_node_to_rest[k]
                    if check_node_weight != infinity_val and check_node_weight_prev_val != infinity_val:
                        val_assign = min(val_assign, check_node_weight + check_node_weight_prev_val)
                new_row.append(val_assign if i != n else 0)
            one_node_to_rest = new_row
        path_pairs.append(one_node_to_rest)
    return path_pairs
def floyd_warshall(G):
    path_pairs = change_edge_matrix(G[1])
    for i in range(len(G[0])):
        path_pairs[i][i] = 0
    for k in range(len(G[0])):
        for i in range(len(path_pairs)):
            for j in range(len(path_pairs[i])):
                path_pairs[i][j] = min(path_pairs[i][j], path_pairs[i][k] + path_pairs[k][j])
    return path_pairs
def read_file(filename):
    with open(filename, 'r') as inFile:
        line1 = inFile.readline()
        graph_match = GRAPH_REGEX.match(line1)
        if not graph_match:
            print(f"First line '{line1}' not properly formatted")
            sys.exit(1)
        vertices = list(range(int(graph_match.group(1))))
        edges = [[float("inf")] * len(vertices) for _ in range(len(vertices))]
        for line in inFile.readlines():
            line = line.strip()
            edge_match = EDGE_REGEX.match(line)
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source >= len(vertices) or sink >= len(vertices):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(vertices)} vertices")
                    sys.exit(1)
                edges[source][sink] = weight
    return vertices, edges
def write_file(length_matrix, filename):
    filename = os.path.splitext(os.path.split(filename)[1])[0]
    with open(f'output/{filename}_output.txt', 'w') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def main(filename, algorithm):
    algorithm = algorithm[1:]
    G = read_file(filename)
    path_lengths = []
    if algorithm.lower() == 'b':
        start = time.clock()
        path_lengths = bellman_ford(G)
        BFTime = time.clock() - start
        print("Bellman-Ford timing:", BFTime)
    elif algorithm.lower() == 'f':
        start = time.clock()
        path_lengths = floyd_warshall(G)
        FWTime = time.clock() - start
        print("Floyd-Warshall timing:", FWTime)
    elif algorithm.lower() == "both":
        start = time.clock()
        bellman_ford(G)
        BFTime = time.clock() - start
        start = time.clock()
        floyd_warshall(G)
        FWTime = time.clock() - start
        print("Bellman-Ford timing:", BFTime)
        print("Floyd-Warshall timing:", FWTime)
    write_file(path_lengths, filename)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])