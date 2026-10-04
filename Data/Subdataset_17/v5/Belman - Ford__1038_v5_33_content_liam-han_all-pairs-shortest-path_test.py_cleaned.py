import argparse
import os
import re
import sys
GRAPH_REGEX = re.compile(r'(\d+)')
EDGE_REGEX = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def read_file(filename):
    with open(filename, 'r') as infile:
        line1 = infile.readline().strip()
        graph_match = GRAPH_REGEX.match(line1)
        if not graph_match:
            print(f"{line1} not properly formatted")
            sys.exit(1)
        vertices_count = int(graph_match.group(1))
        vertices = list(range(vertices_count))
        edges = [[float("inf")] * vertices_count for _ in range(vertices_count)]
        for line in infile:
            line = line.strip()
            edge_match = EDGE_REGEX.match(line)
            if edge_match:
                source = int(edge_match.group(1))
                sink = int(edge_match.group(2))
                weight = float(edge_match.group(3))
                if source > vertices_count or sink > vertices_count:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {vertices_count} vertices")
                    sys.exit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def print_graph(vertices, edges):
    print("Vertices:", vertices)
    print("Edges:")
    for row in edges:
        print(row)
def main():
    parser = argparse.ArgumentParser(description="Read a graph from a file and construct its representation.")
    parser.add_argument("filename", type=str, help="The file containing the graph definition.")
    args = parser.parse_args()
    filename = args.filename
    if not os.path.isfile(filename):
        print(f"File {filename} does not exist.")
        sys.exit(1)
    vertices, edges = read_file(filename)
    print_graph(vertices, edges)
if __name__ == "__main__":
    main()