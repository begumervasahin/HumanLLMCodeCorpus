class class1:
    def fonk1(self, b4, b5, b6, b7, b8, b9):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.a1 = 0
    def fonk2(self):
        while self.b1:
            self.a1 = max(self.a1, len(self.b1) + len(self.b2))
            b10 = self.fonk4()
            b11 = b10[0]
            b12 = b10[1]
            b13 = b10[2]
            b14 = b10[3]
            if self.b7(b11[-1]):
                return [b13, b11, b12, b14]
            self.b1.remove([b11, b12, b13, b14])
            if b11[-1] not in self.b2:
                self.b2.append(b11[-1])
            for action in self.b5(b11[-1]):
                b15 = self.b6(b11[-1], action)
                if b15 not in self.b2:
                    b16 = self.b8(b11[0], b15) + b12
                    b14 = self.b9(b15)
                    b17 = b11[:]
                    b17.append(b15)
                    b18 = b13[:]
                    b18.append(action)
                    self.b1.append([b17, b16, b18, b14])
                    if b15 not in self.b3:
                        self.b3.append(b15)
    def fonk3(self):
        b19 = self.b4()
        self.b1 = [[[b19], 0, [], 0]]
        self.b2 = []
        self.b20 = []
        b6 = self.fonk2()
        if not b6:
            print("There is no b11.")
        else:
            print("Path found:")
            print(b6[0])
            print("Number of visited nodes:", len(self.b3))
            print("Number of nodes in the closed list:", len(self.b2))
            print("Maximum memory usage:", self.a1)
            print("Path cost:", b6[2] + b6[3])
    def fonk4(self):
        b21 = float('inf')
        b22 = None
        for node in self.b1:
            b23 = node[1] + node[3]
            if b23 < b21:
                b21 = b23
                b22 = node
        return b22