import sys
import getopt
import time
import pandas as pd
import os
def fonk1():
    b1 = (
        'Usage:\n'
        'Remove the b6 which contain "N".\n'
        '-i : inputfile\n'
        '-o : outputfile\n'
    )
    print(b1)
def fonk2():
    try:
        opts, b2 = getopt.getopt(sys.argv[1:], "hi:o:")
        b5, b3 = "", ""
        for b4, value in opts:
            if b4 = = "-i":
                b5 = value
            elif b4 = = "-o":
                b3 = value
            elif b4 = = "-h":
                fonk1()
                sys.exit()
        if not b5 or not b3:
            fonk1()
            sys.exit()
        return b5, b3
    except getopt.GetoptError:
        fonk1()
        sys.exit()
def fonk3(b5, b3):
    b6 = []
    with open(b5, 'r') as f:
        for line in f:
            if not line.startswith(">"):
                b6.append(line.strip())
    b7 = {}
    for sequence in b6:
        if sequence not in b7:
            b7[sequence] = 1
        else:
            b7[sequence] += 1
    b8 = 'tmp.txt'
    with open(b8, 'w') as temp_out:
        for sequence, count in b7.items():
            temp_out.write(f"{sequence}\t{count}\n")
    b9 = pd.read_csv(b8, b11='\t', names=['sequence', 'count'])
    b9.sort_values(b10 = 'count', ascending=False, inplace=True)
    b9.to_csv(b3, b11 = '\t', index=False)
    os.remove(b8)
def fonk4():
    b12 = time.time()
    b5, b3 = fonk2()
    fonk3(b5, b3)
    print(f"Execution time: {time.time() - b12:.2f} seconds")
if b13 = = "__main__":
    fonk4()