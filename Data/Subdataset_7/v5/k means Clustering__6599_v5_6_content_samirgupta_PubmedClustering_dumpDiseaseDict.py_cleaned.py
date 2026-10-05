import sys
from time import time
import pickle
def fonk1(b7):
    with open(b7, "r") as file:
        b1 = file.readlines()
    b2 = {}
    b3 = time()
    for line in b1:
        b4 = line.strip().split("\t")
        if len(b4) == 4:
            pmid, b5, dis_mens, b5 = b4
            b6 = dis_mens.split("|")
            b2.setdefault(pmid, []).extend(b6)
    print("Processing done in {:.4f} seconds".format(time() - b3))
    print()
    return b2
def fonk2():
    b7 = sys.argv[1]
    b2 = fonk1(b7)
    b8 = './pubtator_dumps/b2.pickle'
    with open(b8, 'wb') as handle:
        pickle.dump(b2, handle, b9 = pickle.HIGHEST_PROTOCOL)
if b10 = = '__main__':
    fonk2()