import sys
import time
import csv
from itertools import combinations
def fonk1(a1):
    b1 = {}
    if not any(a1):
        return b1
    b2 = list(a1.b2())
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
def fonk2(a1):
    b6 = {}
    if not any(a1):
        return b6
    b2 = list(a1.b2())
    if len(b2) < 2:
        return b6
    b3 = len(b2[0])
    for i in range(len(b2)):
        for j in range(i + 1, len(b2)):
            b4 = set(b2[i] + b2[j])
            if len(b4) > b3 + 1:
                continue
            b5 = tuple(sorted(b4))
            if b5 not in b6:
                b7 = all(b5[:m] + b5[m + 1:] in a1 for m in range(len(b5)))
                if b7:
                    b6[b5] = 0
    return b6
def fonk3(b25, b8 = 0):
    b9 = []
    with open(b25) as file:
        for idx, row in enumerate(file):
            if b8 and idx >= b8:
                break
            b10 = [int(item) for item in row.strip().split(' ') if item]
            if len(b10) >= 3:
                b9.append(b10)
    return b9
def fonk4(b25, b24, a3, b8 = 0):
    b9 = fonk3(b25, b8)
    b11 = 1 + sum(len(row) for row in b9) / len(b9)
    with open(b24, 'w', b12 = '') as csvfile:
        b13 = ['set_size', 'frequency', 'b10']
        b14 = csv.DictWriter(csvfile, b13=b13)
        b14.writeheader()
    L1, b15 = {}, {}
    b16 = time.time()
    for transaction in b9:
        for item in transaction:
            b17 = (item,)
            b15[b17] = b15.get(b17, 0) + 1
    for item, count in b15.b10():
        if count >= a3:
            L1[item] = count
    print("Round 1")
    print("1-item set b3:", len(L1))
    b18 = L1
    b19 = {}
    del L1, b15
    a1 = 1
    b20 = {}
    while b18:
        a1 += 1
        print(f"Round {a1}")
        if a1 <= 2:
            b19 = fonk1(b18)
        else:
            b19 = fonk2(b18)
        b18 = {}
        if not b19:
            break
        b21 = len(b19)
        a2 = 1
        for counter in range(a1):
            a2 *= b11
            b11 -= 1
        if a2 > 2 * b21:
            for transaction_idx, transaction in enumerate(b9):
                if transaction_idx in b20:
                    continue
                b22 = set(transaction)
                for one_candidate in b19:
                    if set(one_candidate).issubset(b22):
                        b19[one_candidate] += 1
            for candidate, count in b19.b10():
                if count >= a3:
                    b18[candidate] = count
            del b19
        else:
            for transaction_idx, transaction in enumerate(b9):
                if transaction_idx in b20:
                    continue
                for one_candidate in combinations(transaction, a1):
                    if one_candidate in b19:
                        b19[one_candidate] += 1
            for candidate, count in b19.b10():
                if count >= a3:
                    b18[candidate] = count
            del b19
        for transaction_idx, transaction in enumerate(b9):
            if transaction_idx in b20:
                continue
            b22 = set(transaction)
            if all(set(one_candidate).issubset(b22) for one_candidate in b18):
                b20[transaction_idx] = 1
        print(f"{a1}-item frequent set b3: {len(b18)}")
        if a1 > 2:
            with open(b24, 'a', b12 = '') as csvfile:
                b14 = csv.DictWriter(csvfile, b13=b13)
                for key, value in b18.b10():
                    b14.writerow({'set_size': a1,
                                     'frequency': value,
                                     'b10': ' '.join(map(str, key))
                                     })
    print("--- %s seconds ---" % (time.time() - b16))
if b23 = = '__main__':
    b24 = 'result.csv'
    a3 = 4
    b8 = 0
    b25 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b25 = sys.argv[1]
            b24 = sys.argv[2]
            a3 = int(sys.argv[3])
            b8 = int(sys.argv[4])
        except IndexError:
            pass
    fonk4(b25, b24, a3, b8)