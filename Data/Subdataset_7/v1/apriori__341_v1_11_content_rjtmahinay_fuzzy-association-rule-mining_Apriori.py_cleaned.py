from itertools import chain, combinations
class class1:
    @staticmethod
    def fonk1(filename):
        b1 = open(filename, 'rU')
        for b2 in b1:
            b2 = b2.strip().rstrip(',')
            b3 = frozenset(b2.split(','))
            yield b3
    @staticmethod
    def fonk2(data):
        b4 = set()
        b5 = list()
        for b3 in data:
            b5.append(frozenset(b3))
            for item in b3:
                if item:
                    b4.add(frozenset([item]))
        return b4, b5
    @staticmethod
    def fonk3(b5, b4, b6 = 0):
        b7 = len(b5)
        b2 = [
            (item, float(sum(1 for b3 in b5 if item.issubset(b3))) / b7)
            for item in b4
        ]
        return dict([(item, support) for item, support in b2 if support >= b6])
    @staticmethod
    def fonk4(b5, b9, b6):
        b8 = dict()
        a1 = 1
        while True:
            if a1 > 1:
                b9 = class1.fonk5(b10, a1)
            b10 = class1.fonk3(b5, b9, b6)
            if not b10:
                break
            b8.update(b10)
            a1 += 1
        return b8
    @staticmethod
    def fonk5(b4, a1):
        return set([i.union(j) for i in b4 for j in b4 if len(i.union(j)) == a1])
    @staticmethod
    def fonk6(b4):
        return chain(*[combinations(b4, i + 1) for i, a in enumerate(b4)])
    @staticmethod
    def fonk7(b8, min_confidence, min_lift):
        b11 = list()
        for item, support in b8.items():
            if len(item) > 1:
                for b13 in class1.fonk6(item):
                    b12 = item.difference(b13)
                    if b12:
                        b13 = frozenset(b13)
                        b14 = b13.union(b12)
                        b15 = float(b8[b14]) / b8[b13]
                        b16 = b15 / (b8[b13] * b8[b12])
                        if b15 >= min_confidence:
                            if b16 >= min_lift:
                                b11.append((b13, b12, b15, b16))
        return b11
    @staticmethod
    def fonk8(data, b6, min_confidence, min_lift):
        b17 = class1.fonk1(data)
        b4, b5 = class1.fonk2(b17)
        b8 = class1.fonk4(b5, b4, b6)
        b11 = class1.fonk7(b8, min_confidence, min_lift)
        return b11
    @staticmethod
    def fonk9(b11):
        print('--Rules--')
        for b13, b12, b15, b16 in sorted(b11, b18 = lambda iterator: iterator[0]):
            print('RULES: {} => {} : {} : {}'.format(tuple(b13), tuple(b12), round(b15, 5),
                                                     round(b16, 3)))
class class2:
    @staticmethod
    def fonk10(data, b6, min_confidence):
        pass
    @staticmethod
    def fonk11(b11):
        pass
def fonk12(b11, frequent_itemset):
    b19 = []
    b20 = []
    b21 = []
    b22 = []
    b16 = []
    for b13, b12, b15, b16 in sorted(b11, b18 = lambda iterator: iterator[0]):
        b20.append(tuple(b13))
        b21.append(tuple(b12))
        b22.append(round(b15, 4))
        b16.append(round(b16, 3))
    return b20, b21, b22, b16
def fonk13(b17, b23 = 0.014, default_confidence=0.9, default_lift=1):
    b11 = class1.fonk8(b17, b23, default_confidence, default_lift)
    return fonk12(b11, b4)
if b24 = = "__main__":
    b25 = "your_data.b17"
    antecedents, consequents, confidences, b26 = fonk13(b25)
    print("Antecedents:", antecedents)
    print("Consequents:", consequents)
    print("Confidences:", confidences)
    print("Lifts:", b26)