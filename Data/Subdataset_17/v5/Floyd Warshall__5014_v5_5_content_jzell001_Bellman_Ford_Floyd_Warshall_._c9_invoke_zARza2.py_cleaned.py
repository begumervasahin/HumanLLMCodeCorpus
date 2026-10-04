import sys
import re
import itertools
import time
graph_pattern = re.compile(r"(\d+)\s(\d+)")
edge_pattern = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def bellman_ford(graph):
    vertices, edges = graph
    num_vertices = len(vertices)
    inf = float('inf')
    dist = [inf] * num_vertices
    dist[0] = 0
    for _ in range(num_vertices - 1):
        for u, v in itertools.permutations(vertices, 2):
            if dist[v] > dist[u] + float(edges[u][v]):
                dist[v] = dist[u] + float(edges[u][v])
    for u, v in itertools.permutations(vertices, 2):
        if dist[v] > dist[u] + float(edges[u][v]):
            print("A negative cycle exists")
            return 'NULL'
    print("No negative cycles exist")
    return dist
def floyd_warshall(graph):
    vertices, edges = graph
    dist = [row[:] for row in edges]
    num_vertices = len(vertices)
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def read_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        graph_match = graph_pattern.match(first_line)
        if not graph_match:
            print(f"{first_line} not properly formatted")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for line in file:
            line = line.strip()
            edge_match = edge_pattern.match(line)
            if edge_match:
                source = int(edge_match.group(1))
                sink = int(edge_match.group(2))
                weight = int(edge_match.group(3))
                edges[source][sink] = weight
    print("\nvertex    edges")
    for i, edge_row in enumerate(edges):
        print(f"{vertices[i]}         {edge_row}")
    print()
    return vertices, edges
def main(filename, algorithm):
    graph = read_file(filename)
    algorithm = algorithm[1:].lower()
    if algorithm == 'b':
        print("\nRunning Bellman-Ford")
        result = bellman_ford(graph)
        print(f"Result: {result}")
    elif algorithm == 'f':
        print("\nRunning Floyd-Warshall")
        result = floyd_warshall(graph)
        print(f"Result: {result}")
    elif algorithm == "both":
        print("\nRunning Both Algorithms")
        start = time.time()
        bellman_ford(graph)
        bf_time = time.time() - start
        start = time.time()
        floyd_warshall(graph)
        fw_time = time.time() - start
        print(f"Bellman-Ford timing: {bf_time:.6f} seconds")
        print(f"Floyd-Warshall timing: {fw_time:.6f} seconds")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])