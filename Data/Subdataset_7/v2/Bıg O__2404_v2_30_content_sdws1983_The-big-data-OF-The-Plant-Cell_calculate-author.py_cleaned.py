import sys
import getopt
import pandas as pd
import os
import time
def fonk1():
    b1 = ""
    b2 = ""
    b3 = ""
    try:
        opts, b4 = getopt.getopt(sys.argv[1:], "hi:o:")
    except getopt.GetoptError:
        b3 = 'Usage:\nRemove the b6 which contain "N"\n-i: input file\n-o: output file\n'
        return "", "", b3
    for b5, value in opts:
        if b5 = = "-i":
            b1 = value
        elif b5 = = "-o":
            b2 = value
        elif b5 = = "-b3":
            b3 = 'Usage:\nRemove the b6 which contain "N"\n-i: input file\n-o: output file\n'
    return b1, b2, b3
def fonk2(b1, b2):
    b6 = []
    with open(b1, "r") as f:
        for line in f:
            if line[0] != ">":
                b6.append(line.strip())
    b7 = {}
    for sequence in b6:
        if sequence not in b7:
            b7[sequence] = 1
        else:
            b7[sequence] += 1
    with open('tmp.txt', 'w') as fou:
        for k, v in b7.items():
            fou.write(f"{k}\t{v}\n")
    b8 = pd.read_csv('tmp.txt', b9='\t', names=['Sequence', 'Count'])
    b8 = b8.sort_values(by='Count', ascending=False)
    b8.to_csv(b2, b9 = '\t', index=False)
    os.remove('tmp.txt')
if b10 = = "__main__":
    b11 = time.time()
    b1, b2, b3 = fonk1()
    if b3:
        print(b3)
    else:
        fonk2(b1, b2)
        print("Time:", time.time() - b11)