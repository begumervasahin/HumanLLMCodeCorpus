class class1(Comparable):
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
    def fonk4(self, count: int):
        self.a1 = count
    @property
    def fonk5(self) -> str:
        return self.b2
    @code.setter
    def fonk6(self, huffman_code: str):
        self.b2 = huffman_code
    @property
    def fonk7(self) -> str:
        return self.b1
    @char.setter
    def fonk8(self, character: str):
        self.b1 = character
    def fonk9(self, other: 'class1') -> int:
        if self.a1 > other.frequency:
            return 1
        elif self.a1 < other.frequency:
            return -1
        return 0
    def fonk10(self) -> str:
        return f"Char: {self.b1} Code: {self.b2} Frequency: {self.a1}"