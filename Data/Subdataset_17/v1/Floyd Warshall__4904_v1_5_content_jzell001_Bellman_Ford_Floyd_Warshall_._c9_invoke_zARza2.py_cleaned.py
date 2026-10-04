import sys
import re
import itertools
import time
graphRE = re.compile(r"(\d+)\s(\d+)")
edgeRE = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
def bellman_ford(graph):
    print("\nEntered BellmanFord")
    vertices, edges = graph
    V = vertices
    E = edges
    inf = float('inf')
    dist = [inf] * len(V)
    dist[0] = 0
    for _ in range(len(V) - 1):
        for u, v in itertools.permutations(V, 2):
            if dist[v] > dist[u] + float(E[u][v]):
                dist[v] = dist[u] + float(E[u][v])
    for u, v in itertools.permutations(V, 2):
        if dist[v] > dist[u] + float(E[u][v]):
            print("A negative cycle exists")
            return 'NULL'
    print("No negative cycles exist")
    return dist
def floyd_warshall(graph):
    print("\nEntered FloydWarshall")
    vertices, edges = graph
    dist = edges
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def read_file(filename):
    global vertices
    global edges
    with open(filename, 'r') as inFile:
        first_line = inFile.readline()
        graphMatch = graphRE.match(first_line)
        if not graphMatch:
            print(first_line + " not properly formatted")
            sys.exit(1)
        num_vertices = int(graphMatch.group(1))
        vertices = list(range(num_vertices))
        edges = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for line in inFile:
            line = line.strip()
            edgeMatch = edgeRE.match(line)
            if edgeMatch:
                source = int(edgeMatch.group(1))
                sink = int(edgeMatch.group(2))
                weight = int(edgeMatch.group(3))
                edges[source][sink] = weight
    print("\nvertex    edges")
    for i in range(len(edges)):
        print(str(vertices[i]) + "         " + str(edges[i]))
    print("\n")
    return vertices, edges
def main(filename, algorithm):
    G = read_file(filename)
    algorithm = algorithm[1:]
    if algorithm in ('b', 'B'):
        print("\nRunning Bellman-Ford")
        bellman_ford(G)
    elif algorithm in ('f', 'F'):
        print("\nRunning Floyd-Warshall")
        floyd_warshall(G)
    elif algorithm == "both":
        print("\nRunning Both Algorithms")
        start = time.time()
        bellman_ford(G)
        BFTime = time.time() - start
        start = time.time()
        floyd_warshall(G)
        FWTime = time.time() - start
        print(f"Bellman-Ford timing: {BFTime}")
        print(f"Floyd-Warshall timing: {FWTime}")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python bellman_ford.py -<f|b> <input_file>")
        sys.exit(1)
    main(sys.argv[2], sys.argv[1])