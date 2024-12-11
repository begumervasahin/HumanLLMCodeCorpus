class class1:
    def fonk1(self, b1: int, b2: int, b3: int, b4: int) -> None:
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
    def fonk2(self) -> str:
        return f"({self.b1}, {self.b2}, {self.b3})"
    def fonk3(self, other: 'class1') -> bool:
        return self.b1 = = other.b1 and self.b2 == other.b2 and self.b3 == other.b3 and self.b4 == other.b4
    @staticmethod
    def fonk4(b1: int, b2: int, b3: int, b4: int) -> 'class1':
        return class1(b1, b2, b3, b4)
    def fonk5(self) -> 'class1':
        self.b2 = (-self.b2) % self.b4
        return self