class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, element1, element2):
        if not self.fonk4(element1) or not self.fonk4(element2):
            raise ValueError("Element value out of range")
        self.b2[element2] = element1
    def fonk3(self, element):
        if not self.fonk4(element):
            raise ValueError("Element value out of range")
        if self.b2[element] < 0:
            return element
        else:
            return self.fonk3(self.b2[element])
    def fonk4(self, element):
        return 0 <= element <= self.b1
if b3 = = "__main__":
    b4 = class1(10)
    b4.fonk2(1, 2)
    b4.fonk2(3, 4)
    print(b4.fonk3(2))
    print(b4.fonk3(4))
    b4.fonk2(1, 3)
    print(b4.fonk3(4))
