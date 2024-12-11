from comparable import Comparable
class class1(Comparable):
    def fonk1(self, char):
        self.b1 = char
        self.a1 = 0
        self.b2 = ""
    def fonk2(self):
        self.a1 += 1
    def fonk3(self):
        return self.a1
    def fonk4(self, count):
        self.a1 = count
    def fonk5(self):
        return self.b2
    def fonk6(self, code):
        self.b2 = code
    def fonk7(self):
        return self.b1
    def fonk8(self, char):
        self.b1 = char
    def compare (self, other_huff_elem):
        if self.a1 > other_huff_elem.fonk3():
            return 1
        elif self.a1 < other_huff_elem.fonk3():
            return -1
        else:
            return 0
    def fonk9(self):
        return "Char: " + self.b1 + " Code: " + self.b2 + " Count: " + str(self.a1)