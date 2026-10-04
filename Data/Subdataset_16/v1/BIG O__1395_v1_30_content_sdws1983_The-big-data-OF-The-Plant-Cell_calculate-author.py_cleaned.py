import sys
import getopt
import time
import pandas as pd
import os
def fonk1():
    opts, b1 = getopt.getopt(sys.argv[1:], "hi:o:")
    b2 = ""
    b3 = ""
    b4 = ""
    for b5, value in opts:
        if b5 = = "-i":
            b2 = value
        elif b5 = = "-o":
            b3 = value
        elif b5 = = "-b4":
            b4 = 'Usage:\nRemove the sequence which contains "N"\n-i : inputfile\n-o : outputfile\n'
    return b2, b3, b4
def fonk2(b2, b3):
    b6 = []
    with open(b2) as f:
        for line in f:
            if line[0] == ">":
                continue
            else:
                b6.append(line.strip())
    b7 = {}
    for sequence in b6:
        if sequence not in b7:
            b7[sequence] = 1
        else:
            b7[sequence] += 1
    with open('tmp.txt', 'w') as fou:
        for sequence, count in b7.items():
            fou.write(f"{sequence}\t{count}\n")
    b8 = pd.read_table('tmp.txt', names=['sequence', 'count'])
    b8 = b8.sort_values(by='count', ascending=False)
    b8.to_csv(b3, b9 = '\t', index=False)
    os.remove('tmp.txt')
if b10 = = "__main__":
    b11 = time.time()
    b2, b3, b4 = fonk1()
    if b4 = = "":
        fonk2(b2, b3)
        print("Execution time: {:.2f} seconds".format(time.time() - b11))
    else:
        print(b4)