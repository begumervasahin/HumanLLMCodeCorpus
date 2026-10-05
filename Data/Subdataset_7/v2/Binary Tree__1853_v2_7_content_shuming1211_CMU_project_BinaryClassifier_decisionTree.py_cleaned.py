import sys
import csv
import math
def fonk1(train_input):
    b1 = {}
    b2 = []
    b3 = []
    with open(train_input) as allData:
        b4 = csv.b4(allData)
        for row in b4:
            if not b3:
                b3 = [[row[b17]] for b17 in range(len(row)-1)]
            else:
                for b17 in range(len(row)-1):
                    b3[b17].append(row[b17])
            b2.append(row[-1])
        for j in range(len(row)-1):
            b5 = b3[j].pop(0)
            b1[b5] = b3[j]
    b6 = list(set(b2))
    return b2, b1, b6
def fonk2(b2, b6):
    b7 = b2.count(b6[0])
    b8 = len(b2) - b7
    return b7, b8
def fonk3(b2, b6):
    b7, b8 = fonk2(b2, b6)
    if b7 = = 0 or b8 == 0:
        return 0
    b9 = 1.0 * b7 / len(b2)
    b10 = 1.0 * b8 / len(b2)
    return -b9 * math.log(b9, 2) - b10 * math.log(b10, 2)
def fonk4(b21, b2):
    b11 = [b2[i] for i in range(len(b21)) if b21[i] in ('n', 'notA', 'no')]
    b12 = [b2[i] for i in range(len(b21)) if b21[i] not in ('n', 'notA', 'no')]
    b6 = list(set(b2))
    b10 = 1.0 * len(b11) / len(b2)
    b13 = 1.0 * len(b12) / len(b2)
    return fonk3(b2, b6) - (b10 * fonk3(b11, b6)) - (b13 * fonk3(b12, b6)), b11, b12
def fonk5(b21, b1):
    b14 = {}
    b15 = {}
    b16 = len(b1[b21])
    for b17 in b1:
        if b17 = = b21:
            continue
        b14[b17] = []
        b15[b17] = []
        for j in range(b16):
            if b1[b21][j] in ('n', 'notA', 'no'):
                b14[b17].append(b1[b17][j])
            else:
                b15[b17].append(b1[b17][j])
    return b14, b15
class class1(object):
    def fonk6(self, b19, b18 = None, b20=None, b21=None):
        self.b19 = b19
        self.b18 = b18
        self.b20 = b20
        self.b21 = b21
    def fonk7(self):
        return self.b18 is None and self.b20 is None
def fonk8(b2, b1, b6, curdepth, maxdepth):
    label0num, b22 = fonk2(b2, b6)
    if label0num > b22:
        b23 = b6[0]
        b24 = label0num
    else:
        b23 = b6[1]
        b24 = b22
    if b24 = = len(b2):
        return class1(b23)
    elif len(b1) == 0:
        return class1(b23)
    elif curdepth > maxdepth:
        return class1(b23)
    else:
        b25 = []
        b26 = []
        a1 = -1
        b21 = []
        for i in b1:
            currentscore, currentnlabels, b27 = fonk4(b1[i], b2)
            if currentscore >= a1:
                a1 = currentscore
                b25 = currentnlabels
                b26 = b27
                b21 = i
        curdepth += 1
        nfeatures, b28 = fonk5(b21, b1)
        b18 = fonk8(b25, nfeatures, b6, curdepth, maxdepth)
        b20 = fonk8(b26, b28, b6, curdepth, maxdepth)
        return class1(b6[0], b18, b20, b21)
def fonk9(b33, test_input, output):
    with open(test_input) as allData:
        b4 = csv.b4(allData)
        b29 = []
        b3 = next(b4)[:-1]
        for row in b4:
            b30 = {b3[b17]: row[b17] for b17 in range(len(row)-1)}
            b31 = fonk10(b33, b30)
            b29.append(b31 + '\n')
    with open(output, 'w') as f:
        f.writelines(b29)
def fonk10(b33, b30):
    if b33.fonk7():
        return b33.b19
    else:
        if b30[b33.b21] in ('n', 'notA', 'no'):
            return fonk10(b33.b18, b30)
        else:
            return fonk10(b33.b20, b30)
def fonk11(train_input, test_input, b38, train_out, test_out, b37):
    train_labelList, train_features, b32 = fonk1(train_input)
    b33 = fonk8(train_labelList, train_features, b32, 0, b38)
    fonk9(b33, train_input, train_out)
    fonk9(b33, test_input, test_out)
    b34 = fonk9(b33, train_input, train_out)
    b35 = fonk9(b33, test_input, test_out)
    with open(b37, 'w') as f:
        f.write(f'error(train): {b34}\nerror(test): {b35}')
if b36 = = '__main__':
    if len(sys.argv) != 7:
        print("Usage: python script.py train_input test_input b38 train_out test_out b37")
        sys.exit(1)
    train_input, test_input, b38, train_out, test_out, b37 = sys.argv[1:]
    b38 = int(b38)
    fonk11(train_input, test_input, b38, train_out, test_out, b37)