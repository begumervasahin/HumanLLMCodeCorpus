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
            if 2 * b3 = = self.b1[0] or self.b1[2 * b3].distance < self.b1[2 * b3 + 1].distance:
                b2 = 2 * b3
            else:
                b2 = 2 * b3 + 1
            if self.b1[b2].distance < self.b1[b3].distance:
                self.b1[b3], self.b1[b2] = self.b1[b2], self.b1[b3]
                b3 = b2
            else:
                break
if b6 = = "__main__":
    b7 = class1()
    b7.fonk2(5)
    b7.fonk2(3)
    b7.fonk2(8)
    b7.fonk2(1)
    b7.fonk2(10)
    print(b7.fonk4())
    print(b7.fonk4())
