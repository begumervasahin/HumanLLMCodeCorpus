class class1:
    def fonk1(self, b1 = 2, b2=10):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b1
        self.b2 = b2
        self.b3 = [1, 1]
    def fonk2(self):
        while self.a1 < self.b2:
            self.a1 += 1
            b4 = sum(self.b3)
            self.a2 = b4 / self.b3[-1]
            if len(self.b3) >= self.b1:
                self.b3.pop(0)
            self.b3.append(b4)
        print(f"Ratio {self.b1}: {self.a2}")
if b5 = = "__main__":
    for i in range(55):
        b6 = class1(i, 54)
        b6.fonk2()