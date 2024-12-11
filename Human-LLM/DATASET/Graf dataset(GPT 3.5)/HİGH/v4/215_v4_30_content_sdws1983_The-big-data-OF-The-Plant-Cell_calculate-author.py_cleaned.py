import sys
import getopt
import re
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
            b4 = 'usage:\nremove the sequence which contains "N"\n-i : inputfile\n-o : outputfile\n'
    return b2, b3, b4
def fonk2(b2, b3):
    b6 = []
    with open(b2) as f:
        for b8 in f:
            if b8[0] != ">":
                b6.append(b8.strip())
    print("Total sequences:", len(b6))
    b7 = {}
    for sequence in b6:
        if sequence not in b7.keys():
            b7[sequence] = 1
        else:
            b7[sequence] += 1
    print("Tag counts:", b7)
    with open('tmp.txt', 'w') as fout:
        for tag, count in b7.items():
            b8 = f"{tag}\t{count}\n"
            fout.write(b8)
    b9 = pd.DataFrame(pd.read_table('tmp.txt', names=['sequence', 'count']))
    b9 = b9.sort_values(by=['count'], ascending=False)
    b9.to_csv(b3, b10 = '\t', index=False)
    os.remove('tmp.txt')
if b11 = = "__main__":
    b12 = time.time()
    b2, b3, b4 = fonk1()
    if b4 = = "":
        fonk2(b2, b3)
        print("Time taken:", time.time() - b12)
    else:
        print(b4)