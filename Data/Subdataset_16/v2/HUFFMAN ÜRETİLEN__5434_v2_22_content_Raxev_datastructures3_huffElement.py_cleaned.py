class class1:
    def fonk1(self, other):
        raise NotImplementedError("Subclasses should implement this method!")
class class2(class1):
    def fonk2(self, char: str):
        self.b1 = char
        self.a1 = 0
        self.b2 = ""
    def fonk3(self) -> None:
        self.a1 += 1
    def fonk4(self) -> int:
        return self.a1
    def fonk5(self, frequency: int) -> None:
        self.a1 = frequency
    def fonk6(self) -> str:
        return self.b2
    def fonk7(self, code: str) -> None:
        self.b2 = code
    def fonk8(self) -> str:
        return self.b1
    def fonk9(self, char: str) -> None:
        self.b1 = char
    def fonk10(self, other: 'class2') -> int:
        return (self.a1 > other.fonk4()) - (self.a1 < other.fonk4())
    def fonk11(self) -> str:
        return f"Char: {self.b1} | Code: {self.b2} | Frequency: {self.a1}"
if b3 = = "__main__":
    b4 = class2('a')
    b4.fonk3()
    b4.fonk7('101')
    print(b4)