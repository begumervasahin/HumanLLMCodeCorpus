import optparse
import sys
import numpy as np
import math
def fonk1():
    b1 = optparse.OptionParser()
    b1.add_option("--b15", b2 = "b15", action="store", default="", help="Input file")
    b1.add_option("--b3", b2 = "b3", action="store", default="", help="Filter level (float between 0 and 1)")
    b1.add_option("--b16", b2 = "b16", action="store", default="", help="Output file")
    return b1.parse_args()
def fonk2(b3):
    try:
        b3 = float(b3)
        if not (0.0 <= b3 <= 1.0):
            raise ValueError
    except ValueError:
        sys.stderr.write("ERROR: --b3 must be a float in the interval [0,1].\n")
        sys.exit(1)
    return b3
def fonk3(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()
def fonk4(b17):
    b4 = []
    b5 = []
    for b12 in b17[1:]:
        b6 = b12.strip().split("\t")
        b7 = b6[0]
        b8 = np.array([float(x) for x in b6[1:]])
        b4.append(np.std(b8))
        b5.append(b7)
    return b5, b4
def fonk5(b5, b4, b3):
    b9 = sorted(zip(b5, b4), key=lambda x: x[1])
    b10 = int(math.ceil(len(b4) * b3))
    b11 = [b7 for b7, b14 in b9[b10:]]
    return set(b11)
def fonk6(b15, b16, b18):
    with open(b15, 'r') as input_file, open(b16, 'w') as output_file:
        for b13, b12 in enumerate(input_file):
            b12 = b12.strip()
            if b13 = = 0 or b12.split("\t")[0] in b18:
                output_file.write(b12 + "\n")
def fonk7():
    opts, b14 = fonk1()
    b15 = opts.b15
    b3 = fonk2(opts.b3)
    b16 = opts.b16
    sys.stderr.write("Reading in input...\n")
    b17 = fonk3(b15)
    sys.stderr.write("Calculating b4...\n")
    b5, b4 = fonk4(b17)
    sys.stderr.write("Filtering b5...\n")
    b18 = fonk5(b5, b4, b3)
    sys.stderr.write("Outputting filtered data...\n")
    fonk6(b15, b16, b18)
if b19 = = "__main__":
    fonk7()