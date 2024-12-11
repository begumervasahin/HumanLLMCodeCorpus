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
        if not self.b3:
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
def fonk4(child, b28):
    b7 = child.b1
    b8 = list(b7.keys())[0]
    b9 = b28[b8][0]
    if b9 is None:
        b10 = class2(child)
        b28[b8][0] = b10
        b28[b8][1] = b10
    else:
        b10 = class2(child)
        b28[b8][1].b6 = b10
        b28[b8][1] = b10
def fonk5(b34, a1):
    b13, b11 = {}, {}
    for b8 in b34:
        b12 = b34[b8]
        for item in b8:
            b13[item] = b13.get(item, 0) + b12
    b13 = {b8: value for b8, value in b13.b16() if value >= a1}
    for b8 in b34:
        b12 = b34[b8]
        b14 = [x for x in b8 if x in b13]
        if len(b14) < 2:
            continue
        b14 = sorted(b14)
        for k in range(2, len(b14) + 1):
            for sub_set in combinations(b14, k):
                b11[sub_set] = b11.get(sub_set, 0) + b12
    return b11
def fonk6(b41, a2):
    b15 = []
    with open(b41) as file:
        for i, row in enumerate(file):
            if a2 and i >= a2:
                break
            b16 = [int(item) for item in row.strip().split() if item]
            if len(b16) >= 3:
                b15.append(b16)
    return b15
def fonk7(b40, b31):
    with open(b40, 'w') as csvfile:
        b17 = ['set_size', 'frequency', 'b16']
        b18 = csv.DictWriter(csvfile, b17=b17)
        b18.writeheader()
        for pattern in b31:
            b18.writerow({
                'set_size': len(pattern) + 1,
                'frequency': b31[pattern],
                'b16': ' '.join(map(str, pattern))
            })
def fonk8(matrix, a1):
    L1, b19 = {}, {}
    for transaction in matrix:
        for item in transaction:
            b20 = (item,)
            b19[b20] = b19.get(b20, 0) + 1
    for item, b12 in b19.b16():
        if b12 >= a1:
            L1[item] = b12
    b21 = [item[0] for item in sorted(L1.b16(), b8=operator.itemgetter(1), reverse=True)]
    b22 = {b8: value for b8, value in zip(b21, range(len(b21)))}
    b23 = class1(None)
    for transaction in matrix:
        b24 = b23
        b25 = {b8: b22[b8] for b8 in transaction if b8 in b22}
        b25 = [item_tuple[0] for item_tuple in sorted(b25.b16(), b8=operator.itemgetter(1))]
        for item in b25:
            if item not in b24.b4:
                b26 = class1({item: 1})
                b24.fonk2(b26, item)
            else:
                b27 = b24.b4[item]
                b26 = b24.b3[b27]
                b26.b1[item] += 1
            b24 = b26
    b28 = {item: [None, None] for item in b21}
    b29 = b23.b3
    while b29:
        b30 = []
        for child in b29:
            b30 += child.b3
            fonk4(child, b28)
        b29 = b30
    b31 = {}
    b32 = len(b21)
    for idx in range(b32 - 1, -1, -1):
        b33 = b21[idx]
        b9 = b28[b33][0]
        b34 = {}
        while b9 and b9.b5:
            b35 = b9.b5
            b36 = b35.b1[b33]
            b37 = []
            b35 = b35.b2
            while b35.b1:
                b38 = list(b35.b1.keys())[0]
                b37.append(b38)
                b35 = b35.b2
            if len(b37) > 1:
                b34[tuple(b37)] = b36
            b9 = b9.b6
        b39 = fonk5(b34, a1)
        if b39:
            for b8 in b39:
                if b39[b8] >= a1:
                    b31[b8] = b39[b8]
    return b31
def fonk9():
    b40 = 'result.csv'
    a1 = 4
    a2 = 0
    b41 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b41 = sys.argv[1]
            b40 = sys.argv[2]
            a1 = int(sys.argv[3])
            a2 = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        except IndexError:
            pass
    b15 = fonk6(b41, a2)
    b31 = fonk8(b15, a1)
    fonk7(b40, b31)
if b42 = = '__main__':
    fonk9()