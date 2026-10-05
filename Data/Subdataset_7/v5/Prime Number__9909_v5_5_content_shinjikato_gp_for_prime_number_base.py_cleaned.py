import numpy as np
import random
from copy import deepcopy
class class1(list):
    def fonk1(self, content):
        super().fonk1(content)
        self.b1 = None
        self.b2 = None
    @property
    def fonk2(self):
        b3 = [0]
        a1 = 0
        for b17 in self:
            b4 = b3.b27()
            a1 = max(a1, b4)
            b3.extend([b4 + 1] * b17[2])
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
            if b12 != 0:
                b3.append(b10 + "(" + ",".join([b3.b27() for _ in range(b12)]) + ")")
            else:
                b3.append(b10)
        return b3[0]
    def fonk5(self, X):
        b8 = np.b8(len(X))
        b9 = X.flatten()
        b3 = []
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            if b10 = = "b9":
                b11 = b9
            elif b12 = = 0:
                b11 = b8 * b7
            else:
                b11 = func(*[b3.b27() for _ in range(b12)])
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
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            b14 = b13[b10]
            b3.append(b14(*[b3.b27() for _ in range(b12)]))
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
        for b17 in self[::-1]:
            b10, func, b12, b7 = b17
            b14 = b13[b10]
            b3.append(b14(*[b3.b27() for _ in range(b12)]))
        return b3[0]
def fonk8(b22, b23):
    b15 = random.randint(5, 5)
    b16 = []
    b3 = [0]
    while b3:
        b4 = b3.b27()
        if b4 = = b15:
            b17 = random.choice(b23)
        else:
            b17 = random.choice(b22)
            b3.extend([b4 + 1] * b17[2])
        b16.append(b17)
    return class1(b16)
def fonk9(tree_a, tree_b, limit):
    if len(tree_a) == 1 or len(tree_b) == 1:
        return tree_a, tree_b
    for _ in range(100):
        b18 = random.randrange(1, len(tree_a))
        b19 = random.randrange(1, len(tree_b))
        b20 = tree_a.fonk3(b18)
        b21 = tree_b.fonk3(b19)
        tree_a[b18:b20], tree_b[b19:b21] = tree_b[b19:b21], tree_a[b18:b20]
        if tree_a.b15 <= limit and tree_b.b15 <= limit:
            break
        tree_a[b18:b18 + (b21 - b19)], tree_b[b19:b19 + (b20 - b18)] = tree_b[b19:b19 + (b20 - b18)], tree_a[b18:b18 + (b21 - b19)]
    return tree_a, tree_b
def fonk10(tree, b22, b23, mutpb):
    for i, b17 in enumerate(tree):
        if random.random() < mutpb:
            b10, func, b12, b7 = b17
            if b12 = = 0:
                tree[i] = random.choice(b23)
            else:
                tree[i] = random.choice([_node for _node in b22 if _node[2] == b12])
    return tree
def fonk11():
    b22 = []
    b23 = []
    b22.append(("add", np.add, 2, None))
    b22.append(("sub", np.subtract, 2, None))
    b22.append(("mul", np.multiply, 2, None))
    b22.append(("div", np.divide, 2, None))
    b22.append(("sin", np.sin, 1, None))
    b22.append(("cos", np.cos, 1, None))
    b22.append(("tan", np.tan, 1, None))
    b22.append(("log", np.log, 1, None))
    b22.append(("exp", np.exp, 1, None))
    b22.append(("sqrt", np.sqrt, 1, None))
    b23.append(("pi", None, 0, np.pi))
    b23.append(("e", None, 0, np.e))
    b23.append(("b9", None, 0, None))
    return b22, b23
def fonk12(n, b22, b23):
    return [fonk8(b22, b23) for _ in range(n)]
def fonk13(b27, X, y):
    for tree in b27:
        if tree.b1 is None:
            b24 = tree.fonk5(X)
            b2 = np.abs(y - b24)
            b1 = np.sum(b2) / len(y)
            if np.isfinite(b1) and b1 < 9999999999:
                tree.b1 = b1
                tree.b2 = b2
            else:
                tree.b1 = None
    return b27
def fonk14(b27, b29, b25 = 8, tour_size=64):
    b26 = len(b27)
    b27 = [tree for tree in b27 if tree.b1 is not None]
    b28 = min(b27, key=lambda tree: tree.b1)
    if b29 is None or b28.b1 < b29.b1:
        b29 = deepcopy(b28)
    b30 = np.arange(len(b27[0].b2))
    np.random.shuffle(b30)
    a2 = 0
    b31 = []
    for _ in range(b26 - 1):
        b28 = None
        a3 = 0
        b32 = random.sample(b27, tour_size) if len(b27) > tour_size else b27
        b33 = a2 + b25 if (a2 + b25) < len(b30) else len(b30)
        for tree in b32:
            b34 = np.sum([tree.b2[t] for t in b30[a2:b33]]) / b25
            if b28 is None or b34 < a3:
                b28 = tree
                a3 = b34
        b31.append(deepcopy(b28))
        a2 = b33
        if a2 = = len(b30):
            a2 = 0
    b31.append(deepcopy(b29))
    return b31, b29
def fonk15(b27, cxpb, limit):
    for i in range(0, len(b27), 2):
        if random.random() < cxpb:
            b27[i], b27[i + 1] = fonk9(b27[i], b27[i + 1], limit)
            b27[i].b1 = None
            b27[i + 1].b1 = None
    return b27
def fonk16(b27, mutpb, b22, b23):
    for i in range(len(b27)):
        b27[i] = fonk10(b27[i], b22, b23, mutpb)
        b27[i].b1 = None
    return b27