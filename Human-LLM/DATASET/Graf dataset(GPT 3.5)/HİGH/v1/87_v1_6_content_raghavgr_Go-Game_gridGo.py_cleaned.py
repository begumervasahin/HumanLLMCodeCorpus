from collections import deque
from enum import Enum
class class1(Enum):
    a1 = 5
    a2 = 2
    a3 = 0
class class2():
    def fonk1(self, b2, nodepairs):
        self.b1 = [[class1.a3 for i in range(b2)] for j in range(b2)]
        self.b2 = b2
        for node in nodepairs:
            self.fonk3(self.b1, node[0], node[1])
    def fonk2(self, arr, location):
        return arr[location[0]][location[1]]
    def fonk3(self, arr, location, value):
        arr[location[0]][location[1]] = value
    def fonk4(self, location):
        if self.fonk2(self.b1, location) == class1.a2:
            return False
        if self.fonk5(location):
            b3 = deque()
            b3.appendleft(location)
            b4 = [[False for i in range(self.b2)] for j in range(self.b2)]
            self.fonk3(b4, location, True)
            while len(b3) != 0:
                b5 = b3.popleft()
                self.fonk3(b4, b5, True)
                if self.fonk6(b3, b4, b5):
                    continue
                else:
                    return False
            return True
        else:
            return False
    def fonk5(self, location):
        if (location[0] >= 0 and location[0] < self.b2 and location[1] >= 0 and location[1] < self.b2):
            return True
        return False
    def fonk6(self, b3, b4, b5):
        b6 = [[b5[0], b5[1]+1], [b5[0], b5[1]-1], [b5[0]+1, b5[1]], [b5[0]-1, b5[1]]]
        for loc in b6:
            if self.fonk5(loc):
                if not self.fonk2(b4, loc):
                    if self.fonk2(self.b1, loc) == class1.a2:
                        self.fonk3(b4, loc, True)
                        continue
                    elif self.fonk2(self.b1, loc) == class1.a3:
                        return False
                    elif self.fonk2(self.b1, loc) == class1.a1:
                        b3.append(loc)
            else:
                continue
        return True
if b7 = = "__main__":
    b8 = class2(5, [([1, 3], class1.a2),
                       ([1, 2], class1.a2),
                       ([3, 3], class1.a2),
                       ([3, 2], class1.a3),
                       ([2, 1], class1.a2),
                       ([2, 4], class1.a2),
                       ([2, 2], class1.a1),
                       ([2, 3], class1.a1),
                       ])
    print(b8.fonk4([2, 2]))