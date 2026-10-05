from ast import literal_eval
import operator
from itertools import combinations
def fonk1(list_l):
    b1 = ','.join(map(str, list_l))
    return b1
def fonk2(b30, b7, b27):
    b2 = {}
    b3 = []
    for x in b7:
        a1 = 0
        for i in range(len(b27)):
            if x in b27[i]:
                a1 += 1
        b2[x] = a1
    b4 = len(b27)
    b5 = False
    for x in b7:
        if not b5:
            if (b2[x] / b4) >= b30[x]:
                b3.append(x)
                b6 = x
                b5 = True
        if b5:
            if (b2[x] / b4) >= b30[b6]:
                if b6 != x:
                    b3.append(x)
    return b3, b2
def fonk3(b31, b30):
    b7 = []
    b8 = sorted(b30.items(), key=operator.itemgetter(1))
    for i in range(len(b8)):
        val1, b9 = b8[i]
        b7.append(val1)
    for i in range(len(b7)):
        b7[i] = (b7[i])
    return b7
def fonk4(b3, b30, b2, b4, b33):
    b10 = []
    if not b33:
        for x in b3:
            if (b2[x] / b4) >= b30[x]:
                b11 = [x]
                b10.append(b11)
    else:
        for x in b3:
            if (b2[x] / b4) >= b30[x] and x in b33:
                b11 = [x]
                b10.append(b11)
    return b10
def fonk5(b3, b36, b30, b2, b4):
    b12 = []
    for l in b3:
        if (b2[l] / b4) >= b30[l]:
            b13 = b3.index(l) + 1
            for h in b3[b13:]:
                if ((b2[h] / b4) >= b30[l]) and (abs((b2[h] / b4) - (b2[l] / b4)) <= b36):
                    b11 = [l, h]
                    b12.append(b11)
    return b12
def fonk6(F, b36, b30, b2, b4):
    b14 = []
    for i in range(len(F) - 1):
        for j in range(i + 1, len(F)):
            f1, b15 = F[i], F[j]
            if (f1[:-1] == b15[:-1] and b30[b15[-1]] >= b30[f1[-1]]
                    and (abs((b2[f1[-1]] / b4) - (b2[b15[-1]] / b4)) <= b36)):
                b16 = f1 + [b15[-1]]
                b17 = False
                b18 = [list(b22) for b22 in combinations(b16, len(b16) - 1)]
                for s in b18:
                    b19 = list(s)
                    if (b16[0] in b19) or b30[b16[1]] == b30[b16[0]]:
                        if b19 not in F:
                            b17 = True
                if not b17:
                    b14.append(b16)
    return b14
def fonk7(b38, b22, b2, b20 = 0):
    b21 = open(b56, 'a+')
    if b22 = = 1:
        b21.write(b52"Frequent {b22}-b23\b4\b4")
        for b52 in b38:
            b21.write(b52"\t{b2[b52[0]]} : {str(b52).replace('[', '{').replace(']', '}')}\b4")
        b21.write(b52"\b4\tTotal number of frequent {b22}-b23 = {len(b38)}\b4\b4")
    else:
        b21.write(b52"Frequent {b22}-b23\b4\b4")
        for b52 in b38:
            b24 = fonk1(b52)
            b25 = b24 + '-' + fonk1(b52[1:])
            b21.write(b52"\t{b2[b24]} : {str(b52).replace('[', '{').replace(']', '}')}\b4")
            b21.write(b52"b26 = {b20[b25]}\b4")
        b21.write(b52"\b4\tTotal number of frequent {b22}-b23 = {len(b38)}\b4\b4")
    b21.close()
def fonk8(b29):
    b27 = []
    with open(b29) as b52:
        for b34 in b52:
            b28 = b34.replace("<", "")
            b28 = b28.replace(">", "")
            b28 = b28.replace("}{", "},{")
            if b28[0] != '{':
                b28 = '{' + b28
            b11 = list(literal_eval(b28))
            if isinstance(b11[0], set):
                b27.extend([list(map(int, x)) for x in b11])
            else:
                b27.append(list(map(int, b11)))
    return b27
def fonk9(b29 = 'parameterfile.txt'):
    b30 = {}
    b31 = []
    b32 = []
    b33 = []
    with open(b29) as b52:
        for b34 in b52:
            b34 = b34.rstrip('\b4')
            if "b8" in b34:
                a, b35 = b34.split("b8(")
                a, b35 = b35.split(") = ")
                b30[int(a)] = float(b35)
                b31.append(a)
            elif "b36" in b34:
                a, b35 = b34.split("b36 = ")
                b36 = float(b35)
            elif "b32" in b34:
                a, b35 = b34.split("b32: ")
                b11 = list(literal_eval(b35))
                if isinstance(b11[0], set):
                    b32.extend(list(map(list, b11)))
                else:
                    b32.append(list(b11))
            elif "must-have" in b34:
                a, b35 = b34.split("must-have:")
                b33 = [int(aa) for aa in b35.split("or")]
    return b30, b31, b36, b32, b33
def fonk10(b27, b30, b31, b36, b33, b32):
    b7 = fonk3(b31, b30)
    b3, b2 = fonk2(b30, b7, b27)
    b10 = fonk4(b3, b30, b2, len(b27), b33)
    fonk7(b10, 1, b2)
    b37 = False
    b22 = 1
    b38 = []
    while not b37:
        b22 += 1
        b39 = dict()
        b40 = dict()
        if b22 = = 2:
            b14 = fonk5(b3, b36, b30, b2, len(b27))
        else:
            b14 = fonk6(b38, b36, b30, b2, len(b27))
        for b16 in b14:
            b41 = fonk1(b16)
            b39[b41] = 0
            b42 = b41 + '-' + fonk1(b16[1:])
            b40[b42] = 0
        for t in b27:
            b43 = set(t)
            for b16 in b14:
                b41 = fonk1(b16)
                b42 = b41 + '-' + fonk1(b16[1:])
                b44 = set(b16)
                if b44.issubset(b43):
                    b39[b41] += 1
                b45 = set(b16[1:])
                if b45.issubset(b43):
                    b40[b42] += 1
        b38 = []
        b46 = []
        for b16 in b14:
            b47 = fonk1(b16)
            if (b39[b47] / len(b27)) >= b30[b16[0]]:
                b48 = True
                b49 = False
                b50 = set(b16)
                b38.append(b16)
                for x in b32:
                    b51 = set(x)
                    if b51.issubset(b50):
                        b48 = False
                for y in b33:
                    if y in b16:
                        b49 = True
                if not b33 or b49:
                    b46.append(b16)
        if not b38:
            b37 = True
        if not b37 and len(b46) >= 1:
            fonk7(b46, b22, b39, b40)
def fonk11(b54, b55):
    global b56
    print("*********WELCOME**********")
    print("b30-Apriori Implementation")
    print("Transaction Details")
    b52 = open(b56, 'w')
    b27 = fonk8(b54)
    b30, b31, b36, b32, b33 = fonk9(b55)
    fonk10(b27, b30, b31, b36, b33, b32)
    b52.close()
if b53 = = "__main__":
    b54 = 'your_input_data_file.txt'
    b55 = 'your_parameter_file.txt'
    b56 = 'output-patterns.txt'
    fonk11(b54, b55)