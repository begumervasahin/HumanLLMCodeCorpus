import argparse
import re
import sys
import time
import math
import cProfile
graph_re = re.compile(r"(\d+)\s(\d+)")
edge_re = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
pr = cProfile.Profile()
def bellman_ford(graph):
    vertices, edge_weights = graph
    path_pairs = []
    edges = []
    num_vertices = len(vertices)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if not math.isinf(float(edge_weights[i][j])):
                edges.append(((i, j), float(edge_weights[i][j])))
    for src in range(num_vertices):
        dist = [float("inf")] * num_vertices
        dist[src] = 0
        for _ in range(num_vertices - 1):
            for (u, v), weight in edges:
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
        for (u, v), weight in edges:
            if dist[v] > dist[u] + weight:
                print("Negative cycle detected")
                return []
        for dest in range(num_vertices):
            path_pairs.append(((src, dest), dist[dest]))
    print(path_pairs)
    return path_pairs
def floyd_warshall(graph):
    vertices, edge_weights = graph
    path_pairs = []
    num_vertices = len(vertices)
    dist_matrix = [row[:] for row in edge_weights]
    for i in range(num_vertices):
        dist_matrix[i][i] = 0
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
    for i in range(num_vertices):
        if dist_matrix[i][i] < 0:
            print("Negative cycle detected")
            return []
    for i in range(num_vertices):
        for j in range(num_vertices):
            path_pairs.append(((i, j), dist_matrix[i][j]))
    print(path_pairs)
    return path_pairs
def read_file(filename):
    global vertices
    global edges
    with open(filename, 'r') as infile:
        first_line = infile.readline()
        graph_match = graph_re.match(first_line)
        if not graph_match:
            print(f"{first_line} not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in infile.readlines():
            edge_match = edge_re.match(line.strip())
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source > num_vertices or sink > num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
                    sys.exit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def matrix_equality(a, b):
    if len(a) != len(b) or not a or not b:
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if value != b[i][j]:
                return False
    return True
def main(filename, algorithm):
    graph = read_file(filename)
    start = time.time()
    if algorithm == 'a':
        print('Running both Bellman-Ford and Floyd-Warshall algorithms')
        bellman_ford(graph)
        floyd_warshall(graph)
    elif algorithm == 'b':
        print('Running Bellman-Ford algorithm')
        bellman_ford(graph)
    elif algorithm == 'f':
        print('Running Floyd-Warshall algorithm')
        floyd_warshall(graph)
    else:
        print("Unknown algorithm selected. Use 'a', 'b', or 'f'.")
    print(f"--- {time.time() - start} seconds ---")
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of vertices in a graph')
    parser.add_argument('--algorithm', default='a', help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ellman-ford only, or (f)loyd-warshall only')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--profile', action='store_true')
    parser.add_argument('filename', metavar='<filename>', help='Input file containing graph')
    args = parser.parse_args()
    if args.profile:
        pr.enable()
    main(args.filename, args.algorithm)
    if args.profile:
        pr.print_stats(sort='time')