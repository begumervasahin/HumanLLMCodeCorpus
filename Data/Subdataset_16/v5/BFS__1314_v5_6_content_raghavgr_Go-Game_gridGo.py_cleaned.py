
from collections import deque
from enum import Enum
class class1(Enum):
    a1 = 5
    a2 = 2
    a3 = 0
class class2:
    def fonk1(self, b1, b9):
        self.b1 = b1
        self.b2 = [[class1.a3 for _ in range(b1)] for _ in range(b1)]
        for location, value in b9:
            self.fonk3(location, value)
    def fonk2(self, location):
        return self.b2[location[0]][location[1]]
    def fonk3(self, location, value):
        self.b2[location[0]][location[1]] = value
    def fonk4(self, location):
        if self.fonk2(location) != class1.a1 or not self.fonk5(location):
            return False
        b3 = deque([location])
        b4 = [[False for _ in range(self.b1)] for _ in range(self.b1)]
        b4[location[0]][location[1]] = True
        while b3:
            b5 = b3.popleft()
            if not self.fonk6(b3, b4, b5):
                return False
        return True
    def fonk5(self, location):
        return 0 <= location[0] < self.b1 and 0 <= location[1] < self.b1
    def fonk6(self, b3, b4, b5):
        b6 = [
            (b5[0], b5[1] + 1),
            (b5[0], b5[1] - 1),
            (b5[0] + 1, b5[1]),
            (b5[0] - 1, b5[1])
        ]
        for loc in b6:
            if self.fonk5(loc):
                if not b4[loc[0]][loc[1]]:
                    b7 = self.fonk2(loc)
                    if b7 = = class1.a2:
                        b4[loc[0]][loc[1]] = True
                    elif b7 = = class1.a3:
                        return False
                    elif b7 = = class1.a1:
                        b4[loc[0]][loc[1]] = True
                        b3.append(loc)
            else:
                return False
        return True
if b8 = = "__main__":
    b9 = [
        ((1, 3), class1.a2),
        ((1, 2), class1.a2),
        ((3, 3), class1.a2),
        ((3, 2), class1.a3),
        ((2, 1), class1.a2),
        ((2, 4), class1.a2),
        ((2, 2), class1.a1),
        ((2, 3), class1.a1),
    ]
    b10 = class2(5, b9)
    print(b10.fonk4((2, 2)))