from collections import deque
import heapq
import time
import resource
import sys
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
def fonk4(path_to_goal, cost_of_path, nodes_expanded, b18, a1, b19, a2, b17, max_ram_usage):
    with open('output.txt', 'w') as f:
        f.write("path_to_goal: {}\n".format(path_to_goal))
        f.write("cost_of_path: {}\n".format(cost_of_path))
        f.write("nodes_expanded: {}\n".format(nodes_expanded))
        f.write("b18: {}\n".format(b18))
        f.write("a1: {}\n".format(a1))
        f.write("b19: {}\n".format(b19))
        f.write("a2: {}\n".format(a2))
        f.write("b17: {}\n".format(b17))
        f.write("max_ram_usage: {}\n".format(max_ram_usage))
def fonk5(b1):
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b1[i][j] == 0:
                return i, j
def fonk6(b1):
    b8 = []
    blank_i, b9 = fonk5(b1)
    b10 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in b10:
        new_i, b11 = blank_i + direction[0], b9 + direction[1]
        if 0 <= new_i < len(b1) and 0 <= b11 < len(b1[0]):
            b12 = [list(row) for row in b1]
            b12[blank_i][b9], b12[new_i][b11] = b12[new_i][b11], b12[blank_i][b9]
            b8.append(b12)
    return b8
def fonk7(b22):
    b13 = time.time()
    b14 = set()
    b15 = deque([class1(b22, None, None, 0, 0, 0)])
    a1 = 0
    a2 = 0
    while b15:
        b16 = b15.popleft()
        b14.add(b16.b7)
        if b16.b1 = = goal_state:
            b17 = time.time() - b13
            path_to_goal, cost_of_path, nodes_expanded, b18 = [], 0, len(b14), len(b15)
            b19 = b16.b4
            while b16.b2:
                path_to_goal.insert(0, b16.b3)
                cost_of_path += 1
                b16 = b16.b2
            fonk4(path_to_goal, cost_of_path, nodes_expanded, b18, a1, b19, a2, b17, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in fonk6(b16.b1):
            if ''.join(str(e) for row in neighbor) not in b14:
                b15.append(class1(neighbor, b16, neighbor, b16.b4 + 1, 0, 0))
                b14.add(''.join(str(e) for row in neighbor))
                a2 = max(a2, b16.b4 + 1)
        a1 = max(a1, len(b15))
def fonk8(b22):
    b13 = time.time()
    b14 = set()
    b15 = [class1(b22, None, None, 0, 0, 0)]
    a1 = 0
    a2 = 0
    while b15:
        b16 = b15.pop()
        b14.add(b16.b7)
        if b16.b1 = = goal_state:
            b17 = time.time() - b13
            path_to_goal, cost_of_path, nodes_expanded, b18 = [], 0, len(b14), len(b15)
            b19 = b16.b4
            while b16.b2:
                path_to_goal.insert(0, b16.b3)
                cost_of_path += 1
                b16 = b16.b2
            fonk4(path_to_goal, cost_of_path, nodes_expanded, b18, a1, b19, a2, b17, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in reversed(fonk6(b16.b1)):
            if ''.join(str(e) for row in neighbor) not in b14:
                b15.append(class1(neighbor, b16, neighbor, b16.b4 + 1, 0, 0))
                b14.add(''.join(str(e) for row in neighbor))
                a2 = max(a2, b16.b4 + 1)
        a1 = max(a1, len(b15))
def fonk9(b22):
    b13 = time.time()
    b14 = set()
    b15 = []
    heapq.heappush(b15, (0, class1(b22, None, None, 0, 0, 0)))
    a1 = 0
    a2 = 0
    while b15:
        current_priority, b16 = heapq.heappop(b15)
        b14.add(b16.b7)
        if b16.b1 = = goal_state:
            b17 = time.time() - b13
            path_to_goal, cost_of_path, nodes_expanded, b18 = [], 0, len(b14), len(b15)
            b19 = b16.b4
            while b16.b2:
                path_to_goal.insert(0, b16.b3)
                cost_of_path += 1
                b16 = b16.b2
            fonk4(path_to_goal, cost_of_path, nodes_expanded, b18, a1, b19, a2, b17, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            return
        for neighbor in fonk6(b16.b1):
            if ''.join(str(e) for row in neighbor) not in b14:
                b20 = b16.b4 + 1
                heapq.heappush(b15, (b20, class1(neighbor, b16, neighbor, b16.b4 + 1, 0, 0)))
                b14.add(''.join(str(e) for row in neighbor))
                a2 = max(a2, b16.b4 + 1)
        a1 = max(a1, len(b15))
def fonk10(b22):
    b13 = time.time()
    b14 = set()
    a3 = 0
    a1 = 0
    a2 = 0
    while True:
        b15 = []
        heapq.heappush(b15, (0, class1(b22, None, None, 0, 0, 0)))
        b14.clear()
        while b15:
            current_priority, b16 = heapq.heappop(b15)
            b14.add(b16.b7)
            if b16.b1 = = goal_state:
                b17 = time.time() - b13
                path_to_goal, cost_of_path, nodes_expanded, b18 = [], 0, len(b14), len(b15)
                b19 = b16.b4
                while b16.b2:
                    path_to_goal.insert(0, b16.b3)
                    cost_of_path += 1
                    b16 = b16.b2
                fonk4(path_to_goal, cost_of_path, nodes_expanded, b18, a1, b19, a2, b17, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                return
            for neighbor in fonk6(b16.b1):
                if ''.join(str(e) for row in neighbor) not in b14:
                    b20 = b16.b4 + 1
                    if b20 <= a3:
                        heapq.heappush(b15, (b20, class1(neighbor, b16, neighbor, b16.b4 + 1, 0, 0)))
                        b14.add(''.join(str(e) for row in neighbor))
                        a2 = max(a2, b16.b4 + 1)
        a1 = max(a1, len(b15))
        a3 += 1
def fonk11():
    b21 = sys.argv[1]
    b22 = [[int(i) for i in sys.argv[2].split(",")]]
    if b21 = = "bfs":
        fonk7(b22)
    elif b21 = = "dfs":
        fonk8(b22)
    elif b21 = = "ast":
        fonk9(b22)
    elif b21 = = "ida":
        fonk10(b22)
if b23 = = "__main__":
    fonk11()