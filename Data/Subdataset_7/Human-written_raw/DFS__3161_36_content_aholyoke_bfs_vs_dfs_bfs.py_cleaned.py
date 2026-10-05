from collections import deque
class class1(deque):
    def fonk1(self, b4):
        self.extend(b4)
    def fonk2(self):
        return self.popleft()
class class2(deque):
    def fonk3(self, b4):
        self.extend(b4)
    def fonk4(self):
        return self.pop()
def fonk5(structure, b1):
    while True:
        yield b1
        structure.fonk3(b1.b4)
        if len(structure) == 0:
            break
        b1 = structure.fonk4()
def fonk6(b5):
    return fonk5(class1(), b5)
def fonk7(b5):
    return fonk5(class2(), b5)
if b2 = = "__main__":
    class class3(object):
        def fonk8(self, b3, *b4):
            self.b3 = b3
            self.b4 = list(b4)
        def fonk9(self):
            return "class3({})".format(self.b3)
    b5 = class3(
        0,
        class3(1, class3(3), class3(4, class3(6), class3(7), class3(8))),
        class3(2, class3(5)),
    )
    print([i.b3 for i in fonk6(b5)])
    print([i.b3 for i in fonk7(b5)])