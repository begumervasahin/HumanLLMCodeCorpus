from collections import defaultdict, deque
class class1:
    def fonk1(self, b11, b1 = False):
        self.b2 = defaultdict(set)
        self.b1 = b1
        self.fonk2(b11)
    def fonk2(self, b11):
        for b4, node2 in b11:
            self.fonk3(b4, node2)
    def fonk3(self, b4, node2):
        self.b2[b4].fonk3(node2)
        if not self.b1:
            self.b2[node2].fonk3(b4)
    def fonk4(self, b8):
        for n, b11 in self.b2.items():
            b11.discard(b8)
        self.b2.pop(b8, None)
    def fonk5(self, b4, node2):
        return node2 in self.b2[b4]
    def fonk6(self, b4, node2, b3 = None):
        if b3 is None:
            b3 = []
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
    def fonk7(self):
        return '{}({})'.format(self.__class__.b10, dict(self.b2))
    def fonk8(self):
        for b8, b11 in self.b2.items():
            print(f"{b8} ---> {b11}")
        print(self.b2[1])
    def fonk9(self, start):
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
    def fonk10(self, start):
        b6 = [False] * len(self.b2)
        self.fonk11(start, b6)
    def fonk11(self, b8, b6):
        b6[b8] = True
        print(b8, b9 = "-->")
        for neighbor in self.b2[b8]:
            if not b6[neighbor]:
                self.fonk11(neighbor, b6)
if b10 = = "__main__":
    b11 = [(0, 1), (1, 2), (2, 3), (2, 4),
                   (3, 4), (5, 6), (7, 3)]
    b12 = class1(b11)
    b12.fonk2([(6, 8), (8, 4), (9, 10)])
    print(b12.b2)
    print()
    print("BFS traversal starting from b8 0:")
    b12.fonk9(0)
    print()
    print("DFS traversal starting from b8 0:")
    b12.fonk10(0)