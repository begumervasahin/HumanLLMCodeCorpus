9. Repository: rach24/b46-Apriori
   File: b46-Apriori.py
   URL: https:
   Code Content:
import sys
from ast import literal_eval
import operator
import collections
from collections import OrderedDict
from itertools import combinations
def fonk1(b42, b46, b47, b52, b49, b48):
    b1 = fonk4(b47, b46)
    b21, b2 = fonk3(b46, b1, b42)
    b3 = fonk5(b21, b46, b2, len(b42), b49)
    fonk8(b3,1,b2)
    b4 = False
    a1 = 1
    b5 = []
    while b4 = = False:
        a1 = a1 + 1
        b6 = dict()
        b7 = dict()
        if (a1 = = 2):
            b8 = fonk6(b21, b52, b46, b2, len(b42))
            print(b8)
        else:
            b8 = fonk7(b5, b52, b46, b2, len(b42))
        for b32 in b8:
            b9 = fonk2(b32)
            b6[b9] = 0
            b10 = b9 +'-'+fonk2(b32[1:])
            b7[b10] = 0
        for t in b42:
            b11 = set(t)
            for b32 in b8:
                b9 = fonk2(b32)
                b10 = b9 + '-' + fonk2(b32[1:])
                b12 = set(b32)
                if b12.issubset(b11):
                    b6[b9] = b6[b9] + 1
                b13 = set(b32[1:])
                if b13.issubset(b11):
                    b7[b10] = b7[b10] + 1
        b5 = []
        b14 = []
        for b32 in b8:
            b15 = fonk2(b32)
            if (((b6[b15]/len(b42))) >= b46[b32[0]]):
                b16 = True
                b17 = False
                b18 = set(b32)
                b5.append(b32)
                for x in b48:
                    b19 = set(x)
                    if b19.issubset(b18):
                        b16 = False
                for y in b49:
                    if y in b32:
                        b17 = True
                if len(b49) == 0:
                     b17 = True
                if b16 = = True and b17 == True:
                    b14.append(b32)
        if len(b5) == 0:
            b4 = True
        if b4 = = False and (len(b14) >= 1):
            fonk8(b14,a1,b6,b7)
def fonk2(list_l):
    b20 = ','.join(map(str,list_l))
    return b20
def fonk3(b46, b1, b42):
    b2 = {}
    b21 = []
    for x in b1:
        a2 = 0
        for i in range(0, len(b42)):
            if x in b42[i]:
                a2 = a2 + 1
        b2[x] = a2
    b22 = len(b42)
    b23 = False
    for x in b1:
        if b23 = = False:
            if ((b2[x] / b22) >= b46[x]):
                b21.append(x)
                b24 = x
                b23 = True
        if b23 = = True:
            if ((b2[x] / b22) >= b46[b24]):
                if (b24 != x):
                    b21.append(x)
    return b21, b2
def fonk4(b47, b46):
    b1 = []
    b25 = sorted(b46.items(), key=operator.itemgetter(1))
    for i in range(0, len(b25)):
        val1, b26 = b25[i]
        b1.append(val1)
    for i in range(0, len(b1)):
        b1[i] = (b1[i])
    return b1
def fonk5(b21, b46, b2, b22, b49):
    b3 = []
    if (len(b49) == 0):
        for x in b21:
            if ((b2[x] / b22) >= b46[x]):
                b27 = []
                b27.append(x)
                b3.append(b27)
    else:
        for x in b21:
            if ((b2[x] / b22) >= b46[x]) and (x in b49):
                b27 = []
                b27.append(x)
                b3.append(b27)
    return b3
def fonk6(b21, b52, b46, b2, b22):
    b28 = []
    for l in b21:
        if (b2[l] / b22) >= b46[l]:
            b29 = b21.index(l) + 1
            for h in b21[b29:]:
                if (((b2[h] / b22) >= b46[l]) and (abs((b2[h] / b22) - (b2[l] / b22)) <= b52)):
                    b27 = [l, h]
                    b28.append(b27)
    return b28
