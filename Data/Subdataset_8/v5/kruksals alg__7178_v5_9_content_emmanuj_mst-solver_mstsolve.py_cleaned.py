from heapq import Heapq
from node import Node
from edge import Edge
from treeset import TreeSet
import argparse
def read_edges_from_file(infile):
    edges = []
    vertices = set()
    with open(infile) as f:
        for line in f:
            if line.startswith("e"):
                parts = line.split()
                u, v, w = map(int, parts[1:])
                edge = Edge(u, v, w)
                edges.append(edge)
                vertices.add(u)
                vertices.add(v)
    return edges, vertices
def read_edges_from_user_input():
    print("Enter edge line by line in the format e u v w. Press enter each time. Press enter twice when done.")
    edges = []
    vertices = set()
    for line in fileinput.input():
        if not line.strip():
            break
        if line.startswith("e"):
            parts = line.split()
            u, v, w = map(int, parts[1:])
            edge = Edge(u, v, w)
            edges.append(edge)
            vertices.add(u)
            vertices.add(v)
    return edges, vertices
def build_priority_queue(edges):
    p_queue = Heapq(args.heap_d)
    p_queue.make_heap(edges)
    return p_queue
def kruskal_algorithm(p_queue, vertices):
    treeset = TreeSet()
    for vertex in vertices:
        treeset.make_set(vertex)
    blue_edges = []
    min_cost = 0
    while p_queue.size() != 0:
        edge = p_queue.find_min()
        if treeset.find(edge.u) != treeset.find(edge.v):
            treeset.union(treeset.find(edge.u), treeset.find(edge.v))
            blue_edges.append(edge)
            min_cost += edge.weight
        p_queue.delete_min()
    return blue_edges, min_cost
def output_result(blue_edges, min_cost, output_file=None):
    if output_file is None:
        print("c Total cost of tree", min_cost)
        for edge in blue_edges:
            print(edge)
    else:
        with open(output_file, "w") as f:
            f.write("c Total cost of tree " + str(min_cost) + "\n")
            for edge in blue_edges:
                f.write(str(edge) + "\n")
def main():
    parser = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
    parser.add_argument("-d", "--heap_d", default=2, type=int, help="balanced head width")
    parser.add_argument("-o", "--output", help="Output file to write solution")
    parser.add_argument("-i", "--infile", help="Input graph file. Graph must be in DIMACS format")
    args = parser.parse_args()
    if args.infile:
        edges, vertices = read_edges_from_file(args.infile)
    else:
        edges, vertices = read_edges_from_user_input()
    if not vertices:
        print("Error: Invalid number of nodes")
        return
    if not edges:
        print("Error: Invalid number of edges")
        return
    p_queue = build_priority_queue(edges)
    blue_edges, min_cost = kruskal_algorithm(p_queue, vertices)
    output_result(blue_edges, min_cost, args.output)
if __name__ == '__main__':
    main()