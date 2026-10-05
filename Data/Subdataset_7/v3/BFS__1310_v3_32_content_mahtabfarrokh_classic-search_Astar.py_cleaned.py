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
            for node in self.b1:
                if node[1] + node[3] < b12 + b15:
                    b12 = node[1]
                    b13 = node[0]
                    b14 = node[2]
                    b15 = node[3]
            b16 = b13[-1]
            for node in self.b1:
                b17 = node[0]
                if b17[-1] == b16 and node[1] + node[3] > b12 + b15:
                    self.b1.remove(node)
            if self.b8(b16):
                return [b14, b13, b12, b15]
            self.b1.remove([b13, b12, b14, b15])
            if b16 not in self.b2:
                self.b2.append(b16)
            for action in self.b6(b16):
                b18 = self.b7(b16, action)
                if b18 not in self.b2:
                    b19 = self.b9(b13[0], b18) + b12
                    b15 = self.b10(b18)
                    b20 = b13 + [b18]
                    b21 = b14 + [action]
                    self.b1.append([b20, b19, b21, b15])
                    if b18 not in self.b4:
                        self.b4.append(b18)
    def fonk3(self):
        b22 = self.b5()
        self.b1 = [[[b22], 0, [], 0]]
        self.b2 = []
        self.b3 = []
        b7 = self.fonk2()
        if not b7:
            print("There is no b13")
        else:
            print("Path found:")
            print(b7[0])
            print("Number of visited nodes:", len(self.b4))
            print("Number of nodes in closed list:", len(self.b2))
            print("Max memory usage:", self.a1)
            print("Path b19:", b7[2] + b7[3])
