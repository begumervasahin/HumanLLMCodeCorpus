from itertools import chain, combinations
class class1:
    @staticmethod
    def fonk1(filename):
        with open(filename, 'rU') as file:
            for b1 in file:
                b1 = b1.strip().rstrip(',')
                b2 = frozenset(b1.split(','))
                yield b2
    @staticmethod
    def fonk2(data):
        b3 = set()
        b4 = []
        for b2 in data:
            b4.append(frozenset(b2))
            for item in b2:
                if item:
                    b3.add(frozenset([item]))
        return b3, b4
    @staticmethod
    def fonk3(b4, b3, b5 = 0):
        b6 = len(b4)
        b7 = {
            item: float(sum(1 for b2 in b4 if item.issubset(b2))) / b6
            for item in b3
        }
        return {item: support for item, support in b7.items() if support >= b5}
    @staticmethod
    def fonk4(b4, b9, b5):
        b8 = {}
        a1 = 1
        while True:
            if a1 > 1:
                b9 = class1.fonk5(b11, a1)
            b10 = class1.fonk3(b4, b9, b5)
            if not b10:
                break
            b8.update(b10)
            b11 = b10
            a1 += 1
        return b8
    @staticmethod
    def fonk5(b3, a1):
        return {i.union(j) for i in b3 for j in b3 if len(i.union(j)) == a1}
    @staticmethod
    def fonk6(b3):
        return chain(*[combinations(b3, i + 1) for i in range(len(b3))])
    @staticmethod
    def fonk7(b8, min_confidence, min_lift):
        b12 = []
        for item, support in b8.items():
            if len(item) > 1:
                for b14 in class1.fonk6(item):
                    b13 = item.difference(b14)
                    if b13:
                        b14 = frozenset(b14)
                        b15 = b8[b14]
                        b16 = b8[item]
                        b17 = b16 / b15
                        b18 = b17 / (b15 * b8[b13])
                        if b17 >= min_confidence and b18 >= min_lift:
                            b12.append((b14, b13, b17, b18))
        return b12
    @staticmethod
    def fonk8(data, b5, min_confidence, min_lift):
        b19 = class1.fonk1(data)
        b3, b4 = class1.fonk2(b19)
        b8 = class1.fonk4(b4, b3, b5)
        b12 = class1.fonk7(b8, min_confidence, min_lift)
        return b12
    @staticmethod
    def fonk9(b12):
        print('--Rules--')
        for b14, b13, b17, b18 in sorted(b12, b20 = lambda x: x[0]):
            print(f'RULES: {tuple(b14)} => {tuple(b13)} : {round(b17, 5)} : {round(b18, 3)}')
class class2:
    @staticmethod
    def fonk10(data, b5, min_confidence):
        pass
    @staticmethod
    def fonk11(b12):
        pass
def fonk12(b12, b8):
    b21 = []
    b22 = []
    b23 = []
    b24 = []
    for b14, b13, b17, b18 in sorted(b12, b20 = lambda x: x[0]):
        b21.append(tuple(b14))
        b22.append(tuple(b13))
        b23.append(round(b17, 4))
        b24.append(round(b18, 3))
    return b21, b22, b23, b24
def fonk13(csv, b25 = 0.014, default_confidence=0.9, default_lift=1):
    b12 = class1.fonk8(csv, b25, default_confidence, default_lift)
    return fonk12(b12, b3)
if b26 = = "__main__":
    b27 = "your_data.csv"
    b21, b22, b23, b24 = fonk13(b27)
    print("Antecedents:", b21)
    print("Consequents:", b22)
    print("Confidences:", b23)
    print("Lifts:", b24)