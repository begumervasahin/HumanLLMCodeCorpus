from collections import deque
class class1:
    def fonk1(self):
        pass
    def fonk2(self, b6):
        b1 = set()
        b2 = deque()
        b2.append(class2(b6))
        while b2:
            b3 = b2.pop()
            for config in b3.b6.extensions():
                if str(config) in b1:
                    continue
                if config.is_solved():
                    return class2(config)
                if config.fail_fast() or len(config.extensions()) == 0:
                    continue
                b4 = class2(config)
                b1.add(str(b4.b6))
                b2.append(b4)
        return None
    def fonk3(self, b6):
        b1 = set()
        b5 = deque()
        b5.append(class2(b6))
        while b5:
            b3 = b5.popleft()
            for child in b3.b6.extensions():
                if str(child) in b1:
                    continue
                if child.is_solved():
                    return class2(child)
                if child.fail_fast() or len(child.extensions()) == 0:
                    continue
                b4 = class2(child)
                b1.add(str(b4.b6))
                b5.append(b4)
        return None
class class2:
    def fonk4(self, b6 = None, b8=None, b7=None):
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8[:] if b8 is not None else []
        self.b1 = False
    def fonk5(self, other):
        return (type(self) == type(other) and
                self.b6 = = other.b6 and
                all(x in self.b8 for x in other.b8) and
                all(x in other.b8 for x in self.b8))
    def fonk6(self):
        return "{}\n\n{}".format(self.b6, "\n".join(str(x) for x in self.b8))
if b9 = = '__main__':
    pass