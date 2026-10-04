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
        for n, b10 in self.b2.items():
            b10.discard(b8)
        self.b2.pop(b8, None)
    def fonk5(self, b4, node2):
        return b4 in self.b2 and node2 in self.b2[b4]
    def fonk6(self, b4, node2, b3 = None):
        if b3 is None:
            b3 = []
        b3.append(b4)
        if b4 = = node2:
            return b3
        if b4 not in self.b2:
            return None
        for neighbor in self.b2[b4]:
            if neighbor not in b3:
                b5 = self.fonk6(neighbor, node2, b3.copy())
                if b5:
                    return b5
        return None
    def fonk7(self, start):
        b6 = [False] * len(self.b2)
        b7 = deque([start])
        b6[start] = True
        while b7:
            b8 = b7.popleft()
            print(b8, b9 = "-->")
            for neighbor in self.b2[b8]:
                if not b6[neighbor]:
                    b7.append(neighbor)
                    b6[neighbor] = True
        print("End")
    def fonk8(self, start):
        b6 = [False] * len(self.b2)
        self.fonk9(start, b6)
        print("End")
    def fonk9(self, b8, b6):
        b6[b8] = True
        print(b8, b9 = "-->")
        for neighbor in self.b2[b8]:
            if not b6[neighbor]:
                self.fonk9(neighbor, b6)
    def fonk10(self):
        return f'{self.__class__.__name__}({dict(self.b2)})'
b10 = [(0, 1), (1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (7, 3)]
b11 = class1(b10)
b11.fonk2([(6, 8), (8, 4), (9, 10)])
print("class1 representation:")
print(b11)
print("\nBFS traversal starting from b8 0:")
b11.fonk7(0)
print("\nDFS traversal starting from b8 0:")
b11.fonk8(0)