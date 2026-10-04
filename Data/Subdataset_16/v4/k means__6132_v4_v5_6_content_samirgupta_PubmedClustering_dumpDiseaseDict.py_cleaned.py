import sys
import time
import pickle
def fonk1(b6):
    b1 = {}
    b2 = time.time()
    with open(b6, "r") as file:
        for line in file:
            b3 = line.strip().split("\t")
            if len(b3) == 4:
                pmid, b4, diseases_mentioned, b4 = b3
                b5 = diseases_mentioned.split("|")
                if pmid not in b1:
                    b1[pmid] = []
                b1[pmid].extend(b5)
    print(f"Processing done in {time.time() - b2:.4f} seconds\n")
    return b1
def fonk2():
    b6 = sys.argv[1]
    b1 = fonk1(b6)
    b7 = './pubtator_dumps/b1.pickle'
    with open(b7, 'wb') as file:
        pickle.dump(b1, file, b8 = pickle.HIGHEST_PROTOCOL)
if b9 = = '__main__':
    fonk2()