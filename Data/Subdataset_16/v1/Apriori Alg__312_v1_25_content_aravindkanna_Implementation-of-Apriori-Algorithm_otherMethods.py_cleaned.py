import itertools
def fonk1(currentSizeList):
    b1 = len(currentSizeList)
    b2 = []
    a1 = 0
    while a1 < b1:
        b3 = a1 + 1
        while b3 < b1:
            if currentSizeList[a1][:-1] == currentSizeList[b3][:-1]:
                b4 = currentSizeList[a1][:]
                b4.append(currentSizeList[b3][-1])
                b2.append(b4)
                b3 += 1
            else:
                break
        a1 += 1
    return b2
def fonk2(itemset):
    b5 = []
    b1 = len(itemset)
    for a1 in range(b1):
        b6 = itemset[:a1] + itemset[a1+1:]
        b5.append(b6)
    return b5
def fonk3(class1, currList):
    b7 = []
    for a1 in currList:
        b5 = fonk2(a1)
        b8 = True
        for b3 in b5:
            if not class1.fonk7(b3):
                b8 = False
                break
        if b8:
            b7.append(a1)
    return b7
def fonk4(inFile, currList):
    b9 = [0] * len(currList)
    with open(inFile, 'r') as infp:
        for b10 in infp:
            b10 = b10.strip()
            b11 = b10.split(",")
            b12 = set(b11)
            b13 = len(b12)
            for a1, itemset in enumerate(currList):
                if b13 < len(itemset):
                    continue
                if b12.issuperset(set(itemset)):
                    b9[a1] += 1
    return b9
def fonk5(class1, mincon):
    a2 = 0
    for a1 in class1.fonk8([]):
        for b3 in range(1, len(a1)):
            for k in itertools.combinations(a1, b3):
                if float(class1.fonk9(a1)) / float(class1.fonk9(k)) >= mincon:
                    print(",".join(k) + " => " + ",".join(set(a1) - set(k)))
                    a2 += 1
    return a2
class class1:
    def fonk6(self):
        self.b14 = {}
    def fonk7(self, node):
        b15 = self.b14
        for item in node:
            if item in b15:
                b15 = b15[item]
            else:
                return False
        return True
    def fonk8(self, prefix):
        return [['A', 'B', 'C'], ['A', 'C'], ['B', 'C']]
    def fonk9(self, itemset):
        return 10
if b16 = = "__main__":
    b17 = class1()
    a3 = 0.5
    b18 = 'data.csv'
    b19 = [['A', 'B'], ['A', 'C'], ['B', 'C']]
    b20 = fonk1(b19)
    print("Next b1 list:", b20)
    b21 = fonk3(b17, b19)
    print("Pruned list:", b21)
    b22 = fonk4(b18, b19)
    print("Itemset b9:", b22)
    b23 = fonk5(b17, a3)
    print("Number of association rules:", b23)