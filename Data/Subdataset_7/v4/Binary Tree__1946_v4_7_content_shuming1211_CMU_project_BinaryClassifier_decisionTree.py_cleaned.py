import sys
import csv
import math
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = int(sys.argv[3])
b4 = sys.argv[4]
b5 = sys.argv[5]
b6 = sys.argv[6]
def fonk1(b1):
    b7 = {}
    b8 = []
    b9 = []
    with open(b1, 'r') as file:
        b10 = csv.b10(file)
        for row in b10:
            if not b9:
                b9 = [row[b23] for b23 in range(len(row) - 1)]
            else:
                for b23 in range(len(row) - 1):
                    b9[b23].append(row[b23])
                b8.append(row[-1])
    for j, b27 in enumerate(b9):
        b11 = b27.pop(0)
        b7[b11] = b27
    b12 = list(set(b8))
    return b8, b7, b12
def fonk2(b8, b12):
    b13 = sum(1 for b23 in b8 if b23 == b12[0])
    b14 = len(b8) - b13
    return b13, b14
def fonk3(b8, b12):
    b13, b14 = fonk2(b8, b12)
    if b13 = = 0 or b14 == 0:
        return 0
    b15 = b13 / len(b8)
    b16 = b14 / len(b8)
    return -b15 * math.log(b15, 2) - b16 * math.log(b16, 2)
def fonk4(b27, b8):
    b17 = []
    b18 = []
    b12 = list(set(b8))
    for b23, value in enumerate(b27):
        if value in ['n', 'notA', 'no']:
            b17.append(b8[b23])
        else:
            b18.append(b8[b23])
    b16 = len(b17) / len(b8)
    b19 = len(b18) / len(b8)
    return fonk3(b8, b12) - (b16 * fonk3(b17, b12)) - (b19 * fonk3(b18, b12)), b17, b18
def fonk5(b27, b7):
    b20 = {}
    b21 = {}
    b22 = len(b7[b27])
    for b23, value in b7.items():
        if b23 = = b27:
            continue
        b20[b23] = []
        b21[b23] = []
        for j in range(b22):
            if b7[b27][j] in ['n', 'notA', 'no']:
                b20[b23].append(value[j])
            else:
                b21[b23].append(value[j])
    return b20, b21
class class1:
    def fonk6(self, b25, b24 = None, b26=None, b27=None):
        self.b25 = b25
        self.b24 = b24
        self.b26 = b26
        self.b27 = b27
    def fonk7(self):
        return self.b24 is None and self.b26 is None
def fonk8(b8, b7, b12, cur_depth, max_depth):
    b30, b28 = fonk2(b8, b12)
    if b30 >= b28:
        b29 = b12[0]
    else:
        b29 = b12[1]
    if b30 = = len(b8) or b28 == len(b8) or not b7 or cur_depth >= max_depth:
        return class1(b29)
    else:
        b17 = []
        b18 = []
        a1 = -1
        b31 = None
        for b27, values in b7.items():
            current_score, current_n_labels, b32 = fonk4(values, b8)
            if current_score >= a1:
                a1 = current_score
                b17 = current_n_labels
                b18 = b32
                b31 = b27
        cur_depth += 1
        b20, b21 = fonk5(b31, b7)
        b24 = fonk8(b17, b20, b12, cur_depth, max_depth)
        b26 = fonk8(b18, b21, b12, cur_depth, max_depth)
        return class1(b12[0], b24, b26, b31)
def fonk9(node, b2, output):
    with open(b2, 'r') as file:
        b10 = csv.b10(file)
        next(b10)
        b33 = []
        for row in b10:
            b34 = fonk10(node, row)
            b33.append(b34 + '\n')
        b35 = ''.join(b33)
    with open(output, 'w') as file:
        file.write(b35)
def fonk10(node, row):
    if node.fonk7():
        return node.b25
    else:
        if row[node.b27] in ['n', 'notA', 'no']:
            return fonk10(node.b24, row)
        else:
            return fonk10(node.b26, row)
def fonk11(b1, b2, b3, b4, b5, b6):
    train_label_list, train_features, b36 = fonk1(b1)
    b37 = fonk8(train_label_list, train_features, b36, 0, b3)
    b38 = fonk9(b37, b1, b4)
    b39 = fonk9(b37, b2, b5)
    b40 = f'error(train): {b38}\nerror(test): {b39}'
    with open(b6, 'w') as file:
        file.write(b40)
if b41 = = '__main__':
    fonk11(b1, b2, b3, b4, b5, b6)