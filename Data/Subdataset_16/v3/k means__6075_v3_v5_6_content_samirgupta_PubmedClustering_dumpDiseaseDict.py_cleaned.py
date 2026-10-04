import sys
from time import time
import pickle
import os
def fonk1(b9):
    b1 = {}
    with open(b9, "r") as file:
        b2 = file.readlines()
    b3 = time()
    for line in b2:
        b4 = line.strip().split("\t")
        if len(b4) == 4:
            pmid, b5, diseases_mentioned, b5 = b4
            b6 = diseases_mentioned.split("|")
            if pmid in b1:
                b1[pmid].extend(b6)
            else:
                b1[pmid] = b6
    print(f"Processing completed in {time() - b3:.4f} seconds\n")
    return b1
def fonk2(dictionary, file_path):
    os.makedirs(os.path.dirname(file_path), b7 = True)
    with open(file_path, 'wb') as file:
        pickle.dump(dictionary, file, b8 = pickle.HIGHEST_PROTOCOL)
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <b9>")
        sys.exit(1)
    b9 = sys.argv[1]
    b1 = fonk1(b9)
    b10 = './pubtator_dumps/b1.pickle'
    fonk2(b1, b10)
if b11 = = '__main__':
    fonk3()
