class class1:
    def fonk1(self):
        self.b1 = [0]
    def fonk2(self, key_value):
        self.b1.append(key_value)
        self.fonk3()
        self.fonk5(self.fonk4())
    def fonk3(self):
        self.b1[0] = self.fonk4()
    def fonk4(self):
        return len(self.b1) - 1
    def fonk5(self, b3):
        while b3 > 1:
            b2 = b3
            if self.fonk6(b2, b3):
                self.fonk7(b2, b3)
                b3 = b2
            else:
                break
    def fonk6(self, b2, b3):
        return int(self.b1[b2].distance) > int(self.b1[b3].distance)
    def fonk7(self, index1, index2):
        self.b1[index1], self.b1[index2] = self.b1[index2], self.b1[index1]
    def fonk8(self):
        b4 = self.fonk4()
        b5 = self.b1[1]
        self.b1[1] = self.b1[b4]
        self.fonk3()
        if self.fonk4() > 1:
            self.fonk9(1)
        self.b1.pop()
        return b5
    def fonk9(self, b3):
        while 2 * b3 <= self.fonk4():
            b6 = 2 * b3
            b7 = b6 + 1
            b8 = self.fonk10(b6, b7)
            if self.fonk11(b8, b3):
                self.fonk7(b3, b8)
                b3 = b8
            else:
                break
    def fonk10(self, b6, b7):
        if b7 > self.fonk4() or \
                int(self.b1[b6].distance) < int(self.b1[b7].distance):
            return b6
        else:
            return b7
    def fonk11(self, child_index, b2):
        return int(self.b1[child_index].distance) < int(self.b1[b2].distance)
if b9 = = "__main__":
    b10 = class1()
    b10.fonk2(5)
    b10.fonk2(3)
    b10.fonk2(8)
    b10.fonk2(1)
    b10.fonk2(10)
    print(b10.fonk8())
    print(b10.fonk8())
