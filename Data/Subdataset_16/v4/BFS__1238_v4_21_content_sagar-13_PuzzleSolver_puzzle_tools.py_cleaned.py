
from b6 import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def fonk1(b6):
    b1 = set()
    b2 = deque([class1(b6)])
    while b2:
        b3 = b2.pop()
        for config in b3.b6.extensions():
            if str(config) in b1:
                continue
            if config.is_solved():
                return class1(config)
            if config.fail_fast() or not config.extensions():
                continue
            b4 = class1(config)
            b1.add(str(b4.b6))
            b2.append(b4)
    return None
def fonk2(b6):
    b1 = set()
    b5 = deque([class1(b6)])
    while b5:
        b3 = b5.popleft()
        for config in b3.b6.extensions():
            if str(config) in b1:
                continue
            if config.is_solved():
                return class1(config)
            if config.fail_fast() or not config.extensions():
                continue
            b4 = class1(config)
            b1.add(str(b4.b6))
            b5.append(b4)
    return None
class class1:
    def fonk3(self, b6 = None, b8=None, b7=None):
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8[:] if b8 else []
    def fonk4(self, other):
        return (
            isinstance(other, class1) and
            self.b6 = = other.b6 and
            set(self.b8) == set(other.b8)
        )
    def fonk5(self):
        b9 = "\n".join(str(child) for child in self.b8)
        return f"{self.b6}\n\n{b9}"