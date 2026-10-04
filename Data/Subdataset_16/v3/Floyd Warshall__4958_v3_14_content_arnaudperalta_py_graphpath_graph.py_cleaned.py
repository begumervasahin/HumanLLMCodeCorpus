import numpy as np
class class1:
    def fonk1(self, data):
        self.b1 = data["nbNoeuds"]
        self.b2 = data["nomSommets"]
        self.b3 = data["nomRdv"]
        self.b4 = data["nomSommetsInitiaux"]
        self.b5 = data["b5"]
        self.b6 = self.fonk2(data)
        self.b7 = np.zeros(self.b1 ** 2, dtype=int)
        self.b8 = np.zeros(self.b1 ** 2, dtype=bool)
        self.a1 = 0
        self.b9 = np.inf
        self.b10 = []
    def fonk2(self, data):
        if len(self.b2) != data["nbNoeuds"]:
            return 1
        if len(self.b3) != data["nbLieuxRdv"]:
            return 2
        return 0
    def fonk3(self):
        return self.b6
    def fonk4(self):
        b11 = np.full((self.b1, self.b1), np.inf)
        for arc in self.b5:
            b12 = self.fonk5(arc["sommetInitial"])
            b13 = self.fonk5(arc["sommetTerminal"])
            b11[b12, b13] = arc["duree"]
        return b11
    def fonk5(self, char):
        return self.b2.index(char)
    def fonk6(self, b11):
        b14 = self.b1 * self.b1
        b15 = np.full((b14, b14), np.inf)
        for b12 in range(self.b1):
            for b13 in range(self.b1):
                for k in range(self.b1):
                    for l in range(self.b1):
                        if b12 = = k and b13 == l:
                            b15[b12 * self.b1 + b13, k * self.b1 + l] = np.inf
                        elif b12 = = k:
                            b15[b12 * self.b1 + b13, k * self.b1 + l] = b11[b13, l]
                        elif b13 = = l:
                            b15[b12 * self.b1 + b13, k * self.b1 + l] = b11[b12, k]
        return b15
    def fonk7(self):
        b16 = self.fonk8(self.fonk6(self.fonk4()))
        b17 = self.fonk5(self.b4[0]) * self.b1 + self.fonk5(self.b4[1])
        b18 = [self.fonk5(c) * self.b1 + self.fonk5(c) for c in self.b3]
        b19 = np.inf
        b20 = None
        for idx, rdv_point in enumerate(b18):
            if b16[b17, rdv_point] < b19:
                b19 = b16[b17, rdv_point]
                b20 = idx
        return self.b3[b20] if b20 is not None else ""
    def fonk8(self, b11):
        b14 = self.b1 * self.b1
        for b12 in range(b14):
            b11[b12, b12] = 0
        for k in range(b14):
            for b12 in range(b14):
                for b13 in range(b14):
                    b11[b12, b13] = min(b11[b12, b13], b11[b12, k] + b11[k, b13])
        return b11
    def fonk9(self, b11, b21, depth):
        if depth > self.b9:
            return
        self.b7[depth] = b21
        if b21 = = self.a1:
            if self.b9 = = depth:
                self.b10.append(np.copy(self.b7[:depth + 1]).tolist())
            if self.b9 > depth:
                self.b9 = depth
                self.b10 = [np.copy(self.b7[:depth + 1]).tolist()]
            return
        self.b8[b21] = True
        for b12 in range(self.b1 ** 2):
            if b11[b21][b12] != np.inf and not self.b8[b12]:
                self.fonk9(b11, b12, depth + 1)
        self.b8[b21] = False
    def fonk10(self):
        b11 = self.fonk6(self.fonk4())
        b17 = self.fonk5(self.b4[0]) * self.b1 + self.fonk5(self.b4[1])
        b18 = [self.fonk5(c) * self.b1 + self.fonk5(c) for c in self.b3]
        b22 = []
        b23 = np.inf
        for a1 in b18:
            self.b8.fill(False)
            self.b7.fill(0)
            self.b9 = np.inf
            self.a1 = a1
            self.fonk9(b11, b17, 0)
            if len(self.b10[0]) < b23:
                b23 = len(self.b10[0])
            b22.append(self.b10)
        b24 = [roads for roads in b22 if len(roads[0]) == b23]
        b19 = np.inf
        b25 = None
        if len(b24) > 1:
            for roads in b24:
                b26 = sum(b11[roads[0][b13]][roads[0][b13 + 1]] for b13 in range(b23 - 1))
                if b26 < b19:
                    b25 = roads[0][b23 - 1]
                    b19 = b26
        else:
            b25 = b24[0][0][b23 - 1]
        return self.b2[b25