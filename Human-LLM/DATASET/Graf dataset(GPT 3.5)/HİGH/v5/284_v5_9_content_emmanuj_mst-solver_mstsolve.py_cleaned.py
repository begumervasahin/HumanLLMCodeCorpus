from heapq import Heapq
from node import Node
from b5 import Edge
from b7 import TreeSet
import argparse
def fonk1(infile):
    b1 = []
    b2 = set()
    with open(infile) as f:
        for line in f:
            if line.startswith("e"):
                b3 = line.split()
                u, v, b4 = map(int, b3[1:])
                b5 = Edge(u, v, b4)
                b1.append(b5)
                b2.add(u)
                b2.add(v)
    return b1, b2
def fonk2():
    print("Enter b5 line by line in the format e u v b4. Press enter each time. Press enter twice when done.")
    b1 = []
    b2 = set()
    for line in fileinput.input():
        if not line.strip():
            break
        if line.startswith("e"):
            b3 = line.split()
            u, v, b4 = map(int, b3[1:])
            b5 = Edge(u, v, b4)
            b1.append(b5)
            b2.add(u)
            b2.add(v)
    return b1, b2
def fonk3(b1):
    b6 = Heapq(b13.heap_d)
    b6.make_heap(b1)
    return b6
def fonk4(b6, b2):
    b7 = TreeSet()
    for vertex in b2:
        b7.make_set(vertex)
    b8 = []
    a1 = 0
    while b6.size() != 0:
        b5 = b6.find_min()
        if b7.find(b5.u) != b7.find(b5.v):
            b7.union(b7.find(b5.u), b7.find(b5.v))
            b8.append(b5)
            a1 += b5.weight
        b6.delete_min()
    return b8, a1
def fonk5(b8, a1, b9 = None):
    if b9 is None:
        print("c Total cost of tree", a1)
        for b5 in b8:
            print(b5)
    else:
        with open(b9, "b4") as f:
            f.write("c Total cost of tree " + str(a1) + "\n")
            for b5 in b8:
                f.write(str(b5) + "\n")
def fonk6():
    b10 = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
    b10.add_argument("-d", "--heap_d", b11 = 2, type=int, b12="balanced head width")
    b10.add_argument("-o", "--output", b12 = "Output file to write solution")
    b10.add_argument("-i", "--infile", b12 = "Input graph file. Graph must be in DIMACS format")
    b13 = b10.parse_args()
    if b13.infile:
        b1, b2 = fonk1(b13.infile)
    else:
        b1, b2 = fonk2()
    if not b2:
        print("Error: Invalid number of nodes")
        return
    if not b1:
        print("Error: Invalid number of b1")
        return
    b6 = fonk3(b1)
    b8, a1 = fonk4(b6, b2)
    fonk5(b8, a1, b13.output)
if b14 = = '__main__':
    fonk6()