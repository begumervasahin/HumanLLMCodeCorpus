import numpy as np
import random
from copy import deepcopy
class class1(list):
    def fonk1(self, content):
        list.fonk8(self, content)
        self.b1 = None
        self.b2 = None
    @property
    def fonk2(self):
        b3 = [0]
        a1 = 0
        for b26 in self:
            b4 = b3.b30()
            a1 = max(a1, b4)
            b3.extend([b4+1]*b26[2])
        return a1
    def fonk3(self, begin):
        b5 = begin + 1
        b6 = self[begin][2]
        while b6 > 0:
            b6 += self[b5][2] - 1
            b5 += 1
        return b5
    def fonk4(self):
        b3 = []
        for b26 in self[::-1]:
            b10, func, b12, b7 = b26
            if b12 != 0:
                b3.append(b10 +  "(" + ",".join([b3.b30() for _ in range(b12)]) + ")")
            else:
                b3.append(b10)
        return b3[0]
    def fonk5(self, b43):
        b8 = np.b8(len(b43))
        b9 = b43.flatten()
        b3 = []
        for b26 in self[::-1]:
            b10, func, b12, b7 = b26
            if b10 = = "b9":
                b11 = b9
            elif b12 = = 0:
                b11 = b8 * b7
            else:
                b11 = func(*[b3.b30() for _ in range(b12)])
            b3.append(b11)
        return b3[0]
    def fonk6(self):
        b13 = {
            "add": lambda a, b: "({}+{})".format(a, b),
            "sub": lambda a, b: "({}-{})".format(a, b),
            "mul": lambda a, b: "{}{}".format(a, b),
            "div": lambda a, b: "\\frac{{{0}}}{{{1}}}".format(a, b),
            "sin": lambda a: "\\sin({})".format(a),
            "cos": lambda a: "\\cos({})".format(a),
            "tan": lambda a: "\\tan({})".format(a),
            "log": lambda a: "\\log({})".format(a),
            "exp": lambda a: "\\exp({})".format(a),
            "sqrt": lambda a: "\\sqrt{{{0}}}".format(a),
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "\\pi",
            "e": lambda: "e",
            "b9": lambda: "b9",
        }
        b3 = []
        for b26 in self[::-1]:
            b10, func, b12, b7 = b26
            b14 = b13[b10]
            b3.append(b14(*[b3.b30() for _ in range(b12)]))
        return b3[0]
    def fonk7(self):
        b13 = {
            "add": lambda a, b: "({}+{})".format(a, b),
            "sub": lambda a, b: "({}-{})".format(a, b),
            "mul": lambda a, b: "{}*{}".format(a, b),
            "div": lambda a, b: "{}/{}".format(a, b),
            "sin": lambda a: "sin({})".format(a),
            "cos": lambda a: "cos({})".format(a),
            "tan": lambda a: "tan({})".format(a),
            "log": lambda a: "log({})".format(a),
            "exp": lambda a: "exp({})".format(a),
            "sqrt": lambda a: "{}**(1/2)".format(a),
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "pi",
            "e": lambda: "e",
            "b9": lambda: "b9",
        }
        b3 = []
        for b26 in self[::-1]:
            b10, func, b12, b7 = b26
            b14 = b13[b10]
            b3.append(b14(*[b3.b30() for _ in range(b12)]))
        return b3[0]
