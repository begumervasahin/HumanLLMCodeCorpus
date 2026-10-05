import sys
from time import time
import pickle
def fonk1(b8):
    b1 = {}
    with open(b8, "r") as lines_fh:
        b2 = lines_fh.readlines()
    b3 = time()
    for b4 in b2:
        b4 = b4.strip()
        b5 = b4.split("\t")
        if len(b5) == 4:
            pmid, mesh_id, dis_mens, b6 = b5[:4]
            b7 = dis_mens.split("|")
            b1.setdefault(pmid, []).extend(b7)
    print("Processing done in {:.2f} seconds".format(time() - b3))
    print()
    return b1
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b8>")
        return
    b8 = sys.argv[1]
    b1 = fonk1(b8)
    b9 = './pubtator_dumps/b1.pickle'
    with open(b9, 'wb') as handle:
        pickle.dump(b1, handle, b10 = pickle.HIGHEST_PROTOCOL)
if b11 = = '__main__':
    fonk2()
