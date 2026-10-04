import math
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return f"class1({self.b1})"
class class2:
    def fonk3(self, b3):
        self.b2 = []
        self.b3 = b3
    def fonk4(self, lst):
        self.b2 = lst
        for b4 in range(self.fonk8() - 1, -1, -1):
            self.fonk10(b4)
    def fonk5(self):
        return self.b2[0] if self.fonk8() > 0 else None
    def fonk6(self, b4):
        if b4 = = self.fonk8() - 1:
            self.b2.pop()
        else:
            b5 = self.b2.pop()
            b6 = self.b2[b4]
            self.b2[b4] = b5
            if b5.b1 < b6.b1:
                self.fonk9(b4)
            else:
                self.fonk10(b4)
    def fonk7(self):
        if self.fonk8() > 0:
            self.fonk6(0)
    def fonk8(self):
        return len(self.b2)
    def fonk9(self, b4):
        while b4 > 0:
            b7 = (b4 - 1)
            if self.b2[b4].b1 < self.b2[b7].b1:
                self.b2[b4], self.b2[b7] = self.b2[b7], self.b2[b4]
                b4 = b7
            else:
                break
    def fonk10(self, b4):
        while True:
            b8 = self.fonk11(b4)
            if b8 is None or self.b2[b8].b1 >= self.b2[b4].b1:
                break
            self.b2[b4], self.b2[b8] = self.b2[b8], self.b2[b4]
            b4 = b8
    def fonk11(self, b4):
        b9 = self.b3 * b4 + 1
        b10 = min(self.b3 * b4 + self.b3, self.fonk8() - 1)
        if b9 > b10:
            return None
        b11 = b9
        b12 = self.b2[b9].b1
        for i in range(b9 + 1, b10 + 1):
            if self.b2[i].b1 < b12:
                b11 = i
                b12 = self.b2[i].b1
        return b11
    def fonk12(self):
        return str(self.b2)
if b13 = = "__main__":
    b14 = [class1(b1) for b1 in [5, 3, 8, 1, 2, 9, 7]]
    b15 = class2(b3=2)
    b15.fonk4(b14)
    print("Heap after creation:", b15)
    print("Minimum element:", b15.fonk5())
    b15.fonk7()
    print("Heap after deleting minimum element:", b15)