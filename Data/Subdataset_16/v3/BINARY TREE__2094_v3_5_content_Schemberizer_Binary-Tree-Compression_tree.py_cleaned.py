class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return self.b3
    def fonk5(self, node):
        self.b2 = node
    def fonk6(self, node):
        self.b3 = node
class class2:
    def fonk7(self):
        self.b4 = None
        self.b5 = []
    def fonk8(self):
        return self.b4 is None
    def fonk9(self):
        return self.fonk10(self.b4)
    def fonk10(self, node):
        if not node:
            return 0
        return 1 + self.fonk10(node.fonk3()) + self.fonk10(node.fonk4())
    def fonk11(self):
        return self.fonk12(self.b4)
    def fonk12(self, node):
        if not node:
            return 0
        return 1 + max(self.fonk12(node.fonk3()), self.fonk12(node.fonk4()))
    def fonk13(self, char):
        if not self.b5:
            self.fonk14(self.b4, "")
            self.b5 = sorted(self.b5, key=lambda x: x.fonk2()[1], reverse=True)
        for node in self.b5:
            if node.fonk2()[0] == char:
                return node.fonk2()[2]
        return "error"
    def fonk14(self, node, path):
        if node.fonk2()[0] == '':
            if node.fonk3():
                self.fonk14(node.fonk3(), path + "0")
            if node.fonk4():
                self.fonk14(node.fonk4(), path + "1")
        if not node.fonk4() and not node.fonk3():
            node.b1.append(path)
            self.b5.append(node)
    def fonk15(self, bit_string):
        return self.fonk16(self.b4, bit_string)
    def fonk16(self, node, bit_string):
        if len(bit_string) > 0:
            if bit_string[0] == "0":
                if node.fonk3():
                    return self.fonk16(node.fonk3(), bit_string[1:])
                else:
                    return node.fonk2()[0], bit_string
            if bit_string[0] == "1":
                if node.fonk4():
                    return self.fonk16(node.fonk4(), bit_string[1:])
                else:
                    return node.fonk2()[0], bit_string
        return node.fonk2()[0], bit_string
    def fonk17(self, b6):
        if isinstance(b6[0], list):
            b6 = [class1(item) for item in b6]
        if len(b6) > 1:
            b7 = class1(['', b6[0].fonk2()[1] + b6[1].fonk2()[1]])
            b7.fonk5(b6[0])
            b7.fonk6(b6[1])
            b6.append(b7)
            b6 = sorted(b6[2:], key=lambda x: x.fonk2()[1])
            self.fonk17(b6)
        else:
            self.b4 = b6[0]
    def fonk18(self):
        self.fonk19(self.b4)
        print()
    def fonk19(self, node):
        if node.fonk3():
            self.fonk19(node.fonk3())
        print(node.fonk2(), b8 = " ")
        if node.fonk4():
            self.fonk19(node.fonk4())
if b9 = = "__main__":
    b10 = class2()
    b11 = [['a', 1], ['b', 1], ['c', 1], ['d', 2], ['e', 6], ['f', 10], ['g', 15]]
    b10.fonk17(b11)
    b12 = b10.fonk13('c')
    b13 = b10.fonk13('a')
    b14 = str(b12 + b13)
    print(b14)
    while b14:
        decoded_char, b14 = b10.fonk15(b14)
        print(decoded_char, b8 = "")