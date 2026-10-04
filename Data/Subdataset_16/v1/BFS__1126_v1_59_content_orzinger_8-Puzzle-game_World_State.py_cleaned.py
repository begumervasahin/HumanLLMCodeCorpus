import heapq
import itertools
class class1:
    def fonk1(self, _state, _operate, _parent, _depth, _f_value):
        self.b1 = _state
        self.b2 = _operate
        self.b3 = _parent
        self.b4 = _depth
        self.b5 = _f_value
    def fonk2(self, other):
        return self.b1 = = other.b1
    def fonk3(self, other):
        return self.b5 < other.b5
def fonk4(filename):
    with open(filename, 'r') as file:
        b6 = file.readlines()
    b7 = int(b6[0].strip())
    b8 = int(b6[1].strip())
    b9 = list(map(int, b6[2].strip().split(',')))
    return b7, b8, b9
def fonk5(b8):
    return list(range(1, b8*b8)) + [0]
def fonk6(b1, b8):
    a1 = 0
    for idx, b10 in enumerate(b1):
        if b10 = = 0:
            continue
        target_row, b11 = divmod(b10 - 1, b8)
        current_row, b12 = divmod(idx, b8)
        a1 += abs(target_row - current_row) + abs(b11 - b12)
    return a1
def fonk7(b1, b8):
    b13 = b1.index(0)
    row, b14 = divmod(b13, b8)
    b15 = []
    if row > 0:
        b16 = b1[:]
        b16[b13], b16[b13 - b8] = b16[b13 - b8], b16[b13]
        b15.append(('Up', b16))
    if row < b8 - 1:
        b16 = b1[:]
        b16[b13], b16[b13 + b8] = b16[b13 + b8], b16[b13]
        b15.append(('Down', b16))
    if b14 > 0:
        b16 = b1[:]
        b16[b13], b16[b13 - 1] = b16[b13 - 1], b16[b13]
        b15.append(('Left', b16))
    if b14 < b8 - 1:
        b16 = b1[:]
        b16[b13], b16[b13 + 1] = b16[b13 + 1], b16[b13]
        b15.append(('Right', b16))
    return b15
def fonk8(b9, b8):
    b17 = class1(b9, None, None, 0, 0)
    if b17.b1 = = fonk5(b8):
        return b17
    b18 = [b17]
    b19 = set()
    while b18:
        b1 = b18.pop(0)
        b19.add(tuple(b1.b1))
        for b2, neighbor in fonk7(b1.b1, b8):
            b20 = class1(neighbor, b2, b1, b1.b4 + 1, 0)
            if tuple(b20.b1) not in b19 and b20 not in b18:
                if b20.b1 = = fonk5(b8):
                    return b20
                b18.append(b20)
    return None
def fonk9(b9, b8):
    b17 = class1(b9, None, None, 0, fonk6(b9, b8))
    b18 = []
    heapq.heappush(b18, b17)
    b19 = set()
    while b18:
        b1 = heapq.heappop(b18)
        if b1.b1 = = fonk5(b8):
            return b1
        b19.add(tuple(b1.b1))
        for b2, neighbor in fonk7(b1.b1, b8):
            b21 = b1.b4 + 1
            b22 = fonk6(neighbor, b8)
            b20 = class1(neighbor, b2, b1, b21, b21 + b22)
            if tuple(b20.b1) not in b19:
                heapq.heappush(b18, b20)
    return None
def fonk10(b9, b8):
    def fonk11(b1, b23):
        if b1.b1 = = fonk5(b8):
            return b1
        elif b23 = = 0:
            return None
        else:
            for b2, neighbor in fonk7(b1.b1, b8):
                b20 = class1(neighbor, b2, b1, b1.b4 + 1, 0)
                b24 = fonk11(b20, b23 - 1)
                if b24 is not None:
                    return b24
            return None
    b4 = 0
    b17 = class1(b9, None, None, 0, 0)
    while True:
        b24 = fonk11(b17, b4)
        if b24 is not None:
            return b24
        b4 += 1
def fonk12(b26):
    b25 = []
    while b26.b3 is not None:
        b25.append(b26.b2)
        b26 = b26.b3
    b25.reverse()
    print("Solution:", b25)
    print("Number of b25:", len(b25))
if b27 = = "__main__":
    b7, b8, b9 = fonk4("input.txt")
    b26 = None
    if b7 = = 1:
        b26 = fonk10(b9, b8)
    elif b7 = = 2:
        b26 = fonk8(b9, b8)
    elif b7 = = 3:
        b26 = fonk9(b9, b8)
    if b26 is not None:
        fonk12(b26)
    else:
        print("No b26 found.")