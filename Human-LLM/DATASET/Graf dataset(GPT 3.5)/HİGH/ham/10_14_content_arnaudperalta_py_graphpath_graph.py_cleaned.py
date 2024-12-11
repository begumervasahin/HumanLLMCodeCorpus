import numpy as np
class class1:
    def fonk1(self, data):
        self.b1 = data["nbNoeuds"]
        self.b2 = list(data["nomSommets"])
        self.b3 = list(data["nomRdv"])
        self.b4 = list(data["nomSommetsInitiaux"])
        self.b5 = list(data["b5"])
        self.a1 = 0
        if self.b2.__len__() != data["nbNoeuds"]:
            self.a1 = 1
        if self.b3.__len__() != data["nbLieuxRdv"]:
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
            b10[self.fonk4(arc["sommetInitial"])
                , self.fonk4(arc["sommetTerminal"])] = arc["duree"]
        return b10
    def fonk4(self, char):
        return self.b2.index(char)
    def fonk5(self, b10):
        b11 = self.b1 * self.b1
        b12 = np.full((b11, b11), np.inf)
        for b13 in range(self.b1):
            for b14 in range(self.b1):
                for k in range(self.b1):
                    for l in range(self.b1):
                        if b13 = = k and b14 == l :
                            b12[b13 * self.b1 + b14, k * self.b1 + l] \
                                = np.inf
                        elif b13 = = k :
                            b12[b13 * self.b1 + b14, k * self.b1 + l] \
                                = b10[b14, l]
                        elif b14 = = l :
                            b12[b13 * self.b1 + b14, k * self.b1 + l] \
                                = b10[b13, k]
        return b12
    def fonk6(self):
        b15 = self.fonk7(self.fonk5(self.fonk3()))
        b16 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b17 = []
        for c in self.b3:
            b17.append(self.fonk4(c) * self.b1 + self.fonk4(c))
        b9 = np.inf
        b18 = np.inf
        for b13 in range(len(b17)):
            if b15[b16, b17[b13]] < b9:
                b9 = b15[b16, b17[b13]]
                b18 = b13
        if b18 != np.inf:
            return str(self.b3[b18])
        else:
            return ""
    def fonk7(self, b10):
        b11 = self.b1 * self.b1
        for b13 in range(b11):
            b10[b13, b13] = 0
        for k in range(b11):
            for b13 in range(b11):
                for b14 in range(b11):
                    b10[b13, b14] = b8(b10[b13, b14], b10[b13, k] + b10[k, b14])
        return b10
    def fonk8(self, b10, b19, depth):
        if depth > self.b8:
            return
        self.b6[depth] = b19
        if b19 = = self.a2:
            if self.b8 = = depth:
                self.b9.append(np.copy(self.b6[0:depth + 1]).astype(int).tolist())
            if self.b8 > depth:
                self.b8 = depth
                self.b9 = [np.copy(self.b6[0:depth + 1]).astype(int).tolist()]
            return
        self.b7[b19] = 1
        for b13 in range(self.b1 ** 2):
            if b10[b19][b13] == np.inf or self.b7[b13] == 1:
                continue
            self.fonk8(b10, b13, depth + 1)
        self.b7[b19] = 0
        return
    def fonk9(self):
        b11 = self.b1 * self.b1
        b10 = self.fonk5(self.fonk3())
        b16 = self.fonk4(self.b4[0]) * self.b1 + self.fonk4(self.b4[1])
        b17 = []
        for c in self.b3:
            b17.append(self.fonk4(c) * self.b1 + self.fonk4(c))
        b20 = []
        b21 = np.inf
        for b13 in range(len(b17)):
            self.b7 = np.zeros(self.b1 ** 2)
            self.b6 = np.zeros(self.b1 ** 2)
            self.b8 = np.inf
            self.a2 = b17[b13]
            self.fonk8(b10, b16, 0)
            if len(self.b9[0]) < b21:
                b21 = len(self.b9[0])
            b20.append(self.b9)
        b22 = []
        for b13 in range(len(b20)):
            if (len(b20[b13][0])) == b21:
                b22.append(b20[b13])
        b23 = np.inf
        b24 = np.inf
        if len(b22) > 1:
            for b13 in range(len(b22)):
                a3 = 0
                for u in range(len(b22[b13])):
                    for b14 in range(b21 - 1):
                        a3 = a3 + b10[b22[b13][u][b14]][b22[b13][u][b14 + 1]]
                    if a3 < b23:
                        b24 = b22[b13][0][b21 - 1]
                        b23 = a3
        else:
            b24 = b22[0][0][b21 - 1]
        return str(self.b2[(b24