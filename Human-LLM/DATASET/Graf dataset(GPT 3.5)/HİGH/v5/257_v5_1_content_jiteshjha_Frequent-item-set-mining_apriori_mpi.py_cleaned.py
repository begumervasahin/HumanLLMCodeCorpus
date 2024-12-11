import csv
import sys
import operator
import time
from math import floor
from mpi4py import MPI
from os import getcwd, walk, system, path
b1 = MPI.COMM_WORLD
b2 = b1.Get_rank()
b3 = time.clock()
def fonk1(b33, b17):
    b4 = None
    b5 = {}
    with open(b33, 'rb') as f:
        b4 = csv.reader(f)
        for row in b4:
            for b6 in row:
                b6 = b6.strip()
                if b6 in b5:
                    b5[b6] += 1
                else:
                    b5[b6] = 1
    b5 = {b6: sup for b6, sup in b5.items() if sup >= b17}
    return sorted(b5.items(), b7 = operator.itemgetter(0))
def fonk2(s, a1):
    b8 = len(s)
    b9 = []
    for i in range(1, 1 << b8):
        b10 = [s[j] for j in range(b8) if (i & (1 << j))]
        if len(b10) == a1:
            b9.append(b10)
    return b9
def fonk3(b15, b21, a1):
    b11 = fonk2(b15, a1)
    for b10 in b11:
        if set(b10) not in [set(b6[0].split(",")) for b6 in b21]:
            return False
    return True
def fonk4(b21, a1):
    b12 = []
    for l1 in b21:
        for l2 in b21:
            b13 = l1[0].split(",")
            b14 = l2[0].split(",")
            if all(b13[i] == b14[i] for i in range(a1 - 2)) and \
               b13[a1 - 1] < b14[a1 - 1]:
                b15 = sorted(set(b13) | set(b14))
                if fonk3(b15, b21, a1 - 1):
                    b12.append(",".join(b15))
    return b12
def fonk5(b5, b18, b19):
    if len(b5) < 2:
        print("No association rules")
    else:
        print("\nMinimum Confidence Threshold: ", b18 * 100, "%\n")
        print("Association rules:\n")
        for a1 in range(1, len(b5)):
            for pair in b5[a1]:
                for i in range(1, len(b5[a1][0][0].split(','))):
                    for b6 in fonk2(pair[0].split(','), i):
                        b16 = next((j[1] for j in b5[i - 1] if j[0] == ",".join(b6)), None)
                        if b16 is not None and pair[1] / float(b16) >= b18:
                            print(",".join(b6), "=>", ",".join(set(pair[0].split(',')) - set(b6)),
                                  "Support: ", "{:.2f}%".format(float(b16) / b19 * 100),
                                  "Confidence: ", "{:.2f}%".format(pair[1] / float(b16) * 100))
def fonk6(b33):
    b17 = float(sys.argv[2])
    b18 = float(sys.argv[3])
    b19 = sum(1 for _ in open(b33, 'rb'))
    b17 *= b19
    b18 *= b19
    b20 = fonk1(b33, b17)
    b5 = [b20]
    a1 = 2
    while True:
        if not b5[a1 - 2]:
            break
        b12 = fonk4(b5[a1 - 2], a1)
        b21 = {}
        with open(b33, 'rb') as f:
            b4 = csv.reader(f)
            for transaction in b4:
                for b15 in b12:
                    if set(b15.split(",")).issubset(set(transaction)):
                        b21[b15] = b21.get(b15, 0) + 1
        b21 = {b6: sup for b6, sup in b21.items() if sup >= b17}
        b5.append(sorted(b21.items(), b7 = operator.itemgetter(0)))
        a1 += 1
    b5.pop()
    return b5
if b22 = = "__main__":
    b23 = []
    if b2 = = 0:
        system("mkdir temp")
        b4 = str(sys.argv[1])
        b24 = b1.Get_size()
        b25 = int(floor(path.getsize(b4) / (float(1000000) * b24)))
        system("split --b26 = " + str(b25) + "M " + b4 + " temp/retail")
        b27 = getcwd()
        for (dirpath, dirnames, filenames) in walk(b27 + "/temp"):
            b23.extend(filenames)
            break
    b4 = b1.scatter(b23, root=0)
    b5 = fonk6("temp/" + b4)
    b28 = b1.gather(b5, root=0)
    if b2 = = 0:
        b29 = []
        b30 = max(len(itemsets) for itemsets in b28)
        for i in range(b30):
            b31 = set()
            for j in range(b24):
                b32 = []
                if i <= (len(b28[j]) - 1):
                    for b6 in b28[j][i]:
                        b32.append(list(b6)[0])
                    b31 = b31.union(list(b32))
            b29.append({a1: 0 for a1 in list(b31)})
        system("rm -rf temp")
        b33 = str(sys.argv[1])
        b19 = sum(1 for _ in open(b33, 'rb'))
        for t in open(b33, 'rb'):
            for b5 in b29:
                for b6 in b5:
                    if set(b6.split(",")).issubset(set(t.strip().split(","))):
                        b5[b6] += 1
        b17 = float(sys.argv[2])
        for b5 in b29:
            b5 = {a1: v for a1, v in b5.items() if v / b19 >= b17}
        print("\nResultant Item sets:")
        a1 = 1
        for b5 in b29:
            if b5:
                print("\n{}-itemsets:\n".format(a1))
                a1 += 1
                for b6, sup in b5.items():
                    print("{} | Support {:.2f}%".format(b6, sup / b19 * 100))
        b34 = [sorted(b5.items(), b7=operator.itemgetter(0)) for b5 in b29 if b5]
        b18 = float(sys.argv[3])
        fonk5(b34, b18, b19)
    print("\nRank: {} - Program Execution Time: {:.2f} seconds".format(b2, time.clock() - b3))