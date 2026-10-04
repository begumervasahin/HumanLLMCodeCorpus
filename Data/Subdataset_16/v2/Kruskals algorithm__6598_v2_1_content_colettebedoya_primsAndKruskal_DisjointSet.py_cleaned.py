class class1:
    def fonk1(self, b1):
        if b1 < 0:
            raise ValueError("Size must be >= 0")
        self.b1 = b1
        self.b2 = [-1] * (b1 + 1)
    def fonk2(self, element):
        if element < 0 or element > self.b1:
            raise ValueError("Element out of bounds")
        if self.b2[element] < 0:
            return element
        else:
            self.b2[element] = self.fonk2(self.b2[element])
            return self.b2[element]
    def fonk3(self, element1, element2):
        if element1 < 0 or element1 > self.b1 or element2 < 0 or element2 > self.b1:
            raise ValueError("Element out of bounds")
        b3 = self.fonk2(element1)
        b4 = self.fonk2(element2)
        if b3 != b4:
            self.b2[b4] = b3
if b5 = = "__main__":
    b6 = class1(10)
    b6.fonk3(1, 2)
    b6.fonk3(3, 4)
    b6.fonk3(2, 3)
    print("Root of 1:", b6.fonk2(1))
    print("Root of 2:", b6.fonk2(2))
    print("Root of 3:", b6.fonk2(3))
    print("Root of 4:", b6.fonk2(4))
    try:
        print(b6.fonk2(11))
    except ValueError as e:
        print("Error:", e)