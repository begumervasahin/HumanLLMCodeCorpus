import numpy as np
import random
from copy import deepcopy
class class1(list):
    def fonk1(self, content):
        list.fonk1(self, content)
        self.b1 = None
        self.b2 = None
    @property
    def fonk2(self):
        b3 = [0]
        a1 = 0
        for b17 in self:
            b4 = b3.b28()
            a1 = max(a1, b4)
            b3.extend([b4+1]*b17[2])
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
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            b3.append(b10 +  "(" + ",".join([b3.b28() for _ in range(b12)]) + ")" if b12 != 0 else b10)
        return b3[0]
    def fonk5(self, b36):
        b8 = np.b8(len(b36))
        b9 = b36.flatten()
        b3 = []
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            if b10 = = "b9":
                b11 = b9
            elif b12 = = 0:
                b11 = b8 * b7
            else:
                b11 = func(*[b3.b28() for _ in range(b12)])
            b3.append(b11)
        return b3[0]
    def fonk6(self):
        b13 = {
            "add":lambda a,b:"({}+{})".format(a,b),
            "sub":lambda a,b:"({}-{})".format(a,b),
            "mul":lambda a,b:"{}{}".format(a,b),
            "div":lambda a,b:"\\frac{{{0}}}{{{1}}}".format(a,b),
            "sin":lambda a:"\\sin({})".format(a),
            "cos":lambda a:"\\cos({})".format(a),
            "tan":lambda a:"\\tan({})".format(a),
            "log":lambda a:"\\log({})".format(a),
            "exp":lambda a:"\\exp({})".format(a),
            "sqrt":lambda a:"\\sqrt{{{0}}}".format(a),
            "-1":lambda : "-1",
            "0":lambda : "0",
            "1":lambda : "1",
            "0.5":lambda : "0.5",
            "pi":lambda : "\\pi",
            "e":lambda : "e",
            "b9":lambda : "b9",
        }
        b3 = []
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            b14 = b13[b10]
            b3.append(b14(*[b3.b28() for _ in range(b12)]))
        return b3[0]
    def fonk7(self):
        b13 = {
            "add":lambda a,b:"({}+{})".format(a,b),
            "sub":lambda a,b:"({}-{})".format(a,b),
            "mul":lambda a,b:"{}*{}".format(a,b),
            "div":lambda a,b:"{}/{}".format(a,b),
            "sin":lambda a:"sin({})".format(a),
            "cos":lambda a:"cos({})".format(a),
            "tan":lambda a:"tan({})".format(a),
            "log":lambda a:"log({})".format(a),
            "exp":lambda a:"exp({})".format(a),
            "sqrt":lambda a:"{}**(1/2)".format(a),
            "-1":lambda : "-1",
            "0":lambda : "0",
            "1":lambda : "1",
            "0.5":lambda : "0.5",
            "pi":lambda : "pi",
            "e":lambda : "e",
            "b9":lambda : "b9",
        }
        b3 = []
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            b14 = b13[b10]
            b3.append(b14(*[b3.b28() for _ in range(b12)]))
        return b3[0]
def fonk8(b23, b24):
    b15 = random.randint(5, 5)
    b16 = []
    b3 = [0]
    while len(b3) != 0:
        b4 = b3.b28()
        if b4 = = b15:
            b17 = random.choice(b24)
        else:
            b17 = random.choice(b23)
            b3.extend([b4+1]*b17[2])
        b16.append(b17)
    b18 = class1(b16)
    return b18
def fonk9(treeA, treeB, a9):
    if len(treeA) == 1 or len(treeB) == 1:
        return treeA, treeB
    for _ in range(100):
        b19 = random.randrange(1, len(treeA))
        b20 = random.randrange(1, len(treeB))
        b21 = treeA.fonk3(b19)
        b22 = treeB.fonk3(b20)
        treeA[b19:b21], treeB[b20:b22] = treeB[b20:b22], treeA[b19:b21]
        if treeA.b15 <= a9 and treeB.b15 <= a9:
            break
        treeA[b19:b19+(b22-b20)], treeB[b20:b20+(b21-b19)] = treeB[b20:b20+(b21-b19)], treeA[b19:b19+(b22-b20)]
    return treeA, treeB
