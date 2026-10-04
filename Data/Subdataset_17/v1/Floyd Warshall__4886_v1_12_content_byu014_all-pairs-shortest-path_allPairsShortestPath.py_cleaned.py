import argparse
import os
import re
import sys
import timeit
GRAPH_RE = re.compile(r"(\d+)\s(\d+)")
EDGE_RE = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def bellman_ford(graph):
    vertices, edges = graph
    path_pairs = []
    for source in range(len(vertices)):
        distances = [float("inf")] * len(vertices)
        distances[source] = 0.0
        for _ in range(len(vertices) - 1):
            for current in range(len(vertices)):
                for other_vertex in range(len(edges[current])):
                    if distances[other_vertex] > distances[current] + edges[current][other_vertex]:
                        distances[other_vertex] = distances[current] + edges[current][other_vertex]
        for current in range(len(vertices)):
            for other_vertex in range(len(edges[current])):
                if distances[other_vertex] > distances[current] + edges[current][other_vertex]:
                    return path_pairs, False
        path_pairs.append(distances)
    return path_pairs, True
def floyd_warshall(graph):
    vertices, edges = graph
    dist = [row[:] for row in edges]
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def read_file(filename):
    with open(filename, 'r') as infile:
        first_line = infile.readline().strip()
        graph_match = GRAPH_RE.match(first_line)
        if not graph_match:
            print(f"{first_line} not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in infile:
            edge_match = EDGE_RE.match(line.strip())
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source >= num_vertices or sink >= num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
                    sys.exit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def matrix_equality(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            if a[i][j] != b[i][j]:
                return False
    return True
def main(filename, algorithm):
    graph = read_file(filename)
    path_pairs = []
    no_cycle = True
    if algorithm in ('b', 'B'):
        start_timer = timeit.default_timer()
        path_pairs, no_cycle = bellman_ford(graph)
        stop_timer = timeit.default_timer()
        print(f"Bellman-Ford Time: {stop_timer - start_timer:.6f} seconds")
    elif algorithm in ('f', 'F'):
        start_timer = timeit.default_timer()
        path_pairs = floyd_warshall(graph)
        stop_timer = timeit.default_timer()
        print(f"Floyd-Warshall Time: {stop_timer - start_timer:.6f} seconds")
    elif algorithm == 'a':
        print('Running both Bellman-Ford and Floyd-Warshall algorithms')
        path_pairs_bellman, no_cycle = bellman_ford(graph)
        path_pairs_floyd = floyd_warshall(graph)
        if not matrix_equality(path_pairs_bellman, path_pairs_floyd) or not no_cycle:
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
        path_pairs = path_pairs_bellman
    output_file = os.path.splitext(filename)[0] + '_shortestPaths.txt'
    with open(output_file, 'w') as outfile:
        if not no_cycle:
            outfile.write("Negative Cycle Detected\n")
        for row in path_pairs:
            outfile.write(' '.join(map(str, row)) + '\n')
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of vertices in a graph')
    parser.add_argument('--algorithm', default='a', help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--profile', action='store_true')
    parser.add_argument('filename', metavar='<filename>', help='Input file containing graph')
    args = parser.parse_args()
    main(args.filename, args.algorithm)