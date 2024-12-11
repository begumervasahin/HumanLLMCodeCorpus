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
        return isinstance(other, class1) and self.b3 = = other.b3
    def fonk3(self):
        return str(self.b3)
class class2(list):
    def fonk4(self, start, b11):
        super().fonk4([class1(start, b11)])
    def fonk5(self, b3, b7, b2, b11):
        if b3 in class1.b1:
            b6 = class1.b1[b3]
            b7 = b7 + b2.b5
            if b7 < b6.b5:
                b6.b5 = b7
                b6.b2 = b2
                self.fonk8(b6)
            return
        self.fonk6(class1(b3, b11, b2, b7))
    def fonk6(self, elem):
        def fonk7(elem):
            return elem.b4 + elem.b5
        b8 = fonk7(elem)
        b9 = len(self)
        while b9 > 0 and fonk7(self[b9 - 1]) > b8:
            b9 -= 1
        self.insert(b9, elem)
    def fonk8(self, elem):
        b9 = self.index(elem)
        while b9 > 0 and elem.b3 < self[b9 - 1].b3:
            b9 -= 1
        if b9 != self.index(elem):
            self.pop(self.index(elem))
            self.fonk6(elem)
    def fonk9(self, b10, reverse):
        class1.b1.clear()
        return list(self.fonk10(b10))[::-1] if reverse else list(self.fonk10(b10))
    def fonk10(self, b10):
        while b10 is not None:
            yield b10.b3
            b10 = b10.b2
def fonk11(calc_possible, start, base_case, b11 = None, b12=0, reverse=False):
    b12 = float('inf') if b12 == 0 else b12
    b13 = time()
    b14 = class2(start, b11)
    while time() < b13 + b12:
        if not b14:
            return False
        b15 = b14.pop()
        if base_case(b15.b3):
            return b14.fonk9(b15, reverse)
        for elem, b7 in calc_possible(b15.b3):
            b14.fonk5(elem, b7, b15, b11)
    raise TimeoutError("Time limit reached, you can manually change or remove it.")