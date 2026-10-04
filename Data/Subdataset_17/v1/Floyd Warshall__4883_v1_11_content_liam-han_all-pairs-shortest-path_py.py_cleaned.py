import sys
import re
import time
import math
graph_re = re.compile(r"(\d+)\s(\d+)")
edge_re = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
class EdgeNode:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    def __repr__(self):
        return f"(({self.u}, {self.v}), {self.w})"
def neg_cycle_floyd_warshall(graph):
    dist = [[0 for _ in range(len(vertices) + 1)] for _ in range(len(vertices) + 1)]
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            dist[i][j] = graph[i][j]
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(len(vertices)):
        if dist[i][i] < 0:
            return True
    return False
def bellman_ford(graph):
    path_pairs = []
    edge_list = []
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if not math.isinf(float(graph[1][i][j])):
                edge_list.append(EdgeNode(i, j, float(graph[1][i][j])))
    for k in range(len(vertices)):
        dist = [float("inf")] * len(vertices)
        dist[k] = 0
        for _ in range(len(vertices) - 1):
            for edge in edge_list:
                if dist[edge.v] > dist[edge.u] + edge.w:
                    dist[edge.v] = dist[edge.u] + edge.w
        for edge in edge_list:
            if dist[edge.v] > dist[edge.u] + edge.w:
                print("There is a negative cycle")
                return 0
        for i in range(len(graph[0])):
            path_pairs.append(EdgeNode(k, i, dist[i]))
    return path_pairs
def floyd_warshall(graph):
    path_pairs = []
    dist = [[float(graph[1][i][j]) for j in range(len(graph[0]))] for i in range(len(graph[0]))]
    for i in range(len(graph[0])):
        dist[i][i] = 0
    for k in range(len(graph[0])):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
            path_pairs.append(EdgeNode(i, j, dist[i][j]))
    return path_pairs
def read_file(filename):
    global vertices
    global edges
    with open(filename, 'r') as infile:
        first_line = infile.readline()
        graph_match = graph_re.match(first_line)
        if not graph_match:
            print(f"{first_line} not properly formatted")
            quit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in infile.readlines():
            edge_match = edge_re.match(line.strip())
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source > num_vertices or sink > num_vertices:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {num_vertices} vertices")
                    quit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def main(filename, algorithm):
    graph = read_file(filename)
    algorithm = algorithm[1:].lower()
    if algorithm == 'b':
        bellman_ford(graph)
    elif algorithm == 'f':
        floyd_warshall(graph)
    elif algorithm == 'both':
        start = time.perf_counter()
        print(bellman_ford(graph))
        end = time.perf_counter()
        print(f"Bellman-Ford timing: {end - start:.6f} seconds")
        start = time.perf_counter()
        floyd_warshall(graph)
        end = time.perf_counter()
        print(f"Floyd-Warshall timing: {end - start:.6f} seconds")
    else:
        print("Unknown algorithm selected. Use '-b' for Bellman-Ford, '-f' for Floyd-Warshall, or '-both' for both.")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py -<f|b|both> <input_file>")
        quit(1)
    main(sys.argv[2], sys.argv[1])