class class2:
    def fonk8(self, b15, b16, b17, b18, b19, b20, b21):
        self.b15 = b15
        self.b16 = b16
        self.b17 = b17
        self.b18 = b18
        self.b19 = b19
        self.b20 = b20
        self.b21 = b21
        self.b23, self.b22 = self.fonk9()
    def fonk9(self):
        b23 = []
        b22 = []
        b23.append(("add", np.add, 2, None))
        b23.append(("sub", np.subtract, 2, None))
        b23.append(("mul", np.multiply, 2, None))
        b23.append(("div", np.divide, 2, None))
        b23.append(("sin", np.sin, 1, None))
        b23.append(("cos", np.cos, 1, None))
        b23.append(("tan", np.tan, 1, None))
        b23.append(("log", np.log, 1, None))
        b23.append(("exp", np.exp, 1, None))
        b23.append(("sqrt", np.sqrt, 1, None))
        b22.append(("pi", None, 0, np.pi))
        b22.append(("e", None, 0, np.e))
        b22.append(("b9", None, 0, None))
        return b23, b22
    def fonk10(self):
        b24 = random.randint(5, 5)
        b25 = []
        b3 = [0]
        while len(b3) != 0:
            b4 = b3.b30()
            if b4 = = b24:
                b26 = random.choice(self.b22)
            else:
                b26 = random.choice(self.b23)
                b3.extend([b4+1]*b26[2])
            b25.append(b26)
        b27 = class1(b25)
        return b27
    def fonk11(self):
        return [self.fonk10() for _ in range(self.b15)]
    def fonk12(self, b30, b43, b44):
        for b27 in b30:
            if b27.b1 = = None:
                b28 = b27.fonk5(b43)
                b2 = np.abs(b44 - b28)
                b1 = np.sum(b2) / len(b44)
                if np.isfinite(b1) and b1 < 9999999999:
                    b27.b1 = b1
                    b27.b2 = b2
                else:
                    b27.b1 = None
        return b30
    def fonk13(self, b30, b32):
        b29 = len(b30)
        b30 = [b27 for b27 in b30 if b27.b1 != None]
        b31 = min(b30, key=lambda b27: b27.b1)
        if b32 = = None or b31.b1 < b32.b1:
            b32 = deepcopy(b31)
        b33 = np.arange(len(b30[0].b2))
        np.random.shuffle(b33)
        a2 = 0
        b34 = []
        for _ in range(b29-1):
            b31 = None
            a3 = 0
            b35 = random.sample(b30, self.b20) if len(b30) > self.b20 else b30
            b36 = a2 + self.b19 if (a2 + self.b19) < len(b33) else len(b33)
            for b27 in b35:
                b37 = np.sum([b27.b2[t] for t in b33[a2:b36]]) / self.b19
                if b31 = = None or b37 < a3:
                    b31 = b27
                    a3 = b37
            b34.append(deepcopy(b31))
            a2 = b36
            if a2 = = len(b33):
                a2 = 0
        b34.append(deepcopy(b32))
        return b34, b32
    def fonk14(self, b30):
        for i in range(int(len(b30)/2)):
            if random.random() < self.b17:
                b30[i*2], b30[i*2+1] = self.fonk15(b30[i*2], b30[i*2+1])
                b30[i*2].b1 = None
                b30[i*2+1].b1 = None
        return b30
    def fonk15(self, treeA, treeB):
        if len(treeA) == 1 or len(treeB) == 1:
            return treeA, treeB
        for _ in range(100):
            b38 = random.randrange(1, len(treeA))
            b39 = random.randrange(1, len(treeB))
            b40 = treeA.fonk3(b38)
            b41 = treeB.fonk3(b39)
            treeA[b38:b40], treeB[b39:b41] = treeB[b39:b41], treeA[b38:b40]
            if treeA.b24 <= self.b21 and treeB.b24 <= self.b21:
                break
            treeA[b38:b38+(b41-b39)], treeB[b39:b39+(b40-b38)] = treeB[b39:b39+(b40-b38)], treeA[b38:b38+(b41-b39)]
        return treeA, treeB
    def fonk16(self, b30):
        for i in range(int(len(b30)/2)):
            b30[i] = self.fonk17(b30[i])
            b30[i].b1 = None
        return b30
    def fonk17(self, b27):
        for i, b26 in enumerate(b27):
            if random.random() < self.b18:
                b10, func, b12, b7 = b26
                if b12 = = 0:
                    b27[i] = random.choice(self.b22)
                else:
                    b27[i] = random.choice([_node for _node in self.b23 if _node[2] == b12])
        return b27
    def fonk18(self, b43, b44):
        b30 = self.fonk11()
        for gen in range(self.b16):
            b30 = self.fonk12(b30, b43, b44)
            b30, b32 = self.fonk13(b30, b32)
            b30 = self.fonk14(b30)
            b30 = self.fonk16(b30)
        b30 = self.fonk12(b30, b43, b44)
        b42 = min(b30, key=lambda b27: b27.b1)
        return b42
b15 = 100
b16 = 50
b17 = 0.8
b18 = 0.2
b19 = 8
b20 = 64
b21 = 10
b43 = np.random.rand(100, 1)
b44 = np.sin(b43).flatten()
b45 = class2(b15, b16, b17, b18, b19, b20, b21)
b42 = b45.fonk18(b43, b44)
print("Best Individual:")
print(b42)
print("Fitness:", b42.b1)