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
def fonk3(file_path):
    b5 = {}
    b6 = []
    with open(file_path, 'r') as file:
        b7 = csv.b7(file)
        b8 = next(b7)[:-1]
        for row in b7:
            b6.append(row[-1])
            for index, value in enumerate(row[:-1]):
                b5.setdefault(b8[index], []).append(value)
    b9 = list(set(b6))
    return b6, b5, b9
def fonk4(b6, b9):
    b10 = b6.count(b9[0])
    b11 = len(b6) - b10
    return b10, b11
def fonk5(b6, b9):
    b10, b11 = fonk4(b6, b9)
    if b10 = = 0 or b11 == 0:
        return 0
    b12 = b10 / len(b6)
    b13 = b11 / len(b6)
    return -b12 * math.log(b12, 2) - b13 * math.log(b13, 2)
def fonk6(b4, b6):
    b14 = [label for index, label in enumerate(b6) if b4[index] in ['n', 'notA', 'no']]
    b15 = [label for index, label in enumerate(b6) if b4[index] not in ['n', 'notA', 'no']]
    b13 = len(b14) / len(b6)
    b16 = len(b15) / len(b6)
    return fonk5(b6, set(b6)) - (b13 * fonk5(b14, set(b6))) - (b16 * fonk5(b15, set(b6))), b14, b15
def fonk7(b4, b5):
    b17 = {key: [] for key in b5.keys() if key != b4}
    b18 = {key: [] for key in b5.keys() if key != b4}
    for index, value in b5.items():
        for j, item in enumerate(value):
            if b5[b4][j] in ['n', 'notA', 'no']:
                b17[index].append(item)
            else:
                b18[index].append(item)
    return b17, b18
def fonk8(b6, b5, b9, cur_depth, max_depth):
    b21, b19 = fonk4(b6, b9)
    if b21 >= b19:
        b20 = b9[0]
    else:
        b20 = b9[1]
    if b21 = = len(b6) or b19 == len(b6) or not b5 or cur_depth >= max_depth:
        return class1(b20)
    else:
        a1 = -1
        b22 = None
        b23 = []
        b24 = []
        for b4, values in b5.items():
            score, b14, b15 = fonk6(values, b6)
            if score >= a1:
                a1 = score
                b22 = b4
                b23 = b14
                b24 = b15
        cur_depth += 1
        b17, b18 = fonk7(b22, b5)
        b1 = fonk8(b23, b17, b9, cur_depth, max_depth)
        b3 = fonk8(b24, b18, b9, cur_depth, max_depth)
        return class1(b9[0], b1, b3, b22)
def fonk9(node, test_input, output):
    with open(test_input, 'r') as file:
        b7 = csv.b7(file)
        next(b7)
        b25 = [fonk10(node, row) + '\n' for row in b7]
    with open(output, 'w') as file:
        file.writelines(b25)
def fonk10(node, row):
    if node.fonk2():
        return node.b2
    else:
        if row[node.b4] in ['n', 'notA', 'no']:
            return fonk10(node.b1, row)
        else:
            return fonk10(node.b3, row)
def fonk11(train_input, test_input, depth, train_out, test_out, b32):
    train_labels, train_features, b26 = fonk3(train_input)
    b27 = fonk8(train_labels, train_features, b26, 0, depth)
    fonk9(b27, train_input, train_out)
    fonk9(b27, test_input, test_out)
    b28 = "Implement calculation of training error"
    b29 = "Implement calculation of testing error"
    b30 = f'error(train): {b28}\nerror(test): {b29}'
    with open(b32, 'w') as file:
        file.write(b30)
if b31 = = '__main__':
    if len(sys.argv) != 7:
        print("Usage: python script.py train_input test_input depth train_out test_out b32")
    else:
        train_input, test_input, depth, train_out, test_out, b32 = sys.argv[1:]
        fonk11(train_input, test_input, int(depth), train_out, test_out, b32)