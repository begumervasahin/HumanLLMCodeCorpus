class class1:
    def fonk1(self, b2, b1 = 0, zeros=True):
        self.b2 = b2
        self.b3 = []
        self.b4 = False
        if b1 != 0:
            self.fonk2(b1)
        else:
            self.fonk3(zeros)
    def fonk2(self, b1):
        self.b3 = [int(digit) for digit in str(b1)]
        self.fonk4()
    def fonk3(self, zeros):
        self.b3 = [0 if zeros else 1] * self.b2
    def fonk4(self):
        while len(self.b3) < self.b2:
            self.b3.insert(0, 0)
    def fonk5(self):
        self.b3[-1] += 1
        for b5 in range(self.b2 - 1, -1, -1):
            if self.b3[b5] > 9:
                if b5 = = 0:
                    self.b4 = True
                self.b3[b5] = 0
                if b5 - 1 >= 0:
                    self.b3[b5 - 1] += 1
    def fonk6(self):
        return int(''.join(map(str, self.b3)))
    def fonk7(self):
        return self.b3