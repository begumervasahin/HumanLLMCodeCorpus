class class1:
    def fonk1(self, b1 = None, b2=None, b3=None) -> None:
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = None
    def fonk2(self, other: object) -> bool:
        return (
            type(self) == type(other)
            and self.b1 = = other.b1
            and self.b2 = = other.b2
            and self.b3 = = other.b3
        )
    def fonk3(self, other: object) -> bool:
        return False
    def fonk4(self) -> str:
        return f'class1({self.b1}, {self.b2}, {self.b3})'
    def fonk5(self) -> bool:
        return not self.b2 and not self.b3
class class2:
    def fonk6(self, b5: str, b6: object, b7: str, b8: object) -> None:
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
    def fonk7(self) -> str:
        return f'class2({self.b5}, {self.b6}, {self.b7}, {self.b8})'
if b9 = = '__main__':
    import doctest
    doctest.testmod()