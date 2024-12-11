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
            if self.b1[b2].distance > self.b1[b3].distance:
                self.b1[b2], self.b1[b3] = self.b1[b3], self.b1[b2]
                b3 = b2
            else:
                break
    def fonk4(self):
        if self.b1[0] < 1:
            return None
        b4 = self.b1[1]
        b5 = self.b1[self.b1[0]]
        self.b1[1] = b5
        self.b1[0] -= 1
        if self.b1[0] > 1:
            self.fonk5(1)
        self.b1.pop()
        return b4
    def fonk5(self, b3):
        while 2 * b3 <= self.b1[0]:
            b6 = 2 * b3
            b7 = b6 + 1
            if b7 > self.b1[0] or self.b1[b6].distance < self.b1[b7].distance:
                b8 = b6
            else:
                b8 = b7
            if self.b1[b3].distance > self.b1[b8].distance:
                self.b1[b3], self.b1[b8] = self.b1[b8], self.b1[b3]
                b3 = b8
            else:
                break
if b9 = = "__main__":
    pass