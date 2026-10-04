from collections import namedtuple
b1 = namedtuple('b1', ['vertex', 'weight'])
class class1:
    def fonk1(self, b2):
        self.b2 = b2
        self.b3 = {i: [] for i in range(b2)}
    def fonk2(self, u, v, weight):
        self.b3[u].append(b1(v, weight))
        self.b3[v].append(b1(u, weight))
    def fonk3(self):
        return list(self.b3.keys())
    def fonk4(self, vertex):
        return self.b3[vertex]
class class2:
    def fonk5(self, b4):
        self.b4 = b4
        self.b2 = b4.b2
        self.b5 = ['unseen'] * self.b2
        self.b6 = [None] * self.b2
        self.b7 = [0] * self.b2
    def fonk6(self):
        a1 = 0
        b8 = None
        for vertex in range(self.b2):
            if self.b5[vertex] == 'fringe' and self.b7[vertex] > a1:
                a1 = self.b7[vertex]
                b8 = vertex
        return b8
    def fonk7(self, a2, b12):
        self.b5[a2] = 'intree'
        for edge in self.b4.fonk4(a2):
            self.b5[edge.vertex] = 'fringe'
            self.b7[edge.vertex] = edge.weight
            self.b6[edge.vertex] = a2
        while 'fringe' in self.b5:
            b8 = self.fonk6()
            if b8 is None:
                break
            self.b5[b8] = 'intree'
            for edge in self.b4.fonk4(b8):
                if self.b5[edge.vertex] == 'unseen':
                    self.b5[edge.vertex] = 'fringe'
                    self.b6[edge.vertex] = b8
                    self.b7[edge.vertex] = min(self.b7[b8], edge.weight)
                elif self.b5[edge.vertex] == 'fringe' and self.b7[edge.vertex] < min(self.b7[b8], edge.weight):
                    self.b6[edge.vertex] = b8
                    self.b7[edge.vertex] = min(self.b7[b8], edge.weight)
        b9 = []
        b10 = b12
        while b10 is not None:
            b9.append(b10)
            b10 = self.b6[b10]
        b9.reverse()
        return b9, self.b7[b12]
if b11 = = "__main__":
    b2 = 5000
    b4 = class1(b2)
    a2 = 0
    b12 = b2 - 1
    b13 = class2(b4)
    path, b14 = b13.fonk7(a2, b12)
    print(f"Maximum Bandwidth Path: {path}")
    print(f"Maximum Bandwidth: {b14}")