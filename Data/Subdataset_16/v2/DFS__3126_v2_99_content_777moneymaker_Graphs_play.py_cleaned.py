b1 = 'Milosz Chodkowski PUT'
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = {i: [] for i in range(b2)}
        self.b4 = []
        self.fonk2()
    def fonk2(self):
        for i in range(self.b2):
            if i < self.b2 - 1:
                self.fonk3(i, i + 1)
            if i % b5 = = 0 and i + b5 < self.b2:
                self.fonk3(i, i + b5)
    def fonk3(self, u, v):
        self.b3[u].append(v)
        self.b3[v].append(u)
    def fonk4(self):
        b6 = set()
        self.b4 = []
        def fonk5(v):
            b6.add(v)
            self.b4.append(v)
            for neighbor in self.b3[v]:
                if neighbor not in b6:
                    fonk5(neighbor)
        if self.b2 > 0:
            fonk5(0)
if b7 = = "__main__":
    b8 = class1(10)
    print("Adjacency List:", b8.b3)
    b8.fonk4()
    print("DFS Path:", b8.b4)