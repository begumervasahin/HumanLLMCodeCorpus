import numpy as np
class class1:
    def fonk1(self, data):
        self.b1 = data["nbNoeuds"]
        self.b2 = data["nomSommets"]
        self.b3 = data["nomRdv"]
        self.b4 = data["nomSommetsInitiaux"]
        self.b5 = data["b5"]
        self.a1 = 0
        if len(self.b2) != data["nbNoeuds"]:
            self.a1 = 1
        if len(self.b3) != data["nbLieuxRdv"]:
            self.a1 = 2
        self.b6 = np.zeros(self.b1 ** 2, dtype=int)
        self.b7 = np.zeros(self.b1 ** 2, dtype=bool)
        self.a2 = 0
        self.b8 = np.inf
        self.b9 = []
    def fonk2(self):
        return self.a1
    def fonk3(self):
        b10 = np.full((self.b1, self.b1), np.inf)
        for arc in self.b5:
            b14, b11 = self.fonk4(arc["sommetInitial"]), self.fonk4(arc["sommetTerminal"])
            b10[b14, b11] = arc["duree"]
        return b10
    def fonk4(self, char):
        return self.b2.index(char)
    def fonk5(self, b10):
        b12 = self.b1 * self.b1
        b13 = np.full((b12, b12), np.inf)
        for b14 in range(self.b1):
            for b11 in range(self.b1):
                for k in range(self.b1):
                    for l in range(self.b1):
                        if b14 = = k and b11 == l:
                            b13[b14 * self.b1 + b11, k * self.b1 + l] = np.inf
                        elif b14 = = k:
                            b13[b14 * self.b1 + b11, k * self.b1 + l] = b10[b11, l]
                        elif b11 = = l:
                            b13[b14 * self.b1 + b11, k * self.b1 + l] = b10[b14, k]
        return b13
    def fonk6(self):
        b15 = self.fonk7(self.fonk5(self.fonk3()))
        b16 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b17 = [self.fonk4(c) * self.b1 + self.fonk4(c) for c in self.b3]
        b18 = np.inf
        b19 = None
        for idx, rdv_point in enumerate(b17):
            if b15[b16, rdv_point] < b18:
                b18 = b15[b16, rdv_point]
                b19 = idx
        return self.b3[b19] if b19 is not None else ""
    def fonk7(self, b10):
        b12 = self.b1 * self.b1
        for b14 in range(b12):
            b10[b14, b14] = 0
        for k in range(b12):
            for b14 in range(b12):
                for b11 in range(b12):
                    b10[b14, b11] = min(b10[b14, b11], b10[b14, k] + b10[k, b11])
        return b10
    def fonk8(self, b10, b20, depth):
        if depth > self.b8:
            return
        self.b6[depth] = b20
        if b20 = = self.a2:
            if self.b8 = = depth:
                self.b9.append(np.copy(self.b6[:depth + 1]).tolist())
            if self.b8 > depth:
                self.b8 = depth
                self.b9 = [np.copy(self.b6[:depth + 1]).tolist()]
            return
        self.b7[b20] = True
        for b14 in range(self.b1 ** 2):
            if b10[b20][b14] != np.inf and not self.b7[b14]:
                self.fonk8(b10, b14, depth + 1)
        self.b7[b20] = False
    def fonk9(self):
        b12 = self.b1 * self.b1
        b10 = self.fonk5(self.fonk3())
        b16 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b17 = [self.fonk4(c) * self.b1 + self.fonk4(c) for c in self.b3]
        b21 = []
        b22 = np.inf
        for a2 in b17:
            self.b7.fill(False)
            self.b6.fill(0)
            self.b8 = np.inf
            self.a2 = a2
            self.fonk8(b10, b16, 0)
            if len(self.b9[0]) < b22:
                b22 = len(self.b9[0])
            b21.append(self.b9)
        b23 = [roads for roads in b21 if len(roads[0]) == b22]
        b18 = np.inf
        b24 = None
        if len(b23) > 1:
            for roads in b23:
                b25 = sum(b10[roads[0][b11]][roads[0][b11 + 1]] for b11 in range(b22 - 1))
                if b25 < b18:
                    b24 = roads[0][b22 - 1]
                    b18 = b25
        else:
            b24 = b23[0][0][b22 - 1]
        return self.b2[b24