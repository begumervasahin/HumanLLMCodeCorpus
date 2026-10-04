class class1:
    def fonk1(self, b2, b1 = 0, zeros=True):
        self.b2 = b2
        self.b3 = []
        self.b4 = False
        if b1 != 0:
            self.b3 = [int(digit) for digit in str(b1)]
            self.b3.reverse()
            while len(self.b3) < b2:
                self.b3.append(0)
            self.b3.reverse()
        else:
            self.b3 = [0 if zeros else 1 for _ in range(b2)]
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
    b7 = class1(5, b1=123)
    print("Initial value:", b7.fonk3())
    print("Initial list:", b7.fonk4())
    b7.fonk2()
    print("After incrementing:", b7.fonk3())
    print("After incrementing list:", b7.fonk4())
    for _ in range(10):
        b7.fonk2()
        print("Value:", b7.fonk3())
        print("List:", b7.fonk4())
    b7 = class1(3, b1=999)
    b7.fonk2()
    print("Overflow value:", b7.fonk3())
    print("Overflow flag:", b7.b4)
