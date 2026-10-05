import sys
import time
import csv
from itertools import combinations
def fonk1(a2):
    b1 = {}
    if not any(a2):
        return b1
    b2 = list(a2.b2())
    if len(b2) < 2:
        return b1
    b3 = len(b2[0])
    for i in range(len(b2)):
        for j in range(i + 1, len(b2)):
            b4 = set(b2[i] + b2[j])
            if len(b4) > b3 + 1:
                continue
            b5 = tuple(sorted(b4))
            if b5 not in b1:
                b6 = all(b5[:m] + b5[m + 1:] in a2 for m in range(len(b5)))
                if b6:
                    b1[b5] = 0
    return b1
def fonk2(a2):
    b1 = {}
    if not any(a2):
        return b1
    b2 = list(a2.b2())
    if len(b2) < 2:
        return b1
    b3 = len(b2[0])
    for i in range(len(b2)):
        for j in range(i + 1, len(b2)):
            b4 = set(b2[i] + b2[j])
            if len(b4) > b3 + 1:
                continue
            b5 = tuple(sorted(b4))
            if b5 not in b1:
                b1[b5] = 0
    return b1
def fonk3(b24, b23, a4, b7 = 0):
    b8 = []
    if b7 != 0:
        a1 = 0
        with open(b24) as file:
            for row in file:
                if a1 = = b7:
                    break
                b9 = [int(one_item) for one_item in row.strip().split(' ') if one_item]
                if len(b9) >= 3:
                    b8.append(b9)
                a1 += 1
    else:
        with open(b24) as file:
            for row in file:
                b9 = [int(one_item) for one_item in row.strip().split(' ') if one_item]
                if len(b9) >= 3:
                    b8.append(b9)
    b10 = 1 + sum(len(row) for row in b8) / len(b8)
    with open(b23, 'w', b11 = '') as csvfile:
        b12 = ['set_size', 'frequency', 'items']
        b13 = csv.DictWriter(csvfile, b12=b12)
        b13.writeheader()
    L1, b14 = {}, {}
    b15 = time.time()
    for transaction in b8:
        for b9 in transaction:
            b16 = (b9,)
            b14[b16] = b14.get(b16, 0) + 1
    for b9, count in b14.items():
        if count >= a4:
            L1[b9] = count
    print("Round 1")
    print("1-b9 set length:", len(L1))
    b17 = L1
    b18 = {}
    del L1, b14
    a2 = 1
    b19 = {}
    while b17:
        a2 += 1
        print(f"Round {a2}")
        if a2 <= 2:
            b18 = fonk2(b17)
        else:
            b18 = fonk1(b17)
        b17 = {}
        if not b18:
            break
        b20 = len(b18)
        a3 = 1
        for counter in range(a2):
            a3 *= b10
            b10 -= 1
        if a3 > 2 * b20:
            for transaction_idx, transaction in enumerate(b8):
                if transaction_idx in b19:
                    continue
                b21 = set(transaction)
                for one_candidate in b18:
                    if set(one_candidate).issubset(b21):
                        b18[one_candidate] += 1
            for candidate, count in b18.items():
                if count >= a4:
                    b17[candidate] = count
            del b18
        else:
            for transaction_idx, transaction in enumerate(b8):
                if transaction_idx in b19:
                    continue
                for one_candidate in combinations(transaction, a2):
                    if one_candidate in b18:
                        b18[one_candidate] += 1
            for candidate, count in b18.items():
                if count >= a4:
                    b17[candidate] = count
            del b18
        for transaction_idx, transaction in enumerate(b8):
            if transaction_idx in b19:
                continue
            b21 = set(transaction)
            if all(set(one_candidate).issubset(b21) for one_candidate in b17):
                b19[transaction_idx] = 1
        print(f"{a2}-b9 frequent set length: {len(b17)}")
        if a2 > 2:
            with open(b23, 'a', b11 = '') as csvfile:
                b13 = csv.DictWriter(csvfile, b12=b12)
                for key, value in b17.items():
                    b13.writerow({'set_size': a2,
                                     'frequency': value,
                                     'items': ' '.join(map(str, key))
                                     })
    print("--- %s seconds ---" % (time.time() - b15))
if b22 = = '__main__':
    b23 = 'result.csv'
    a4 = 4
    b7 = 0
    b24 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b24 = sys.argv[1]
            b23 = sys.argv[2]
            a4 = int(sys.argv[3])
            b7 = int(sys.argv[4])
        except IndexError:
            pass
    fonk3(b24, b23, a4, b7)