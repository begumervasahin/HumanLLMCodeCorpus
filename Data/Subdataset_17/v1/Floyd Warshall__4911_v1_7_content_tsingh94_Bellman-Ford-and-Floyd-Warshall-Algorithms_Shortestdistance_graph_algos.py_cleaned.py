import os
import re
import sys
import time
import math
GRAPH_PATTERN = re.compile(r"(\d+)\s(\d+)")
EDGE_PATTERN = re.compile(r"(\d+)\s(\d+)\s(\d+)")
def change_edge_matrix(edges):
    for v in range(len(edges)):
        for e in range(len(edges[v])):
            if isinstance(edges[v][e], str):
                edges[v][e] = int(edges[v][e])
    return edges
def bellman_ford(graph):
    vertices, edges = graph
    path_pairs = []
    val_infinity = float('inf')
    edges = change_edge_matrix(edges)
    for src in range(len(vertices)):
        dist = [val_infinity] * len(vertices)
        dist[src] = 0
        for _ in range(len(vertices) - 1):
            for u in range(len(vertices)):
                for v in range(len(vertices)):
                    if edges[u][v] != val_infinity and dist[u] != val_infinity:
                        if dist[v] > dist[u] + edges[u][v]:
                            dist[v] = dist[u] + edges[u][v]
        path_pairs.append(dist)
    return path_pairs
def floyd_warshall(graph):
    vertices, edges = graph
    dist = change_edge_matrix(edges)
    num_vertices = len(vertices)
    for i in range(num_vertices):
        dist[i][i] = 0
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
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
        edges = [[float('inf')] * num_vertices for _ in range(num_vertices)]
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
    with open(output_filename, 'w') as out_file:
        for row in length_matrix:
            out_file.write(','.join(map(str, row)) + '\n')
def main(filename, algorithm):
    graph = read_file(filename)
    path_lengths = []
    if algorithm.lower() == 'b':
        start = time.time()
        path_lengths = bellman_ford(graph)
        end = time.time()
        print(f"Bellman-Ford timing: {end - start:.6f} seconds")
    elif algorithm.lower() == 'f':
        start = time.time()
        path_lengths = floyd_warshall(graph)
        end = time.time()
        print(f"Floyd-Warshall timing: {end - start:.6f} seconds")
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