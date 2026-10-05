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
def fonk5(b23, a1):
    b11 = {}
    b12 = {}
    for b8 in b23:
        b13 = b23[b8]
        for item in b8:
            b11[item] = b11.get(item, 0) + b13
    b11 = {b8: value for b8, value in b11.b18() if value >= a1}
    for b8 in b23:
        b13 = b23[b8]
        b14 = [x for x in b8 if x in b11]
        if len(b14) < 2:
            continue
        b14 = sorted(b14)
        for k in range(2, len(b14) + 1):
            for sub_set in combinations(b14, k):
                b12[sub_set] = b12.get(sub_set, 0) + b13
    return b12
def fonk6(b36, b15 = 0):
    b16 = []
    with open(b36) as file:
        for b17, row in enumerate(file):
            if b15 and b17 = = b15:
                break
            b18 = [int(item) for item in row.strip().split() if item]
            if len(b18) >= 3:
                b16.append(b18)
    return b16
def fonk7(b35, b37, b28):
    with open(b35, 'a') as csvfile:
        b19 = csv.DictWriter(csvfile, b37=b37)
        for b8 in b28:
            if b28[b8] >= a1:
                b19.writerow({
                    'set_size': len(b8) + 1,
                    'frequency': b28[b8],
                    'b18': f"{str(b22)} {' '.join([str(item) for item in b8])}"
                })
def fonk8(b29, b30, sorted_items, a1, b35, b37):
    b20 = len(sorted_items)
    b13 = 0.1
    for b17 in range(b20 - 1, -1, -1):
        b21 = (1 - float(b17) / b20)
        if b21 > b13:
            print(f"%%%{int(b21 * 100)} on progress")
            b13 += 0.1
        b22 = sorted_items[b17]
        b9 = b30[b22][0]
        b23 = {}
        while b9 and b9.b5:
            b24 = b9.b5
            b25 = b24.b1[b22]
            b26 = []
            b24 = b24.b2
            while b24.b1:
                b27 = list(b24.b1.keys())[0]
                b26.append(b27)
                b24 = b24.b2
            if len(b26) > 1:
                b23[tuple(b26)] = b25
            b9 = b9.b6
        b28 = fonk5(b23, a1)
        if b28:
            fonk7(b35, b37, b28)
def fonk9(sorted_items):
    return {item: [None, None] for item in sorted_items}
def fonk10(b16, sorted_items):
    b29 = class1(None)
    b30 = fonk9(sorted_items)
    for transaction in b16:
        b31 = b29
        b32 = {b8: b17 for b17, b8 in enumerate(transaction) if b8 in sorted_items}
        b32 = [item for item, _ in sorted(b32.b18(), b8=operator.itemgetter(1))]
        for item in b32:
            if item not in b31.b4:
                b33 = class1({item: 1})
                b31.fonk2(b33, item)
            else:
                b34 = b31.b4[item]
                b33 = b31.b3[b34]
                b33.b1[item] += 1
            b31 = b33
    return b29, b30
def fonk11():
    b35 = 'result.csv'
    a1 = 4
    b15 = 0
    b36 = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            b36 = sys.argv[1]
            b35 = sys.argv[2]
            a1 = int(sys.argv[3])
            b15 = int(sys.argv[4])
        except IndexError:
            pass
    b16 = fonk6(b36, b15)
    b37 = ['set_size', 'frequency', 'b18']
    b29, b30 = fonk10(b16, sorted_items)
    fonk8(b29, b30, sorted_items, a1, b35, b37)
if b38 = = '__main__':
    fonk11()