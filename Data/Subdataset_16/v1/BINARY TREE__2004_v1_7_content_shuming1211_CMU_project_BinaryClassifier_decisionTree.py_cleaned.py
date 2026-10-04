import sys
import csv
import math
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = int(sys.argv[3])
b4 = sys.argv[4]
b5 = sys.argv[5]
b6 = sys.argv[6]
def fonk1(file_path):
    b7 = {}
    b8 = []
    b9 = []
    with open(file_path, 'r') as allData:
        b10 = csv.b10(allData)
        for row in b10:
            if not b9:
                for b23 in range(len(row) - 1):
                    b9.append([row[b23]])
            else:
                for b23 in range(len(row) - 1):
                    b9[b23].append(row[b23])
                b8.append(row[-1])
    for j in range(len(row) - 1):
        b11 = b9[j].pop(0)
        b7[b11] = b9[j]
    b12 = list(set(b8))
    return [b8, b7, b12]
def fonk2(b8, b12):
    b13 = b8.count(b12[0])
    b14 = b8.count(b12[1])
    return b13, b14
def fonk3(b8, b12):
    b13, b14 = fonk2(b8, b12)
    if b13 = = 0 or b14 == 0:
        return 0
    b15 = 1.0 * b13 / len(b8)
    b16 = 1.0 * b14 / len(b8)
    return -b15 * math.log(b15, 2) - b16 * math.log(b16, 2)
def fonk4(b27, b8):
    b17 = []
    b18 = []
    b12 = list(set(b8))
    for b23 in range(len(b27)):
        if b27[b23] in ('n', 'notA', 'no'):
            b17.append(b8[b23])
        else:
            b18.append(b8[b23])
    b16 = 1.0 * len(b17) / len(b8)
    b19 = 1.0 * len(b18) / len(b8)
    return (fonk3(b8, b12) -
            (b16 * fonk3(b17, b12)) -
            (b19 * fonk3(b18, b12)),
            b17, b18)
def fonk5(b27, b7):
    b20 = {}
    b21 = {}
    b22 = len(b7[b27])
    for b23 in b7:
        if b23 = = b27:
            continue
        b20[b23] = []
        b21[b23] = []
        for j in range(b22):
            if b7[b27][j] in ('n', 'notA', 'no'):
                b20[b23].append(b7[b23][j])
            else:
                b21[b23].append(b7[b23][j])
    return b20, b21
class class1:
    def fonk6(self, b25, b24 = None, b26=None, b27=None):
        self.b25 = b25
        self.b24 = b24
        self.b26 = b26
        self.b27 = b27
    def fonk7(self):
        return self.b24 is None and self.b26 is None
def fonk8(b8, b7, b12, curdepth, maxdepth):
    label0num, b28 = fonk2(b8, b12)
    b29 = b12[0] if label0num > b28 else b12[1]
    b30 = max(label0num, b28)
    if b30 = = len(b8) or not b7 or curdepth > maxdepth:
        return class1(b29)
    nlabels, ylabels, score, b27 = [], [], -1, None
    for i in b7:
        currentscore, currentnlabels, b31 = fonk4(b7[i], b8)
        if currentscore >= score:
            score, nlabels, ylabels, b27 = currentscore, currentnlabels, b31, i
    curdepth += 1
    nfeatures, b32 = fonk5(b27, b7)
    b24 = fonk8(nlabels, nfeatures, b12, curdepth, maxdepth)
    b26 = fonk8(ylabels, b32, b12, curdepth, maxdepth)
    return class1(b12[0], b24, b26, b27)
def fonk9(node, file_path, output):
    data, b9, count, b33 = [], [], 0, 0
    with open(file_path, 'r') as allData:
        b10 = csv.b10(allData)
        for row in b10:
            if b33 = = 0:
                for b23 in range(len(row) - 1):
                    b9.append(row[b23])
            else:
                b34 = {b9[b23]: row[b23] for b23 in range(len(row) - 1)}
                b35 = fonk10(node, b34)
                data.append(b35 + '\n')
                if b35 != row[-1]:
                    count += 1
            b33 += 1
    with open(output, 'w') as f:
        f.writelines(data)
    return 1.0 * count / (b33 - 1)
def fonk10(node, b34):
    if node.fonk7():
        return node.b25
    if b34[node.b27] in ('n', 'notA', 'no'):
        return fonk10(node.b24, b34)
    return fonk10(node.b26, b34)
def fonk11(b1, b2, b3, b4, b5, b6):
    b36 = fonk1(b1)
    train_labelList, train_features, b37 = b36
    b38 = fonk8(train_labelList, train_features, b37, 0, b3)
    b39 = fonk9(b38, b1, b4)
    b40 = fonk9(b38, b2, b5)
    with open(b6, 'w') as f:
        f.write(f'error(train): {b39}\n')
        f.write(f'error(test): {b40}\n')
if b41 = = '__main__':
    fonk11(b1, b2, b3, b4, b5, b6)