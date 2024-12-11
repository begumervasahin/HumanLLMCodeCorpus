from collections import deque
from enum import Enum
class class1(Enum):
    a1 = 5
    a2 = 2
    a3 = 0
class class2:
    def fonk1(self, b2, node_pairs):
        self.b1 = [[class1.a3 for _ in range(b2)] for _ in range(b2)]
        self.b2 = b2
        for location, node_state in node_pairs:
            self.fonk3(location, node_state)
    def fonk2(self, location):
        return self.b1[location[0]][location[1]]
    def fonk3(self, location, state):
        self.b1[location[0]][location[1]] = state
    def fonk4(self, location):
        if self.fonk2(location) == class1.a2:
            return False
        if self.fonk5(location):
            b3 = deque()
            b3.appendleft(location)
            b4 = [[False for _ in range(self.b2)] for _ in range(self.b2)]
            b4[location[0]][location[1]] = True
            while b3:
                b5 = b3.popleft()
                if self.fonk6(b3, b4, b5):
                    continue
                else:
                    return False
            return True
        else:
            return False
    def fonk5(self, location):
        row, b6 = location
        return 0 <= row < self.b2 and 0 <= b6 < self.b2
    def fonk6(self, b3, b4, b5):
        row, b6 = b5
        b7 = [(row, b6 + 1), (row, b6 - 1), (row + 1, b6), (row - 1, b6)]
        for neighbor_row, neighbor_col in b7:
            if self.fonk5((neighbor_row, neighbor_col)):
                if not b4[neighbor_row][neighbor_col]:
                    b8 = self.fonk2((neighbor_row, neighbor_col))
                    if b8 = = class1.a2:
                        b4[neighbor_row][neighbor_col] = True
                        continue
                    elif b8 = = class1.a3:
                        return False
                    elif b8 = = class1.a1:
                        b3.append((neighbor_row, neighbor_col))
            else:
                continue
        return True
if b9 = = "__main__":
    b10 = class2(5, [([1, 3], class1.a2),
                        ([1, 2], class1.a2),
                        ([3, 3], class1.a2),
                        ([3, 2], class1.a3),
                        ([2, 1], class1.a2),
                        ([2, 4], class1.a2),
                        ([2, 2], class1.a1),
                        ([2, 3], class1.a1),
                        ])
    print(b10.fonk4([2, 2]))