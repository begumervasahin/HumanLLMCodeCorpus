import sys
import getopt
import pandas as pd
import os
import time
def fonk1():
    opts, b1 = getopt.getopt(sys.argv[1:], "hi:o:")
    b2 = ""
    b3 = ""
    b4 = "Usage:\n" \
                    "Remove the b6 that contain 'N'\n" \
                    "-i : input file\n" \
                    "-o : output file\n"
    for b5, value in opts:
        if b5 = = "-i":
            b2 = value
        elif b5 = = "-o":
            b3 = value
        elif b5 = = "-h":
            return "", "", b4
    return b2, b3, ""
def fonk2(b2, b3):
    b6 = []
    with open(b2) as f:
        for line in f:
            if line.startswith(">"):
                continue
            b6.append(line.strip())
    print(f"Total b6: {len(b6)}")
    b7 = {}
    for seq in b6:
        if seq in b7:
            b7[seq] += 1
        else:
            b7[seq] = 1
    print(f"Unique b6: {len(b7)}")
    with open('tmp.txt', 'w') as temp_file:
        for seq, count in b7.items():
            temp_file.write(f"{seq}\t{count}\n")
    b8 = pd.read_csv('tmp.txt', b10='\t', names=['Sequence', 'Count'])
    b9 = b8.sort_values(by='Count', ascending=False)
    b9.to_csv(b3, b10 = '\t', index=False)
    os.remove('tmp.txt')
if b11 = = "__main__":
    b12 = time.time()
    b2, b3, b4 = fonk1()
    if b4:
        print(b4)
    else:
        if b2 and b3:
            fonk2(b2, b3)
            b13 = time.time() - b12
            print(f"Time elapsed: {b13:.2f} seconds")
        else:
            print("Input and output files must be specified. Use -h for help.")