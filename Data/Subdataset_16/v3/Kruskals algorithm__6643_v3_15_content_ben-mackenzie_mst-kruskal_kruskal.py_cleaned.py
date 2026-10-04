import heapq
class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, item):
        self.b1[item] = item
        self.b2[item] = 0
    def fonk3(self, item):
        if self.b1[item] != item:
            self.b1[item] = self.fonk3(self.b1[item])
        return self.b1[item]
    def fonk4(self, item1, item2):
        b3 = self.fonk3(item1)
        b4 = self.fonk3(item2)
        if b3 != b4:
            if self.b2[b3] > self.b2[b4]:
                self.b1[b4] = b3
            else:
                self.b1[b3] = b4
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b4] += 1
class class2:
    def fonk5(self):
        self.b5 = []
    def fonk6(self, item):
        heapq.heappush(self.b5, item)
    def fonk7(self):
        return heapq.heappop(self.b5)
    def fonk8(self):
        return len(self.b5) == 0
def fonk9(b12):
    b6 = []
    b7 = class2()
    b8 = class1()
    for vertex in b12['V']:
        b8.fonk2(vertex)
    for edge in b12['E']:
        b7.fonk6(edge)
    a1 = 0
    while len(b6) < len(b12['V']) - 1 and not b7.fonk8():
        weight, u, b9 = b7.fonk7()
        b10 = b8.fonk3(u)
        b11 = b8.fonk3(b9)
        if b10 != b11:
            b6.append((u, b9, weight))
            a1 += weight
            b8.fonk4(b10, b11)
    return b6, a1
b12 = {
    'V': ['A', 'B', 'C', 'D', 'E'],
    'E': [
        (1, 'A', 'B'),
        (2, 'B', 'C'),
        (3, 'C', 'D'),
        (4, 'D', 'E'),
        (5, 'A', 'E'),
        (6, 'B', 'D')
    ]
}
b6, a1 = fonk9(b12)
print("Minimum Spanning Tree:", b6)
print("Total Weight of MST:", a1)