class class1:
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
            raise ValueError("Tree is empty")
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
            raise ValueError("Tree is empty")
    def fonk7(self, b2):
        if self.b1:
            self.b1 = self.b1.fonk17(b2)
        else:
            raise ValueError("Tree is empty")
    def fonk8(self):
        if self.b1:
            return iter(self.b1)
        else:
            return iter([])
class class2:
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
                raise ValueError("Value not found")
        elif b2 > self.b2:
            if self.b4:
                return self.b4.fonk11(b2)
            else:
                raise ValueError("Value not found")
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
        for b2 in b9:
            b8.append(b2)
        return b8
    def fonk16(self, b2):
        if b2 < self.b2:
            if self.b3:
                self.b3 = self.b3.fonk16(b2)
            else:
                raise ValueError("Value not found")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk16(b2)
            else:
                raise ValueError("Value not found")
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
                raise ValueError("Value not found")
        elif b2 > self.b2:
            if self.b4:
                self.b4 = self.b4.fonk17(b2)
            else:
                raise ValueError("Value not found")
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
        return class3(self)
class class3:
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
        yield from binary_search_node.b3
    yield binary_search_node.b2
    if binary_search_node.b4:
        yield from binary_search_node.b4