class class1:
    def fonk1(self, nodes):
        self.b1 = nodes
        self.b2 = []
    def fonk2(self, u, v, w):
        self.b2.append((u, v, w))
    def fonk3(self, b5, node):
        if b5[node] != node:
            b5[node] = self.fonk3(b5, b5[node])
        return b5[node]
    def fonk4(self, b5, b6, root1, root2):
        if b6[root1] < b6[root2]:
            b5[root1] = root2
        elif b6[root1] > b6[root2]:
            b5[root2] = root1
        else:
            b5[root2] = root1
            b6[root1] += 1
    def fonk5(self):
        b3 = []
        self.b2.sort(b4 = lambda edge: edge[2])
        b5 = list(range(self.b1))
        b6 = [0] * self.b1
        for u, v, w in self.b2:
            b7 = self.fonk3(b5, u)
            b8 = self.fonk3(b5, v)
            if b7 != b8:
                b3.append((u, v, w))
                self.fonk4(b5, b6, b7, b8)
                if len(b3) == self.b1 - 1:
                    break
        self.fonk6(b3)
        return b3
    def fonk6(self, b3):
        print("Resulting Minimum Spanning Tree (MST):")
        b9 = sum(weight for _, _, weight in b3)
        for u, v, weight in b3:
            print(f"{u} -- {v} == weight: {weight}")
        print(f"The total weight of the MST is {b9}")
if b10 = = "__main__":
    b11 = class1(5)
    b11.fonk2(0, 1, 9)
    b11.fonk2(0, 2, 7)
    b11.fonk2(0, 3, 2)
    b11.fonk2(1, 2, 2)
    b11.fonk2(2, 3, 2)
    b11.fonk2(1, 3, 2)
    b11.fonk2(1, 4, 3)
    b11.fonk2(3, 4, 3)
    b11.fonk5()