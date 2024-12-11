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
        for child in node.b1.b37():
            self.fonk6(child, support_count, frequent_itemsets)
    def fonk7(self, val):
        return int(val) % self.b6
def fonk8(candidate_itemsets, b5, b6):
    b11 = class2(b6, b5)
    for b9 in candidate_itemsets:
        b11.fonk4(b9)
    return b11
def fonk9(dataset, a1):
    b12 = []
    b13 = len(dataset)
    for i in range(b13):
        for j in range(i + 1, b13):
            b14 = list(dataset[i])[:a1 - 2]
            b15 = list(dataset[j])[:a1 - 2]
            if b14 = = b15:
                b12.append(sorted(list(set(dataset[i]) | set(dataset[j]))))
    b16 = []
    for candidate in b12:
        b17 = list(subset_generation(set(candidate), a1 - 1))
        b18 = True
        for i in range(len(b17)):
            b19 = list(sorted(b17[i]))
            if b19 not in dataset:
                b18 = False
        if b18:
            b16.append(candidate)
    return b12, b16
def fonk10(b12, b31):
    b20 = {}
    for val in b38:
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
        if b20[item_set] >= b31:
            b22.append(sorted(list(item_set)))
    return b22
def fonk11(b14, b31):
    a1 = 2
    b23 = [0, b14]
    b5 = 5
    b6 = 10
    b24 = time.time()
    while len(b23[a1 - 1]) > 0:
        b12, b16 = fonk9(b23[a1 - 1], a1)
        b25 = fonk8(b12, b5, b6)
        if a1 > 2:
            while len(b23[a1 - 1]) > 0:
                b26 = fonk10(b16, b31)
                b23.append(b26)
                a1 += 1
                b12, b16 = fonk9(b23[a1 - 1], a1)
            break
        b27 = generate_k_subsets(b38, a1)
        for subset in b27:
            b25.fonk5(subset)
        b28 = []
        b25.fonk6(b25.b4, b31, b28)
        b23.append(b28)
        a1 += 1
    b29 = time.time()
    return b23, (b29 - b24)
b30 = input("Enter the b30: ")
b31 = int(input("Enter the minimum support count: "))
with open(b30) as f:
    b32 = f.readlines()
b32 = [x.strip() for x in b32]
b33 = []
b34 = {}
for i in range(len(b32)):
    b33.append(b32[i].split())
def fonk12(b33, b31):
    b35 = {}
    for i in range(len(b33)):
        for j in range(len(b33[i])):
            if b33[i][j] not in b35:
                b35[b33[i][j]] = 1
            else:
                b35[b33[i][j]] += 1
    b36 = []
    for b19 in b35:
        if b35[b19] >= b31:
            b36.append([b19])
            b34[tuple(b19)] = b35[b19]
    return b36
b37 = fonk12(b33, b31)
print(b37)
print(b34)
b38 = []
for i in range(len(b33)):
    b39 = []
    for j in range(len(b33[i])):
        if [b33[i][j]] in b37:
            b39.append(b33[i][j])
    b38.append(b39)
L_value, b40 = fonk11(b37, b31)
print("Time Taken is:")
print(b40)
print("All frequent itemsets with their support count:")
print(b34)