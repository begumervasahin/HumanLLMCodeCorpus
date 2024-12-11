from heapq import Heapq
from node import Node
from b14 import Edge
from b16 import TreeSet
import sys
import argparse
import fileinput
import time
b1 = argparse.ArgumentParser(description='Minimum Spanning Tree (MST) Solver')
b1.add_argument("-b8","--heap_d",b2 = 2, type=int, b3="balanced head width")
b1.add_argument("-o","--b18", b3 = "Output file to write solution")
b1.add_argument("-i","--infile", b3 = "Input graph file. Graph must be in DIMACS format")
b4 = b1.parse_args()
b5 = []
b6 = []
b7 = []
b8 = int(b4.heap_d)
b9 = Heapq(b8)
if(b4.infile != None):
    with open(b4.infile) as f:
        for b15 in f:
            if b15[0] == "e":
                b10 = b15.split(" ")
                b11 = int(b10[1].strip())
                b12 = int(b10[2].strip())
                b13 = int(b10[3].strip())
                b14 = Edge(b11, b12, b13)
                b5.append(b14)
                if b11 not in b6:
                    b6.append(b11)
                if b12 not in b6:
                    b6.append(b12)
else:
    print "Enter b14 b15 by b15 in the format e b11 b12 b13. Press enter each time. Press enter twice when done."
    b15 = raw_input("==> ")
    while b15 !="":
        if b15[0] == "e":
            b10 = b15.split(" ")
            b11 = int(b10[1].strip())
            b12 = int(b10[2].strip())
            b13 = int(b10[3].strip())
            b14 = Edge(b11, b12, b13)
            b5.append(b14)
            if b11 not in b6:
                b6.append(b11)
            if b12 not in b6:
                b6.append(b12)
        b15 = raw_input("==> ")
if(len(b6) <= 0):
    print "Error: Invalid number of nodes"
    exit(0)
if(len(b5) <= 0):
    print "Error: Invalid number of b5"
    exit(0)
b9.make_heap(b5)
b16 = TreeSet()
for i in b6:
    b16.make_set(i)
a1 = 0
while b9.size() != 0:
    b17 = b9.find_min()
    if b16.find(b17.b11) != b16.find(b17.b12):
        b16.union(b16.find(b17.b11),b16.find(b17.b12))
        b7.append(b17)
        a1 = b17.weight + a1
    b9.delete_min()
if(b4.b18 = = None):
    print "c Total cost of tree ", a1
    for i in b7:
        print i
else:
    with open(b4.b18,"b13") as f:
        f.write("c Total cost of tree "+ str(a1)+"\n")
        for i in b7:
            f.write(str(i)+"\n")
            f.flush()