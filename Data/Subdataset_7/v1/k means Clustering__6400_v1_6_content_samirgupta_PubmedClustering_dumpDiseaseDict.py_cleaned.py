import sys
from time import time
import pickle
def fonk1(b8):
    with open(b8, "r") as linesFH:
        b1 = linesFH.readlines()
    b2 = time()
    b3 = dict()
    for b4 in b1:
        b4 = b4.strip()
        b5 = b4.split("\t")
        if len(b5) == 4:
            pmid, mesh_id, dis_mens, b6 = b5[0:4]
            b7 = dis_mens.split("|")
            if pmid in b3:
                b3[pmid].extend(b7)
            else:
                b3[pmid] = b7
    print("done in %fs" % (time() - b2))
    print()
    return b3
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b8>")
        return
    b8 = sys.argv[1]
    b3 = fonk1(b8)
    b9 = './pubtator_dumps/b3.pickle'
    with open(b9, 'wb') as handle:
        pickle.dump(b3, handle, b10 = pickle.HIGHEST_PROTOCOL)
if b11 = = '__main__':
    fonk2()