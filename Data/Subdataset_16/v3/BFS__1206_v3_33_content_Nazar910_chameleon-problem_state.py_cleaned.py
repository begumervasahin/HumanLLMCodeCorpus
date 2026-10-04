from collections import deque, defaultdict
import heapq
class class1:
    def fonk1(self, b7, green, blue, b1 = None):
        self.b2 = b7
        self.b3 = green
        self.b4 = blue
        self.b1 = b1
    def fonk2(self):
        return (self.b2 = = 0 and self.b3 == 0) or \
               (self.b2 = = 0 and self.b4 == 0) or \
               (self.b3 = = 0 and self.b4 == 0)
    def fonk3(self):
        if self.b2 < 1 or self.b3 < 1:
            return None
        return class1(self.b2 - 1, self.b3 - 1, self.b4 + 2, self)
    def fonk4(self):
        if self.b3 < 1 or self.b4 < 1:
            return None
        return class1(self.b2 + 2, self.b3 - 1, self.b4 - 1, self)
    def fonk5(self):
        if self.b4 < 1 or self.b2 < 1:
            return None
        return class1(self.b2 - 1, self.b3 + 2, self.b4 - 1, self)
    def fonk6(self):
        b5 = []
        if (new_state := self.fonk3()) is not None:
            b5.append(new_state)
        if (new_state := self.fonk4()) is not None:
            b5.append(new_state)
        if (new_state := self.fonk5()) is not None:
            b5.append(new_state)
        return b5
    def fonk7(self):
        b6 = deque([self])
        b1 = self.b1
        while b1:
            b6.appendleft(b1)
            b1 = b1.b1
        return b6
    def fonk8(self):
        return f"(b7 = {self.b2}, green={self.b3}, blue={self.b4})"
    def fonk9(self, other):
        return self.b2 = = other.b2 and \
               self.b3 = = other.b3 and \
               self.b4 = = other.b4
    def fonk10(self):
        return hash((self.b2, self.b3, self.b4))
def fonk11(b14):
    b8 = deque([b14])
    b9 = set()
    while b8:
        b10 = b8.popleft()
        if b10 in b9:
            continue
        b9.add(b10)
        if b10.fonk2():
            return b10.fonk7()
        for neighbor in b10.fonk6():
            if neighbor not in b9:
                b8.append(neighbor)
    return None
def fonk12(b14):
    b8 = [b14]
    b9 = set()
    while b8:
        b10 = b8.pop()
        if b10 in b9:
            continue
        b9.add(b10)
        if b10.fonk2():
            return b10.fonk7()
        for neighbor in b10.fonk6():
            if neighbor not in b9:
                b8.append(neighbor)
    return None
def fonk13(b14):
    b8 = []
    heapq.heappush(b8, (0, b14))
    b9 = set()
    b11 = defaultdict(lambda: float('inf'))
    b11[b14] = 0
    while b8:
        _, b10 = heapq.heappop(b8)
        if b10 in b9:
            continue
        b9.add(b10)
        if b10.fonk2():
            return b10.fonk7()
        for neighbor in b10.fonk6():
            b12 = b11[b10] + 1
            if b12 < b11[neighbor]:
                b11[neighbor] = b12
                b13 = b12 + fonk14(neighbor)
                heapq.heappush(b8, (b13, neighbor))
    return None
def fonk14(b10):
    return min(b10.b2, b10.b3, b10.b4)
def fonk15(b6):
    for b10 in b6:
        print(b10)
def fonk16():
    b14 = class1(b7=13, green=16, blue=17)
    print("Solving with BFS...")
    b15 = fonk11(b14)
    if b15:
        fonk15(b15)
    else:
        print("No solution found with BFS.")
    print("\nSolving with DFS...")
    b16 = fonk12(b14)
    if b16:
        fonk15(b16)
    else:
        print("No solution found with DFS.")
    print("\nSolving with A*...")
    b17 = fonk13(b14)
    if b17:
        fonk15(b17)
    else:
        print("No solution found with A*.")
if b18 = = "__main__":
    fonk16()