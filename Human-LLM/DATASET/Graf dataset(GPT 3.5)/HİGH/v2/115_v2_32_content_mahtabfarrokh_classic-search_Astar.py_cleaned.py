class class1:
    def fonk1(self, b5, b6, b7, b8, b9, b10):
        self.b1 = []
        self.b2 = []
        self.b3 = []
        self.b4 = []
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.a1 = 0
    def fonk2(self):
        while self.b1:
            self.a1 = max(self.a1, len(self.b1) + len(self.b2))
            b11 = self.b1[0]
            b12 = b11[1]
            b13 = b11[0]
            b14 = b11[2]
            b15 = b11[3]
            for b18 in self.b1:
                if b18[1] + b18[3] < b12 + b15:
                    b12 = b18[1]
                    b13 = b18[0]
                    b14 = b18[2]
                    b15 = b18[3]
            b16 = b13[-1]
            for b18 in self.b1:
                b17 = b18[0]
                if b17[-1] == b16 and b18[1] + b18[3] > b12 + b15:
                    self.b1.remove(b18)
            if self.b8(b16):
                return [b14, b13, b12, b15]
            self.b1.remove([b13, b12, b14, b15])
            if b16 not in self.b2:
                self.b2.append(b16)
            for act in self.b6(b16):
                b18 = self.b7(b16, act)
                if b18 not in self.b2:
                    b19 = self.b9(b13[0], b18) + b12
                    b15 = self.b10(b18)
                    b20 = b13 + [b18]
                    b21 = b14 + [act]
                    self.b1.append([b20, b19, b21, b15])
                    if b18 not in self.b4:
                        self.b4.append(b18)
    def fonk3(self):
        b22 = self.b5()
        self.b1 = [[[b22], 0, [], 0]]
        self.b2 = []
        self.b3 = []
        b17 = self.fonk2()
        if not b17:
            print("There is no b13")
        else:
            print("Path found:")
            print(b17[0])
            print("Number of b4 nodes:", len(self.b4))
            print("Number of nodes in closed list:", len(self.b2))
            print("Max memory usage:", self.a1)
            print("Path cost:", b17[2] + b17[3])
