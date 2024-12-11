import numpy as np
class class1:
    def fonk1(self, b26):
        self.b1 = b26["nbNoeuds"]
        self.b2 = list(b26["nomSommets"])
        self.b3 = list(b26["nomRdv"])
        self.b4 = list(b26["nomSommetsInitiaux"])
        self.b5 = list(b26["b5"])
        self.a1 = 0
        if len(self.b2) != self.b1:
            self.a1 = 1
        if len(self.b3) != b26["nbLieuxRdv"]:
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
        b13 = np.full((self.b1 ** 2, self.b1 ** 2), np.inf)
        for b14 in range(self.b1):
            for b15 in range(self.b1):
                for k in range(self.b1):
                    for l in range(self.b1):
                        if b14 = = k and b15 == l:
                            b13[b14 * self.b1 + b15, k * self.b1 + l] = np.inf
                        elif b14 = = k:
                            b13[b14 * self.b1 + b15, k * self.b1 + l] = matrix[b15, l]
                        elif b15 = = l:
                            b13[b14 * self.b1 + b15, k * self.b1 + l] = matrix[b14, k]
        return b13
    def fonk6(self):
        b16 = self.fonk7(self.fonk5(self.fonk3()))
        b17 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b18 = [self.fonk4(vertex) * self.b1 + self.fonk4(vertex) for vertex in self.b3]
        b19 = np.inf
        b20 = np.inf
        for b14 in range(len(b18)):
            if b16[b17, b18[b14]] < b19:
                b19 = b16[b17, b18[b14]]
                b20 = b14
        if b20 != np.inf:
            return str(self.b3[b20])
        else:
            return ""
    def fonk7(self, matrix):
        for b14 in range(self.b1 ** 2):
            matrix[b14, b14] = 0
        for k in range(self.b1 ** 2):
            for b14 in range(self.b1 ** 2):
                for b15 in range(self.b1 ** 2):
                    matrix[b14, b15] = min(matrix[b14, b15], matrix[b14, k] + matrix[k, b15])
        return matrix
    def fonk8(self, matrix, b21, depth):
        if depth > self.b8:
            return
        self.b6[depth] = b21
        if b21 = = self.a2:
            if self.b8 = = depth:
                self.b9.append(np.copy(self.b6[0:depth + 1]).astype(int).tolist())
            if self.b8 > depth:
                self.b8 = depth
                self.b9 = [np.copy(self.b6[0:depth + 1]).astype(int).tolist()]
            return
        self.b7[b21] = 1
        for b14 in range(self.b1 ** 2):
            if matrix[b21][b14] == np.inf or self.b7[b14] == 1:
                continue
            self.fonk8(matrix, b14, depth + 1)
        self.b7[b21] = 0
        return
    def fonk9(self):
        b13 = self.fonk5(self.fonk3())
        b17 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b18 = [self.fonk4(vertex) * self.b1 + self.fonk4(vertex) for vertex in self.b3]
        b22 = []
        b23 = np.inf
        for b14 in range(len(b18)):
            self.b7 = np.zeros(self.b1 ** 2)
            self.b6 = np.zeros(self.b1 ** 2)
            self.b8 = np.inf
            self.a2 = b18[b14]
            self.fonk8(b13, b17, 0)
            if len(self.b9[0]) < b23:
                b23 = len(self.b9[0])
            b22.append(self.b9)
        b24 = []
        for b14 in range(len(b22)):
            if len(b22[b14][0]) == b23:
                b24.append(b22[b14])
        b25 = np.inf
        b20 = np.inf
        if len(b24) > 1:
            for b14 in range(len(b24)):
                a3 = 0
                for u in range(len(b24[b14])):
                    for b15 in range(b23 - 1):
                        a3 += b13[b24[b14][u][b15]][b24[b14][u][b15 + 1]]
                if a3 < b25:
                    b20 = b24[b14][0][b23 - 1]
                    b25 = a3
        else:
            b20 = b24[0][0][b23 - 1]
        return str(self.b2[(b20
b26 = {
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
b27 = class1(b26)
print("Optimal rendezvous point:", b27.fonk6())
print("Optimal rendezvous point 2:", b27.fonk9())