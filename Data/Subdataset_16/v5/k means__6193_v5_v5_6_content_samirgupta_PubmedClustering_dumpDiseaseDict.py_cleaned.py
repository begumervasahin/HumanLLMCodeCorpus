import sys
import time
import pickle
def fonk1(b7):
    b1 = {}
    b2 = time.time()
    with open(b7, "r") as file:
        for line in file:
            b3 = line.strip().split("\t")
            if len(b3) == 4:
                pmid, b4, diseases_mentioned, b4 = b3
                b5 = diseases_mentioned.split("|")
                b1.setdefault(pmid, []).extend(b5)
    print(f"Processing done in {time.time() - b2:.4f} seconds\n")
    return b1
def fonk2(b1, b8):
    with open(b8, 'wb') as file:
        pickle.dump(b1, file, b6 = pickle.HIGHEST_PROTOCOL)
def fonk3():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b7>")
        sys.exit(1)
    b7 = sys.argv[1]
    b1 = fonk1(b7)
    b8 = './pubtator_dumps/b1.pickle'
    fonk2(b1, b8)
if b9 = = '__main__':
    fonk3()