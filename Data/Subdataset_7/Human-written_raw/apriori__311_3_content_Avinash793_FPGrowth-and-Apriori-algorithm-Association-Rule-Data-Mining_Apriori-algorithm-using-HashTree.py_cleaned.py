3. Repository: Avinash793/FPGrowth-and-Apriori-algorithm-Association-Rule-Data-Mining
   File: Apriori-algorithm-using-class2.py
   URL: https:
   Code Content:
import itertools
import time
print("Enter the b1:")
b1 = input()
print("Enter the minimum support count:")
b2 = int(input())
with open(b1) as f:
    b3 = f.readlines()
b3 = [x.strip() for x in b3]
b4 = []
b5 = {}
for i in range(0,len(b3)):
    b4.append(b3[i].split())
def fonk1(b4,b2):
    b6 = {}
    for i in range(0,len(b4)):
        for j in range(0,len(b4[i])):
            if b4[i][j] not in b6:
                b6[b4[i][j]] = 1
            else:
                b6[b4[i][j]] += 1
    b7 = []
    for b31 in b6:
        if b6[b31] >= b2:
            b7 = b7 + [[b31]]
            b5[tuple(b31)] = b6[b31]
    return b7
b8 = fonk1(b4,b2)
print(b8)
print(b5)
b9 = []
for i in range(0,len(b4)):
    b10 = []
    for j in range(0,len(b4[i])):
        if [b4[i][j]] in b8:
            b10.append(b4[i][j])
    b9.append(b10)
class class1:
    def fonk2(self):
        self.b11 = {}
        self.b12 = True
        self.b13 = {}
class class2:
    def fonk3(self, b15, b16):
        self.b14 = class1()
        self.b15 = b15
        self.b16 = b16
        self.b17 = []
    def fonk4(self, node, b20, b18, count):
        if b18 = = len(b20):
            if b20 in node.b13:
                node.b13[b20] += count
            else:
                node.b13[b20] = count
            return
        if node.b12:
            if b20 in node.b13:
                node.b13[b20] += count
            else:
                node.b13[b20] = count
            if len(node.b13) == self.b15:
                for old_itemset, old_count in node.b13.items():
                    b19 = self.fonk8(old_itemset[b18])
                    if b19 not in node.b11:
                        node.b11[b19] = class1()
                    self.fonk4(node.b11[b19], old_itemset, b18 + 1, old_count)
                del node.b13
                node.b12 = False
        else:
            b19 = self.fonk8(b20[b18])
            if b19 not in node.b11:
                node.b11[b19] = class1()
            self.fonk4(node.b11[b19], b20, b18 + 1, count)
    def fonk5(self, b20):
        b20 = tuple(b20)
        self.fonk4(self.b14, b20, 0, 0)
    def fonk6(self, b20):
        b21 = self.b14
        b20 = tuple(b20)
        b18 = 0
        while True:
            if b21.b12:
                if b20 in b21.b13:
                    b21.b13[b20] += 1
                break
            b19 = self.fonk8(b20[b18])
            if b19 in b21.b11:
                b21 = b21.b11[b19]
            else:
                break
            b18 += 1
    def fonk7(self, node, support_count,b17):
        if node.b12:
            for key, b31 in node.b13.items():
                if b31 >= support_count:
                    b17.append(list(key))
                    b5[key] = b31
            return
        for child in node.b11.b8():
            self.fonk7(child, support_count,b17)
    def fonk8(self, val):
        return int(val) % self.b16
def fonk9(candidate_itemsets, b15, b16):
    b22 = class2(b16, b15)
    for b20 in candidate_itemsets:
        b22.fonk5(b20)
    return b22
def fonk10(dataset, length):
    b23 = []
    for b20 in dataset:
        b23.extend(map(list, itertools.combinations(b20, length)))
    return b23
def fonk11(ck_data,b39):
    return map(list,set(itertools.combinations(ck_data,b39)))
def fonk12(dataset,b35):
    b24 = []
    b25 = len(dataset)
    for i in range(b25):
        for j in range(i+1,b25):
            b26 = list(dataset[i])[:b35 - 2]
            b27 = list(dataset[j])[:b35 - 2]
            if b26 = = b27:
                b24.append(sorted(list(set(dataset[i]) | set(dataset[j]))))
    b28 = []
    for candidate in b24:
        b29 = list(fonk11(set(candidate), b35 - 1))
        b30 = True
        for i in range(len(b29)):
            b31 = list(sorted(b29[i]))
            if b31 not in dataset:
                b30 = False
        if b30 = = True:
            b28.append(candidate)
    return b24,b28
def fonk13(b24,b2):
    b32 = {}
    for val in b9:
        for val1 in b24:
            b31 = set(val)
            b33 = set(val1)
            if b33.issubset(b31):
                if tuple(val1) not in b32:
                    b32[tuple(val1)] = 1
                else:
                    b32[tuple(val1)] += 1
    b34 = []
    for item_set in b32:
        if b32[item_set] >= b2:
            b34.append(sorted(list(item_set)))
            b5[item_set] = b32[item_set]
    return b34
def fonk14(b26,b2):
    b35 = 2;
    b36 = []
    b36.append(0)
    b36.append(b26)
    print("enter b15")
    b15 = int(input())
    print("enter b16")
    b16 = int(input())
    b37 = time.time()
    while(len(b36[b35-1])>0):
        b24,b28 = fonk12(b36[b35-1],b35)
        print("C%d" %(b35))
        print(b28)
        b38 = fonk9(b24,b15,b16)
        if (b35 > 2):
            while(len(b36[b35-1])>0):
                b39 = fonk13(b28, b2)
                b36.append(b39)
                print("Frequent %d item" % (b35))
                print(b39)
                b35 = b35 + 1
                b24, b28 = fonk12(b36[b35 - 1], b35)
                print("C%d" % (b35))
                print(b28)
            break
        b40 = fonk10(b9,b35)
        for subset in b40:
            b38.fonk6(subset)
        b41 = []
        b38.fonk7(b38.b14,b2,b41)
        print("Frequent %d item" %(b35))
        print(b41)
        b36.append(b41)
        b35 = b35 + 1
    b42 = time.time()
    return b36,(b42-b37)
L_value,b43 = fonk14(b8,b2)
print("Time Taken is:")
print(b43)
print("All frequent itemsets with their support count:")
print(b5)
   README Content:
Implementation of FPTree Algorithm and Apriori Algorithm using class2 for finding frequent pattern in Transactional Database. Run the code and enter the b1
and minimum support count as input. I have also attached two input files of chess-dataset and basket-datset (retail) from the official site http:
