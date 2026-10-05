class class1:
    def fonk1(self, b1 = 2, b2=10):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b1
        self.b2 = b2
        self.b3 = [1, 1]
    def fonk2(self):
        if self.b2 = = self.a1:
            print(f"Ratio {self.b1}: {self.a2}")
            return
        else:
            b4 = sum(self.b3)
            self.a2 = b4 / self.b3[-1]
            self.a1 += 1
            if len(self.b3) >= self.b1:
                b5 = self.b3[slice(len(self.b3) + 1 - self.b1, len(self.b3))]
                b5.append(b4)
                self.b3 = b5
            else:
                self.b3.append(b4)
            self.fonk2()
if b6 = = "__main__":
    for i in range(55):
        b7 = class1(i, 54)
        b7.fonk2()