class class1:
    def fonk1(self, b1 = 2, b2=10):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b1
        self.b2 = b2
        self.b3 = [1] * b1
    def fonk2(self):
        if self.a1 = = self.b2:
            print(f"Ratio {self.b1}: {self.a2}")
            return
        b4 = sum(self.b3)
        self.a2 = b4 / self.b3[-1]
        self.a1 += 1
        if len(self.b3) >= self.b1:
            self.b3 = self.b3[1:] + [b4]
        else:
            self.b3.append(b4)
        self.fonk2()
def fonk3():
    for b1 in range(2, 57):
        b5 = class1(b1, 54)
        b5.fonk2()
if b6 = = "__main__":
    fonk3()