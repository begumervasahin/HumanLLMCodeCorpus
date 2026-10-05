import argparse
import os
import re
import sys
GRAPH_REGEX = re.compile(r'(\d+)')
EDGE_REGEX = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def read_graph_from_file(filename):
    vertices = []
    edges = []
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        match = GRAPH_REGEX.match(first_line)
        if not match:
            print(f"Error: First line '{first_line}' is not properly formatted.")
            sys.exit(1)
        num_vertices = int(match.group(1))
        vertices = list(range(num_vertices))
        edges = [[float("inf")] * num_vertices for _ in range(num_vertices)]
        for line in file:
            line = line.strip()
            edge_match = EDGE_REGEX.match(line)
            if edge_match:
                source = int(edge_match.group(1)) - 1
                sink = int(edge_match.group(2)) - 1
                if source >= num_vertices or sink >= num_vertices:
                    print(f"Error: Attempting to insert an edge between {source + 1} and {sink + 1} "
                          f"in a graph with {num_vertices} vertices")
                    sys.exit(1)
                weight = int(edge_match.group(3))
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
    vertices, edges = read_graph_from_file(filename)
    print("Vertices:", vertices)
    print("Edges:", edges)