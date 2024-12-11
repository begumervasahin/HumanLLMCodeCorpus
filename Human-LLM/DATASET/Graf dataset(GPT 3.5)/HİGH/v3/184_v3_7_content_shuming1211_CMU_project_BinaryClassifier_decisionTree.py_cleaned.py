import sys
import csv
import math
class class1:
    def fonk1(self, b2, b1 = None, b3=None, b4=None):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return self.b1 is None and self.b3 is None
def fonk3(train_input):
    b5 = {}
    b6 = []
    b7 = []
    with open(train_input) as all_data:
        b8 = csv.b8(all_data)
        for row in b8:
            if not b7:
                b7 = [[row[b21]] for b21 in range(len(row)-1)]
            else:
                for b21 in range(len(row)-1):
                    b7[b21].append(row[b21])
            b6.append(row[-1])
        for j in range(len(row)-1):
            b9 = b7[j].pop(0)
            b5[b9] = b7[j]
    b10 = list(set(b6))
    return b6, b5, b10
def fonk4(b6, b10):
    b11 = b6.count(b10[0])
    b12 = len(b6) - b11
    return b11, b12
def fonk5(b6, b10):
    b11, b12 = fonk4(b6, b10)
    if b11 = = 0 or b12 == 0:
        return 0
    b13 = 1.0 * b11 / len(b6)
    b14 = 1.0 * b12 / len(b6)
    return -b13 * math.log(b13, 2) - b14 * math.log(b14, 2)
def fonk6(b4, b6):
    b15 = [b6[i] for i in range(len(b4)) if b4[i] in ('n', 'notA', 'no')]
    b16 = [b6[i] for i in range(len(b4)) if b4[i] not in ('n', 'notA', 'no')]
    b10 = list(set(b6))
    b14 = 1.0 * len(b15) / len(b6)
    b17 = 1.0 * len(b16) / len(b6)
    return fonk5(b6, b10) - (b14 * fonk5(b15, b10)) - (b17 * fonk5(b16, b10)), b15, b16
def fonk7(b4, b5):
    b18 = {}
    b19 = {}
    b20 = len(b5[b4])
    for b21 in b5:
        if b21 = = b4:
            continue
        b18[b21] = []
        b19[b21] = []
        for j in range(b20):
            if b5[b4][j] in ('n', 'notA', 'no'):
                b18[b21].append(b5[b21][j])
            else:
                b19[b21].append(b5[b21][j])
    return b18, b19
def fonk8(b6, b5, b10, cur_depth, max_depth):
    label0_num, b22 = fonk4(b6, b10)
    if label0_num > b22:
        b23 = b10[0]
        b24 = label0_num
    else:
        b23 = b10[1]
        b24 = b22
    if b24 = = len(b6):
        return class1(b23)
    elif len(b5) == 0:
        return class1(b23)
    elif cur_depth > max_depth:
        return class1(b23)
    else:
        b15 = []
        b16 = []
        a1 = -1
        b4 = []
        for i in b5:
            current_score, current_n_labels, b25 = fonk6(b5[i], b6)
            if current_score >= a1:
                a1 = current_score
                b15 = current_n_labels
                b16 = b25
                b4 = i
        cur_depth += 1
        b18, b19 = fonk7(b4, b5)
        b1 = fonk8(b15, b18, b10, cur_depth, max_depth)
        b3 = fonk8(b16, b19, b10, cur_depth, max_depth)
        return class1(b10[0], b1, b3, b4)
def fonk9(b30, test_input, output):
    with open(test_input) as all_data:
        b8 = csv.b8(all_data)
        b26 = []
        b7 = next(b8)[:-1]
        for row in b8:
            b27 = {b7[b21]: row[b21] for b21 in range(len(row)-1)}
            b28 = fonk10(b30, b27)
            b26.append(b28 + '\n')
    with open(output, 'w') as f:
        f.writelines(b26)
def fonk10(b30, b27):
    if b30.fonk2():
        return b30.b2
    else:
        if b27[b30.b4] in ('n', 'notA', 'no'):
            return fonk10(b30.b1, b27)
        else:
            return fonk10(b30.b3, b27)
def fonk11(train_input, test_input, b35, train_out, test_out, b34):
    train_label_list, train_features, b29 = fonk3(train_input)
    b30 = fonk8(train_label_list, train_features, b29, 0, b35)
    fonk9(b30, train_input, train_out)
    fonk9(b30, test_input, test_out)
    b31 = fonk9(b30, train_input, train_out)
    b32 = fonk9(b30, test_input, test_out)
    with open(b34, 'w') as f:
        f.write(f'error(train): {b31}\nerror(test): {b32}')
if b33 = = '__main__':
    if len(sys.argv) != 7:
        print("Usage: python script.py train_input test_input b35 train_out test_out b34")
        sys.exit(1)
    train_input, test_input, b35, train_out, test_out, b34 = sys.argv[1:]
    b35 = int(b35)
    fonk11(train_input, test_input, b35, train_out, test_out, b34)