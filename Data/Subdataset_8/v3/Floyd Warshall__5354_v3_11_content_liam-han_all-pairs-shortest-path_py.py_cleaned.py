import sys
import re
import time
import math
class EdgeNode:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    def __repr__(self):
        return f"(({self.source}, {self.target}), {self.weight})"
GRAPH_REGEX = re.compile(r"(\d+)\s(\d+)")
EDGE_REGEX = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
def bellman_ford(graph):
    path_pairs = []
    edge_list = []
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if not math.isinf(float(graph[1][i][j])):
                edge = EdgeNode(i, j, float(graph[1][i][j]))
                edge_list.append(edge)
    for k in range(len(vertices)):
        distances = [float("inf")] * len(vertices)
        distances[k] = 0
        for _ in range(len(vertices) - 1):
            for edge in edge_list:
                if distances[edge.target] > distances[edge.source] + edge.weight:
                    distances[edge.target] = distances[edge.source] + edge.weight
        for edge in edge_list:
            if distances[edge.target] > distances[edge.source] + edge.weight:
                print("There is a negative cycle")
                return
        for i in range(len(graph[0])):
            path = EdgeNode(k, i, distances[i])
            path_pairs.append(path)
    return path_pairs
def floyd_warshall(graph):
    path_pairs = []
    distances = []
    for i in range(len(graph[0])):
        row = []
        for j in range(len(graph[0])):
            row.append(float(edges[i][j]))
        distances.append(row)
        distances[i][i] = 0
    for k in range(len(graph[0])):
        for i in range(len(graph[0])):
            for j in range(len(graph[0])):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    for i in range(len(graph[0])):
        for j in range(len(graph[0])):
            path = EdgeNode(i, j, distances[i][j])
            path_pairs.append(path)
    return path_pairs
def read_file(filename):
    global vertices, edges
    with open(filename, 'r') as file:
        line1 = file.readline()
        graph_match = GRAPH_REGEX.match(line1)
        if not graph_match:
            print(line1 + " not properly formatted")
            return [], []
        vertices = list(range(int(graph_match.group(1))))
        edges = [[float("inf")] * len(vertices) for _ in range(len(vertices))]
        for line in file.readlines():
            edge_match = EDGE_REGEX.match(line.strip())
            if edge_match:
                source, sink, weight = map(int, edge_match.groups())
                if source > len(vertices) or sink > len(vertices):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(vertices)} vertices")
                    return [], []
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def main(filename, algorithm):
    algorithm = algorithm.lower()
    graph = read_file(filename)
    if algorithm == 'b':
        bellman_ford(graph)
    elif algorithm == 'f':
        floyd_warshall(graph)
    elif algorithm == 'both':
        start = time.clock()
        bellman_ford(graph)
        end = time.clock()
        bf_time = end - start
        start = time.clock()
        floyd_warshall(graph)
        end = time.clock()
        fw_time = end - start
        print("Bellman-Ford timing:", bf_time)
        print("Floyd-Warshall timing:", fw_time)
    else:
        print("Invalid algorithm option. Please choose 'b', 'f', or 'both'.")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python script.py -<f|b|both> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])