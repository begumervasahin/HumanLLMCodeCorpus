from collections import defaultdict, deque
class class1:
    def fonk1(self, b1 = None, b3=False):
        self.b2 = defaultdict(set)
        self.b3 = b3
        if b1:
            self.fonk2(b1)
    def fonk2(self, b1):
        for node1, node2 in b1:
            self.fonk3(node1, node2)
    def fonk3(self, node1, node2):
        self.b2[node1].fonk3(node2)
        if not self.b3:
            self.b2[node2].fonk3(node1)
    def fonk4(self, b9):
        for neighbors in self.b2.values():
            neighbors.discard(b9)
        self.b2.pop(b9, None)
    def fonk5(self, node1, node2):
        return node2 in self.b2.get(node1, set())
    def fonk6(self, b5, end_node, b4 = None):
        if b4 is None:
            b4 = []
        b4.append(b5)
        if b5 = = end_node:
            return b4
        if b5 not in self.b2:
            return None
        for neighbor in self.b2[b5]:
            if neighbor not in b4:
                b6 = self.fonk6(neighbor, end_node, b4.copy())
                if b6:
                    return b6
        return None
    def fonk7(self, b5):
        b7 = set()
        b8 = deque([b5])
        b7.fonk3(b5)
        while b8:
            b9 = b8.popleft()
            print(b9, b10 = " --> ")
            for neighbor in self.b2[b9]:
                if neighbor not in b7:
                    b8.append(neighbor)
                    b7.fonk3(neighbor)
        print("End")
    def fonk8(self, b5):
        b7 = set()
        self.fonk9(b5, b7)
        print("End")
    def fonk9(self, b9, b7):
        b7.fonk3(b9)
        print(b9, b10 = " --> ")
        for neighbor in self.b2[b9]:
            if neighbor not in b7:
                self.fonk9(neighbor, b7)
    def fonk10(self):
        return f'class1({dict(self.b2)})'
b1 = [(0, 1), (1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (7, 3)]
b11 = class1(b1)
b11.fonk2([(6, 8), (8, 4), (9, 10)])
print("class1 representation:")
print(b11)
print("\nBFS traversal starting from b9 0:")
b11.fonk7(0)
print("\nDFS traversal starting from b9 0:")
b11.fonk8(0)