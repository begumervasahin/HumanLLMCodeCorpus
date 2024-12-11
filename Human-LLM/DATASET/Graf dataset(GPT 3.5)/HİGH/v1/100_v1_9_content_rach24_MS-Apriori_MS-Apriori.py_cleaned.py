from ast import literal_eval
import operator
from itertools import combinations
def fonk1(list_l):
    b1 = ','.join(map(str, list_l))
    return b1
def fonk2(b33, b7, b29):
    b2 = {}
    b3 = []
    for x in b7:
        a1 = 0
        for i in range(len(b29)):
            if x in b29[i]:
                a1 += 1
        b2[x] = a1
    b4 = len(b29)
    b5 = False
    for x in b7:
        if b5 = = False:
            if (b2[x] / b4) >= b33[x]:
                b3.append(x)
                b6 = x
                b5 = True
        if b5 = = True:
            if (b2[x] / b4) >= b33[b6]:
                if (b6 != x):
                    b3.append(x)
    return b3, b2
def fonk3(b34, b33):
    b7 = []
    b8 = sorted(b33.items(), key=operator.itemgetter(1))
    for i in range(len(b8)):
        val1, b9 = b8[i]
        b7.append(val1)
    for i in range(len(b7)):
        b7[i] = (b7[i])
    return b7
def fonk4(b3, b33, b2, b4, b36):
    b10 = []
    if (len(b36) == 0):
        for x in b3:
            if ((b2[x] / b4) >= b33[x]):
                b11 = []
                b11.append(x)
                b10.append(b11)
    else:
        for x in b3:
            if ((b2[x] / b4) >= b33[x]) and (x in b36):
                b11 = []
                b11.append(x)
                b10.append(b11)
    return b10
def fonk5(b3, b39, b33, b2, b4):
    b12 = []
    for l in b3:
        if (b2[l] / b4) >= b33[l]:
            b13 = b3.index(l) + 1
            for h in b3[b13:]:
                if (((b2[h] / b4) >= b33[l]) and (abs((b2[h] / b4) - (b2[l] / b4)) <= b39)):
                    b11 = [l, h]
                    b12.append(b11)
    return b12
def fonk6(F, b39, b33, b2, b4):
    b14 = []
    for i in range(len(F)-1):
        for j in range(i+1, len(F)):
            b15 = F[i]
            b16 = F[j]
            if (b15[:(len(b15)-1)] == b16[:(len(b16)-1)] and b33[b16[len(b16)-1]] >= b33[b15[len(b15)-1]] and (abs((b2[b15[len(b15)-1]]/b4) - (b2[b16[len(b16)-1]]/b4)) <= b39)):
                b17 = []
                for x in b15:
                    b17.append(x)
                b17.append(b16[-1])
                b14.append(b17)
                b18 = False
                b19 = [list(b23) for b23 in combinations(b17, len(b17) - 1)]
                for s in b19:
                    b20 = list(s)
                    if (b17[0] in b20) or b33[b17[1]] == b33[b17[0]]:
                        if b20 not in F:
                            b18 = True
                if b18 = = True:
                    b14.remove(b17)
    return b14
def fonk7(b41, b23, b2, b21 = 0):
    b22 = open(b58, 'a+')
    if b23 = = 1:
        b22.write("Frequent ")
        b22.write(str(b23))
        b22.write("-b25\b4\b4")
        for b54 in b41:
            b22.write("\t")
            b22.write(str(b2[b54[0]]))
            b22.write(" : ")
            b11 = str(b54)
            b24 = b11.replace("[", "{")
            b11 = b24.replace("]", "}")
            b22.write(b11)
            b22.write("\b4")
        b22.write("\b4\tTotal number of frequent ")
        b22.write(str(b23))
        b22.write("-b25 = ")
        b22.write(str(len(b41)))
        b22.write("\b4\b4")
    else:
        b22.write("Frequent ")
        b22.write(str(b23))
        b22.write("-b25\b4\b4")
        for b54 in b41:
            b26 = fonk1(b54)
            b27 = b26 + '-' + fonk1(b54[1:])
            b22.write("\t")
            b22.write(str(b2[b26]))
            b22.write(" : ")
            b11 = str(b54)
            b24 = b11.replace("[", "{")
            b11 = b24.replace("]", "}")
            b22.write(b11)
            b22.write("\b4")
            b22.write("b28 = ")
            b22.write(str(b21[b27]))
            b22.write("\b4")
        b22.write("\b4\tTotal number of frequent ")
        b22.write(str(b23))
        b22.write("-b25 = ")
        b22.write(str(len(b41)))
        b22.write("\b4\b4")
    b22.close()
