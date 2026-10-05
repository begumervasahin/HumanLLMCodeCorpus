import os
import re
import sys
import time
graph_re = re.compile(r"(\d+)\s(\d+)")
edge_re = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def bellman_ford(G):
    path_pairs = []
    num_vertices = len(G[0])
    for _ in range(num_vertices):
        distances = [float("inf")] * num_vertices
        distances[_] = 0
        for _ in range(1, num_vertices - 1):
            for source in range(num_vertices):
                for destination in range(num_vertices):
                    if float(G[1][source][destination]) < float("inf"):
                        new_distance = distances[source] + float(G[1][source][destination])
                        if distances[destination] > new_distance:
                            distances[destination] = new_distance
        path_pairs.append(distances)
    return path_pairs
def floyd_warshall(G):
    path_pairs = []
    num_vertices = len(G[0])
    distances = [[float("inf")] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        distances[i][i] = 0
    for source in range(num_vertices):
        for destination in range(num_vertices):
            if float(G[1][source][destination]) < float("inf"):
                distances[source][destination] = float(G[1][source][destination])
    for intermediate in range(num_vertices):
        for source in range(num_vertices):
            for destination in range(num_vertices):
                distances[source][destination] = min(
                    distances[source][destination],
                    distances[source][intermediate] + distances[intermediate][destination]
                )
    path_pairs.append(distances)
    return path_pairs
def read_file(filename):
    with open(filename, 'r') as inFile:
        line1 = inFile.readline().strip()
        graph_match = graph_re.match(line1)
        if not graph_match:
            print(f"First line '{line1}' not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in inFile.readlines():
            line = line.strip()
            edge_match = edge_re.match(line)
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source >= num_vertices or sink >= num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
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
    G = read_file(filename)
    path_lengths = []
    if algorithm in {'b', 'B'}:
        path_lengths = bellman_ford(G)
    elif algorithm in {'f', 'F'}:
        path_lengths = floyd_warshall(G)
    elif algorithm.lower() == "both":
        start = time.clock()
        bellman_ford(G)
        BFTime = time.clock() - start
        start = time.clock()
        floyd_warshall(G)
        FWTime = time.clock() - start
        print(f"Bellman-Ford timing: {BFTime}")
        print(f"Floyd-Warshall timing: {FWTime}")
    write_file(path_lengths, filename)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])