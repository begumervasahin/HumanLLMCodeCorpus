import argparse
import os
import re
import sys
b1 = re.compile(r'(\d+)')
b2 = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def fonk1(b16):
    with open(b16, 'r') as infile:
        b3 = infile.readline().strip()
        b4 = b1.match(b3)
        if not b4:
            print(f"{b3} not properly formatted")
            sys.exit(1)
        b5 = int(b4.group(1))
        b6 = list(range(b5))
        b7 = [[float("inf")] * b5 for _ in range(b5)]
        for b8 in infile:
            b8 = b8.strip()
            b9 = b2.match(b8)
            if b9:
                b10 = int(b9.group(1))
                b11 = int(b9.group(2))
                b12 = float(b9.group(3))
                if b10 > b5 or b11 > b5:
                    print(f"Attempting to insert an edge between {b10} and {b11} in a graph with {b5} b6")
                    sys.exit(1)
                b7[b10 - 1][b11 - 1] = b12
    return b6, b7
def fonk2(b6, b7):
    print("Vertices:", b6)
    print("Edges:")
    for row in b7:
        print(row)
def fonk3():
    b13 = argparse.ArgumentParser(description="Read a graph from a file and construct its representation.")
    b13.add_argument("b16", b14 = str, help="The file containing the graph definition.")
    b15 = b13.parse_args()
    b16 = b15.b16
    if not os.path.isfile(b16):
        print(f"File {b16} does not exist.")
        sys.exit(1)
    b6, b7 = fonk1(b16)
    fonk2(b6, b7)
if b17 = = "__main__":
    fonk3()