def fonk8(b32):
    b29 = []
    with open(b32) as b54:
        for b37 in b54:
            b30 = b37.replace("<", "")
            b30 = b30.replace(">", "")
            b30 = b30.replace("}{", "},{")
            if b30[0] != '{':
                b30 = '{' + b30
            b11 = list(literal_eval(b30))
            if isinstance(b11[0], set):
                for x in b11:
                    b31 = [int(i) for i in x]
                    b29.append(b31)
            else:
                b31 = [int(i) for i in b11]
                b29.append(b31)
    return b29
def fonk9(b32 = 'parameterfile.txt'):
    b33 = {}
    b34 = []
    b35 = []
    b36 = []
    with open(b32) as b54:
        for b37 in b54:
            b37 = b37.rstrip('\b4')
            if "b8" in b37:
                a, b38 = b37.split("b8(")
                a, b38 = b38.split(") = ")
                b33[int(a)] = float(b38)
                b34.append(a)
            elif "b39" in b37:
                a, b38 = b37.split("b39 = ")
                b39 = float(b38)
            elif "b35" in b37:
                a, b38 = b37.split("b35: ")
                b11 = list(literal_eval(b38))
                if isinstance(b11[0], set):
                    for x in b11:
                        b35.append(list(x))
                else:
                    b35.append(list(b11))
            elif "must-have" in b37:
                a, b38 = b37.split("must-have:")
                b36 = [int(aa) for aa in b38.split("or")]
    return b33, b34, b39, b35, b36
def fonk10(b29, b33, b34, b39, b36, b35):
    b7 = fonk3(b34, b33)
    b3, b2 = fonk2(b33, b7, b29)
    b10 = fonk4(b3, b33, b2, len(b29), b36)
    fonk7(b10, 1, b2)
    b40 = False
    b23 = 1
    b41 = []
    while b40 = = False:
        b23 += 1
        b26 = dict()
        b42 = dict()
        if (b23 = = 2):
            b14 = fonk5(b3, b39, b33, b2, len(b29))
            print(b14)
        else:
            b14 = fonk6(b41, b39, b33, b2, len(b29))
        for b17 in b14:
            b43 = fonk1(b17)
            b26[b43] = 0
            b44 = b43 + '-' + fonk1(b17[1:])
            b42[b44] = 0
        for t in b29:
            b45 = set(t)
            for b17 in b14:
                b43 = fonk1(b17)
                b44 = b43 + '-' + fonk1(b17[1:])
                b46 = set(b17)
                if b46.issubset(b45):
                    b26[b43] += 1
                b47 = set(b17[1:])
                if b47.issubset(b45):
                    b42[b44] += 1
        b41 = []
        b48 = []
        for b17 in b14:
            b49 = fonk1(b17)
            if (((b26[b49] / len(b29))) >= b33[b17[0]]):
                b50 = True
                b51 = False
                b52 = set(b17)
                b41.append(b17)
                for x in b35:
                    b53 = set(x)
                    if b53.issubset(b52):
                        b50 = False
                for y in b36:
                    if y in b17:
                        b51 = True
                if len(b36) == 0:
                    b51 = True
                if b50 = = True and b51 == True:
                    b48.append(b17)
        if len(b41) == 0:
            b40 = True
        if b40 = = False and (len(b48) >= 1):
            fonk7(b48, b23, b26, b42)
def fonk11(b56, b57):
    global b58
    print("*********WELCOME**********")
    print("b33-Apriori Implementation")
    print("Transaction Details")
    b54 = open(b58, 'w')
    b29 = fonk8(b56)
    b33, b34, b39, b35, b36 = fonk9(b57)
    fonk10(b29, b33, b34, b39, b36, b35)
    b54.close()
if b55 = = "__main__":
    b56 = 'your_input_data_file.txt'
    b57 = 'your_parameter_file.txt'
    b58 = 'output-patterns.txt'
    fonk11(b56, b57)