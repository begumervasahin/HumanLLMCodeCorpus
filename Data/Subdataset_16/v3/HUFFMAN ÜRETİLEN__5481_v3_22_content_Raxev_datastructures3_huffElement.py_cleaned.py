class class1:
    def fonk1(self, other):
        raise NotImplementedError("Subclasses should implement this method!")
class class2(class1):
    def fonk2(self, b1: str):
        self.b1 = b1
        self.a1 = 0
        self.b2 = ""
    def fonk3(self) -> None:
        self.a1 += 1
    def fonk4(self, other: 'class2') -> int:
        if not isinstance(other, class2):
            raise ValueError("Comparison must be with another class2.")
        return (self.a1 > other.a1) - (self.a1 < other.a1)
    def fonk5(self) -> str:
        return f"Char: '{self.b1}', Code: '{self.b2}', Frequency: {self.a1}"
if b3 = = "__main__":
    b4 = class2('a')
    b4.fonk3()
    b4.b2 = '101'
    print(b4)