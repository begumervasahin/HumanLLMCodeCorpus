import os
import re
import sys
import time
GRAPH_PATTERN = re.compile(r"(\d+)\s(\d+)")
EDGE_PATTERN = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def bellman_ford(graph):
    vertices, edges = graph
    num_vertices = len(vertices)
    path_pairs = []
    for src in range(num_vertices):
        dist = [float("inf")] * num_vertices
        dist[src] = 0
        for _ in range(num_vertices - 1):
            for u in range(num_vertices):
                for v in range(num_vertices):
                    if edges[u][v] < float("inf"):
                        if dist[v] > dist[u] + edges[u][v]:
                            dist[v] = dist[u] + edges[u][v]
        path_pairs.append(dist)
    return path_pairs
def floyd_warshall(graph):
    vertices, edges = graph
    num_vertices = len(vertices)
    dist = [[float("inf")] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u == v:
                dist[u][v] = 0
            elif edges[u][v] < float("inf"):
                dist[u][v] = edges[u][v]
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def read_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        graph_match = GRAPH_PATTERN.match(first_line)
        if not graph_match:
            print(f"{first_line} not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in file:
            line = line.strip()
            edge_match = EDGE_PATTERN.match(line)
            if edge_match:
                source = int(edge_match.group(1))
                sink = int(edge_match.group(2))
                weight = int(edge_match.group(3))
                if source >= num_vertices or sink >= num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
                    sys.exit(1)
                edges[source][sink] = weight
    return vertices, edges
def write_file(length_matrix, filename):
    base_filename = os.path.splitext(os.path.basename(filename))[0]
    output_filename = f'output/{base_filename}_output.txt'
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    with open(output_filename, 'w') as outFile:
        for vertex in length_matrix:
            outFile.write(','.join(map(str, vertex)) + '\n')
def main(filename, algorithm):
    graph = read_file(filename)
    path_lengths = []
    if algorithm.lower() == 'b':
        path_lengths = bellman_ford(graph)
    elif algorithm.lower() == 'f':
        path_lengths = floyd_warshall(graph)
    elif algorithm.lower() == 'both':
        start = time.time()
        bellman_ford(graph)
        bf_time = time.time() - start
        start = time.time()
        floyd_warshall(graph)
        fw_time = time.time() - start
        print(f"Bellman-Ford timing: {bf_time:.6f} seconds")
        print(f"Floyd-Warshall timing: {fw_time:.6f} seconds")
    write_file(path_lengths, filename)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b|both> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])