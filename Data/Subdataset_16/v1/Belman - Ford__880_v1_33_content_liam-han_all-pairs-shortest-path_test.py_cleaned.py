import argparse
import os
import re
import sys
import time
from allPairsShortestPath import b13, b14
def fonk1(filename):
    global b4
    global b5
    b1 = open(filename,'r')
    b2 = b1.readline()
    b3 = b13.match(b2)
    if not b3:
        print(b2+" not properly formatted")
        quit(1)
    b4 = list(range(int(b3.group(1))))
    b5 = []
    for i in range(len(b4)):
        b6 = []
        for j in range(len(b4)):
            b6.append(float("inf"))
        b5.append(b6)
    for b7 in b1.readlines():
        b7 = b7.strip()
        b8 = b14.match(b7)
        if b8:
            b9 = b8.group(1)
            b10 = b8.group(2)
            if int(b9) > len(b4) or int(b10) > len(b4):
                print("Attempting to insert an edge between "+b9+" and "+b10+" in a graph with "+b4+" b4")
                quit(1)
            b11 = b8.group(3)
            b5[int(b9)-1][int(b10)-1]=b11
    b12 = (b4,b5)
    return (b4,b5)
 Please compose a Python script that replicates the functionality described above q
import argparse
import os
import re
import sys
b13 = re.compile(r'(\d+)')
b14 = re.compile(r'(\d+)\s+(\d+)\s+(\d+)')
def fonk2(filename):
    with open(filename, 'r') as infile:
        b2 = infile.readline().strip()
        b15 = b13.match(b2)
        if not b15:
            print(f"{b2} not properly formatted")
            sys.exit(1)
        b16 = int(b15.group(1))
        b4 = list(range(b16))
        b5 = [[float("inf")] * b16 for _ in range(b16)]
        for b7 in infile:
            b7 = b7.strip()
            b17 = b14.match(b7)
            if b17:
                b9 = int(b17.group(1))
                b10 = int(b17.group(2))
                b11 = float(b17.group(3))
                if b9 > b16 or b10 > b16:
                    print(f"Attempting to insert an edge between {b9} and {b10} in a graph with {b16} b4")
                    sys.exit(1)
                b5[b9 - 1][b10 - 1] = b11
    return b4, b5
def fonk3():
    b18 = argparse.ArgumentParser(description="Read a graph from a file and construct its representation.")
    b18.add_argument("filename", b19 = str, help="The file containing the graph definition.")
    b20 = b18.parse_args()
    if not os.path.isfile(b20.filename):
        print(f"File {b20.filename} does not exist.")
        sys.exit(1)
    b4, b5 = fonk2(b20.filename)
    print("Vertices:", b4)
    print("Edges:")
    for b6 in b5:
        print(b6)
if b21 = = "__main__":
    fonk3()