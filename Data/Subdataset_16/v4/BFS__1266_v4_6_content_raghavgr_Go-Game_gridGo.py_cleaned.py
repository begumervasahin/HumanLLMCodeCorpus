
from collections import deque
from enum import Enum
class class1(Enum):
    a1 = 5
    a2 = 2
    a3 = 0
class class2:
    def fonk1(self, b2, b8):
        self.b1 = [[class1.a3 for _ in range(b2)] for _ in range(b2)]
        self.b2 = b2
        for location, value in b8:
            self.fonk3(location, value)
    def fonk2(self, location):
        return self.b1[location[0]][location[1]]
    def fonk3(self, location, value):
        self.b1[location[0]][location[1]] = value
    def fonk4(self, location):
        if self.fonk7(location) == class1.a2:
            return False
        if not self.fonk5(location):
            return False
        b3 = deque([location])
        b4 = [[False for _ in range(self.b2)] for _ in range(self.b2)]
        self.fonk3(b4, location, True)
        while b3:
            b5 = b3.popleft()
            self.fonk3(b4, b5, True)
            if self.fonk6(b3, b4, b5):
                continue
            else:
                return False
        return True
    def fonk5(self, location):
        return 0 <= location[0] < self.b2 and 0 <= location[1] < self.b2
    def fonk6(self, b3, b4, b5):
        b6 = [
            [b5[0], b5[1] + 1],
            [b5[0], b5[1] - 1],
            [b5[0] + 1, b5[1]],
            [b5[0] - 1, b5[1]]
        ]
        for loc in b6:
            if self.fonk5(loc):
                if not self.fonk7(b4, loc):
                    if self.fonk7(loc) == class1.a2:
                        self.fonk3(b4, loc, True)
                        continue
                    elif self.fonk7(loc) == class1.a3:
                        return False
                    elif self.fonk7(loc) == class1.a1:
                        b3.append(loc)
            else:
                continue
        return True
    def fonk7(self, b4, location):
        return b4[location[0]][location[1]]
if b7 = = "__main__":
    b8 = [
        ([1, 3], class1.a2),
        ([1, 2], class1.a2),
        ([3, 3], class1.a2),
        ([3, 2], class1.a3),
        ([2, 1], class1.a2),
        ([2, 4], class1.a2),
        ([2, 2], class1.a1),
        ([2, 3], class1.a1),
    ]
    b9 = class2(5, b8)
    print(b9.fonk4([2, 2]))