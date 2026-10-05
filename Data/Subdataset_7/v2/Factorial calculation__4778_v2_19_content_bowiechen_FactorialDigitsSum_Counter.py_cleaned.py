class class1:
    def fonk1(self, b2, b1 = 0, zeros=True):
        self.b2 = b2
        self.b3 = []
        self.b4 = False
        if b1 != 0:
            self.b3 = [int(digit) for digit in str(b1)]
            while len(self.b3) < b2:
                self.b3.insert(0, 0)
        else:
            self.b3 = [0 if zeros else 1] * b2
    def fonk2(self):
        self.b3[-1] += 1
        for b5 in range(self.b2 - 1, -1, -1):
            if self.b3[b5] > 9:
                if b5 = = 0:
                    self.b4 = True
                self.b3[b5] = 0
                if b5 - 1 >= 0:
                    self.b3[b5 - 1] += 1
    def fonk3(self):
        return int(''.join(map(str, self.b3)))
    def fonk4(self):
        return self.b3
if b6 = = "__main__":
    b7 = class1(3)
    for _ in range(10):
        b7.fonk2()
        print("Current value:", b7.fonk3())