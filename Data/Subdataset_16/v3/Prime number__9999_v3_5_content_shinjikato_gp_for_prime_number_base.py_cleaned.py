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
        for b15 in self:
            b4 = b3.pop()
            a1 = max(a1, b4)
            b3.extend([b4 + 1] * b15[2])
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
        for b9, func, b11, b20 in self[::-1]:
            b3.append(f"{b9}({','.join([b3.pop() for _ in range(b11)])})" if b11 != 0 else b9)
        return b3[0]
    def fonk5(self, X):
        b7 = np.b7(len(X))
        b8 = X.flatten()
        b3 = []
        for b9, func, b11, b20 in self[::-1]:
            if b9 = = "b8":
                b10 = b8
            elif b11 = = 0:
                b10 = b7 * b20
            else:
                b10 = func(*[b3.pop() for _ in range(b11)])
            b3.append(b10)
        return b3[0]
    def fonk6(self):
        return self.fonk8({
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
        })
    def fonk7(self):
        return self.fonk8({
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
        })
    def fonk8(self, trans_dict):
        b3 = []
        for b9, func, b11, b20 in self[::-1]:
            b12 = trans_dict[b9]
            b3.append(b12(*[b3.pop() for _ in range(b11)]))
        return b3[0]
def fonk9(b21, b22, b13 = 5):
    b14 = []
    b3 = [0]
    while b3:
        b4 = b3.pop()
        b15 = random.choice(b22 if b4 == b13 else b21)
        b3.extend([b4 + 1] * b15[2])
        b14.append(b15)
    return class1(b14)
def fonk10(treeA, treeB, limit):
    if len(treeA) == 1 or len(treeB) == 1:
        return treeA, treeB
    for _ in range(100):
        b16 = random.randrange(1, len(treeA))
        b17 = random.randrange(1, len(treeB))
        b18 = treeA.fonk3(b16)
        b19 = treeB.fonk3(b17)
        treeA[b16:b18], treeB[b17:b19] = treeB[b17:b19], treeA[b16:b18]
        if treeA.b13 <= limit and treeB.b13 <= limit:
            break
        treeA[b16:b18], treeB[b17:b19] = treeB[b17:b19], treeA[b16:b18]
    return treeA, treeB
def fonk11(tree, b21, b22, mutation_prob):
    for i, b15 in enumerate(tree):
        if random.random() < mutation_prob:
            b9, func, b11, b20 = b15
            tree[i] = random.choice(b22 if b11 = = 0 else [n for n in b21 if n[2] == b11])
    return tree
def fonk12():
    b21 = [
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
    b22 = [
        ("pi", None, 0, np.pi),
        ("e", None, 0, np.e),
        ("b8", None, 0, None)
    ]
    return b21, b22
def fonk13(size, b21, b22):
    return [fonk9(b21, b22) for _ in range(size)]
def fonk14(b25, X, y):
    for tree in b25:
        if tree.b1 is None:
            b23 = tree.fonk5(X)
            b2 = np.abs(y - b23)
            b1 = np.mean(b2)
            tree.b1 = b1 if np.isfinite(b1) else None
            tree.b2 = b2 if np.isfinite(b1) else None
    return b25
def fonk15(b25, b27, b24 = 8, tour_size=64):
    b25 = [tree for tree in b25 if tree.b1 is not None]
    b26 = min(b25, key=lambda tree: tree.b1)
    b27 = deepcopy(b26) if b27 is None or b26.b1 < b27.b1 else b27
    b28 = []
    b29 = np.arange(len(b25[0].b2))
    np.random.shuffle(b29)
    a2 = 0
    for _ in range(len(b25) - 1):
        b30 = None
        a3 = 0
        b31 = random.sample(b25, tour_size) if len(b25) > tour_size else b25
        b32 = min(a2 + b24, len(b29))
        for tree in b31:
            b33 = np.mean([tree.b2[t] for t in b29[a2:b32]])
            if b30 is None or b33 < a3:
                b30 = tree
                a3 = b33
        b28.append(deepcopy(b30))
        a2 = b32 if b32 < len(b29) else 0
    b28.append(deepcopy(b27))
    return b28, b27
def fonk16(b25, crossover_prob, height_limit):
    for i in range(0, len(b25), 2):
        if random.random() < crossover_prob:
            b25[i], b25[i+1] = fonk10(b25[i], b25[i+1], height_limit)
            b25[i].b1 = None
            b25[i+1].b1 = None
    return b25
def fonk17(b25, mutation_prob, b21, b22):
    for i in range(len(b25)):
        b25[i] = fonk11(b25[i], b21, b22, mutation_prob)
        b25[i].b1 = None
    return b25