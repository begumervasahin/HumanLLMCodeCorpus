from typing import Set
class class1:
    def fonk1(self, b2: int, b3: int, b4: int, b6: int, b1 = False):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b6
        self.b1 = b1
        if self.b6 = = 0:
            self.b7 = set(range(1, 10))
        else:
            self.b7 = set()
    @property
    def fonk2(self):
        return self.b6 = = 0
    @property
    def fonk3(self):
        return self.b5
    @b6.setter
    def fonk4(self, b6):
        if b6 in range(0, 10) and not self.b1:
            self.b5 = b6
    @property
    def fonk5(self):
        return self.b7
    @b10.setter
    def fonk6(self, b10: Set[int]):
        self.b7 = b10
    def fonk7(self):
        if self.is_empty:
            return '.'
        else:
            return str(self.b6)
if b8 = = "__main__":
    b9 = class1(0, 0, 0, 5)
    print("Initial class1 Value:", b9)
    print("Is Empty:", b9.is_empty)
    print("Possibilities:", b9.b10)
    b9.b6 = 3
    print("\nUpdated class1 Value:", b9)
    print("Is Empty:", b9.is_empty)
    b9.b10 = {1, 2, 4, 6}
    print("\nUpdated Possibilities:", b9.b10)