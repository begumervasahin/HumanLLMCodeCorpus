import sys
import re
import itertools
import time
GRAPH_PATTERN = re.compile(r"(\d+)\s(\d+)")
EDGE_PATTERN = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def bellman_ford(graph):
    vertices, edges = graph
    num_vertices = len(vertices)
    inf = float('inf')
    path_pairs = []
    for i in range(num_vertices):
        dist = [inf] * num_vertices
        dist[i] = 0
        for _ in range(num_vertices - 1):
            for u, v in itertools.permutations(vertices, 2):
                if dist[v] > dist[u] + float(edges[u][v]):
                    dist[v] = dist[u] + float(edges[u][v])
        neg_cycle = False
        for u, v in itertools.permutations(vertices, 2):
            if dist[v] > dist[u] + float(edges[u][v]):
                neg_cycle = True
        for j in range(num_vertices):
            if dist[j] != inf:
                dist[j] = int(dist[j])
            path_pairs.append(((str(i), str(j)), str(dist[j])))
    if neg_cycle:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    return path_pairs
def floyd_warshall(graph):
    vertices, edges = graph
    num_vertices = len(vertices)
    dist = [[float(edges[i][j]) for j in range(num_vertices)] for i in range(num_vertices)]
    for v in vertices:
        dist[v][v] = 0
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    path_pairs = []
    for i in vertices:
        for j in vertices:
            if dist[i][j] != float('inf'):
                dist[i][j] = int(dist[i][j])
            path_pairs.append(((str(i), str(j)), str(dist[i][j])))
    return path_pairs
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
        start = time.time()
        result = bellman_ford(graph)
        end = time.time()
        print(f"\nBellman-Ford timing: {end - start:.6f} seconds")
        print(f"Result: {result}")
    elif algorithm == 'f':
        start = time.time()
        result = floyd_warshall(graph)
        end = time.time()
        print(f"\nFloyd-Warshall timing: {end - start:.6f} seconds")
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
        print("Usage: python bellman_ford.py -<f|b|both> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])