def fonk7(F, b52, b46, b2, b22):
    b8 = []
    for i in range(0,len(F)-1):
        for j in range(i+1,len(F)):
            b30 = F[i]
            b31 = F[j]
            if (b30[:(len(b30)-1)] == b31[:(len(b31)-1)] and b46[b31[len(b31)-1]] >= b46[b30[len(b30)-1]] and (abs((b2[b30[len(b30)-1]]/b22) - (b2[b31[len(b31)-1]]/b22)) <= b52)):
                b32 = []
                for x in b30:
                    b32.append(x)
                b32.append(b31[-1])
                b8.append(b32)
                b33 = False
                b34 = [list(a1) for a1 in combinations(b32, len(b32) - 1)]
                for s in b34:
                    b35 = list(s)
                    if (b32[0] in b35) or b46[b32[1]] == b46[b32[0]]:
                        if b35 not in F:
                            b33 = True
                if b33 = = True:
                    b8.remove(b32)
    return b8
def fonk8(b5,a1,b2,b36 = 0):
    b37 = open(b53, 'a+')
    if a1 = = 1:
        b37.write ("Frequent ")
        b37.write (str(a1))
        b37.write ("-b39\b22\b22")
        for b54 in b5:
            b37.write ("\t")
            b37.write (str(b2[b54[0]]))
            b37.write (" : ")
            b27 = str(b54)
            b38 = b27.replace ("[","{")
            b27 = b38.replace ("]","}")
            b37.write (b27)
            b37.write ("\b22")
        b37.write ("\b22\tTotal number of frequent ")
        b37.write (str(a1))
        b37.write ("-b39 = ")
        b37.write (str(len(b5)))
        b37.write ("\b22")
        b37.write ("\b22")
    else:
        b37.write ("Frequent ")
        b37.write (str(a1))
        b37.write ("-b39\b22\b22")
        for b54 in b5:
            b6 = string_convertor (b54)
            b40 = b6 +'-'+ string_convertor (b54[1:])
            b37.write ("\t")
            b37.write (str(b2[b6]))
            b37.write (" : ")
            b27 = str(b54)
            b38 = b27.replace ("[","{")
            b27 = b38.replace ("]","}")
            b37.write (b27)
            b37.write ("\b22")
            b37.write ("b41 = ")
            b37.write (str(b36[b40]))
            b37.write ("\b22")
        b37.write ("\b22\tTotal number of frequent ")
        b37.write (str(a1))
        b37.write ("-b39 = ")
        b37.write (str(len(b5)))
        b37.write ("\b22")
        b37.write ("\b22")
    b37.close()
def fonk9(b45):
    b42 = []
    with open(b45) as b54:
        for b50 in b54:
            b43 = b50.replace("<", "")
            b43 = b43.replace(">", "")
            b43 = b43.replace("}{","},{")
            if b43[0] != '{':
                b43 = '{'+b43
            b27 = list(literal_eval (b43))
            if isinstance(b27[0], set):
                for x in b27:
                   b44 = [int(i) for i in x]
                   b42.append(b44)
            else:
                b44 = [int(i) for i in b27]
                b42.append(b44)
    return b42
def fonk10(b45 = 'parameterfile.txt'):
    b46 = {}
    b47 = []
    b48 = []
    b49 = []
    with open(b45) as b54:
        for b50 in b54:
            b50 = b50.rstrip('\b22')
            if "b25" in b50:
                a, b51 = b50.split("b25(")
                a, b51 = b51.split(") = ")
                b46[int(a)] = float(b51)
                b47.append(a)
            elif "b52" in b50:
                a, b51 = b50.split("b52 = ")
                b52 = float(b51)
            elif "b48" in b50:
                a, b51 = b50.split("b48: ")
                b27 = list(literal_eval (b51))
                if isinstance(b27[0], set):
                    for x in b27:
                        b48.append(list(x))
                else:
                    b48.append(list(b27))
            elif "must-have" in b50:
                a, b51 = b50.split("must-have:")
                b49 = [int(aa) for aa in b51.split("or")]
    return b46, b47, b52, b48, b49
b53 = 'output-patterns.txt'
def fonk11(inputdata, parameters):
    global b53
    print("*********WELCOME**********")
    print("b46-Apriori Implementation")
    print("Transaction Details")
    b54 = open(b53, 'w')
    b42 = fonk9(inputdata)
    b46, b47, b52, b48, b49 = fonk10(parameters)
    fonk1(b42, b46, b47, b52, b49, b48)
    b54.close
if b55 = = "__main__":
    fonk11(sys.argv[1], sys.argv[2])
   README Content:
This is an implementation of the b46 Apriori algorithm in Data Mining
