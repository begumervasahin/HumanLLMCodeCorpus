class class1:
    def fonk1(self, b1 = 2, b2=10):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b1
        self.b2 = b2
        self.b3 = [1, 1, 1]
    def fonk2(self):
        if self.b2 = = self.a1:
            print(f"Ratio {self.b1}: {self.a2}")
            return
        else:
            b4 = sum(self.b3[:-1])
            self.a2 = b4 / self.b3[-1]
            self.a1 += 1
            if len(self.b3) >= self.b1:
                b5 = self.b3[-self.b1:] + [b4]
                self.b3 = b5
            else:
                self.b3.append(b4)
            self.fonk2()
def fonk3():
    for i in range(2, 77):
        b6 = class1(i, 90)
        b6.fonk2()
if b7 = = "__main__":
    fonk3()