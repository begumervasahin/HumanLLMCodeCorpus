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
    def fonk4(self, node):
        for n, cxns in self.b2.items():
            cxns.discard(node)
        self.b2.pop(node, None)
    def fonk5(self, b4, node2):
        return b4 in self.b2 and node2 in self.b2[b4]
    def fonk6(self, b4, node2, b3 = []):
        b3 = b3 + [b4]
        if b4 = = node2:
            return b3
        if b4 not in self.b2:
            return None
        for node in self.b2[b4]:
            if node not in b3:
                b5 = self.fonk6(node, node2, b3)
                if b5:
                    return b5
        return None
    def fonk7(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.b2))
    def fonk8(self):
        for node, b10 in self.b2.items():
            print(node, '--->', b10)
        print(self.b2['B'])
    def fonk9(self, start_node):
        b6 = [False] * len(self.b2)
        b7 = deque()
        b7.append(start_node)
        b6[start_node] = True
        while b7:
            b8 = b7.popleft()
            print(b8, b9 = " --> ")
            for adjacent_node in self.b2[b8]:
                if not b6[adjacent_node]:
                    b7.append(adjacent_node)
                    b6[adjacent_node] = True
    def fonk10(self, start_node):
        b6 = [False] * len(self.b2)
        self.fonk11(start_node, b6)
    def fonk11(self, b8, b6):
        b6[b8] = True
        print(b8, b9 = " --> ")
        for adjacent_node in self.b2[b8]:
            if not b6[adjacent_node]:
                self.fonk11(adjacent_node, b6)
b10 = [(0, 1), (1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (7, 3)]
b11 = class1(b10)
b11.fonk2([[6, 8], [8, 4], [9, 10]])
print(b11.b2)
print()
print("Breadth-First Search:")
b11.fonk9(0)
print()
print("Depth-First Search:")
b11.fonk10(0)