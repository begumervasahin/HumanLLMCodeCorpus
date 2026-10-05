class class1:
    def fonk1(self):
        self.b1 = [0]
    def fonk2(self, key_value):
        self.b1.append(key_value)
        self.b1[0] = len(self.b1) - 1
        self.fonk3(self.b1[0])
    def fonk3(self, b3):
        while b3 > 1:
            b2 = b3
            if int(self.b1[b2].distance) > int(self.b1[b3].distance):
                self.b1[b3], self.b1[b2] = self.b1[b2], self.b1[b3]
                b3 = b2
            else:
                break
    def fonk4(self):
        b4 = self.b1[0]
        b5 = self.b1[1]
        self.b1[1] = self.b1[b4]
        self.b1[0] -= 1
        if self.b1[0] > 1:
            self.fonk5(1)
        del self.b1[-1]
        return b5
    def fonk5(self, b3):
        while 2 * b3 <= self.b1[0]:
            b6 = 2 * b3
            b7 = 2 * b3 + 1 if (2 * b3 < self.b1[0]) else b6
            if self.b1[b6].distance < self.b1[b7].distance:
                b8 = b6
            else:
                b8 = b7
            if self.b1[b8].distance < self.b1[b3].distance:
                self.b1[b3], self.b1[b8] = self.b1[b8], self.b1[b3]
                b3 = b8
            else:
                break
if b9 = = "__main__":
    b10 = class1()
    b10.fonk2(5)
    b10.fonk2(3)
    b10.fonk2(8)
    b10.fonk2(1)
    b10.fonk2(10)
    print(b10.fonk4())
    print(b10.fonk4())
w