class class1(object):
    def fonk1(self):
        self.b1 = None
    def fonk2(self, b2):
        if self.b1:
            self.b1.fonk10(b2)
        else:
            self.b1 = class2(b2)
    def fonk3(self, b2):
        if self.b1:
            return self.b1.fonk11(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk4(self):
        if self.b1:
            return self.b1.fonk14()
        else:
            return []
    def fonk5(self):
        if self.b1:
            return self.b1.fonk15()
        else:
            return []
    def fonk6(self, b2):
        if self.b1:
            self.b1 = self.b1.fonk16(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk7(self, b2):
        if self.b1:
            self.b1 = self.b1.fonk17(b2)
        else:
            raise ValueError("Value not found in the tree")
    def fonk8(self):
        if self.b1:
            return iter(self.b1)
        else:
            return iter([])
class class2(object):
    def fonk9(self, b2):
        self.b2 = b2
        self.b3 = None
        self.b4 = None
    def fonk10(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3.fonk10(b2)
            else:
                self.b3 = class2(b2)
        else:
            if self.b4:
                self.b4.fonk10(b2)
            else:
                self.b4 = class2(b2)
    def fonk11(self, b2):
        if b2 < self.b2:
            if self.b3:
                return self.b3.fonk11(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                return self.b4.fonk11(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            return self
    def fonk12(self):
        if self.b4:
            return self.b4.fonk12()
        else:
            return self
    def fonk13(self):
        if self.b3:
            return self.b3.fonk13()
        else:
            return self
    def fonk14(self):
        b5 = self.b3.fonk14() if self.b3 else []
        b6 = [self.b2]
        b7 = self.b4.fonk14() if self.b4 else []
        return b5 + b6 + b7
    def fonk15(self):
        b8 = []
        b9 = class3(self)
        while True:
            try:
                b2 = next(b9)
            except StopIteration:
                break
            else:
                b8.append(b2)
        return b8
    def fonk16(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3 = self.b3.fonk16(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk16(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            if self.b3:
                b10 = self.b3.fonk12()
                self.b2 = b10.b2
                self.b3 = self.b3.fonk18()
            else:
                return self.b4
        return self
    def fonk17(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3 = self.b3.fonk17(b2)
            else:
                raise ValueError("Value not found in the tree")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk17(b2)
            else:
                raise ValueError("Value not found in the tree")
        else:
            if self.b4:
                b11 = self.b4.fonk13()
                self.b2 = b11.b2
                self.b4 = self.b4.fonk19()
            else:
                return self.b3
        return self
    def fonk18(self):
        if self.b4:
            self.b4 = self.b4.fonk18()
        else:
            return self.b3
        return self
    def fonk19(self):
        if self.b3:
            self.b3 = self.b3.fonk19()
        else:
            return self.b4
        return self
    def fonk20(self):
        return fonk29(self)
class class3(object):
    def fonk21(self, b1):
        b12 = class2(None)
        b12.b4 = b1
        self.b13 = [b12]
    def fonk22(self):
        if self.fonk25().b4:
            self.fonk23()
        else:
            self.fonk24()
        return self.fonk25().b2
    def fonk23(self):
        self.b13.append(self.fonk25().b4)
        while self.fonk25().b3:
            self.b13.append(self.fonk25().b3)
    def fonk24(self):
        try:
            while self.b13.pop() == self.fonk25().b4:
                pass
        except IndexError:
            raise StopIteration
    def fonk25(self):
        return self.b13[-1]
    def fonk26(self):
        return self
def fonk27(binary_search_node):
    return iter(binary_search_node.fonk14())
def fonk28(binary_search_node):
    return class3(binary_search_node)
def fonk29(binary_search_node):
    if binary_search_node.b3:
        yield from fonk29(binary_search_node.b3)
    yield binary_search_node.b2
    if binary_search_node.b4:
        yield from fonk29(binary_search_node.b4)
if b14 = = "__main__":
    b15 = class1()
    b15.fonk10(5)
    b15.fonk10(3)
    b15.fonk10(7)
    b15.fonk10(2)
    b15.fonk10(4)
    b15.fonk10(6)
    b15.fonk10(8)
    print("Tree list:", b15.fonk14())
    print("Tree list sequentially:", b15.fonk15())
    b15.fonk16(3)
    print("Tree list after deleting 3 (b3):", b15.fonk14())
    b15.fonk17(7)
    print("Tree list after deleting 7 (b4):", b15.fonk14())