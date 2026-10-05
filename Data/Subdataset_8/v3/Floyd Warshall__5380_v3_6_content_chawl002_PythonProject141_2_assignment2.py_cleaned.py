import os
import re
import sys
import time
graph_re = re.compile(r"(\d+)\s(\d+)")
edge_re = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def bellman_ford(graph):
    path_pairs = []
    d = []
    for _ in range(len(graph[0])):
        d = [float("inf")] * len(graph[0])
        d[_] = 0
        for _ in range(1, len(graph[0]) - 1):
            for e in range(len(graph[0])):
                for f in range(len(graph[0])):
                    if float(graph[1][e][f]) < float("inf"):
                        if d[f] > d[e] + float(graph[1][e][f]):
                            d[f] = int(d[e]) + int(float(graph[1][e][f]))
        path_pairs.append(d)
    return path_pairs
def floyd_warshall(graph):
    path_pairs = []
    d = []
    for _ in range(len(graph[0])):
        drow = [float("inf")] * len(graph[0])
        d.append(drow)
    for c in range(len(graph[0])):
        for e in range(len(graph[0])):
            if c == e:
                d[c][c] = 0
            elif float(graph[1][c][e]) < float("inf"):
                d[c][e] = int(float(graph[1][c][e]))
            else:
                d[c][e] = float("inf")
    for c in range(len(graph[0])):
        for a in range(len(graph[0])):
            for b in range(len(graph[0])):
                d[a][b] = min(d[a][b], d[a][c] + d[c][b])
    path_pairs.append(d)
    return path_pairs
def read_file(filename):
    with open(filename, 'r') as inFile:
        line1 = inFile.readline().strip()
        graph_match = graph_re.match(line1)
        if not graph_match:
            print(f"First line '{line1}' not properly formatted")
            sys.exit(1)
        vertices = list(range(int(graph_match.group(1))))
        edges = [[float("inf")] * len(vertices) for _ in range(len(vertices))]
        for line in inFile.readlines():
            line = line.strip()
            edge_match = edge_re.match(line)
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source >= len(vertices) or sink >= len(vertices):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(vertices)} vertices")
                    sys.exit(1)
                edges[source][sink] = weight
    return vertices, edges
def write_file(length_matrix, filename):
    filename = os.path.splitext(os.path.split(filename)[1])[0]
    with open(f'output/{filename}_output.txt', 'w+') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def main(filename, algorithm):
    algorithm = algorithm[1:]
    graph = read_file(filename)
    path_lengths = []
    if algorithm in {'b', 'B'}:
        path_lengths = bellman_ford(graph)
    elif algorithm in {'f', 'F'}:
        path_lengths = floyd_warshall(graph)
    elif algorithm.lower() == "both":
        start = time.clock()
        bellman_ford(graph)
        BFTime = time.clock() - start
        start = time.clock()
        floyd_warshall(graph)
        FWTime = time.clock() - start
        print(f"Bellman-Ford timing: {BFTime}")
        print(f"Floyd-Warshall timing: {FWTime}")
    write_file(path_lengths, filename)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])