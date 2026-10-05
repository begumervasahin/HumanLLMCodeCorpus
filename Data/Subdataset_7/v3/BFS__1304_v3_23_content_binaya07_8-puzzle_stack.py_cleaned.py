from collections import deque
import heapq
import time
import resource
import sys
class class1:
    def fonk1(self):
        self.b1 = []
        self.b2 = set()
    def fonk2(self, item):
        self.b1.append(item)
        self.b2.add(tuple(item.b8))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1.fonk3()
            self.b2.remove(tuple(b3.b8))
            return b3
        else:
            return 0
    def fonk4(self):
        return len(self.b1) == 0
    def fonk5(self):
        self.b1.clear()
        self.b2.clear()
def fonk6(path_to_goal, cost_of_path, nodes_expanded, b10, a1, b11, a2, b9, max_ram_usage):
    with open('output.txt', 'w') as f:
        f.write("path_to_goal: {}\n".format(path_to_goal))
        f.write("cost_of_path: {}\n".format(cost_of_path))
        f.write("nodes_expanded: {}\n".format(nodes_expanded))
        f.write("b10: {}\n".format(b10))
        f.write("a1: {}\n".format(a1))
        f.write("b11: {}\n".format(b11))
        f.write("a2: {}\n".format(a2))
        f.write("b9: {}\n".format(b9))
        f.write("max_ram_usage: {}\n".format(max_ram_usage))
def fonk7(b24):
    b4 = time.time()
    b5 = set()
    b6 = deque([b24])
    a1 = 0
    a2 = 0
    while b6:
        b7 = b6.popleft()
        b5.add(tuple(b7.b8))
        if b7.b8 = = b22:
            b9 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b10 = [], 0, len(b5), len(b6)
            b11 = b7.b15
            while b7.b13:
                path_to_goal.insert(0, b7.b14)
                cost_of_path += 1
                b7 = b7.b13
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b10, a1, b11, a2, b9, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b8) not in b5:
                b6.append(neighbor)
                b5.add(tuple(neighbor.b8))
                a2 = max(a2, neighbor.b15)
        a1 = max(a1, len(b6))
def fonk8(b24):
    b4 = time.time()
    b5 = set()
    b6 = class1()
    b6.fonk2(b24)
    a1 = 0
    a2 = 0
    while not b6.fonk4():
        b7 = b6.fonk3()
        b5.add(tuple(b7.b8))
        if b7.b8 = = b22:
            b9 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b10 = [], 0, len(b5), len(b6.b1)
            b11 = b7.b15
            while b7.b13:
                path_to_goal.insert(0, b7.b14)
                cost_of_path += 1
                b7 = b7.b13
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b10, a1, b11, a2, b9, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b8) not in b5:
                b6.fonk2(neighbor)
                b5.add(tuple(neighbor.b8))
                a2 = max(a2, neighbor.b15)
        a1 = max(a1, len(b6.b1))
def fonk9(b24, b25):
    b4 = time.time()
    b5 = set()
    b6 = class1()
    b6.fonk2(b24)
    a1 = 0
    a2 = 0
    while not b6.fonk4():
        b7 = b6.fonk3()
        b5.add(tuple(b7.b8))
        if b7.b8 = = b22:
            b9 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b10 = [], 0, len(b5), len(b6.b1)
            b11 = b7.b15
            while b7.b13:
                path_to_goal.insert(0, b7.b14)
                cost_of_path += 1
                b7 = b7.b13
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b10, a1, b11, a2, b9, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        if b7.b15 < b25:
            for neighbor in b7.fonk13():
                if tuple(neighbor.b8) not in b5:
                    b6.fonk2(neighbor)
                    b5.add(tuple(neighbor.b8))
                    a2 = max(a2, neighbor.b15)
            a1 = max(a1, len(b6.b1))
def fonk10(b24):
    b4 = time.time()
    b5 = set()
    b6 = []
    heapq.heappush(b6, (0, b24))
    a1 = 0
    a2 = 0
    while b6:
        current_priority, b7 = heapq.heappop(b6)
        b5.add(tuple(b7.b8))
        if b7.b8 = = b22:
            b9 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b10 = [], 0, len(b5), len(b6)
            b11 = b7.b15
            while b7.b13:
                path_to_goal.insert(0, b7.b14)
                cost_of_path += 1
                b7 = b7.b13
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b10, a1, b11, a2, b9, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b8) not in b5:
                b12 = neighbor.b15 + neighbor.fonk12()
                heapq.heappush(b6, (b12, neighbor))
                b5.add(tuple(neighbor.b8))
                a2 = max(a2, neighbor.b15)
        a1 = max(a1, len(b6))
class class2:
    def fonk11(self, b2, b13, b14, b15):
        self.b8 = b2
        self.b13 = b13
        self.b14 = b14
        self.b15 = b15
    def fonk12(self):
        return sum([1 if self.b8[i] != b22[i] else 0 for i in range(len(self.b8))])
    def fonk13(self):
        b16 = []
        b17 = self.b8.index(0)
        row, b18 = divmod(b17, 3)
        for b14 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, b19 = row + b14[0], b18 + b14[1]
            if 0 <= new_row < 3 and 0 <= b19 < 3:
                b20 = self.b8[:]
                b21 = new_row * 3 + b19
                b20[b17], b20[b21] = b20[b21], b20[b17]
                b16.append(class2(b20, self, b14, self.b15 + 1))
        return b16
b22 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def fonk14():
    b23 = sys.argv[1]
    b24 = class2([int(i) for i in sys.argv[2].split(",")], None, None, 0)
    if b23 = = "bfs":
        fonk7(b24)
    elif b23 = = "dfs":
        fonk8(b24)
    elif b23 = = "dls":
        b25 = int(sys.argv[3])
        fonk9(b24, b25)
    elif b23 = = "ast":
        fonk10(b24)
if b26 = = "__main__":
    fonk14()