class class1:
    a1 = 0
    a2 = 1
    a3 = 2
    def fonk1(self, b3, b1 = None, right=None):
        self.b2 = [b3, b1, right]
    @classmethod
    def fonk2(cls, a_list):
        return cls(a_list[0], a_list[1], a_list[2])
    def fonk3(self, value):
        self.b2[self.a2] = class1(value, self.b2[self.a2], None)
    def fonk4(self, value):
        self.b2[self.a3] = class1(value, None, self.b2[self.a3])
    def fonk5(self, b4):
        self.b2[self.a2] = b4
    def fonk6(self, b4):
        self.b2[self.a3] = b4
    def fonk7(self, new_value):
        self.b2[self.a1] = new_value
    def fonk8(self):
        return self.b2[self.a1]
    def fonk9(self):
        return self.b2[self.a2]
    def fonk10(self):
        return self.b2[self.a3]
    def fonk11(self):
        return f'[{self.b2[self.a1]}, {self.b2[self.a2]}, {self.b2[self.a3]}]'
def fonk12(b9, b10, b5, end):
    if b5 > end:
        return None
    b3 = b10[construct_tree.a4]
    construct_tree.a4 += 1
    b4 = class1(b3)
    if b5 = = end:
        return b4
    b6 = b9.index(b3)
    b7 = fonk12(b9, b10, b5, b6 - 1)
    b8 = fonk12(b9, b10, b6 + 1, end)
    b4.fonk5(b7)
    b4.fonk6(b8)
    return b4
def fonk13():
    print("Binary Tree reconstructed by gsoa420:")
    b9 = input("Please enter the b9 sequence: ").split()
    b10 = input("Please enter the b10 sequence: ").split()
    construct_tree.a4 = 0
    b4 = fonk12(b9, b10, 0, len(b10) - 1)
    print(b4)
if b11 = = "__main__":
    fonk13()