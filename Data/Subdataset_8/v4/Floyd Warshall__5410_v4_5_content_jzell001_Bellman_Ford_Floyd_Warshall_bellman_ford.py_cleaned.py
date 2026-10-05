import sys
import re
import time
import itertools
graph_re = re.compile(r"(\d+)\s(\d+)")
edge_re = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
def bellman_ford(graph):
    path_pairs = []
    print("\nEntered Bellman-Ford")
    V, E = graph
    permutations = list(itertools.permutations(V, 2))
    inf = float('inf')
    for index in range(len(V)):
        dist = [inf] * len(V)
        source = V[index]
        dist[source] = 0
        for _ in range(1, len(V)):
            for i in range(len(permutations)):
                u, v = permutations[i]
                if dist[v] > dist[u] + float(E[u][v]):
                    dist[v] = dist[u] + float(E[u][v])
        neg_cycle = False
        for i in range(len(permutations)):
            u, v = permutations[i]
            if dist[v] > dist[u] + float(E[u][v]):
                neg_cycle = True
        for i in range(len(V)):
            if dist[i] != float('inf'):
                dist[i] = int(dist[i])
            new = ((str(source), str(V[i])), str(dist[i]))
            path_pairs.append(new)
    print("\npathPairs")
    print(path_pairs)
    if neg_cycle:
        print("\nNote: A negative cycle exists")
    else:
        print("\nNote: No negative cycles exist")
    print("\nExiting Bellman-Ford\n")
    return path_pairs
def floyd_warshall(graph):
    path_pairs = []
    print("\nEntered Floyd-Warshall")
    V, E = graph
    inf = float('inf')
    dist = E
    for i in V:
        for j in V:
            dist[i][j] = float(dist[i][j])
    for v in V:
        dist[v][v] = 0
    for k in V:
        for i in V:
            for j in V:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in V:
        for j in V:
            if dist[i][j] != float('inf'):
                dist[i][j] = int(dist[i][j])
            new = ((str(i), str(j)), str(dist[i][j]))
            path_pairs.append(new)
    print("\npathPairs")
    print(path_pairs)
    print("\nExiting Floyd-Warshall\n")
    return path_pairs
def read_file(filename):
    global vertices, edges
    infile = open(filename, 'r')
    line1 = infile.readline().strip()
    graph_match = graph_re.match(line1)
    if not graph_match:
        print(line1 + " not properly formatted")
        quit(1)
    vertices = list(range(int(graph_match.group(1))))
    edges = [[float("inf")] * len(vertices) for _ in range(len(vertices))]
    for line in infile.readlines():
        line = line.strip()
        edge_match = edge_re.match(line)
        if edge_match:
            source = int(edge_match.group(1))
            sink = int(edge_match.group(2))
            if source > len(vertices) or sink > len(vertices):
                print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(vertices)} vertices")
                quit(1)
            weight = edge_match.group(3)
            edges[source][sink] = weight
    print("\nvertex    edges")
    for i in range(len(edges)):
        print(str(vertices[i]) + "         " + str(edges[i]))
    print("")
    return vertices, edges
def main(filename, algorithm):
    algorithm = algorithm[1:]
    G = read_file(filename)
    if algorithm == 'b' or algorithm == 'B':
        start = time.clock()
        bellman_ford(G)
        end = time.clock()
        bf_time = end - start
        print("\nBellman-Ford timing: " + str(bf_time) + "\n")
    if algorithm == 'f' or algorithm == 'F':
        start = time.clock()
        floyd_warshall(G)
        end = time.clock()
        fw_time = end - start
        print("Floyd-Warshall timing: " + str(fw_time))
    if algorithm == "both":
        start = time.clock()
        bellman_ford(G)
        end = time.clock()
        bf_time = end - start
        print("\nBellman-Ford timing: " + str(bf_time))
        start = time.clock()
        floyd_warshall(G)
        end = time.clock()
        fw_time = end - start
        print("Floyd-Warshall timing: " + str(fw_time) + "\n")
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2], sys.argv[1])