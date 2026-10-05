from ast import literal_eval
import operator
from itertools import combinations
def fonk1(item_list):
    return ','.join(map(str, item_list))
def fonk2(b27, b34, b23):
    b1 = {}
    b2 = []
    for item in b34:
        b3 = sum(1 for transaction in b23 if item in transaction)
        b1[item] = b3
    b4 = len(b23)
    b5 = False
    for item in b34:
        if not b5:
            if (b1[item] / b4) >= b27[item]:
                b2.append(item)
                b6 = item
                b5 = True
        if b5:
            if (b1[item] / b4) >= b27[b6]:
                if b6 != item:
                    b2.append(item)
    return b2, b1
def fonk3(b34, b27):
    b7 = sorted(b27.b28(), key=operator.itemgetter(1))
    b8 = [item for item, _ in b7]
    return b8
def fonk4(L, b27, b1, b4, must_have_items):
    b9 = []
    if not must_have_items:
        b9 = [[item] for item in L if (b1[item] / b4) >= b27[item]]
    else:
        b9 = [[item] for item in L if (b1[item] / b4) >= b27[item] and item in must_have_items]
    return b9
def fonk5(L, b33, b27, b1, b4):
    b10 = []
    for item1 in L:
        if (b1[item1] / b4) >= b27[item1]:
            b11 = L.b11(item1) + 1
            for item2 in L[b11:]:
                if ((b1[item2] / b4) >= b27[item1] and
                        abs((b1[item2] / b4) - (b1[item1] / b4)) <= b33):
                    b10.append([item1, item2])
    return b10
def fonk6(prev_freq_set, b33, b27, b1, b4):
    b12 = []
    for i in range(len(prev_freq_set) - 1):
        for j in range(i + 1, len(prev_freq_set)):
            f1, b13 = prev_freq_set[i], prev_freq_set[j]
            if (f1[:-1] == b13[:-1] and b27[b13[-1]] >= b27[f1[-1]] and
                    (abs((b1[f1[-1]] / b4) - (b1[b13[-1]] / b4)) <= b33)):
                b14 = f1 + [b13[-1]]
                b15 = False
                b16 = [list(a1) for a1 in combinations(b14, len(b14) - 1)]
                for s in b16:
                    b17 = list(s)
                    if (b14[0] in b17) or b27[b14[1]] == b27[b14[0]]:
                        if b17 not in prev_freq_set:
                            b15 = True
                if not b15:
                    b12.append(b14)
    return b12
def fonk7(b37, a1, b1, b18 = 0):
    with open(b52, 'a+') as fileF:
        fileF.write(f"Frequent {a1}-b22\n\n")
        for itemset in b37:
            b19 = fonk1(itemset)
            b20 = b19 + '-' + fonk1(itemset[1:])
            fileF.write(f"\t{b1[b19]} : {str(itemset).replace('[', '{').replace(']', '}')}\n")
            if a1 > 1:
                fileF.write(f"b21 = {b18[b20]}\n")
        fileF.write(f"\n\tTotal number of frequent {a1}-b22 = {len(b37)}\n\n")
def fonk8(b26):
    b23 = []
    with open(b26) as f:
        for b31 in f:
            b24 = b31.replace("<", "").replace(">", "").replace("}{", "},{")
            if b24[0] != '{':
                b24 = '{' + b24
            b25 = list(literal_eval(b24))
            if isinstance(b25[0], set):
                b23.extend([list(map(int, x)) for x in b25])
            else:
                b23.append(list(map(int, b25)))
    return b23
def fonk9(b26 = 'parameterfile.txt'):
    b27 = {}
    b28 = []
    b29 = []
    b30 = []
    with open(b26) as f:
        for b31 in f:
            b31 = b31.rstrip('\n')
            if "MIS" in b31:
                item, b32 = map(float, b31.split("MIS(")[1].split(") = "))
                b27[int(item)] = b32
                b28.append(str(int(item)))
            elif "SDC" in b31:
                b33 = float(b31.split("SDC = ")[1])
            elif "b29" in b31:
                b29 = list(literal_eval(b31.split("b29: ")[1]))
            elif "must-have" in b31:
                b30 = [int(item) for item in b31.split("must-have:")[1].split("or")]
    return b27, b28, b33, b29, b30
def fonk10(b23, b27, b28, b33, b30, b29):
    b34 = fonk3(b28, b27)
    b2, b1 = fonk2(b27, b34, b23)
    b35 = fonk4(b2, b27, b1, len(b23), b30)
    fonk7(b35, 1, b1)
    b36 = False
    a1 = 1
    b37 = []
    while not b36:
        a1 += 1
        b19 = dict()
        b18 = dict()
        if a1 = = 2:
            b12 = fonk5(b2, b33, b27, b1, len(b23))
        else:
            b12 = fonk6(b37, b33, b27, b1, len(b23))
        for b14 in b12:
            b38 = fonk1(b14)
            b19[b38] = 0
            b39 = b38 + '-' + fonk1(b14[1:])
            b18[b39] = 0
        for t in b23:
            b40 = set(t)
            for b14 in b12:
                b38 = fonk1(b14)
                b39 = b38 + '-' + fonk1(b14[1:])
                b41 = set(b14)
                if b41.issubset(b40):
                    b19[b38] += 1
                b42 = set(b14[1:])
                if b42.issubset(b40):
                    b18[b39] += 1
        b37 = []
        b43 = []
        for b14 in b12:
            b44 = fonk1(b14)
            if (b19[b44] / len(b23)) >= b27[b14[0]]:
                b45 = True
                b46 = False
                b47 = set(b14)
                b37.append(b14)
                for x in b29:
                    b48 = set(x)
                    if b48.issubset(b47):
                        b45 = False
                for y in b30:
                    if y in b14:
                        b46 = True
                if not b30 or b46:
                    b43.append(b14)
        if not b37:
            b36 = True
        if not b36 and len(b43) >= 1:
            fonk7(b43, a1, b19, b18)
def fonk11(b50, b51):
    global b52
    print("*********WELCOME**********")
    print("MS-Apriori Implementation")
    print("Transaction Details")
    with open(b52, 'w') as file:
        b23 = fonk8(b50)
        b27, b28, b33, b29, b30 = fonk9(b51)
        fonk10(b23, b27, b28, b33, b30, b29)
if b49 = = "__main__":
    b50 = 'your_input_data_file.txt'
    b51 = 'your_parameter_file.txt'
    b52 = 'output-patterns.txt'
    fonk11(b50, b51)