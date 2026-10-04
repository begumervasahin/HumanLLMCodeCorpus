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
        for b16 in self:
            b4 = b3.pop()
            a1 = max(a1, b4)
            b3.extend([b4 + 1] * b16[2])
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
        for b9, func, b11, b21 in self[::-1]:
            b3.append(f"{b9}({','.join([b3.pop() for _ in range(b11)])})" if b11 != 0 else b9)
        return b3[0]
    def fonk5(self, X):
        b7 = np.b7(len(X))
        b8 = X.flatten()
        b3 = []
        for b9, func, b11, b21 in self[::-1]:
            if b9 = = "b8":
                b10 = b8
            elif b11 = = 0:
                b10 = b7 * b21
            else:
                b10 = func(*[b3.pop() for _ in range(b11)])
            b3.append(b10)
        return b3[0]
    def fonk6(self):
        b12 = {
            "add": lambda a, b: f"({a}+{b})",
            "sub": lambda a, b: f"({a}-{b})",
            "mul": lambda a, b: f"{a}{b}",
            "div": lambda a, b: f"\\frac{{{a}}}{{{b}}}",
            "sin": lambda a: f"\\sin({a})",
            "cos": lambda a: f"\\cos({a})",
            "tan": lambda a: f"\\tan({a})",
            "log": lambda a: f"\\log({a})",
            "exp": lambda a: f"\\exp({a})",
            "sqrt": lambda a: f"\\sqrt{{{a}}}",
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "\\pi",
            "e": lambda: "e",
            "b8": lambda: "b8",
        }
        b3 = []
        for b9, func, b11, b21 in self[::-1]:
            b13 = b12[b9]
            b3.append(b13(*[b3.pop() for _ in range(b11)]))
        return b3[0]
    def fonk7(self):
        b12 = {
            "add": lambda a, b: f"({a}+{b})",
            "sub": lambda a, b: f"({a}-{b})",
            "mul": lambda a, b: f"{a}*{b}",
            "div": lambda a, b: f"{a}/{b}",
            "sin": lambda a: f"sin({a})",
            "cos": lambda a: f"cos({a})",
            "tan": lambda a: f"tan({a})",
            "log": lambda a: f"log({a})",
            "exp": lambda a: f"exp({a})",
            "sqrt": lambda a: f"{a}**(1/2)",
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "pi",
            "e": lambda: "e",
            "b8": lambda: "b8",
        }
        b3 = []
        for b9, func, b11, b21 in self[::-1]:
            b13 = b12[b9]
            b3.append(b13(*[b3.pop() for _ in range(b11)]))
        return b3[0]
def fonk8(b22, b23, b14 = 5):
    b15 = []
    b3 = [0]
    while b3:
        b4 = b3.pop()
        b16 = random.choice(b23 if b4 == b14 else b22)
        b3.extend([b4 + 1] * b16[2])
        b15.append(b16)
    return class1(b15)
def fonk9(treeA, treeB, limit):
    if len(treeA) == 1 or len(treeB) == 1:
        return treeA, treeB
    for _ in range(100):
        b17 = random.randrange(1, len(treeA))
        b18 = random.randrange(1, len(treeB))
        b19 = treeA.fonk3(b17)
        b20 = treeB.fonk3(b18)
        treeA[b17:b19], treeB[b18:b20] = treeB[b18:b20], treeA[b17:b19]
        if treeA.b14 <= limit and treeB.b14 <= limit:
            break
        treeA[b17:b19], treeB[b18:b20] = treeB[b18:b20], treeA[b17:b19]
    return treeA, treeB
def fonk10(tree, b22, b23, mutation_prob):
    for i, b16 in enumerate(tree):
        if random.random() < mutation_prob:
            b9, func, b11, b21 = b16
            tree[i] = random.choice(b23 if b11 = = 0 else [n for n in b22 if n[2] == b11])
    return tree
def fonk11():
    b22 = [
        ("add", np.add, 2, None),
        ("sub", np.subtract, 2, None),
        ("mul", np.multiply, 2, None),
        ("div", np.divide, 2, None),
        ("sin", np.sin, 1, None),
        ("cos", np.cos, 1, None),
        ("tan", np.tan, 1, None),
        ("log", np.log, 1, None),
        ("exp", np.exp, 1, None),
        ("sqrt", np.sqrt, 1, None)
    ]
    b23 = [
        ("pi", None, 0, np.pi),
        ("e", None, 0, np.e),
        ("b8", None, 0, None)
    ]
    return b22, b23
def fonk12(size, b22, b23):
    return [fonk8(b22, b23) for _ in range(size)]
def fonk13(b26, X, y):
    for tree in b26:
        if tree.b1 is None:
            b24 = tree.fonk5(X)
            b2 = np.abs(y - b24)
            b1 = np.mean(b2)
            tree.b1 = b1 if np.isfinite(b1) else None
            tree.b2 = b2 if np.isfinite(b1) else None
    return b26
def fonk14(b26, b28, b25 = 8, tour_size=64):
    b26 = [tree for tree in b26 if tree.b1 is not None]
    b27 = min(b26, key=lambda tree: tree.b1)
    b28 = deepcopy(b27) if b28 is None or b27.b1 < b28.b1 else b28
    b29 = []
    b30 = np.arange(len(b26[0].b2))
    np.random.shuffle(b30)
    a2 = 0
    for _ in range(len(b26) - 1):
        b31 = None
        a3 = 0
        b32 = random.sample(b26, tour_size) if len(b26) > tour_size else b26
        b33 = min(a2 + b25, len(b30))
        for tree in b32:
            b34 = np.mean([tree.b2[t] for t in b30[a2:b33]])
            if b31 is None or b34 < a3:
                b31 = tree
                a3 = b34
        b29.append(deepcopy(b31))
        a2 = b33 if b33 < len(b30) else 0
    b29.append(deepcopy(b28))
    return b29, b28
def fonk15(b26, crossover_prob, height_limit):
    for i in range(0, len(b26), 2):
        if random.random() < crossover_prob:
            b26[i], b26[i+1] = fonk9(b26[i], b26[i+1], height_limit)
            b26[i].b1 = None
            b26[i+1].b1 = None
    return b26
def fonk16(b26, mutation_prob, b22, b23):
    for i in range(len(b26)):
        b26[i] = fonk10(b26[i], b22, b23, mutation_prob)
        b26[i].b1 = None
    return b26