import heapq
class class1:
    def fonk1(self, b1 = None, move=None, b4=None, b20=None):
        if b20 is None:
            self.b2 = b1
            self.b3 = move
            self.b4 = b4
        else:
            self.b2 = b20.b1
            self.b3 = b20.move
            self.b4 = b20.b4
    def fonk2(self):
        import copy
        b5 = copy.copy(self.b2)
        return class1(b1 = b5, move=self.b3, b4=self.b4)
    def fonk3(self):
        return hash(tuple(self.b2))
    @property
    def fonk4(self):
        return self.b2
    @property
    def fonk5(self):
        return self.b3
    def fonk6(self, other):
        return self.b2 = = other.b1
class class2(class1):
    def fonk7(self, b1 = None, move=None, b4=None, b20=None):
        super().fonk7(b1, move, b4, b20)
        self.a1 = 0
        self.a2 = 0
    def fonk8(self, other):
        return self.f_cost < other.f_cost
    @property
    def fonk9(self):
        return self.a1 + self.a2
def fonk10(filename):
    with open(filename, 'r') as file:
        b6 = file.readlines()
    b7 = int(b6[0].strip())
    b8 = int(b6[1].strip())
    b9 = list(map(int, b6[2].strip().split('-')))
    return b7, b8, b9
def fonk11(b8):
    return list(range(1, b8 * b8)) + [0]
def fonk12(b20, b8):
    a3 = 0
    for idx, b10 in enumerate(b20):
        if b10 = = 0:
            continue
        target_row, b11 = divmod(b10 - 1, b8)
        current_row, b12 = divmod(idx, b8)
        a3 += abs(target_row - current_row) + abs(b11 - b12)
    return a3
def fonk13(b20, b8):
    b13 = b20.index(0)
    row, b14 = divmod(b13, b8)
    b15 = []
    if row > 0:
        b16 = b20[:]
        b16[b13], b16[b13 - b8] = b16[b13 - b8], b16[b13]
        b15.append(('U', b16))
    if row < b8 - 1:
        b16 = b20[:]
        b16[b13], b16[b13 + b8] = b16[b13 + b8], b16[b13]
        b15.append(('D', b16))
    if b14 > 0:
        b16 = b20[:]
        b16[b13], b16[b13 - 1] = b16[b13 - 1], b16[b13]
        b15.append(('L', b16))
    if b14 < b8 - 1:
        b16 = b20[:]
        b16[b13], b16[b13 + 1] = b16[b13 + 1], b16[b13]
        b15.append(('R', b16))
    return b15
def fonk14(b9, b8):
    b17 = class1(b9, None, None)
    if b17.b1 = = fonk11(b8):
        return b17
    b18 = [b17]
    b19 = set()
    while b18:
        b20 = b18.pop(0)
        b19.add(tuple(b20.b1))
        for move, neighbor in fonk13(b20.b1, b8):
            b21 = class1(neighbor, move, b20)
            if tuple(b21.b1) not in b19 and b21 not in b18:
                if b21.b1 = = fonk11(b8):
                    return b21
                b18.append(b21)
    return None
def fonk15(b9, b8):
    b17 = class2(b9, None, None)
    b17.a1 = fonk12(b9, b8)
    b18 = []
    heapq.heappush(b18, b17)
    b19 = set()
    while b18:
        b20 = heapq.heappop(b18)
        if b20.b1 = = fonk11(b8):
            return b20
        b19.add(tuple(b20.b1))
        for move, neighbor in fonk13(b20.b1, b8):
            b22 = b20.a2 + 1
            b23 = fonk12(neighbor, b8)
            b21 = class2(neighbor, move, b20)
            b21.a2 = b22
            b21.a1 = b23
            if tuple(b21.b1) not in b19:
                heapq.heappush(b18, b21)
    return None
def fonk16(b9, b8):
    def fonk17(b20, b24):
        if b20.b1 = = fonk11(b8):
            return b20
        elif b24 = = 0:
            return None
        else:
            for move, neighbor in fonk13(b20.b1, b8):
                b21 = class1(neighbor, move, b20)
                b25 = fonk17(b21, b24 - 1)
                if b25 is not None:
                    return b25
            return None
    a4 = 0
    b17 = class1(b9, None, None)
    while True:
        b25 = fonk17(b17, a4)
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
    b7, b8, b9 = fonk10("input.txt")
    b27 = None
    if b7 = = 1:
        b27 = fonk16(b9, b8)
    elif b7 = = 2:
        b27 = fonk14(b9, b8)
    elif b7 = = 3:
        b27 = fonk15(b9, b8)
    if b27 is not None:
        fonk18(b27)
    else:
        print("No b27 found.")