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
    b10 = open(b1)
    b11 = csv.b11(b10)
    for row in b11:
        if (len(b9) == 0):
            for b14 in range (len(row)-1):
                b9.append([row[b14]])
        else:
            for b14 in range (len(row)-1):
                b9[b14].append(row[b14])
            b8.append(row[-1])
    for j in range(len(row)-1):
        b12 = b9[j].pop(0)
        b7[b12] = b9[j]
    b13 = list(set(b8))
    return [b8, b7, b13]
def fonk2(b8, b13):
    a1 = 0
    a2 = 0
    for b14 in b8:
        if b14 = = b13[0]:
            a1 += 1
        else:
            a2 += 1
    return a1, a2
def fonk3(b8, b13):
    a1, a2 = fonk2(b8, b13)
    if(a1 = = 0 or a2 == 0):
        return 0
    b15 = 1.0*a1/len(b8)
    b16 = 1.0*a2/len(b8)
    return -b15*math.log(b15,2) - b16*math.log(b16,2)
def fonk4(b26, b8):
    b17 = []
    b18 = []
    b13 = list(set(b8))
    for b14 in range(len(b26)):
        if (b26[b14] == ('n'or 'notA' or 'no')):
            b17.append(b8[b14])
        else:
            b18.append(b8[b14])
    b16 = 1.0*(len(b17))/len(b8)
    b19 = 1.0*(len(b18))/len(b8)
    return fonk3(b8, b13) - (b16 *fonk3(b17, b13))- (b19 *fonk3(b18, b13)), b17, b18
def fonk5(b26, b7):
    b20 = {}
    b21 = {}
    b22 = len(b7[b26])
    for b14 in b7:
        if (b14 = = b26):
            continue
        b20[b14] = []
        b21[b14] = []
        for j in range(b22):
            if (b7[b26][j] == ('n'or 'notA' or 'no')):
                b20[b14].append(b7[b14][j])
            else:
                b21[b14].append(b7[b14][j])
    return b20, b21
class class1(object):
    def fonk6(self, b24, b23 = None, b25 = None, b26 = None):
        self.b24 = b24
        self.b23 = b23
        self.b25 = b25
        self.b26 = b26
    def fonk7(self):
        if (self.b23 = = None and self.b25 == None):
            return True
        else:
            return False
def fonk8(b8, b7, b13, curdepth, maxdepth):
    label0num, b27 = fonk2(b8, b13)
    if (label0num > b27):
        b28 = b13[0]
        b29 = label0num
    else:
        b28 = b13[1]
        b29 = b27
    if (b29 = = len(b8)):
        return class1(b28)
    elif (len(b7) == 0):
        return class1(b28)
    elif (curdepth > maxdepth):
        return class1(b28)
    else:
        b30 = []
        b31 = []
        a3 = -1
        b26 = []
        for i in b7:
            currentscore, currentnlabels, b32 = fonk4(b7[i], b8)
            if (currentscore >= a3):
                a3 = currentscore
                b30 = currentnlabels
                b31 = b32
                b26 = i
        curdepth += 1
        nfeatures, b33 = fonk5(b26, b7)
        b23 = fonk8(b30, nfeatures, b13, curdepth, maxdepth)
        b25 = fonk8(b31, b33, b13, curdepth, maxdepth)
        return class1(b13[0], b23, b25, b26)
def fonk9(b41, b2, output):
    b10 = open(b1)
    b11 = csv.b11(b10)
    a4 = 0
    a5 = 0
    b34 = []
    b9 = []
    for row in b11:
        if (a5 = = 0):
            for b14 in range(len(row)- 1):
                b9.append(row[b14])
        else :
            b35 = {}
            for b14 in range(len(row)- 1):
                b35[b9[b14]] = row[b14]
            b36 = fonk10(b41, b35)
            b34.append(b36 + '\n')
            if (b36 != row[-1]):
                a4 = a4 + 1
        a5 = a5 +1
    b37 = "".join(b34)
    with open(output,'w') as f:
        f.writelines(b37)
    f.close()
    return 1.0*a4/(a5-1)
def fonk10(b41, b35):
    if (b41.fonk7()):
        return b41.b24
    else:
        if (b35[b41.b26] == ('n'or 'notA' or 'no')):
            return fonk10(b41.b23, b35)
        else:
            return fonk10(b41.b25, b35)
def fonk11(b41, b3):
    if (b41.fonk7()):
        print(' '*b3, b41.b24)
    else:
        print(' '*b3, b41.b24, ': ',b41.b26)
        fonk11(b41.b23, b3 + 1)
        fonk11(b41.b25, b3 + 1)
        0
def fonk12(b1, b2, b3, b4, b5, b6):
    b34 = fonk1(b1)
    b38 = b34[0]
    b39 = b34[1]
    b40 = b34[2]
    b41 = fonk8(b38, b39, b40, 0, b3)
    b42 = fonk9(b41, b1, b4)
    b43 = fonk9(b41, b2, b5)
    b37 = 'error(train):{}\nerror(test):{}'.format(b42, b43)
    with open(b6,'w') as f:
        f.writelines(b37)
    f.close()
if b44 = = '__main__':
    fonk12(b1, b2, b3, b4, b5, b6)