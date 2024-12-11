import itertools
import time
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = True
        self.b3 = {}
class class2:
    def fonk2(self, b5, b6):
        self.b4 = class1()
        self.b5 = b5
        self.b6 = b6
    def fonk3(self, node, b9, b7, count):
        if b7 = = len(b9):
            if b9 in node.b3:
                node.b3[b9] += count
            else:
                node.b3[b9] = count
            return
        if node.b2:
            if b9 in node.b3:
                node.b3[b9] += count
            else:
                node.b3[b9] = count
            if len(node.b3) == self.b5:
                for old_itemset, old_count in node.b3.items():
                    b8 = self.fonk7(old_itemset[b7])
                    if b8 not in node.b1:
                        node.b1[b8] = class1()
                    self.fonk3(node.b1[b8], old_itemset, b7 + 1, old_count)
                del node.b3
                node.b2 = False
        else:
            b8 = self.fonk7(b9[b7])
            if b8 not in node.b1:
                node.b1[b8] = class1()
            self.fonk3(node.b1[b8], b9, b7 + 1, count)
    def fonk4(self, b9):
        b9 = tuple(b9)
        self.fonk3(self.b4, b9, 0, 0)
    def fonk5(self, b9):
        b10 = self.b4
        b9 = tuple(b9)
        b7 = 0
        while True:
            if b10.b2:
                if b9 in b10.b3:
                    b10.b3[b9] += 1
                break
            b8 = self.fonk7(b9[b7])
            if b8 in b10.b1:
                b10 = b10.b1[b8]
            else:
                break
            b7 += 1
    def fonk6(self, node, support_count, frequent_itemsets):
        if node.b2:
            for key, b19 in node.b3.items():
                if b19 >= support_count:
                    frequent_itemsets.append(list(key))
            return
        for child in node.b1.b38():
            self.fonk6(child, support_count, frequent_itemsets)
    def fonk7(self, val):
        return int(val) % self.b6
def fonk8(candidate_itemsets, b5, b6):
    b11 = class2(b6, b5)
    for b9 in candidate_itemsets:
        b11.fonk4(b9)
    return b11
def fonk9(dataset, b23):
    b12 = []
    b13 = len(dataset)
    for i in range(b13):
        for j in range(i + 1, b13):
            b14 = list(dataset[i])[:b23 - 2]
            b15 = list(dataset[j])[:b23 - 2]
            if b14 = = b15:
                b12.append(sorted(list(set(dataset[i]) | set(dataset[j]))))
    b16 = []
    for candidate in b12:
        b17 = list(subset_generation(set(candidate), b23 - 1))
        b18 = True
        for i in range(len(b17)):
            b19 = list(sorted(b17[i]))
            if b19 not in dataset:
                b18 = False
        if b18 = = True:
            b16.append(candidate)
    return b12, b16
def fonk10(b12, b32):
    b20 = {}
    for val in b39:
        for val1 in b12:
            b19 = set(val)
            b21 = set(val1)
            if b21.issubset(b19):
                if tuple(val1) not in b20:
                    b20[tuple(val1)] = 1
                else:
                    b20[tuple(val1)] += 1
    b22 = []
    for item_set in b20:
        if b20[item_set] >= b32:
            b22.append(sorted(list(item_set)))
    return b22
def fonk11(b14, b32):
    b23 = 2;
    b24 = []
    b24.append(0)
    b24.append(b14)
    b5 = 5
    b6 = 10
    b25 = time.time()
    while (len(b24[b23 - 1]) > 0):
        b12, b16 = fonk9(b24[b23 - 1], b23)
        b26 = fonk8(b12, b5, b6)
        if (b23 > 2):
            while (len(b24[b23 - 1]) > 0):
                b27 = fonk10(b16, b32)
                b24.append(b27)
                b23 = b23 + 1
                b12, b16 = fonk9(b24[b23 - 1], b23)
            break
        b28 = generate_k_subsets(b39, b23)
        for subset in b28:
            b26.fonk5(subset)
        b29 = []
        b26.fonk6(b26.b4, b32, b29)
        b24.append(b29)
        b23 = b23 + 1
    b30 = time.time()
    return b24, (b30 - b25)
b31 = input("Enter the b31: ")
b32 = int(input("Enter the minimum support count: "))
with open(b31) as f:
    b33 = f.readlines()
b33 = [x.strip() for x in b33]
b34 = []
b35 = {}
for i in range(0, len(b33)):
    b34.append(b33[i].split())
def fonk12(b34, b32):
    b36 = {}
    for i in range(0, len(b34)):
        for j in range(0, len(b34[i])):
            if b34[i][j] not in b36:
                b36[b34[i][j]] = 1
            else:
                b36[b34[i][j]] += 1
    b37 = []
    for b19 in b36:
        if b36[b19] >= b32:
            b37 = b37 + [[b19]]
            b35[tuple(b19)] = b36[b19]
    return b37
b38 = fonk12(b34, b32)
print(b38)
print(b35)
b39 = []
for i in range(0, len(b34)):
    b40 = []
    for j in range(0, len(b34[i])):
        if [b34[i][j]] in b38:
            b40.append(b34[i][j])
    b39.append(b40)
L_value, b41 = fonk11(b38, b32)
print("Time Taken is:")
print(b41)
print("All frequent itemsets with their support count:")
print(b35)