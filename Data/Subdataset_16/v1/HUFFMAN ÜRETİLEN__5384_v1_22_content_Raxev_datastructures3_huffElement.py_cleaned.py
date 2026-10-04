class class1:
    def fonk1(self, other):
        raise NotImplementedError("Subclasses should implement this!")
class class2(class1):
    def fonk2(self, char):
        self.b1 = char
        self.a1 = 0
        self.b2 = ""
    def fonk3(self):
        self.a1 += 1
    def fonk4(self):
        return self.a1
    def fonk5(self, count):
        self.a1 = count
    def fonk6(self):
        return self.b2
    def fonk7(self, code):
        self.b2 = code
    def fonk8(self):
        return self.b1
    def fonk9(self, char):
        self.b1 = char
    def fonk10(self, other_huff_elem):
        if self.a1 > other_huff_elem.fonk4():
            return 1
        elif self.a1 < other_huff_elem.fonk4():
            return -1
        else:
            return 0
    def fonk11(self):
        return f"Char: {self.b1} Code: {self.b2} Count: {self.a1}"
if b3 = = "__main__":
    b4 = class2('a')
    b4.fonk3()
    b4.fonk7('101')
    print(b4)