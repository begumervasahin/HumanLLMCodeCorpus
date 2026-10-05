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
    def fonk13(self, query):
        b6 = class1(query)
        if not self.b5:
            self.fonk14(self.b4, "")
            self.b5 = sorted(self.b5, key=lambda x: x.fonk2()[1], reverse=True)
        for node in self.b5:
            if node.fonk2()[0] == b6.fonk2():
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
    def fonk15(self, b15):
        return self.fonk16(self.b4, b15)
    def fonk16(self, node, b15):
        if len(b15) > 0:
            if b15[0] == "0":
                if node.fonk3():
                    return self.fonk16(node.fonk3(), b15[1:])
                else:
                    return node.fonk2()[0], b15
            if b15[0] == "1":
                if node.fonk4():
                    return self.fonk16(node.fonk4(), b15[1:])
                else:
                    return node.fonk2()[0], b15
        return node.fonk2()[0], b15
    def fonk17(self, b8):
        if isinstance(b8[0], list):
            b7 = []
            for i in b8:
                b7.append(class1(i))
            b8 = b7
        if len(b8) > 1:
            b9 = class1(['', b8[0].fonk2()[1] + b8[1].fonk2()[1]])
            b9.fonk5(b8[0])
            b9.fonk6(b8[1])
            b8.append(b9)
            b8 = sorted(b8[2:], key=lambda x: x.fonk2()[1], reverse=False)
            self.fonk17(b8)
        else:
            self.b4 = b8[0]
    def fonk18(self):
        self.fonk19(self.b4)
        print()
    def fonk19(self, node):
        if node.fonk3():
            self.fonk19(node.fonk3())
        print(node.fonk2(), b10 = " ")
        if node.fonk4():
            self.fonk19(node.fonk4())
if b11 = = "__main__":
    b12 = class2()
    b12.fonk17([['a', 1], ['b', 1], ['c', 1], ['d', 2], ['e', 6], ['f', 10], ['g', 15]])
    b13 = b12.fonk13('c')
    b14 = b12.fonk13('a')
    b15 = str(b13 + b14)
    print(b15)
    while b15:
        character, b15 = b12.fonk15(b15)
        print(character, b10 = "")