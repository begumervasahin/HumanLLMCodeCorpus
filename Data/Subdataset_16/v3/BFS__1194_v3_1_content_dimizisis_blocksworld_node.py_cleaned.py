import configparser
import heapq
import sys
import time
class class1:
    def fonk1(self, b1 = None, b2=None, b3=0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 < other.b3
    def fonk3(self, other):
        return self.b2 = = other.b2
    def fonk4(self):
        return hash(str(self.b2))
def fonk5(b17):
    b4 = configparser.ConfigParser()
    b4.read(b17)
    b5 = {}
    b6 = {}
    for b7, value in b4['START'].items():
        if b7 = = 'b8':
            b8 = tuple(map(int, value.split(',')))
        else:
            b5[b7] = tuple(map(int, value.split(',')))
    for b7, value in b4['GOAL'].items():
        b6[b7] = tuple(map(int, value.split(',')))
    return b8, b5, b6
def fonk6(b18, b14, a1, b21):
    with open(b18, 'w') as f:
        for state in b14:
            for block, position in state.items():
                f.write(f"{block} {position}\n")
            f.write("----------\n")
        f.write(f"Nodes expanded: {a1}\n")
        f.write(f"--- Execution time (seconds): {b21:.4f} ---\n")
def fonk7(state, b6):
    return sum(abs(state[block][0] - b6[block][0]) + abs(state[block][1] - b6[block][1]) for block in state)
def fonk8(b13, b8):
    b9 = []
    return b9
def fonk9(b5, b6, b8):
    b10 = []
    b11 = set()
    b12 = class1(None, b5, 0)
    heapq.heappush(b10, (0, b12))
    a1 = 0
    while b10:
        current_priority, b13 = heapq.heappop(b10)
        a1 += 1
        if b13.b2 = = b6:
            b14 = []
            while b13:
                b14.append(b13.b2)
                b13 = b13.b1
            return b14[::-1], a1
        b11.add(b13)
        b9 = fonk8(b13, b8)
        for successor_state in b9:
            b15 = class1(b13, successor_state, fonk7(successor_state, b6))
            if b15 in b11:
                continue
            heapq.heappush(b10, (b15.b3, b15))
    return None, a1
def fonk10():
    if len(sys.argv) != 4:
        print("Usage: python main.py <b16> <b17> <b18>")
        return
    b16 = sys.argv[1]
    b17 = sys.argv[2]
    b18 = sys.argv[3]
    b8, b5, b6 = fonk5(b17)
    b19 = time.time()
    if b16 = = 'astar':
        b14, a1 = fonk9(b5, b6, b8)
    elif b16 = = 'best':
        b14, a1 = best_first_search(b5, b6, b8)
    else:
        print(f"Unknown search method: {b16}")
        return
    b20 = time.time()
    b21 = b20 - b19
    if b14:
        fonk6(b18, b14, a1, b21)
    else:
        print("No solution found")
if b22 = = "__main__":
    fonk10()