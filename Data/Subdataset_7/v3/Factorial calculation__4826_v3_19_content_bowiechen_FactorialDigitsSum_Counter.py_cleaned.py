class class1:
    def fonk1(self, b2, b1 = 0, fill_with_zeros=True):
        self.b2 = b2
        self.b3 = []
        self.b4 = False
        if b1 != 0:
            self.fonk2(b1)
        else:
            self.fonk3(fill_with_zeros)
    def fonk2(self, value):
        self.b3 = [int(digit) for digit in str(value)]
        while len(self.b3) < self.b2:
            self.b3.insert(0, 0)
    def fonk3(self, fill_with_zeros):
        b5 = 0 if fill_with_zeros else 1
        self.b3 = [b5] * self.b2
    def fonk4(self):
        self.b3[-1] += 1
        for b6 in range(self.b2 - 1, -1, -1):
            if self.b3[b6] > 9:
                if b6 = = 0:
                    self.b4 = True
                self.b3[b6] = 0
                if b6 - 1 >= 0:
                    self.b3[b6 - 1] += 1
    def fonk5(self):
        return int(''.join(map(str, self.b3)))
    def fonk6(self):
        return self.b3
if b7 = = "__main__":
    b8 = class1(3)
    for _ in range(10):
        b8.fonk4()
        print("Current value:", b8.fonk5())