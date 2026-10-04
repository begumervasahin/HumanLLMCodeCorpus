class class1:
    def fonk1(self, char: str):
        self.b1 = char
        self.a1 = 0
        self.b2 = ""
    def fonk2(self):
        self.a1 += 1
    @property
    def fonk3(self) -> int:
        return self.a1
    @frequency.setter
    def fonk4(self, value: int):
        self.a1 = value
    @property
    def fonk5(self) -> str:
        return self.b2
    @code.setter
    def fonk6(self, value: str):
        self.b2 = value
    @property
    def fonk7(self) -> str:
        return self.b1
    @char.setter
    def fonk8(self, value: str):
        self.b1 = value
    def fonk9(self, other: 'class1') -> int:
        if self.a1 > other.frequency:
            return 1
        elif self.a1 < other.frequency:
            return -1
        else:
            return 0
    def fonk10(self) -> str:
        return f"Char: '{self.b1}', Code: '{self.b2}', Frequency: {self.a1}"