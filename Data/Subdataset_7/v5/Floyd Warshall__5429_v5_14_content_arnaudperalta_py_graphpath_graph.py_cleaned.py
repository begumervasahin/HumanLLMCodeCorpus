import numpy as np
class class1:
    def fonk1(self, data):
        self.b1 = data["nbNoeuds"]
        self.b2 = list(data["nomSommets"])
        self.b3 = list(data["nomRdv"])
        self.b4 = list(data["nomSommetsInitiaux"])
        self.b5 = list(data["b5"])
        self.b6 = self.fonk2(data)
        self.b7 = np.zeros(self.b1 ** 2)
        self.b8 = np.zeros(self.b1 ** 2)
        self.a1 = 0
        self.b9 = np.inf
        self.b10 = []
    def fonk2(self, data):
        if len(self.b2) != self.b1:
            return 1
        elif len(self.b3) != data["nbLieuxRdv"]:
            return 2
        return 0
    def fonk3(self, vertex):
        return self.b2.index(vertex)
    def fonk4(self):
        b11 = np.full((self.b1, self.b1), np.inf)
        for arc in self.b5:
            b12 = self.fonk3(arc["sommetInitial"])
            b13 = self.fonk3(arc["sommetTerminal"])
            b11[b12, b13] = arc["duree"]
        return b11
    def fonk5(self, matrix):
        b14 = np.full((self.b1 ** 2, self.b1 ** 2), np.inf)
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
        b17 = self.fonk7(self.fonk5(self.fonk4()))
        b18 = self.fonk3(self.b4[0]) * self.b1 + self.fonk3(self.b4[1])
        b19 = [self.fonk3(vertex) * self.b1 + self.fonk3(vertex) for vertex in self.b3]
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
        for b15 in range(self.b1 ** 2):
            matrix[b15, b15] = 0
        for k in range(self.b1 ** 2):
            for b15 in range(self.b1 ** 2):
                for b16 in range(self.b1 ** 2):
                    matrix[b15, b16] = min(matrix[b15, b16], matrix[b15, k] + matrix[k, b16])
        return matrix
    def fonk8(self, matrix, b22, depth):
        if depth > self.b9:
            return
        self.b7[depth] = b22
        if b22 = = self.a1:
            if self.b9 = = depth:
                self.b10.append(np.copy(self.b7[0:depth + 1]).astype(int).tolist())
            if self.b9 > depth:
                self.b9 = depth
                self.b10 = [np.copy(self.b7[0:depth + 1]).astype(int).tolist()]
            return
        self.b8[b22] = 1
        for b15 in range(self.b1 ** 2):
            if matrix[b22][b15] == np.inf or self.b8[b15] == 1:
                continue
            self.fonk8(matrix, b15, depth + 1)
        self.b8[b22] = 0
        return
    def fonk9(self):
        b14 = self.fonk5(self.fonk4())
        b18 = self.fonk3(self.b4[0]) * self.b1 + self.fonk3(self.b4[1])
        b19 = [self.fonk3(vertex) * self.b1 + self.fonk3(vertex) for vertex in self.b3]
        b23 = []
        b24 = np.inf
        for b15 in range(len(b19)):
            self.b8 = np.zeros(self.b1 ** 2)
            self.b7 = np.zeros(self.b1 ** 2)
            self.b9 = np.inf
            self.a1 = b19[b15]
            self.fonk8(b14, b18, 0)
            if len(self.b10[0]) < b24:
                b24 = len(self.b10[0])
            b23.append(self.b10)
        b25 = []
        for b15 in range(len(b23)):
            if len(b23[b15][0]) == b24:
                b25.append(b23[b15])
        b26 = np.inf
        b21 = np.inf
        if len(b25) > 1:
            for b15 in range(len(b25)):
                a2 = 0
                for u in range(len(b25[b15])):
                    for b16 in range(b24 - 1):
                        a2 += b14[b25[b15][u][b16]][b25[b15][u][b16 + 1]]
                if a2 < b26:
                    b21 = b25[b15][0][b24 - 1]
                    b26 = a2
        else:
            b21 = b25[0][0][b24 - 1]
        return str(self.b2[(b21