import sys
import time
import heapq
from collections import deque
class class1:
    def fonk1(self, b1, b2, b3, b4, b5, b6):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        if self.b1:
            self.b7 = ''.join(str(e) for e in self.b1)
    def fonk2(self, other):
        return self.b7 = = other.b7
    def fonk3(self, other):
        return self.b7 < other.b7
def fonk4(start_state):
    b8 = deque([class1(start_state, None, None, 0, 0, 0)])
    b9 = set()
    a1 = 0
    a2 = 0
    while b8:
        b10 = b8.popleft()
        b9.add(b10.b7)
        a1 += 1
        if fonk9(b10.b1):
            return fonk11(b10), a1, len(b8), max(len(b8), a2), b10.b4
        b11 = fonk10(b10)
        for neighbor in b11:
            if neighbor.b7 not in b9 and neighbor not in b8:
                b8.append(neighbor)
                a2 = max(a2, len(b8))
    return None, a1, len(b8), a2, b10.b4
def fonk5(start_state):
    b8 = [class1(start_state, None, None, 0, 0, 0)]
    b9 = set()
    a1 = 0
    a2 = 0
    while b8:
        b10 = b8.pop()
        b9.add(b10.b7)
        a1 += 1
        if fonk9(b10.b1):
            return fonk11(b10), a1, len(b8), max(len(b8), a2), b10.b4
        b11 = fonk10(b10)
        for neighbor in reversed(b11):
            if neighbor.b7 not in b9 and neighbor not in b8:
                b8.append(neighbor)
                a2 = max(a2, len(b8))
    return None, a1, len(b8), a2, b10.b4
def fonk6(start_state):
    b8 = []
    b9 = set()
    b12 = class1(start_state, None, None, 0, 0, 0)
    heapq.heappush(b8, (0, b12))
    a1 = 0
    a2 = 0
    while b8:
        b10 = heapq.heappop(b8)[1]
        b9.add(b10.b7)
        a1 += 1
        if fonk9(b10.b1):
            return fonk11(b10), a1, len(b8), max(len(b8), a2), b10.b4
        b11 = fonk10(b10)
        for neighbor in b11:
            if neighbor.b7 not in b9:
                heapq.heappush(b8, (neighbor.b5 + fonk12(neighbor.b1), neighbor))
                a2 = max(a2, len(b8))
    return None, a1, len(b8), a2, b10.b4
def fonk7(start_state):
    def fonk8(b18, g, b17):
        b13 = b18[-1]
        b14 = g + fonk12(b13.b1)
        if b14 > b17:
            return b14
        if fonk9(b13.b1):
            return b18
        b15 = float('inf')
        for neighbor in fonk10(b13):
            if neighbor not in b18:
                b18.append(neighbor)
                b16 = fonk8(b18, g + 1, b17)
                if isinstance(b16, list):
                    return b16
                if b16 < b15:
                    b15 = b16
                b18.pop()
        return b15
    b12 = class1(start_state, None, None, 0, 0, 0)
    b17 = fonk12(start_state)
    b18 = [b12]
    a1 = 0
    a2 = 0
    while True:
        b16 = fonk8(b18, 0, b17)
        if isinstance(b16, list):
            return fonk11(b16[-1]), a1, len(b18), a2, b16[-1].b4
        if b16 = = float('inf'):
            return None, a1, len(b18), a2, 0
        b17 = b16
def fonk9(b1):
    return b1 = = [1, 2, 3, 4, 5, 6, 7, 8, 0]
def fonk10(b10):
    b11 = []
    b19 = {
        'Up': -3,
        'Down': 3,
        'Left': -1,
        'Right': 1
    }
    b20 = b10.b1.b20(0)
    for b3, position in b19.items():
        b21 = b20 + position
        if 0 <= b21 < len(b10.b1):
            b22 = b10.b1[:]
            b22[b20], b22[b21] = b22[b21], b22[b20]
            b11.append(class1(b22, b10, b3, b10.b4 + 1, b10.b5 + 1, 0))
    return b11
def fonk11(b1):
    b18 = []
    while b1.b2:
        b18.append(b1.b3)
        b1 = b1.b2
    return b18[::-1]
def fonk12(b1):
    return sum(abs((val - 1) % 3 - i % 3) + abs((val - 1)
               for i, val in enumerate(b1) if val != 0)
def fonk13(b16, a1, fringe_size, a2, b27, b29):
    with open('output.txt', 'w') as b14:
        if b16:
            b14.write(b14"path_to_goal: {b16}\n")
        b14.write(b14"cost_of_path: {len(b16) if b16 else 0}\n")
        b14.write(b14"a1: {a1}\n")
        b14.write(b14"fringe_size: {fringe_size}\n")
        b14.write(b14"a2: {a2}\n")
        b14.write(b14"b27: {b27}\n")
        b14.write(b14"max_search_depth: {b27}\n")
        b14.write(b14"b29: {b29}\n")
if b23 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python driver.py <b24> <b25>")
        sys.exit(1)
    b24 = sys.argv[1]
    b25 = list(b7(int, sys.argv[2].split(',')))
    b26 = time.time()
    if b24 = = 'bfs':
        b16, a1, fringe_size, a2, b27 = fonk4(b25)
    elif b24 = = 'dfs':
        b16, a1, fringe_size, a2, b27 = fonk5(b25)
    elif b24 = = 'ast':
        b16, a1, fringe_size, a2, b27 = fonk6(b25)
    elif b24 = = 'ida':
        b16, a1, fringe_size, a2, b27 = fonk7(b25)
    else:
        print("Unknown b24")
        sys.exit(1)
    b28 = time.time()
    b29 = b28 - b26
    fonk13(b16, a1, fringe_size, a2, b27, b29)