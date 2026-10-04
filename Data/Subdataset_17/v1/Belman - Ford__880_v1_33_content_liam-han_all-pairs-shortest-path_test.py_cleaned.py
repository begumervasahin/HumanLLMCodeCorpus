import argparse
import os
import re
import sys
import time
from allPairsShortestPath import graphRE, edgeRE
def readFile(filename):
    global vertices
    global edges
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)-1][int(sink)-1]=weight
    G = (vertices,edges)
    return (vertices,edges)
 Please compose a Python script that replicates the functionality described above q
import argparse
import os
import re
import sys
graphRE = re.compile(r'(\d+)')
edgeRE = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def read_file(filename):
    with open(filename, 'r') as infile:
        line1 = infile.readline().strip()
        graph_match = graphRE.match(line1)
        if not graph_match:
            print(f"{line1} not properly formatted")
            sys.exit(1)
        vertices_count = int(graph_match.group(1))
        vertices = list(range(vertices_count))
        edges = [[float("inf")] * vertices_count for _ in range(vertices_count)]
        for line in infile:
            line = line.strip()
            edge_match = edgeRE.match(line)
            if edge_match:
                source = int(edge_match.group(1))
                sink = int(edge_match.group(2))
                weight = float(edge_match.group(3))
                if source > vertices_count or sink > vertices_count:
                    print(f"Attempting to insert an edge between {source} and {sink} in a graph with {vertices_count} vertices")
                    sys.exit(1)
                edges[source - 1][sink - 1] = weight
    return vertices, edges
def main():
    parser = argparse.ArgumentParser(description="Read a graph from a file and construct its representation.")
    parser.add_argument("filename", type=str, help="The file containing the graph definition.")
    args = parser.parse_args()
    if not os.path.isfile(args.filename):
        print(f"File {args.filename} does not exist.")
        sys.exit(1)
    vertices, edges = read_file(args.filename)
    print("Vertices:", vertices)
    print("Edges:")
    for row in edges:
        print(row)
if __name__ == "__main__":
    main()