def fonk10(b18, b23, b24, a7):
    for i, b17 in enumerate(b18):
        if random.random() < a7:
            b10, func, b12, b7 = b17
            if b12 = = 0:
                b18[i] = random.choice(b24)
            else:
                b18[i] = random.choice([_node for _node in b23 if _node[2] == b12])
    return b18
def fonk11():
    b23 = []
    b24 = []
    b23.append(("add",  np.add,                 2,      None))
    b23.append(("sub",  np.subtract,    2,      None))
    b23.append(("mul",  np.multiply,    2,      None))
    b23.append(("div",  np.divide,              2,      None))
    b23.append(("sin",  np.sin,                 1,      None))
    b23.append(("cos",  np.cos,                 1,      None))
    b23.append(("tan",  np.tan,                 1,      None))
    b23.append(("log",  np.log,                 1,      None))
    b23.append(("exp",  np.exp,                 1,      None))
    b23.append(("sqrt", np.sqrt,                1,      None))
    b24.append(("pi",   None,                   0,      np.pi))
    b24.append(("e",    None,                   0,      np.e))
    b24.append(("b9",    None,                   0,      None))
    return b23, b24
def fonk12(a4, b23, b24):
    return [fonk8(b23, b24) for _ in range(a4)]
def fonk13(b28, b36, b37):
    for b18 in b28:
        if b18.b1 = = None:
            b25 = b18.fonk5(b36)
            b2 = np.abs(b37 - b25)
            b1 = np.sum(b2) / len(b37)
            if np.isfinite(b1) and b1 < 9999999999:
                b18.b1 = b1
                b18.b2 = b2
            else:
                b18.b1 = None
    return b28
def fonk14(b28, b30, b26 = 8, a8=64):
    b27 = len(b28)
    b28 = [b18 for b18 in b28 if b18.b1 != None]
    b29 = min(b28, key=lambda b18: b18.b1)
    if b30 = = None or b29.b1 < b30.b1:
        b30 = deepcopy(b29)
    b31 = np.arange(len(b28[0].b2))
    np.random.shuffle(b31)
    a2 = 0
    b32 = []
    for _ in range(b27-1):
        b29 = None
        a3 = 0
        b33 = random.sample(b28, a8) if len(b28) > a8 else b28
        b34 = a2 + b26 if (a2 + b26) < len(b31) else len(b31)
        for b18 in b33:
            b35 = np.sum([b18.b2[t] for t in b31[a2:b34]]) / b26
            if b29 = = None or b35 < a3:
                b29 = b18
                a3 = b35
        b32.append(deepcopy(b29))
        a2 = b34
        if a2 = = len(b31):
            a2 = 0
    b32.append(deepcopy(b30))
    return b32, b30
def fonk15(b28, a6, a9):
    for i in range(int(len(b28)/2)):
        if random.random() < a6:
            b28[i*2], b28[i*2+1] = fonk9(b28[i*2], b28[i*2+1], a9)
            b28[i*2].b1 = None
            b28[i*2+1].b1 = None
    return b28
def fonk16(b28, a7, b23, b24):
    for i in range(int(len(b28)/2)):
        b28[i] = fonk10(b28[i], b23, b24, a7)
        b28[i].b1 = None
    return b28
a4 = 100
a5 = 50
b30 = None
a6 = 0.8
a7 = 0.2
b26 = 8
a8 = 64
a9 = 10
b36 = np.random.rand(100, 1)
b37 = np.sin(b36).flatten()
b23, b24 = fonk11()
b28 = fonk12(a4, b23, b24)
for gen in range(a5):
    b28 = fonk13(b28, b36, b37)
    b28, b30 = fonk14(b28, b30, b26=b26, a8=a8)
    b28 = fonk15(b28, a6, a9)
    b28 = fonk16(b28, a7, b23, b24)
b28 = fonk13(b28, b36, b37)
b38 = min(b28, key=lambda b18: b18.b1)
print("Best Individual:")
print(b38)
print("Fitness:", b38.b1)