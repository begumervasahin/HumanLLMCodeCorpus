class class1:
    def fonk1(self):
        self.b1 = {}
    def fonk2(self, item):
        self.b1[item] = item
    def fonk3(self, item):
        if self.b1[item] != item:
            self.b1[item] = self.fonk3(self.b1[item])
        return self.b1[item]
    def fonk4(self, item1, item2):
        b2 = self.fonk3(item1)
        b3 = self.fonk3(item2)
        if b2 != b3:
            self.b1[b3] = b2
def fonk5(b9, b10):
    b4 = class1()
    b5 = []
    for node in b9:
        b4.fonk2(node)
    b6 = len(b9) - 1
    for src, dest, weight in b10:
        b7 = b4.fonk3(src)
        b8 = b4.fonk3(dest)
        if b7 != b8:
            b5.append((src, dest, weight))
            b4.fonk4(b7, b8)
            b6 -= 1
            if b6 = = 0:
                break
    return b5
b9 = ['A', 'B', 'C', 'D', 'E']
b10 = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('C', 'D', 3),
    ('D', 'E', 4),
    ('A', 'E', 5),
    ('B', 'D', 6)
]
b5 = fonk5(b9, b10)
print("Minimum Spanning Tree:", b5)