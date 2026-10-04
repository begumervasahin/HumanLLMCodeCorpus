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
            self.b2[b4] = b5
            if b5.b1 < self.b2[b4].b1:
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
            b6 = (b4 - 1)
            if self.b2[b4].b1 < self.b2[b6].b1:
                self.b2[b4], self.b2[b6] = self.b2[b6], self.b2[b4]
                b4 = b6
            else:
                break
    def fonk10(self, b4):
        while True:
            b7 = self.fonk11(b4)
            if b7 is None or self.b2[b7].b1 >= self.b2[b4].b1:
                break
            self.b2[b4], self.b2[b7] = self.b2[b7], self.b2[b4]
            b4 = b7
    def fonk11(self, b4):
        b8 = self.b3 * b4 + 1
        b9 = min(self.b3 * b4 + self.b3, self.fonk8() - 1)
        if b8 > b9:
            return None
        b10 = b8
        b11 = self.b2[b8].b1
        for i in range(b8 + 1, b9 + 1):
            if self.b2[i].b1 < b11:
                b10 = i
                b11 = self.b2[i].b1
        return b10
    def fonk12(self):
        return str(self.b2)
if b12 = = "__main__":
    b13 = [class1(b1) for b1 in [5, 3, 8, 1, 2, 9, 7]]
    b14 = class2(b3=2)
    b14.fonk4(b13)
    print("Heap after creation:", b14)
    print("Minimum element:", b14.fonk5())
    b14.fonk7()
    print("Heap after deleting minimum element:", b14)