import numpy as np
class class1:
    def fonk1(self, b27):
        self.b1 = b27["nbNoeuds"]
        self.b2 = list(b27["nomSommets"])
        self.b3 = list(b27["nomRdv"])
        self.b4 = list(b27["nomSommetsInitiaux"])
        self.b5 = list(b27["b5"])
        self.a1 = 0
        if len(self.b2) != b27["nbNoeuds"]:
            self.a1 = 1
        if len(self.b3) != b27["nbLieuxRdv"]:
            self.a1 = 2
        self.b6 = np.zeros(self.b1 ** 2)
        self.b7 = np.zeros(self.b1 ** 2)
        self.a2 = 0
        self.b8 = np.inf
        self.b9 = []
    def fonk2(self):
        return self.a1
    def fonk3(self):
        b10 = np.full((self.b1, self.b1), np.inf)
        for arc in self.b5:
            b11 = self.fonk4(arc["sommetInitial"])
            b12 = self.fonk4(arc["sommetTerminal"])
            b10[b11, b12] = arc["duree"]
        return b10
    def fonk4(self, vertex):
        return self.b2.index(vertex)
    def fonk5(self, matrix):
        b13 = self.b1 * self.b1
        b14 = np.full((b13, b13), np.inf)
        for b15 in range(self.b1):
            for b16 in range(self.b1):
                for k in range(self.b1):
                    for l in range(self.b1):
                        if b15 = = k and b16 == l:
                            b14[b15 * self.b1 + b16, k * self.b1 + l] = np.inf
                        elif b15 = = k:
                            b14[b15 * self.b1 + b16, k * self.b1 + l] = matrix[b16, l]
                        elif b16 = = l:
                            b14[b15 * self.b1 + b16, k * self.b1 + l] = matrix[b15, k]
        return b14
    def fonk6(self):
        b17 = self.fonk7(self.fonk5(self.fonk3()))
        b18 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b19 = [self.fonk4(vertex) * self.b1 + self.fonk4(vertex) for vertex in self.b3]
        b20 = np.inf
        b21 = np.inf
        for b15 in range(len(b19)):
            if b17[b18, b19[b15]] < b20:
                b20 = b17[b18, b19[b15]]
                b21 = b15
        if b21 != np.inf:
            return str(self.b3[b21])
        else:
            return ""
    def fonk7(self, matrix):
        b13 = self.b1 * self.b1
        for b15 in range(b13):
            matrix[b15, b15] = 0
        for k in range(b13):
            for b15 in range(b13):
                for b16 in range(b13):
                    matrix[b15, b16] = b8(matrix[b15, b16], matrix[b15, k] + matrix[k, b16])
        return matrix
    def fonk8(self, matrix, b22, depth):
        if depth > self.b8:
            return
        self.b6[depth] = b22
        if b22 = = self.a2:
            if self.b8 = = depth:
                self.b9.append(np.copy(self.b6[0:depth + 1]).astype(int).tolist())
            if self.b8 > depth:
                self.b8 = depth
                self.b9 = [np.copy(self.b6[0:depth + 1]).astype(int).tolist()]
            return
        self.b7[b22] = 1
        for b15 in range(self.b1 ** 2):
            if matrix[b22][b15] == np.inf or self.b7[b15] == 1:
                continue
            self.fonk8(matrix, b15, depth + 1)
        self.b7[b22] = 0
        return
    def fonk9(self):
        b14 = self.fonk5(self.fonk3())
        b18 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b19 = [self.fonk4(vertex) * self.b1 + self.fonk4(vertex) for vertex in self.b3]
        b23 = []
        b24 = np.inf
        for b15 in range(len(b19)):
            self.b7 = np.zeros(self.b1 ** 2)
            self.b6 = np.zeros(self.b1 ** 2)
            self.b8 = np.inf
            self.a2 = b19[b15]
            self.fonk8(b14, b18, 0)
            if len(self.b9[0]) < b24:
                b24 = len(self.b9[0])
            b23.append(self.b9)
        b25 = []
        for b15 in range(len(b23)):
            if len(b23[b15][0]) == b24:
                b25.append(b23[b15])
        b26 = np.inf
        b21 = np.inf
        if len(b25) > 1:
            for b15 in range(len(b25)):
                a3 = 0
                for u in range(len(b25[b15])):
                    for b16 in range(b24 - 1):
                        a3 += b14[b25[b15][u][b16]][b25[b15][u][b16 + 1]]
                if a3 < b26:
                    b21 = b25[b15][0][b24 - 1]
                    b26 = a3
        else:
            b21 = b25[0][0][b24 - 1]
        return str(self.b2[(b21
b27 = {
    "nbNoeuds": 4,
    "nomSommets": ["A", "B", "C", "D"],
    "nomRdv": ["C", "D"],
    "nomSommetsInitiaux": ["A", "B"],
    "nbLieuxRdv": 2,
    "b5": [
        {"sommetInitial": "A", "sommetTerminal": "B", "duree": 2},
        {"sommetInitial": "A", "sommetTerminal": "C", "duree": 5},
        {"sommetInitial": "B", "sommetTerminal": "D", "duree": 3},
        {"sommetInitial": "C", "sommetTerminal": "D", "duree": 1}
    ]
}
b28 = class1(b27)
print("Optimal rendezvous point:", b28.fonk6())
print("Optimal rendezvous point 2:", b28.fonk9())