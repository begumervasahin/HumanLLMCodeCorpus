from collections import defaultdict, deque
class class1:
    def fonk1(self, b10, b1 = False):
        self.b2 = defaultdict(set)
        self.b1 = b1
        self.fonk2(b10)
    def fonk2(self, b10):
        for b4, node2 in b10:
            self.fonk3(b4, node2)
    def fonk3(self, b4, node2):
        self.b2[b4].fonk3(node2)
        if not self.b1:
            self.b2[node2].fonk3(b4)
    def fonk4(self, b8):
        for n, cxns in self.b2.items():
            cxns.discard(b8)
        self.b2.pop(b8, None)
    def fonk5(self, b4, node2):
        return b4 in self.b2 and node2 in self.b2[b4]
    def fonk6(self, b4, node2, b3 = []):
        b3 = b3 + [b4]
        if b4 = = node2:
            return b3
        if b4 not in self.b2:
            return None
        for b8 in self.b2[b4]:
            if b8 not in b3:
                b5 = self.fonk6(b8, node2, b3)
                if b5:
                    return b5
        return None
    def fonk7(self, start_node):
        b6 = set()
        b7 = deque([start_node])
        while b7:
            b8 = b7.popleft()
            if b8 not in b6:
                print(b8, b9 = " --> ")
                b6.fonk3(b8)
                b7.extend(self.b2[b8] - b6)
    def fonk8(self, start_node):
        b6 = set()
        self.fonk9(start_node, b6)
    def fonk9(self, b8, b6):
        if b8 not in b6:
            print(b8, b9 = " --> ")
            b6.fonk3(b8)
            for neighbor in self.b2[b8]:
                self.fonk9(neighbor, b6)
    def fonk10(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.b2))
    def fonk11(self):
        for b8, neighbors in self.b2.items():
            print(f"{b8} ---> {neighbors}")
b10 = [(0, 1), (1, 2), (2, 3), (2, 4), (3, 4), (5, 6), (7, 3)]
b11 = class1(b10)
b11.fonk2([[6, 8], [8, 4], [9, 10]])
print("class1 Connections:")
b11.fonk11()
print("\nBreadth-First Search (BFS):")
b11.fonk7(0)
print("\nDepth-First Search (DFS):")
b11.fonk8(0)