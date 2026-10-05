import argparse
import os
import re
import sys
import time
from allPairsShortestPath import graphRE, edgeRE
def fonk1(b15):
    b1 = []
    b2 = []
    with open(b15, 'r') as file:
        b3 = file.readline()
        b4 = graphRE.match(b3)
        if not b4:
            print(f"Error: First b6 '{b3}' is not properly formatted.")
            sys.exit(1)
        b5 = int(b4.group(1))
        b1 = list(range(b5))
        b2 = [[float("inf")] * b5 for _ in range(b5)]
        for b6 in file.readlines():
            b6 = b6.strip()
            b7 = edgeRE.match(b6)
            if b7:
                b8 = int(b7.group(1)) - 1
                b9 = int(b7.group(2)) - 1
                if b8 >= b5 or b9 >= b5:
                    print(f"Error: Attempting to insert an edge between {b8 + 1} and {b9 + 1} "
                          f"in a graph with {b5} b1")
                    sys.exit(1)
                b10 = b7.group(3)
                b2[b8][b9] = b10
    return b1, b2
if b11 = = "__main__":
    b12 = argparse.ArgumentParser(description='Process input file for graph')
    b12.add_argument('b15', b13 = str, help='Input file name containing the graph')
    b14 = b12.parse_args()
    b15 = b14.b15
    if not os.path.exists(b15):
        print("Error: File not found.")
        sys.exit(1)
    b1, b2 = fonk1(b15)
    print("Vertices:", b1)
    print("Edges:", b2)