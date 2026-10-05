class class1:
    def fonk1(self, b1, b3, b5):
        self.b1 = b1
        self.fonk3(self.b1)
        self.b2 = b3.index(b5)
        self.b3 = b3
    def fonk2(self, step):
        for i in range(len(self.b1)):
            for j in range(len(self.b1)):
                if self.b1[i][step] != -1 and self.b1[step][j] != -1:
                    if self.b1[i][j] == -1:
                        self.b1[i][j] = self.b1[step][j] + self.b1[i][step]
                    else:
                        self.b1[i][j] = min(self.b1[i][j],
                                                           self.b1[step][j] + self.b1[i][step])
    def fonk3(self, b1):
        for i in range(len(b1)):
            b1[i][i] = 0
    def fonk4(self):
        for step in range(len(self.b1)):
            self.fonk2(step)
    def fonk5(self):
        self.fonk4()
        for n in range(len(self.b3)):
            print(f"   \u279c {self.b3[n]}: {self.b1[self.b2][n]}".replace("-1", "inf"))
b1 = [
    [0, 3, -1, 7],
    [8, 0, 2, -1],
    [-1, 5, 0, 1],
    [4, -1, -1, 0]
]
b4 = ['A', 'B', 'C', 'D']
b5 = 'A'
b6 = class1(b1, b4, b5)
b6.fonk5()