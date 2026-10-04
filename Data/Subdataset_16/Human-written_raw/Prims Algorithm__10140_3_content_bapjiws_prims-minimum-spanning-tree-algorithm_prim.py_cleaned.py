import heapq
import operator
import time
import argparse
def fonk1():
    b1 = time.process_time()
    b2 = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    b2.add_argument("-s", b3 = "the b14 of the MST", action="store_true")
    b2.add_argument("-t", b3 = "execution time", action="store_true")
    b2.add_argument("filename", b3 = ".txt file to parse")
    b4 = b2.parse_args()
    with open(b4.filename, 'r') as file:
        b5 = [ list(map(float, i.split())) for i in file.readlines() ]
    b6 = int(min([v[0] for v in b5[1:]] + [v[1] for v in b5[1:]]))
    b7 = int(max([v[0] for v in b5[1:]] + [v[1] for v in b5[1:]]))
    b8 = { k: [ (v[2], v[0], v[1]) for v in b5[1:] if v[0] == k or v[1] == k ] for k in range(b6, b7 + 1) }
    while True:
        b9 = int(input("Source node: "))
        if b9 not in [v[0] for v in b5[1:]] + [v[1] for v in b5[1:]]:
            print("No such node, please try again")
            continue
        else:
            break
    b10 = []
    b11 = set()
    b12 = b9
    b11.add(float(b12))
    b13 = []
    b14 = []
    while len(b11) < int(b5[0][0]):
        for item in b8[b12]:
            heapq.heappush(b13, item)
        while True:
            b15 = heapq.heappop(b13)
            if not operator.xor(b15[1] in b11, b15[2] in b11 ):
                continue
            break
        b8[b15[1]].remove(b15)
        b8[b15[2]].remove(b15)
        if b15[1] not in b11:
            b12 = b15[1]
            b11.add(b12)
            b14.append((b15[2], b15[1], b15[0]))
        if b15[2] not in b11:
            b12 = b15[2]
            b11.add(b15[2])
            b14.append((b15[1], b15[2], b15[0]))
        b10.append(b15[0])
    print("The overall cost of the MST: {}".format(sum(b10)))
    if b4.s:
        print("The b14 of the MST: {}".format(b14))
    if b4.t:
        print("--- {} seconds ---".format(time.process_time() - b1))
if b16 = = "__main__":
    fonk1()