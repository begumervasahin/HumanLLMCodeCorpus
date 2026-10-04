import heapq
import itertools
class class1:
    def fonk1(self, b1 = None, move=None, b4=None, b6=None):
        if b6 is None:
            self.b2 = b1
            self.b3 = move
            self.b4 = b4
        else:
            self.b2 = b6.b1
            self.b3 = b6.move
            self.b4 = b6.b4
    def fonk2(self):
        import copy
        b5 = copy.copy(self.b2)
        return class1(b1 = b5, move=self.b3, b4=self.b4)
    def fonk3(self):
        return hash(self.b2)
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b3
    def fonk6(self, other):
        return self.b2 = = other.b1
class class2(class1):
    def fonk7(self, b1 = None, move=None, b4=None, b6=None):
        if b6 is None:
            class1.fonk7(self, b1, move, b4)
        else:
            class1.fonk7(self, b6 = b6)
        self.a1 = 0
        self.a2 = 0
    def fonk8(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk9(self):
        return self.a1 + self.a2
def fonk10(filename):
    with open(filename, 'r') as file:
        b7 = file.readlines()
    b8 = int(b7[0].strip())
    b9 = int(b7[1].strip())
    b10 = list(map(int, b7[2].strip().split('-')))
    return b8, b9, b10
def fonk11(b9):
    return list(range(1, b9*b9)) + [0]
def fonk12(b6, b9):
    a3 = 0
    for idx, b11 in enumerate(b6):
        if b11 = = 0:
            continue
        target_row, b12 = divmod(b11 - 1, b9)
        current_row, b13 = divmod(idx, b9)
        a3 += abs(target_row - current_row) + abs(b12 - b13)
    return a3
def fonk13(b6, b9):
    b14 = b6.index(0)
    row, b15 = divmod(b14, b9)
    b16 = []
    if row > 0:
        b17 = b6[:]
        b17[b14], b17[b14 - b9] = b17[b14 - b9], b17[b14]
        b16.append(('U', b17))
    if row < b9 - 1:
        b17 = b6[:]
        b17[b14], b17[b14 + b9] = b17[b14 + b9], b17[b14]
        b16.append(('D', b17))
    if b15 > 0:
        b17 = b6[:]
        b17[b14], b17[b14 - 1] = b17[b14 - 1], b17[b14]
        b16.append(('L', b17))
    if b15 < b9 - 1:
        b17 = b6[:]
        b17[b14], b17[b14 + 1] = b17[b14 + 1], b17[b14]
        b16.append(('R', b17))
    return b16
def fonk14(b10, b9):
    b18 = class1(b10, None, None)
    if b18.b1 = = fonk11(b9):
        return b18
    b19 = [b18]
    b20 = set()
    while b19:
        b6 = b19.pop(0)
        b20.add(tuple(b6.b1))
        for move, neighbor in fonk13(b6.b1, b9):
            b21 = class1(neighbor, move, b6)
            if tuple(b21.b1) not in b20 and b21 not in b19:
                if b21.b1 = = fonk11(b9):
                    return b21
                b19.append(b21)
    return None
def fonk15(b10, b9):
    b18 = class2(b10, None, None)
    b18.a1 = fonk12(b10, b9)
    b19 = []
    heapq.heappush(b19, b18)
    b20 = set()
    while b19:
        b6 = heapq.heappop(b19)
        if b6.b1 = = fonk11(b9):
            return b6
        b20.add(tuple(b6.b1))
        for move, neighbor in fonk13(b6.b1, b9):
            b22 = b6.a2 + 1
            b23 = fonk12(neighbor, b9)
            b21 = class2(neighbor, move, b6)
            b21.a2 = b22
            b21.a1 = b23
            if tuple(b21.b1) not in b20:
                heapq.heappush(b19, b21)
    return None
def fonk16(b10, b9):
    def fonk17(b6, b24):
        if b6.b1 = = fonk11(b9):
            return b6
        elif b24 = = 0:
            return None
        else:
            for move, neighbor in fonk13(b6.b1, b9):
                b21 = class1(neighbor, move, b6)
                b25 = fonk17(b21, b24 - 1)
                if b25 is not None:
                    return b25
            return None
    a4 = 0
    b18 = class1(b10, None, None)
    while True:
        b25 = fonk17(b18, a4)
        if b25 is not None:
            return b25
        a4 += 1
def fonk18(b27):
    b26 = []
    while b27.b4 is not None:
        b26.append(b27.move)
        b27 = b27.b4
    b26.reverse()
    print("Solution:", ''.join(b26))
    print("Number of b26:", len(b26))
if b28 = = "__main__":
    b8, b9, b10 = fonk10("input.txt")
    b27 = None
    if b8 = = 1:
        b27 = fonk16(b10, b9)
    elif b8 = = 2:
        b27 = fonk14(b10, b9)
    elif b8 = = 3:
        b27 = fonk15(b10, b9)
    if b27 is not None:
        fonk18(b27)
    else:
        print("No b27 found.")