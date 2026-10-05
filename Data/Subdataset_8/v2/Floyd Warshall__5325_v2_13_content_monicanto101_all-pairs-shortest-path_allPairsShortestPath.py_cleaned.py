import argparse
import os
import re
import cProfile
import pstats
import io
parser = argparse.ArgumentParser(description='Calculate the shortest path between all pairs of vertices in a graph')
parser.add_argument('--algorithm', default='a', help='Algorithm: Select the algorithm to run, default is all. (a)ll, (b)ellman-ford only or (f)loyd-warshall only')
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('--profile', action='store_true')
parser.add_argument('filename', metavar='<filename>', help='Input file containing graph')
graphRE = re.compile(r"(\d+)\s(\d+)")
edgeRE = re.compile(r"(\d+)\s(\d+)\s(-?\d+)")
vertices = []
edges = []
def BellmanFord(G):
    pathPairs = []
    numVertices = len(vertices)
    for j in vertices:
        dist = [float("inf")] * numVertices
        dist[j] = 0
        for _ in range(0, len(vertices) - 1):
            for V in range(0, len(vertices)):
                for U in range(0, len(edges)):
                    w = float(edges[V][U])
                    tempDist = dist[V] + w
                    if tempDist < dist[U]:
                        dist[U] = tempDist
        pathPairs.append(dist)
    for j in vertices:
        if pathPairs[j][j] < 0:
            return [[0, 0]]
    print('BellmanFord algorithm is incomplete')
    return pathPairs
def FloydWarshall(G):
    pathPairs = []
    numVertices = len(vertices)
    dist = [[float("inf")] * numVertices for _ in vertices]
    for V in range(0, len(vertices)):
        for U in range(0, len(edges)):
            dist[U][V] = float(edges[U][V])
        dist[V][V] = 0
    for k in range(0, len(vertices)):
        for i in range(0, len(vertices)):
            for j in range(0, len(vertices)):
                temp = dist[i][k] + dist[k][j]
                if dist[i][j] > temp:
                    dist[i][j] = temp
    for j in vertices:
        if dist[j][j] < 0:
            return [[0, 0]]
    pathPairs = dist
    print('FloydWarshall algorithm is incomplete')
    return pathPairs
def readFile(filename):
    global vertices, edges
    with open(filename, 'r') as inFile:
        line1 = inFile.readline()
        graphMatch = graphRE.match(line1)
        if not graphMatch:
            print(line1 + " not properly formatted")
            quit(1)
        vertices = list(range(int(graphMatch.group(1))))
        edges = [[float("inf")] * len(vertices) for _ in vertices]
        for line in inFile.readlines():
            line = line.strip()
            edgeMatch = edgeRE.match(line)
            if edgeMatch:
                source, sink, weight = map(int, edgeMatch.groups())
                if source > len(vertices) or sink > len(vertices):
                    print("Attempting to insert an edge between " + str(source) + " and " + str(sink) + " in a graph with " + str(len(vertices)) + " vertices")
                    quit(1)
                edges[source - 1][sink - 1] = weight
    return (vertices, edges)
def matrixEquality(a, b):
    if len(a) == 0 or len(b) == 0 or len(a) != len(b): return False
    if len(a[0]) != len(b[0]): return False
    for i, row in enumerate(a):
        for j, value in enumerate(b):
            if a[i][j] != b[i][j]:
                return False
    return True
def main(filename, algorithm):
    G = readFile(filename)
    pathPairs = []
    if algorithm.lower() == 'b':
        pr = cProfile.Profile()
        pr.enable()
        pathPairs = BellmanFord(G)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
    elif algorithm.lower() == 'f':
        pr = cProfile.Profile()
        pr.enable()
        pathPairsFloyd = FloydWarshall(G)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
    elif algorithm.lower() == 'a':
        print('running both')
        pathPairsBellman = BellmanFord(G)
        pathPairsFloyd = FloydWarshall(G)
        pathPairs = pathPairsBellman
        if not matrixEquality(pathPairsBellman, pathPairsFloyd):
            print('Floyd-Warshall and Bellman-Ford did not produce the same result')
    with open(os.path.splitext(filename)[0] + '_shortestPaths.txt', 'w') as f:
        for row in pathPairs:
            f.write(' '.join(map(str, row)) + '\n')
if __name__ == '__main__':
    args = parser.parse_args()
    main(args.filename, args.algorithm)