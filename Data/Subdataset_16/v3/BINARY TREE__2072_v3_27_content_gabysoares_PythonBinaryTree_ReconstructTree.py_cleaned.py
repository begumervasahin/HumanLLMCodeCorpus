class class1:
    a1 = 0
    a2 = 1
    a3 = 2
    def fonk1(self, root_value, b1 = None, right=None):
        self.b2 = [root_value, b1, right]
    def fonk2(self, a_list):
        return class1(a_list[0], a_list[1], a_list[2])
    def fonk3(self, value):
        self.b2[self.a2] = class1(value, self.b2[self.a2], None)
    def fonk4(self, value):
        self.b2[self.a3] = class1(value, None, self.b2[self.a3])
    def fonk5(self, b3):
        self.b2[self.a2] = b3
    def fonk6(self, b3):
        self.b2[self.a3] = b3
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
def fonk12(b6, b7, b4, end):
    if b4 > end:
        return None
    b3 = class1(b7[construct_tree.a4])
    construct_tree.a4 += 1
    if b4 = = end:
        return b3
    b5 = b6.index(b3.fonk8())
    b3.fonk5(fonk12(b6, b7, b4, b5 - 1))
    b3.fonk6(fonk12(b6, b7, b5 + 1, end))
    return b3
construct_tree.a4 = 0
def fonk13():
    print("Binary Tree reconstructed:")
    b6 = input("Please enter the b6 sequence (space-separated): ")
    b7 = input("Please enter the b7 sequence (space-separated): ")
    b6 = b6.split()
    b7 = b7.split()
    b3 = fonk12(b6, b7, 0, len(b7) - 1)
    print(b3)
if b8 = = "__main__":
    fonk13()