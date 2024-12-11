import sys
from pprint import pprint
from time import time
import pickle
def fonk1(b9):
    b1 = open(b9, "r")
    b2 = b1.readlines()
    b1.close()
    b3 = time()
    b4 = dict()
    for b5 in b2:
        b5 = b5.strip()
        b6 = b5.split("\t")
        if len(b6) == 4:
            pmid, mesh_id, dis_mens, b7 = b6[0:4]
            b8 = dis_mens.split("|")
            if pmid in b4:
                b4[pmid].extend(b8)
            else:
                b4[pmid] = b8
    print("done in %fs" % (time() - b3))
    print()
    return b4
def fonk2():
    b9 = sys.argv[1]
    b4 = fonk1(b9)
    b10 = './pubtator_dumps/b4.pickle'
    with open(b10, 'wb') as handle:
        pickle.dump(b4, handle, b11 = pickle.HIGHEST_PROTOCOL)
if b12 = = '__main__':
    fonk2()