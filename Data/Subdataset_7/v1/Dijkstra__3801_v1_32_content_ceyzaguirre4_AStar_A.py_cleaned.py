from time import time
class class1:
    b1 = {}
    def fonk1(self, b3, heuristic_func, b2 = None, path_cost=1):
        self.b3 = b3
        self.b4 = 0 if not heuristic_func else heuristic_func(self.b3)
        self.b5 = b2.b5 + path_cost if b2 else 0
        self.b2 = b2
        class1.b1[self.b3] = self
    def fonk2(self, other):
        if other and self.b3 = = other:
            return True
        return False
    def fonk3(self):
        return str(self.b3)
class class2(list):
    def fonk4(self, start, b13):
        super().fonk4()
        self.append(class1(start, b13))
    def fonk5(self, other, b7, other_father, b13):
        if other in class1.b1:
            b6 = class1.b1[other]
            b7 = b7 + other_father.b5
            if b7 < b6.b5:
                b6.b5 = b7
                b6.b2 = other_father
                self.fonk8(b6)
            return
        self.fonk6(class1(other, b13, other_father, b7))
    def fonk6(self, elem):
        def fonk7(elem):
            return elem.b4 + elem.b5
        if len(self):
            b8 = fonk7(elem)
            b11, b9 = 0, len(self)
            b10 = (b11 + b9)
            while b9 - b11 > 1:
                if b8 >= fonk7(self[b10]):
                    b9 = b10
                else:
                    b11 = b10
                b10 = (b11 + b9)
            if b8 > fonk7(self[b11]):
                self[b11:b11] = [elem]
            else:
                self[b9:b9] = [elem]
        else:
            self.append(elem)
    def fonk8(self, elem):
        if len(self):
            b11, b9 = 0, len(self)
            b10 = (b11 + b9)
            while b9 - b11 > 1:
                if elem.b3 >= self[b10].b3:
                    b9 = b10
                else:
                    b11 = b10
                b10 = (b11 + b9)
            if elem.b3 = = self[b11].b3:
                del self[b11]
                self.fonk6(elem)
    def fonk9(self, b12, reverse):
        class1.b1.clear()
        if reverse:
            return self.fonk10(b12)
        return list(self.fonk10(b12))[::-1]
    def fonk10(self, b12):
        while b12 is not None:
            yield b12.b3
            b12 = b12.b2
def fonk11(calc_posibles, start, basecase, b13 = None, b14=0, reverse=False):
    b14 = float('inf') if b14 == 0 else b14
    b15 = time()
    b16 = class2(start, b13)
    while time() < b15 + b14:
        if not b16:
            return False
        b17 = b16.pop()
        if fonk13(b17.b3):
            return b16.fonk9(b17, reverse)
        b18 = fonk12(b17.b3)
        for elem, cost in b18:
            b16.fonk5(elem, cost, b17, b13)
    raise TimeoutError("Time limit reached, you can manually change or remove it.")
def fonk12(b3):
    pass
def fonk13(b3):
    pass
def fonk14(b3):
    pass
b19 = fonk11(calc_posibles, start='start_node', basecase=basecase, b13=b13, b14=10, reverse=False)
print(b19)