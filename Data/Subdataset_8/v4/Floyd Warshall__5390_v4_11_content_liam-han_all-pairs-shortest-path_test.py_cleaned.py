import argparse
import os
import re
import sys
import time
from allPairsShortestPath import graphRE, edgeRE
def read_file(filename):
    vertices = []
    edges = []
    with open(filename, 'r') as file:
        first_line = file.readline()
        graph_match = graphRE.match(first_line)
        if not graph_match:
            print(f"Error: First line '{first_line}' is not properly formatted.")
            sys.exit(1)
        num_vertices = int(graph_match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in file.readlines():
            line = line.strip()
            edge_match = edgeRE.match(line)
            if edge_match:
                source = int(edge_match.group(1)) - 1
                sink = int(edge_match.group(2)) - 1
                if source >= num_vertices or sink >= num_vertices:
                    print(f"Error: Attempting to insert an edge between {source + 1} and {sink + 1} "
                          f"in a graph with {num_vertices} vertices")
                    sys.exit(1)
                weight = edge_match.group(3)
                edges[source][sink] = weight
    return vertices, edges
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process input file for graph')
    parser.add_argument('filename', type=str, help='Input file name containing the graph')
    args = parser.parse_args()
    filename = args.filename
    if not os.path.exists(filename):
        print("Error: File not found.")
        sys.exit(1)
    vertices, edges = read_file(filename)
    print("Vertices:", vertices)
    print("Edges:", edges)