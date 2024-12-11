import sys
import time
import csv
from itertools import combinations
import operator
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = []
        self.b4 = {}
    def fonk2(self, obj, b5):
        if len(self.b3) < 1:
            self.b3.append(obj)
            obj.b2 = self
            self.b4[b5] = 0
        else:
            self.b4[b5] = len(self.b3)
            self.b3.append(obj)
            obj.b2 = self
class class2:
    def fonk3(self, b1):
        self.b5 = b1
        self.b6 = None
def fonk4(child, b31):
    b7 = child.b1
    b8 = list(b7.keys())[0]
    b9 = b31[b8][0]
    if b9 is None:
        b10 = class2(child)
        b31[b8][0] = b10
        b31[b8][1] = b10
    else:
        b10 = class2(child)
        b31[b8][1].b6 = b10
        b31[b8][1] = b10
def fonk5(b37, a2):
    d, b11 = {}, {}
    for b8 in b37:
        b12 = b37[b8]
        for b18 in b8:
            if b18 not in d:
                d[b18] = b12
            else:
                d[b18] += b12
    b13 = list(d.keys())
    for b8 in b13:
        if d[b8] < a2:
            d.pop(b8)
    for b8 in b37:
        b12 = b37[b8]
        b14 = list(b8)
        b15 = [x for x in b14 if x in d]
        if len(b15) < 2:
            continue
        b15 = sorted(b15)
        for k in range(2, len(b15) + 1):
            for sub_set in combinations(b15, k):
                if sub_set not in b11:
                    b11[sub_set] = b12
                else:
                    b11[sub_set] += b12
    return b11
def fonk6(b45, b44, a2, b16 = 0):
    b17 = []
    if b16 != 0:
        a1 = 0
        for row in open(b45):
            if a1 = = b16:
                break
            b18 = row.strip().split(' ')
            if len(b18) >= 3:
                b18 = [int(one_item) for one_item in b18]
                b17.append(b18)
            a1 += 1
    else:
        for row in open(b45):
            b18 = row.strip().split(' ')
            if len(b18) >= 3:
                b18 = [int(one_item) for one_item in b18]
                b17.append(b18)
    with open(b44, 'w') as csvfile:
        b19 = ['set_size', 'frequency', 'items']
        b20 = csv.DictWriter(csvfile, b19=b19)
        b20.writeheader()
    L1, b21 = {}, {}
    b22 = time.time()
    for transaction in b17:
        for b18 in transaction:
            b23 = (b18,)
            if b23 not in b21:
                b21[b23] = 1
            else:
                b21[b23] += 1
    for b18 in b21:
        if b21[b18] >= a2:
            L1[b18] = b21[b18]
    b24 = [i[0] for i in sorted(L1.items(), b8=operator.itemgetter(1), reverse=True)]
    b25 = {b8: value for b8, value in zip(b24, range(len(b24)))}
    b26 = class1(None)
    for transaction in b17:
        b27 = b26
        b28 = {b8: b25[b8] for b8 in transaction if b8 in b25}
        b28 = [item_tuple[0] for item_tuple in sorted(b28.items(), b8=operator.itemgetter(1))]
        for b18 in b28:
            if b18 not in b27.b4:
                b29 = class1({b18: 1})
                b27.fonk2(b29, b18)
            else:
                b30 = b27.b4[b18]
                b29 = b27.b3[b30]
                b29.b1[b18] += 1
            b27 = b29
    b31 = {b18: [None, None] for b18 in b24}
    b32 = b26.b3
    while True:
        b33 = []
        for child in b32:
            b33 += child.b3
            fonk4(child, b31)
        b32 = b33
        if len(b32) < 1:
            break
    b34 = len(b24)
    b12 = 0.1
    for idx in range(b34 - 1, -1, -1):
        b35 = (1 - float(idx) / b34)
        if b35 > b12:
            print('%%%d on progress' % (int(b35 * 100)))
            b12 += 0.1
        b36 = b24[idx]
        b9 = b31[b36][0]
        b37 = {}
        while b9 is not None and b9.b5 is not None:
            b38 = b9.b5
            b39 = b38.b1[b36]
            b40 = []
            b38 = b38.b2
            while b38.b1 is not None:
                b41 = list(b38.b1.keys())[0]
                b40.append(b41)
                b38 = b38.b2
            if len(b40) > 1:
                b37[tuple(b40)] = b39
            b9 = b9.b6
        b42 = fonk5(b37, a2)
        if len(b42.keys()) < 1:
            continue
        with open(b44, 'a') as csvfile:
            b19 = ['set_size', 'frequency', 'items']
            b20 = csv.DictWriter(csvfile, b19=b19)
            for b8 in b42:
                if b42[b8] < a2:
                    continue
                b20.writerow({'set_size': len(b8) + 1,
                                 'frequency': b42[b8],
                                 'items': str(b36) + ' ' + ' '.join([str(b18) for b18 in b8])
                                 })
    print("--- %s seconds ---" % (time.time() - b22))
if b43 = = '__main__':
    b44 = 'result.csv'
    a2 = 4
    b16 = 0
    b45 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b45 = sys.argv[1]
            b44 = sys.argv[2]
            a2 = int(sys.argv[3])
            b16 = int(sys.argv[4])
        except IndexError:
            pass
    fonk6(b45, b44, a2, b16)