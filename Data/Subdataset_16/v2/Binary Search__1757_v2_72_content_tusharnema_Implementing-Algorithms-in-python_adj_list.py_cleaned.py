from collections import defaultdict, deque
class class1:
    def fonk1(self, b11, b1 = False):
        self.b2 = defaultdict(set)
        self.b1 = b1
        self.fonk2(b11)
    def fonk2(self, b11):
        for node1, node2 in b11:
            self.fonk3(node1, node2)
    def fonk3(self, node1, node2):
        self.b2[node1].add(node2)
        if not self.b1:
            self.b2[node2].add(node1)
    def fonk4(self, b8):
        for b11 in self.b2.values():
            b11.discard(b8)
        self.b2.pop(b8, None)
    def fonk5(self, node1, node2):
        return node2 in self.b2[node1]
    def fonk6(self, b4, b9, b3 = None):
        if b3 is None:
            b3 = []
        b3.append(b4)
        if b4 = = b9:
            return b3
        if b4 not in self.b2:
            return None
        for neighbor in self.b2[b4]:
            if neighbor not in b3:
                b5 = self.fonk6(neighbor, b9, b3)
                if b5:
                    return b5
        b3.pop()
        return None
    def fonk7(self):
        return f"{self.__class__.b10}({dict(self.b2)})"
    def fonk8(self):
        for b8, b11 in self.b2.items():
            print(f"{b8} ---> {', '.join(map(str, b11))}")
    def fonk9(self, b4):
        b6 = set()
        b7 = deque([b4])
        while b7:
            b8 = b7.popleft()
            if b8 not in b6:
                print(b8, b9 = "-->")
                b6.add(b8)
                b7.extend(self.b2[b8] - b6)
        print("End")
    def fonk10(self, b4):
        b6 = set()
        self.fonk11(b4, b6)
        print("End")
    def fonk11(self, b8, b6):
        if b8 not in b6:
            print(b8, b9 = "-->")
            b6.add(b8)
            for neighbor in self.b2[b8]:
                self.fonk11(neighbor, b6)
if b10 = = "__main__":
    b11 = [
        (0, 1), (1, 2), (2, 3), (2, 4),
        (3, 4), (5, 6), (7, 3)
    ]
    b12 = class1(b11)
    b12.fonk2([(6, 8), (8, 4), (9, 10)])
    b12.fonk8()
    print()
    print("BFS traversal starting from b8 0:")
    b12.fonk9(0)
    print()
    print("DFS traversal starting from b8 0:")
    b12.fonk10(0)