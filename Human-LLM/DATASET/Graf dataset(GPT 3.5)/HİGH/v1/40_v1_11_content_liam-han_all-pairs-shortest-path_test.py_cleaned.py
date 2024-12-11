import argparse
import os
import re
import sys
import time
b1 = re.compile(r'(\d+)')
b2 = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def fonk1(b18):
    b3 = []
    b4 = []
    b5 = open(b18, 'r')
    b6 = b5.readline()
    b7 = b1.match(b6)
    if not b7:
        print(b6 + " not properly formatted")
        quit(1)
    b8 = int(b7.group(1))
    b3 = list(range(b8))
    b4 = [[float("inf")] * b8 for _ in range(b8)]
    for b9 in b5.readlines():
        b9 = b9.strip()
        b10 = b2.match(b9)
        if b10:
            b11 = int(b10.group(1)) - 1
            b12 = int(b10.group(2)) - 1
            if b11 >= b8 or b12 >= b8:
                print(f"Attempting to insert an edge between {b11 + 1} and {b12 + 1} in a graph with {b8} b3")
                quit(1)
            b13 = int(b10.group(3))
            b4[b11][b12] = b13
    return (b3, b4)
if b14 = = "__main__":
    b15 = argparse.ArgumentParser(description='Process input file for graph')
    b15.add_argument('b18', b16 = str, help='Input file name containing the graph')
    b17 = b15.parse_args()
    b18 = b17.b18
    if not os.path.exists(b18):
        print("File not found.")
        sys.exit(1)
    b3, b4 = fonk1(b18)
    print("Vertices:", b3)
    print("Edges:", b4)