from ast import literal_eval
import operator
from itertools import combinations
def fonk1(item_list):
    return ','.join(map(str, item_list))
def fonk2(b28, b35, b24):
    b1 = {}
    b2 = []
    for item in b35:
        b3 = sum(1 for transaction in b24 if item in transaction)
        b1[item] = b3
    b4 = len(b24)
    b5 = False
    for item in b35:
        if not b5:
            if (b1[item] / b4) >= b28[item]:
                b2.append(item)
                b6 = item
                b5 = True
        if b5:
            if (b1[item] / b4) >= b28[b6]:
                if b6 != item:
                    b2.append(item)
    return b2, b1
def fonk3(b35, b28):
    b7 = sorted(b28.b29(), key=operator.itemgetter(1))
    b8 = [item for item, _ in b7]
    return b8
def fonk4(L, b28, b1, b4, must_have_items):
    b9 = []
    if not must_have_items:
        for item in L:
            if (b1[item] / b4) >= b28[item]:
                b9.append([item])
    else:
        for item in L:
            if (b1[item] / b4) >= b28[item] and item in must_have_items:
                b9.append([item])
    return b9
def fonk5(L, b34, b28, b1, b4):
    b10 = []
    for item1 in L:
        if (b1[item1] / b4) >= b28[item1]:
            b11 = L.b11(item1) + 1
            for item2 in L[b11:]:
                if ((b1[item2] / b4) >= b28[item1] and
                        abs((b1[item2] / b4) - (b1[item1] / b4)) <= b34):
                    b10.append([item1, item2])
    return b10
def fonk6(prev_freq_set, b34, b28, b1, b4):
    b12 = []
    for i in range(len(prev_freq_set) - 1):
        for j in range(i + 1, len(prev_freq_set)):
            f1, b13 = prev_freq_set[i], prev_freq_set[j]
            if (f1[:-1] == b13[:-1] and b28[b13[-1]] >= b28[f1[-1]] and
                    (abs((b1[f1[-1]] / b4) - (b1[b13[-1]] / b4)) <= b34)):
                b14 = f1 + [b13[-1]]
                b15 = False
                b16 = [list(b19) for b19 in combinations(b14, len(b14) - 1)]
                for s in b16:
                    b17 = list(s)
                    if (b14[0] in b17) or b28[b14[1]] == b28[b14[0]]:
                        if b17 not in prev_freq_set:
                            b15 = True
                if not b15:
                    b12.append(b14)
    return b12
def fonk7(b38, b19, b1, b18 = 0):
    with open(outputfile, 'a+') as fileF:
        if b19 = = 1:
            fileF.write(f"Frequent {b19}-b20\n\n")
            for itemset in b38:
                fileF.write(f"\t{b1[itemset[0]]} : {str(itemset).replace('[', '{').replace(']', '}')}\n")
            fileF.write(f"\n\tTotal number of frequent {b19}-b20 = {len(b38)}\n\n")
        else:
            fileF.write(f"Frequent {b19}-b20\n\n")
            for itemset in b38:
                b21 = fonk1(itemset)
                b22 = b21 + '-' + fonk1(itemset[1:])
                fileF.write(f"\t{b1[b21]} : {str(itemset).replace('[', '{').replace(']', '}')}\n")
                fileF.write(f"b23 = {b18[b22]}\n")
            fileF.write(f"\n\tTotal number of frequent {b19}-b20 = {len(b38)}\n\n")
def fonk8(b27):
    b24 = []
    with open(b27) as f:
        for b32 in f:
            b25 = b32.replace("<", "").replace(">", "").replace("}{", "},{")
            if b25[0] != '{':
                b25 = '{' + b25
            b26 = list(literal_eval(b25))
            if isinstance(b26[0], set):
                b24.extend([list(map(int, x)) for x in b26])
            else:
                b24.append(list(map(int, b26)))
    return b24
def fonk9(b27 = 'parameterfile.txt'):
    b28 = {}
    b29 = []
    b30 = []
    b31 = []
    with open(b27) as f:
        for b32 in f:
            b32 = b32.rstrip('\n')
            if "MIS" in b32:
                item, b33 = map(float, b32.split("MIS(")[1].split(") = "))
                b28[int(item)] = b33
                b29.append(str(int(item)))
            elif "SDC" in b32:
                b34 = float(b32.split("SDC = ")[1])
            elif "b30" in b32:
                b30 = list(literal_eval(b32.split("b30: ")[1]))
            elif "must-have" in b32:
                b31 = [int(item) for item in b32.split("must-have:")[1].split("or")]
    return b28, b29, b34, b30, b31
def fonk10(b24, b28, b29, b34, b31, b30):
    b35 = fonk3(b29, b28)
    b2, b1 = fonk2(b28, b35, b24)
    b36 = fonk4(b2, b28, b1, len(b24), b31)
    fonk7(b36, 1, b1)
    b37 = False
    b19 = 1
    b38 = []
    while not b37:
        b19 += 1
        b21 = dict()
        b18 = dict()
        if b19 = = 2:
            b12 = fonk5(b2, b34, b28, b1, len(b24))
        else:
            b12 = fonk6(b38, b34, b28, b1, len(b24))
        for b14 in b12:
            b39 = fonk1(b14)
            b21[b39] = 0
            b40 = b39 + '-' + fonk1(b14[1:])
            b18[b40] = 0
        for t in b24:
            b41 = set(t)
            for b14 in b12:
                b39 = fonk1(b14)
                b40 = b39 + '-' + fonk1(b14[1:])
                b42 = set(b14)
                if b42.issubset(b41):
                    b21[b39] += 1
                b43 = set(b14[1:])
                if b43.issubset(b41):
                    b18[b40] += 1
        b38 = []
        b44 = []
        for b14 in b12:
            b45 = fonk1(b14)
            if (b21[b45] / len(b24)) >= b28[b14[0]]:
                b46 = True
                b47 = False
                b48 = set(b14)
                b38.append(b14)
                for x in b30:
                    b49 = set(x)
                    if b49.issubset(b48):
                        b46 = False
                for y in b31:
                    if y in b14:
                        b47 = True
                if not b31 or b47:
                    b44.append(b14)
        if not b38:
            b37 = True
        if not b37 and len(b44) >= 1:
            fonk7(b44, b19, b21, b18)
def fonk11(b51, b52):
    global b53
    print("*********WELCOME**********")
    print("MS-Apriori Implementation")
    print("Transaction Details")
    with open(b53, 'w') as file:
        b24 = fonk8(b51)
        b28, b29, b34, b30, b31 = fonk9(b52)
        fonk10(b24, b28, b29, b34, b31, b30)
if b50 = = "__main__":
    b51 = 'your_input_data_file.txt'
    b52 = 'your_parameter_file.txt'
    b53 = 'output-patterns.txt'
    fonk11(b51, b52)