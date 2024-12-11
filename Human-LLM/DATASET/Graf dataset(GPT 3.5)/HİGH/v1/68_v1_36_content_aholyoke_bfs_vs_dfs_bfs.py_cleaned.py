from collections import deque
class class1(deque):
    def fonk1(self, items):
        self.extend(items)
    def fonk2(self):
        return self.popleft()
class class2(deque):
    def fonk3(self, items):
        self.extend(items)
    def fonk4(self):
        return self.fonk4()
def fonk5(structure, b1):
    while True:
        yield b1
        structure.fonk1(b1.b4)
        if len(structure) == 0:
            break
        b1 = structure.fonk2()
def fonk6(b5):
    return fonk5(class1(), b5)
def fonk7(b5):
    return fonk5(class2(), b5)
if b2 = = "__main__":
    class class3:
        def fonk8(self, b3, *b4):
            self.b3 = b3
            self.b4 = list(b4)
        def fonk9(self):
            return f"class3({self.b3})"
    b5 = class3(
        0,
        class3(1, class3(3), class3(4, class3(6), class3(7), class3(8))),
        class3(2, class3(5))
    )
    b6 = [node.b3 for node in fonk6(b5)]
    b7 = [node.b3 for node in fonk7(b5)]
    print("BFS traversal:", b6)
    print("DFS traversal:", b7)