import argparse
import os
import re
import sys
import cProfile
import pstats
import io
parser = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of vertices in a graph')
parser.add_argument('--algorithm', default='a',
                    help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('--profile', action='store_true')
parser.add_argument('filename', metavar='<filename>', help='Input file containing graph')
graphRE = re.compile(r"(\d+)\s(\d+)")
edgeRE = re.compile(r"(\d+)\s(\\d+)\s(-?\d+)")
vertices = []
edges = []
def bellman_ford(graph):
    path_pairs = []
    num_vertices = len(vertices)
    for j in vertices:
        dist = [float("inf")] * num_vertices
        dist[j] = 0
        for _ in range(num_vertices - 1):
            for V in range(num_vertices):
                for U in range(num_vertices):
                    weight = float(edges[V][U])
                    if dist[V] != float("inf") and dist[V] + weight < dist[U]:
                        dist[U] = dist[V] + weight
        path_pairs.append(dist)
    for j in vertices:
        if path_pairs[j][j] < 0:
            return [[0, 0]]
    return path_pairs
def floyd_warshall(graph):
    num_vertices = len(vertices)
    dist = [[float("inf")] * num_vertices for _ in range(num_vertices)]
    for V in range(num_vertices):
        for U in range(num_vertices):
            dist[U][V] = float(edges[U][V])
        dist[V][V] = 0
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for j in vertices:
        if dist[j][j] < 0:
            return [[0, 0]]
    return dist
def read_file(filename):
    global vertices, edges
    with open(filename, 'r') as infile:
        line1 = infile.readline().strip()
        graph_match = graphRE.match(line1)
        if not graph_match:
            print(f"{line1} not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in infile:
            line = line.strip()
            edge_match = edgeRE.match(line)
            if edge_match:
                source, sink, weight = int(edge_match.group(1)), int(edge_match.group(2)), float(edge_match.group(3))
                if source > num_vertices or sink > num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
                    sys.exit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def matrix_equality(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] != b[i][j]:
                return False
    return True
def main(filename, algorithm):
    graph = read_file(filename)
    path_pairs = []
    if algorithm in ['b', 'B']:
        if args.profile:
            pr = cProfile.Profile()
            pr.enable()
        path_pairs = bellman_ford(graph)
        if args.profile:
            pr.disable()
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
    elif algorithm in ['f', 'F']:
        if args.profile:
            pr = cProfile.Profile()
            pr.enable()
        path_pairs = floyd_warshall(graph)
        if args.profile:
            pr.disable()
            s = io.StringIO()
            sortby = 'cumulative'
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats()
            print(s.getvalue())
    elif algorithm == 'a':
        print('Running both algorithms')
        path_pairs_bellman = bellman_ford(graph)
        path_pairs_floyd = floyd_warshall(graph)
        if not matrix_equality(path_pairs_bellman, path_pairs_floyd):
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
        path_pairs = path_pairs_bellman
    with open(os.path.splitext(filename)[0] + '_shortestPaths.txt', 'w') as f:
        for row in path_pairs:
            f.write(' '.join(map(str, row)) + '\n')
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.filename, args.algorithm)