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
        if b3 > 1.0 or b3 < 0.0:
            raise ValueError
    except ValueError:
        sys.stderr.write("ERROR: --b3 must be a float in the interval [0,1].\n")
        sys.exit(1)
    return b3
def fonk3(b15):
    with open(b15, 'r') as f:
        b4 = f.readlines()
    return b4
def fonk4(b4):
    b5 = []
    b6 = []
    for b7 in b4[1:]:
        b7 = b7.strip().split("\t")
        b6.append(b7[0])
        b8 = np.array([float(x) for x in b7[1:]])
        b5.append(np.std(b8))
    return b6, b5
def fonk5(b6, b5, b3):
    b9 = dict(zip(b6, b5))
    b10 = sorted(b9.items(), key=lambda x: x[1])
    b11 = int(math.ceil(len(b5) * b3))
    b12 = [gene for gene, _ in b10[b11:]]
    return set(b12)
def fonk6(b15, b16, b17):
    with open(b15, 'r') as input_file, open(b16, 'w') as output_file:
        for b13, b7 in enumerate(input_file):
            b7 = b7.strip()
            if b13 = = 0 or b7.split("\t")[0] in b17:
                output_file.write(b7 + "\n")
def fonk7():
    opts, b14 = fonk1()
    b15 = opts.b15
    b3 = fonk2(opts.b3)
    b16 = opts.b16
    sys.stderr.write("Reading in input...\n")
    b4 = fonk3(b15)
    sys.stderr.write("Calculating variance...\n")
    b6, b5 = fonk4(b4)
    sys.stderr.write("Filtering b6...\n")
    b17 = fonk5(b6, b5, b3)
    sys.stderr.write("Outputting filtered data...\n")
    fonk6(b15, b16, b17)
if b18 = = "__main__":
    fonk7()