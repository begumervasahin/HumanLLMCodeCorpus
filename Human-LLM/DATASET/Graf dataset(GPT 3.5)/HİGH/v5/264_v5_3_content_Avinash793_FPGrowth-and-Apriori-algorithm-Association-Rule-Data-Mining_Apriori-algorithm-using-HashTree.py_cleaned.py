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
            for key, b20 in node.b3.items():
                if b20 >= support_count:
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
        b17 = list(fonk13(set(candidate), a1 - 1))
        b18 = all(list(sorted(subset)) in dataset for subset in b17)
        if b18:
            b16.append(candidate)
    return b12, b16
def fonk10(b12, b33, b38):
    b19 = {}
    for val in b38:
        for val1 in b12:
            b20 = set(val)
            b21 = set(val1)
            if b21.issubset(b20):
                b19.setdefault(tuple(val1), 0)
                b19[tuple(val1)] += 1
    b22 = [sorted(list(item_set)) for item_set, support in b19.items() if support >= b33]
    return b22
def fonk11(b14, b33, b38):
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
                b26 = fonk10(b16, b33, b38)
                b23.append(b26)
                a1 += 1
                b12, b16 = fonk9(b23[a1 - 1], a1)
            break
        b27 = generate_k_subsets(b38, a1)
        for subset in b27:
            b25.fonk5(subset)
        b28 = []
        b25.fonk6(b25.b4, b33, b28)
        b23.append(b28)
        a1 += 1
    b29 = time.time()
    return b23, (b29 - b24)
def fonk12(b35, b33):
    b30 = {}
    for transaction in b35:
        for item in transaction:
            b30[item] = b30.get(item, 0) + 1
    b31 = [[b20] for b20, count in b30.items() if count >= b33]
    return b31
def fonk13(ck_data, b26):
    return map(list, set(itertools.combinations(ck_data, b26)))
b32 = input("Enter the b32: ")
b33 = int(input("Enter the minimum support count: "))
with open(b32) as f:
    b34 = f.readlines()
b34 = [x.strip() for x in b34]
b35 = [line.split() for line in b34]
b36 = {}
b37 = fonk12(b35, b33)
b38 = [[item for item in transaction if item in b37] for transaction in b35]
L_value, b39 = fonk11(b37, b33, b38)
print("Time Taken is:")
print(b39)
print("All frequent itemsets with their support count:")
print(b36)