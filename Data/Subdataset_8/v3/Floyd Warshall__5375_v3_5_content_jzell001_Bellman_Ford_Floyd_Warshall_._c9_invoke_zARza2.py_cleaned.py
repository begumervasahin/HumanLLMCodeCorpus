import sys
import re
import time
import itertools
graph_regex = re.compile(r"(\d+)\s(\d+)")
edge_regex = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
def bellman_ford(graph):
    print("\nEntered Bellman-Ford\n")
    vertices, edges = graph
    print("\nV:", vertices)
    print("\nE:", edges)
    print("\nLength of E:", len(edges))
    vertex_permutations = list(itertools.permutations(vertices, 2))
    print("\nPermutations of V:")
    for permutation in vertex_permutations:
        print(permutation)
    print("\n")
    inf = float('inf')
    dist = [inf] * len(vertices)
    dist[0] = 0
    print("\nDist before:")
    print(*dist, sep='\n')
    print("\nLength of vertex_permutations:", len(vertex_permutations))
    print("\nU and V combinations:\n")
    print("|V|:", len(vertices))
    print("\n")
    for j in range(1, len(vertices)):
        print("\n")
        for i in range(len(vertex_permutations)):
            u, v = vertex_permutations[i]
            print("u:", u, "v:", v)
            print("Weight:", edges[u][v])
            print("\n")
            if dist[v] > dist[u] + float(edges[u][v]):
                dist[v] = dist[u] + float(edges[u][v])
    print("\nDist after:")
    print(*dist, sep='\n')
    print("\nChecking if negative cycle exists:")
    neg_cycle = any(dist[v] > dist[u] + float(edges[u][v]) for u, v in vertex_permutations)
    if neg_cycle:
        print("A negative cycle exists")
    else:
        print("No negative cycles exist")
    path_pairs = [(('0', '0'), '0')]
    print(path_pairs)
    print("\nExiting Bellman-Ford")
    return path_pairs
def floyd_warshall(graph):
    path_pairs = []
    return path_pairs
def read_file(filename):
    with open(filename, 'r') as infile:
        line1 = infile.readline().strip()
        graph_match = graph_regex.match(line1)
        if not graph_match:
            print(f"{line1} not properly formatted")
            quit(1)
        vertices = list(range(int(graph_match.group(1))))
        edges = [[float("inf")] * len(vertices) for _ in range(len(vertices))]
        for line in infile.readlines():
            line = line.strip()
            edge_match = edge_regex.match(line)
            if edge_match:
                source = int(edge_match.group(1))
                sink = int(edge_match.group(2))
                if source > len(vertices) or sink > len(vertices):
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {len(vertices)} vertices")
                    quit(1)
                weight = edge_match.group(3)
                edges[source][sink] = weight
    print("\nVertex    Edges")
    for i in range(len(edges)):
        print(f"{vertices[i]}         {edges[i]}")
    print("\n")
    return vertices, edges
def main(filename, algorithm):
    algorithm = algorithm[1:]
    graph = read_file(filename)
    print("\nAlgorithm:", algorithm)
    if algorithm == 'b' or algorithm == 'B':
        print("\nAbout to call Bellman-Ford")
        bellman_ford(graph)
        print("\nCalled Bellman-Ford\n")
    if algorithm == 'f' or algorithm == 'F':
        floyd_warshall(graph)
    if algorithm == "both":
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
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2], sys.argv[1])