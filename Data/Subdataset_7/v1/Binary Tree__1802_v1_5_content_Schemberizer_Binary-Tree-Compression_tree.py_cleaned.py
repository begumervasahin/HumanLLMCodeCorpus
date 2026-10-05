import random
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
        return self.b4 = = None
    def fonk9(self):
        return self.fonk29(self.b4)
    def fonk10(self, node):
        if not node:
            return 0
        return 1 + self.fonk29(node.fonk22()) + self.fonk29(node.fonk23())
    def fonk11(self):
        return self.fonk31(self.b4)
    def fonk12(self, node):
        if not node:
            return 0
        return 1 + max(self.fonk31(node.fonk22()), self.fonk31(node.fonk23()))
    def fonk13(self, b6):
        b6 = class3(b6)
        if self.b5 = = []:
            self.fonk33(self.b4, "")
            self.b5 = sorted(self.b5, key=lambda x: x.fonk21()[1], reverse=True)
        for node in self.b5:
            if node.fonk21()[0] == b6.fonk21():
                return node.fonk21()[2]
        return "error"
    def fonk14(self, node, path):
        if node.fonk21()[0] == '':
            if node.fonk22():
                self.fonk33(node.fonk22(), path + "0")
            if node.fonk23():
                self.fonk33(node.fonk23(), path + "1")
        if not node.fonk23() and not node.fonk22():
            node.b1.append(path)
            self.b5.append(node)
    def fonk15(self, bit):
        return self.fonk35(self.b4, bit)
    def fonk16(self, node, bit):
        if len(bit) > 0:
            if bit[0] == "0":
                if node.fonk22():
                    return self.fonk35(node.fonk22(), bit[1:])
                else:
                    return node.fonk21()[0], bit
            if bit[0] == "1":
                if node.fonk23():
                    return self.fonk35(node.fonk23(), bit[1:])
                else:
                    return node.fonk21()[0], bit
        return node.fonk21()[0], bit
    def fonk17(self, b8):
        if isinstance(b8[0], list):
            b7 = []
            for i in b8:
                b7.append(class3(i))
            b8 = b7
        if len(b8) > 1:
            b9 = class3(['', b8[0].fonk21()[1] + b8[1].fonk21()[1]])
            b9.fonk24(b8[0])
            b9.fonk25(b8[1])
            b8.append(b9)
            b8 = sorted(b8[2:], key=lambda x: x.fonk21()[1], reverse=False)
            self.fonk36(b8)
        else:
            self.b4 = b8[0]
    def fonk18(self):
        self.fonk38(self.b4)
        print()
    def fonk19(self, node):
        if node.fonk22():
            self.fonk38(node.fonk22())
        print(node.fonk21(), b10 = " ")
        if node.fonk23():
            self.fonk38(node.fonk23())
if b11 = = "__main__":
    b12 = class4()
    b12.fonk36([['b14',1],['b',1],['b13',1],['d',2],['e',6],['f',10],['g',15]])
    b13 = b12.fonk32('b13')
    b14 = b12.fonk32('b14')
    b15 = str(b13 + b14)
    print(b15)
    while b15:
        char, b15 = b12.fonk34(b15)
        print(char, b10 = "")
import random
class class3:
    def fonk20(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
    def fonk21(self):
        return self.b1
    def fonk22(self):
        return self.b2
    def fonk23(self):
        return self.b3
    def fonk24(self, node):
        self.b2 = node
    def fonk25(self, node):
        self.b3 = node
class class4:
    def fonk26(self):
        self.b4 = None
        self.b5 = []
    def fonk27(self):
        return self.b4 = = None
    def fonk28(self):
        return self.fonk29(self.b4)
    def fonk29(self, node):
        if not node:
            return 0
        return 1 + self.fonk29(node.fonk22()) + self.fonk29(node.fonk23())
    def fonk30(self):
        return self.fonk31(self.b4)
    def fonk31(self, node):
        if not node:
            return 0
        return 1 + max(self.fonk31(node.fonk22()), self.fonk31(node.fonk23()))
    def fonk32(self, b6):
        b6 = class3(b6)
        if self.b5 = = []:
            self.fonk33(self.b4, "")
            self.b5 = sorted(self.b5, key=lambda x: x.fonk21()[1], reverse=True)
        for node in self.b5:
            if node.fonk21()[0] == b6.fonk21():
                return node.fonk21()[2]
        return "error"
    def fonk33(self, node, path):
        if node.fonk21()[0] == '':
            if node.fonk22():
                self.fonk33(node.fonk22(), path + "0")
            if node.fonk23():
                self.fonk33(node.fonk23(), path + "1")
        if not node.fonk23() and not node.fonk22():
            node.b1.append(path)
            self.b5.append(node)
    def fonk34(self, bit):
        return self.fonk35(self.b4, bit)
    def fonk35(self, node, bit):
        if len(bit) > 0:
            if bit[0] == "0":
                if node.fonk22():
                    return self.fonk35(node.fonk22(), bit[1:])
                else:
                    return node.fonk21()[0], bit
            if bit[0] == "1":
                if node.fonk23():
                    return self.fonk35(node.fonk23(), bit[1:])
                else:
                    return node.fonk21()[0], bit
        return node.fonk21()[0], bit
    def fonk36(self, b8):
        if isinstance(b8[0], list):
            b7 = []
            for i in b8:
                b7.append(class3(i))
            b8 = b7
        if len(b8) > 1:
            b9 = class3(['', b8[0].fonk21()[1] + b8[1].fonk21()[1]])
            b9.fonk24(b8[0])
            b9.fonk25(b8[1])
            b8.append(b9)
            b8 = sorted(b8[2:], key=lambda x: x.fonk21()[1], reverse=False)
            self.fonk36(b8)
        else:
            self.b4 = b8[0]
    def fonk37(self):
        self.fonk38(self.b4)
        print()
    def fonk38(self, node):
        if node.fonk22():
            self.fonk38(node.fonk22())
        print(node.fonk21(), b10 = " ")
        if node.fonk23():
            self.fonk38(node.fonk23())
if b11 = = "__main__":
    b12 = class4()
    b12.fonk36([['b14',1],['b',1],['b13',1],['d',2],['e',6],['f',10],['g',15]])
    b13 = b12.fonk32('b13')
    b14 = b12.fonk32('b14')
    b15 = str(b13 + b14)
    print(b15)
    while b15:
        char, b15 = b12.fonk34(b15)
        print(char, b10 = "")