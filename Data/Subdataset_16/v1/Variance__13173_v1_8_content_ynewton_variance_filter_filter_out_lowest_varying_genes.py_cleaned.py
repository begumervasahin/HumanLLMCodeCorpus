import argparse
import sys
import numpy as np
import math
def fonk1():
    b1 = argparse.ArgumentParser(description="Filter b8 based on b7")
    b1.add_argument("--b4", b2 = True, help="Input file")
    b1.add_argument("--b5", b2 = True, type=float, help="Filter level (must be a float below 1)")
    b1.add_argument("--out_file", b2 = True, help="Output file")
    b3 = b1.parse_args()
    b4 = b3.b4
    b5 = b3.b5
    b6 = b3.out_file
    if not (0 <= b5 <= 1):
        sys.stderr.write("ERROR: --b5 must be in interval [0,1].\n")
        sys.exit(1)
    sys.stderr.write("Reading in input...\n")
    a1 = 1
    b7 = []
    b8 = []
    with open(b4, 'r') as input_file:
        for b9 in input_file:
            b9 = b9.strip()
            if a1 > 1:
                b10 = b9.split("\t")
                b8.append(b10[0])
                b11 = [float(x) for x in b10[1:]]
                b7.append(np.std(np.array(b11)))
            a1 += 1
    sys.stderr.write("Sorting on b7...\n")
    b12 = int(math.ceil(len(b7) * b5))
    b13 = dict(zip(b8, b7))
    b14 = sorted(b13.items(), key=lambda x: x[1])
    b15 = b14[b12:]
    b16 = {x: y for x, y in b15}
    b17 = set(b16.keys())
    sys.stderr.write("Outputting filtered data...\n")
    a1 = 1
    with open(b4, 'r') as input_file, open(b6, 'w') as output_file:
        for b9 in input_file:
            b9 = b9.strip()
            if a1 = = 1:
                output_file.write(b9 + "\n")
            else:
                b10 = b9.split("\t")
                if b10[0] in b17:
                    output_file.write(b9 + "\n")
            a1 += 1
if b18 = = "__main__":
    fonk1()