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
        self.b2.add(tuple(item.b1))
    def fonk3(self):
        if not self.fonk4():
            b3 = self.b1[-1]
            del self.b1[-1]
            self.b2.remove(tuple(b3.b1))
            return b3
        else:
            return 0
    def fonk4(self):
        if len(self.b1) == 0:
            return 1
        else:
            return 0
    def fonk5(self):
        self.b1.clear()
        self.b2.clear()
def fonk6(path_to_goal, cost_of_path, nodes_expanded, b9, a1, b10, a2, b8, max_ram_usage):
    with open('output.txt', 'w') as f:
        f.write("path_to_goal: {}\n".format(path_to_goal))
        f.write("cost_of_path: {}\n".format(cost_of_path))
        f.write("nodes_expanded: {}\n".format(nodes_expanded))
        f.write("b9: {}\n".format(b9))
        f.write("a1: {}\n".format(a1))
        f.write("b10: {}\n".format(b10))
        f.write("a2: {}\n".format(a2))
        f.write("b8: {}\n".format(b8))
        f.write("max_ram_usage: {}\n".format(max_ram_usage))
def fonk7(b23):
    b4 = time.time()
    b5 = set()
    b6 = deque([b23])
    a1 = 0
    a2 = 0
    while b6:
        b7 = b6.popleft()
        b5.add(tuple(b7.b1))
        if b7.b1 = = b21:
            b8 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b9 = [], 0, len(b5), len(b6)
            b10 = b7.b14
            while b7.b12:
                path_to_goal.insert(0, b7.b13)
                cost_of_path += 1
                b7 = b7.b12
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b9, a1, b10, a2, b8, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b1) not in b5:
                b6.append(neighbor)
                b5.add(tuple(neighbor.b1))
                a2 = max(a2, neighbor.b14)
        a1 = max(a1, len(b6))
def fonk8(b23):
    b4 = time.time()
    b5 = set()
    b6 = class1()
    b6.fonk2(b23)
    a1 = 0
    a2 = 0
    while not b6.fonk4():
        b7 = b6.fonk3()
        b5.add(tuple(b7.b1))
        if b7.b1 = = b21:
            b8 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b9 = [], 0, len(b5), len(b6.b1)
            b10 = b7.b14
            while b7.b12:
                path_to_goal.insert(0, b7.b13)
                cost_of_path += 1
                b7 = b7.b12
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b9, a1, b10, a2, b8, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b1) not in b5:
                b6.fonk2(neighbor)
                b5.add(tuple(neighbor.b1))
                a2 = max(a2, neighbor.b14)
        a1 = max(a1, len(b6.b1))
def fonk9(b23, b24):
    b4 = time.time()
    b5 = set()
    b6 = class1()
    b6.fonk2(b23)
    a1 = 0
    a2 = 0
    while not b6.fonk4():
        b7 = b6.fonk3()
        b5.add(tuple(b7.b1))
        if b7.b1 = = b21:
            b8 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b9 = [], 0, len(b5), len(b6.b1)
            b10 = b7.b14
            while b7.b12:
                path_to_goal.insert(0, b7.b13)
                cost_of_path += 1
                b7 = b7.b12
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b9, a1, b10, a2, b8, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        if b7.b14 < b24:
            for neighbor in b7.fonk13():
                if tuple(neighbor.b1) not in b5:
                    b6.fonk2(neighbor)
                    b5.add(tuple(neighbor.b1))
                    a2 = max(a2, neighbor.b14)
            a1 = max(a1, len(b6.b1))
def fonk10(b23):
    b4 = time.time()
    b5 = set()
    b6 = []
    heapq.heappush(b6, (0, b23))
    a1 = 0
    a2 = 0
    while b6:
        current_priority, b7 = heapq.heappop(b6)
        b5.add(tuple(b7.b1))
        if b7.b1 = = b21:
            b8 = time.time() - b4
            path_to_goal, cost_of_path, nodes_expanded, b9 = [], 0, len(b5), len(b6)
            b10 = b7.b14
            while b7.b12:
                path_to_goal.insert(0, b7.b13)
                cost_of_path += 1
                b7 = b7.b12
            fonk6(path_to_goal, cost_of_path, nodes_expanded, b9, a1, b10, a2, b8, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in b7.fonk13():
            if tuple(neighbor.b1) not in b5:
                b11 = neighbor.b14 + neighbor.fonk12()
                heapq.heappush(b6, (b11, neighbor))
                b5.add(tuple(neighbor.b1))
                a2 = max(a2, neighbor.b14)
        a1 = max(a1, len(b6))
class class2:
    def fonk11(self, b2, b12, b13, b14):
        self.b1 = b2
        self.b12 = b12
        self.b13 = b13
        self.b14 = b14
    def fonk12(self):
        return sum([1 if self.b1[i] != b21[i] else 0 for i in range(len(self.b1))])
    def fonk13(self):
        b15 = []
        b16 = self.b1.index(0)
        row, b17 = divmod(b16, 3)
        for b13 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, b18 = row + b13[0], b17 + b13[1]
            if 0 <= new_row < 3 and 0 <= b18 < 3:
                b19 = self.b1[:]
                b20 = new_row * 3 + b18
                b19[b16], b19[b20] = b19[b20], b19[b16]
                b15.append(class2(b19, self, b13, self.b14 + 1))
        return b15
b21 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def fonk14():
    b22 = sys.argv[1]
    b23 = class2([int(i) for i in sys.argv[2].split(",")], None, None, 0)
    if b22 = = "bfs":
        fonk7(b23)
    elif b22 = = "dfs":
        fonk8(b23)
    elif b22 = = "dls":
        b24 = int(sys.argv[3])
        fonk9(b23, b24)
    elif b22 = = "ast":
        fonk10(b23)
if b25 = = "__main__":
    fonk14()