class class1:
    def fonk1(self, nodes):
        self.b1 = nodes
        self.b2 = []
    def fonk2(self, u, v, w):
        self.b2.append((u, v, w))
    def fonk3(self, b7, i):
        if b7[i] != i:
            b7[i] = self.fonk3(b7, b7[i])
        return b7[i]
    def fonk4(self, b7, b8, x, y):
        b3 = self.fonk3(b7, x)
        b4 = self.fonk3(b7, y)
        if b8[b3] < b8[b4]:
            b7[b3] = b4
        elif b8[b3] > b8[b4]:
            b7[b4] = b3
        else:
            b7[b4] = b3
            b8[b3] += 1
    def fonk5(self):
        b5 = []
        self.b2.sort(b6 = lambda edge: edge[2])
        b7 = list(range(self.b1))
        b8 = [0] * self.b1
        for u, v, w in self.b2:
            b9 = self.fonk3(b7, u)
            b10 = self.fonk3(b7, v)
            if b9 != b10:
                b5.append((u, v, w))
                self.fonk4(b7, b8, b9, b10)
            if len(b5) == self.b1 - 1:
                break
        print("Resulting Minimum Spanning Tree (MST):")
        a1 = 0
        for u, v, w in b5:
            print(f"{u} -- {v} == weight: {w}")
            a1 += w
        print(f"The total weight of the MST is {a1}")
        return b5
if b11 = = "__main__":
    b12 = class1(5)
    b12.fonk2(0, 1, 9)
    b12.fonk2(0, 2, 7)
    b12.fonk2(0, 3, 2)
    b12.fonk2(1, 2, 2)
    b12.fonk2(2, 3, 2)
    b12.fonk2(1, 3, 2)
    b12.fonk2(1, 4, 3)
    b12.fonk2(3, 4, 3)
    b12.fonk5()