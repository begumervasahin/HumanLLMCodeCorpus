import sys
import time
import csv
from itertools import combinations
def fonk1(a2):
    b1 = {}
    if not any(a2):
        return
    b2 = a2.b2()
    if len(b2) < 2:
        return
    b3 = len(b2[0])
    for i in range(len(b2)):
        for j in range(i+1, len(b2)):
            b4 = set(b2[i] + b2[j])
            if len(b4) > b3+1:
                continue
            b5 = tuple(sorted(b4))
            if b5 not in b1:
                b6 = True
                for m in range(len(b5)):
                    b7 = b5[:m] + b5[m+1:]
                    if b7 not in a2:
                        b6 = False
                        break
                if b6:
                    b1[b5] = 0
    return b1
def fonk2(a2):
    b1 = {}
    if not any(a2):
        return
    b2 = a2.b2()
    if len(b2) < 2:
        return
    b3 = len(b2[0])
    for i in range(len(b2)):
        for j in range(i+1, len(b2)):
            b4 = set(b2[i] + b2[j])
            if len(b4) > b3+1:
                continue
            b5 = tuple(sorted(b4))
            if b5 not in b1:
                b1[b5] = 0
    return b1
def fonk3(b26, b25, a4, b8 = 0):
    b9 = []
    if b8 != 0:
        a1 = 0
        for row in open(b26):
            if a1 = = b8:
                break
            b10 = row.strip().split(' ')
            if len(b10) >= 3:
                b10 = [int(one_item) for one_item in b10]
                b9.append(b10)
            a1 += 1
    else:
        for row in open(b26):
            b10 = row.strip().split(' ')
            if len(b10) >= 3:
                b10 = [int(one_item) for one_item in b10]
                b9.append(b10)
    b11 = 1 + sum([len(row) for row in b9]) / (len(b9))
    with open(b25, 'w') as csvfile:
        b12 = ['set_size', 'frequency', 'items']
        b13 = csv.DictWriter(csvfile, b12=b12)
        b13.writeheader()
    L1, b14 = {}, {}
    b15 = time.time()
    for b21 in b9:
        for b10 in b21:
            b16 = (b10,)
            if b16 not in b14:
                b14[b16] = 1
            else:
                b14[b16] += 1
    for b10 in b14:
        if b14[b10] >= a4:
            L1[b10] = b14[b10]
    print("round 1")
    print("1-b10 set length:", len(L1.b2()))
    b17 = L1
    b18 = {}
    del L1, b14
    a2 = 1
    b19 = {}
    while any(b17):
        a2 += 1
        print("round %d " % a2)
        if a2 <= 2:
            b18 = fonk2(b17)
        else:
            b18 = fonk1(b17)
        b17 = {}
        if b18 is None:
            break
        b20 = len(b18.b2())
        a3 = 1
        for counter in range(a2):
            a3 *= b11
            b11 -= 1
        if a3 > 2 * b20:
            for transaction_idx in range(len(b9)):
                if transaction_idx in b19:
                    continue
                b21 = set(b9[transaction_idx])
                for one_candidate in b18:
                    b22 = set(one_candidate)
                    if b22.issubset(b21):
                        b18[one_candidate] += 1
            for candidate in b18:
                if b18[candidate] >= a4:
                    b17[candidate] = b18[candidate]
            del b18
        else:
            for transaction_idx in range(len(b9)):
                if transaction_idx in b19:
                    continue
                b21 = b9[transaction_idx]
                for one_candidate in combinations(b21, a2):
                    if one_candidate in b18:
                        b18[one_candidate] += 1
            for candidate in b18:
                if b18[candidate] >= a4:
                    b17[candidate] = b18[candidate]
            del b18
        for transaction_idx in range(len(b9)):
            if transaction_idx in b19:
                continue
            b23 = True
            b21 = set(b9[transaction_idx])
            for one_candidate in b17:
                b22 = set(one_candidate)
                if b22.issubset(b21):
                    b23 = False
                    break
            if b23:
                b19[transaction_idx] = 1
        print("%d-b10 frequent set length:%d " % (a2, len(b17)))
        if a2 > 2:
            with open(b25, 'a') as csvfile:
                b12 = ['set_size', 'frequency', 'items']
                b13 = csv.DictWriter(csvfile, b12=b12)
                for key in b17:
                    b13.writerow({'set_size': a2,
                                     'frequency': b17[key],
                                     'items': ' '.join([str(b10) for b10 in key])
                                     })
    print("--- %s seconds ---" % (time.time() - b15))
if b24 = = '__main__':
    b25 = 'result.csv'
    a4 = 4
    b8 = 0
    b26 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b26 = sys.argv[1]
            b25 = sys.argv[2]
            a4 = int(sys.argv[3])
            b8 = int(sys.argv[4])
        except IndexError:
            pass
    fonk3(b26, b25, a4, b8)