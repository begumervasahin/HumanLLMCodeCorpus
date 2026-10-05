import argparse
import os
import re
import sys
b1 = re.compile(r'(\d+)')
b2 = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def fonk1(b17):
    b3 = []
    b4 = []
    with open(b17, 'r') as file:
        b5 = file.readline().strip()
        b6 = b1.b6(b5)
        if not b6:
            print(f"Error: First b8 '{b5}' is not properly formatted.")
            sys.exit(1)
        b7 = int(b6.group(1))
        b3 = list(range(b7))
        b4 = [[float("inf")] * b7 for _ in range(b7)]
        for b8 in file:
            b8 = b8.strip()
            b9 = b2.b6(b8)
            if b9:
                b10 = int(b9.group(1)) - 1
                b11 = int(b9.group(2)) - 1
                if b10 >= b7 or b11 >= b7:
                    print(f"Error: Attempting to insert an edge between {b10 + 1} and {b11 + 1} "
                          f"in a graph with {b7} b3")
                    sys.exit(1)
                b12 = int(b9.group(3))
                b4[b10][b11] = b12
    return b3, b4
if b13 = = "__main__":
    b14 = argparse.ArgumentParser(description='Process input file for graph')
    b14.add_argument('b17', b15 = str, help='Input file name containing the graph')
    b16 = b14.parse_args()
    b17 = b16.b17
    if not os.path.exists(b17):
        print("Error: File not found.")
        sys.exit(1)
    b3, b4 = fonk1(b17)
    print("Vertices:", b3)
    print("Edges:", b4)