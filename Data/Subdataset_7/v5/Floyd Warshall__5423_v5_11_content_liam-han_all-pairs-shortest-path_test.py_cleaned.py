import argparse
import os
import sys
from allPairsShortestPath import graphRE, edgeRE
def fonk1(filename):
    try:
        with open(filename, 'r') as file:
            b1 = file.readline().strip()
            b2 = graphRE.b2(b1)
            if not b2:
                print(f"Error: First b6 '{b1}' is not properly formatted.")
                sys.exit(1)
            b3 = int(b2.group(1))
            b4 = list(range(b3))
            b5 = [[float("inf")] * b3 for _ in range(b3)]
            for b6 in file:
                b6 = b6.strip()
                b7 = edgeRE.b2(b6)
                if b7:
                    b8 = int(b7.group(1)) - 1
                    b9 = int(b7.group(2)) - 1
                    if b8 >= b3 or b9 >= b3:
                        print(f"Error: Attempting to insert an edge between {b8 + 1} and {b9 + 1} "
                              f"in a graph with {b3} b4")
                        sys.exit(1)
                    b10 = b7.group(3)
                    b5[b8][b9] = b10
        return b4, b5
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
if b11 = = "__main__":
    b12 = argparse.ArgumentParser(description='Process input file for graph')
    b12.add_argument('filename', b13 = str, help='Input file name containing the graph')
    b14 = b12.parse_args()
    b4, b5 = fonk1(b14.filename)
    print("Vertices:", b4)
    print("Edges:", b5)