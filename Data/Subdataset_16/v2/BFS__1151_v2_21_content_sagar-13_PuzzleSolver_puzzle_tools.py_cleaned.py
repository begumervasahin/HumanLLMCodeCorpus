import sys
from collections import deque
sys.setrecursionlimit(10**6)
class class1:
    def fonk1(self):
        pass
    def fonk2(self):
        pass
    def fonk3(self):
        pass
class class2:
    def fonk4(self, b1 = None, b3=None, b2=None):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3[:] if b3 else []
        self.b4 = False
    def fonk5(self, other):
        return (type(self) == type(other) and
                self.b1 = = other.b1 and
                all(x in self.b3 for x in other.b3) and
                all(x in other.b3 for x in self.b3))
    def fonk6(self):
        return "{}\n\n{}".format(self.b1, "\n".join(str(x) for x in self.b3))
def fonk7(b1):
    b4 = set()
    b5 = deque([class2(b1)])
    while b5:
        b6 = b5.pop()
        for config in b6.b1.fonk10():
            if str(config) in b4:
                continue
            if config.fonk11():
                return class2(config)
            if config.fonk12() or not config.fonk10():
                continue
            b7 = class2(config)
            b4.add(str(b7.b1))
            b5.append(b7)
    return None
def fonk8(b1):
    b4 = set()
    b8 = deque([class2(b1)])
    while b8:
        b6 = b8.popleft()
        for child in b6.b1.fonk10():
            if str(child) in b4:
                continue
            if child.fonk11():
                return class2(child)
            if child.fonk12() or not child.fonk10():
                continue
            b7 = class2(child)
            b4.add(str(b7.b1))
            b8.append(b7)
    return None
if b9 = = "__main__":
    class class3(class1):
        def fonk9(self, b10):
            self.b10 = b10
        def fonk10(self):
            pass
        def fonk11(self):
            pass
        def fonk12(self):
            pass
        def fonk13(self):
            return str(self.b10)
    b11 = class3(b10="initial b10")
    b12 = fonk7(b11)
    if b12:
        print("Solution found using DFS:")
        print(b12)
    else:
        print("No solution found using DFS.")
    b12 = fonk8(b11)
    if b12:
        print("Solution found using BFS:")
        print(b12)
    else:
        print("No solution found using BFS.")