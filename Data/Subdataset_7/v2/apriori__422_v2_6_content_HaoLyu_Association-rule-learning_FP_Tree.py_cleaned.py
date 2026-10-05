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
def fonk4(child, b30):
    b7 = child.b1
    b8 = list(b7.keys())[0]
    b9 = b30[b8][0]
    if b9 is None:
        b10 = class2(child)
        b30[b8][0] = b10
        b30[b8][1] = b10
    else:
        b10 = class2(child)
        b30[b8][1].b6 = b10
        b30[b8][1] = b10
def fonk5(b36, a2):
    b13, b11 = {}, {}
    for b8 in b36:
        b12 = b36[b8]
        for item in b8:
            b13[item] = b13.get(item, 0) + b12
    b13 = {b8: value for b8, value in b13.b17() if value >= a2}
    for b8 in b36:
        b12 = b36[b8]
        b14 = [x for x in b8 if x in b13]
        if len(b14) < 2:
            continue
        b14 = sorted(b14)
        for k in range(2, len(b14) + 1):
            for sub_set in combinations(b14, k):
                b11[sub_set] = b11.get(sub_set, 0) + b12
    return b11
def fonk6(b44, b43, a2, b15 = 0):
    b16 = []
    if b15 != 0:
        a1 = 0
        with open(b44) as file:
            for row in file:
                if a1 = = b15:
                    break
                b17 = [int(item) for item in row.strip().split(' ') if item]
                if len(b17) >= 3:
                    b16.append(b17)
                a1 += 1
    else:
        with open(b44) as file:
            for row in file:
                b17 = [int(item) for item in row.strip().split(' ') if item]
                if len(b17) >= 3:
                    b16.append(b17)
    with open(b43, 'w') as csvfile:
        b18 = ['set_size', 'frequency', 'b17']
        b19 = csv.DictWriter(csvfile, b18=b18)
        b19.writeheader()
    L1, b20 = {}, {}
    b21 = time.time()
    for transaction in b16:
        for item in transaction:
            b22 = (item,)
            b20[b22] = b20.get(b22, 0) + 1
    for item, b12 in b20.b17():
        if b12 >= a2:
            L1[item] = b12
    b23 = [item[0] for item in sorted(L1.b17(), b8=operator.itemgetter(1), reverse=True)]
    b24 = {b8: value for b8, value in zip(b23, range(len(b23)))}
    b25 = class1(None)
    for transaction in b16:
        b26 = b25
        b27 = {b8: b24[b8] for b8 in transaction if b8 in b24}
        b27 = [item_tuple[0] for item_tuple in sorted(b27.b17(), b8=operator.itemgetter(1))]
        for item in b27:
            if item not in b26.b4:
                b28 = class1({item: 1})
                b26.fonk2(b28, item)
            else:
                b29 = b26.b4[item]
                b28 = b26.b3[b29]
                b28.b1[item] += 1
            b26 = b28
    b30 = {item: [None, None] for item in b23}
    b31 = b25.b3
    while b31:
        b32 = []
        for child in b31:
            b32 += child.b3
            fonk4(child, b30)
        b31 = b32
    b33 = len(b23)
    b12 = 0.1
    for idx in range(b33 - 1, -1, -1):
        b34 = (1 - float(idx) / b33)
        if b34 > b12:
            print('%%%b13 on progress' % (int(b34 * 100)))
            b12 += 0.1
        b35 = b23[idx]
        b9 = b30[b35][0]
        b36 = {}
        while b9 and b9.b5:
            b37 = b9.b5
            b38 = b37.b1[b35]
            b39 = []
            b37 = b37.b2
            while b37.b1:
                b40 = list(b37.b1.keys())[0]
                b39.append(b40)
                b37 = b37.b2
            if len(b39) > 1:
                b36[tuple(b39)] = b38
            b9 = b9.b6
        b41 = fonk5(b36, a2)
        if b41:
            with open(b43, 'a') as csvfile:
                b19 = csv.DictWriter(csvfile, b18=b18)
                for b8 in b41:
                    if b41[b8] >= a2:
                        b19.writerow({'set_size': len(b8) + 1,
                                         'frequency': b41[b8],
                                         'b17': str(b35) + ' ' + ' '.join([str(item) for item in b8])
                                         })
    print("--- %s seconds ---" % (time.time() - b21))
if b42 = = '__main__':
    b43 = 'result.csv'
    a2 = 4
    b15 = 0
    b44 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b44 = sys.argv[1]
            b43 = sys.argv[2]
            a2 = int(sys.argv[3])
            b15 = int(sys.argv[4])
        except IndexError:
            pass
    fonk6(b44, b43, a2, b15)