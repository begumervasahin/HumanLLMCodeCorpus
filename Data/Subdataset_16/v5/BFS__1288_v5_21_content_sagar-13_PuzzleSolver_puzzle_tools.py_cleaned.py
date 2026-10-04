
from b6 import Puzzle
from collections import deque
import sys
sys.setrecursionlimit(10**6)
def fonk1(b6):
    b1 = set()
    b2 = deque([class1(b6)])
    while b2:
        b3 = b2.pop()
        if b3.b6.is_solved():
            return b3
        b1.add(str(b3.b6))
        for config in b3.b6.extensions():
            if str(config) not in b1 and not config.fail_fast():
                b2.append(class1(config, b4 = b3))
    return None
def fonk2(b6):
    b1 = set()
    b5 = deque([class1(b6)])
    while b5:
        b3 = b5.popleft()
        if b3.b6.is_solved():
            return b3
        b1.add(str(b3.b6))
        for config in b3.b6.extensions():
            if str(config) not in b1 and not config.fail_fast():
                b5.append(class1(config, b4 = b3))
    return None
class class1:
    def fonk3(self, b6 = None, b7=None, b4=None):
        self.b6 = b6
        self.b4 = b4
        self.b7 = b7[:] if b7 else []
    def fonk4(self, other):
        return (
            isinstance(other, class1) and
            self.b6 = = other.b6 and
            set(self.b7) == set(other.b7)
        )
    def fonk5(self):
        b8 = "\n".join(str(child) for child in self.b7)
        return f"{self.b6}\n\n{b8}"