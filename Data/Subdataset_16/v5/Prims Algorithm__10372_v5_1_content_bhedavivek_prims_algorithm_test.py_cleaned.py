import sys
class class1:
    def fonk1(self, b2, b1 = 9999999, b3=0, b4=0):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
class class2:
    def fonk2(self, n):
        self.b5 = [[] for _ in range(n)]
    def fonk3(self, u, v, b19):
        b6 = class1(b2=v, b3=u, b1=b19)
        self.b5[u - 1].append(b6)
class class3:
    def fonk4(self):
        self.b7 = [0]
        self.b8 = []
    def fonk5(self, b6):
        self.b7.append(b6)
        self.b7[0] = len(self.b7) - 1
        self.fonk6(self.b7[0])
        self.b8[b6.b2 - 1].b4 = self.b7[0]
    def fonk6(self, b10):
        while b10 > 1:
            b9 = b10
            if self.b7[b9].b1 > self.b7[b10].b1:
                self.fonk10(b9, b10)
                b10 = b9
            else:
                break
    def fonk7(self):
        self.fonk10(1, self.b7[0])
        b11 = self.b7.pop()
        self.b7[0] -= 1
        if self.b7[0] > 1:
            self.fonk9(1)
        return b11
    def fonk8(self, heap_index, updated_distance, b3):
        if heap_index > 0:
            self.b7[heap_index].b1 = updated_distance
            self.b7[heap_index].b3 = b3
            self.fonk6(heap_index)
    def fonk9(self, b10):
        while 2 * b10 <= self.b7[0]:
            b12 = 2 * b10
            if b12 < self.b7[0] and self.b7[b12 + 1].b1 < self.b7[b12].b1:
                b12 += 1
            if self.b7[b12].b1 < self.b7[b10].b1:
                self.fonk10(b10, b12)
                b10 = b12
            else:
                break
    def fonk10(self, i, j):
        self.b8[self.b7[i].b2 - 1].b4 = j
        self.b8[self.b7[j].b2 - 1].b4 = i
        self.b7[i], self.b7[j] = self.b7[j], self.b7[i]
def fonk11(b18, b20):
    b13 = class3()
    b13.fonk5(b20)
    b14 = []
    for i in range(len(b13.b8)):
        if i != b20.b2 - 1:
            b6 = class1(b2=i + 1)
            b13.fonk5(b6)
    while len(b13.b7) > 1:
        b11 = b13.fonk7()
        b14.append(b11)
        for neighbor in b18.b5[b11.b2 - 1]:
            if neighbor.b1 < b13.b8[neighbor.b2 - 1].b1:
                b13.fonk8(b13.b8[neighbor.b2 - 1].b4, neighbor.b1, b11.b2)
                b13.b8[neighbor.b2 - 1].b3 = b11.b2
    return b14
def fonk12():
    b15 = input().split()
    b16 = int(b15[0])
    b17 = int(b15[1])
    b18 = class2(b16)
    for _ in range(b17):
        u, v, b19 = map(int, input().split())
        b18.fonk5(u, v, b19)
        b18.fonk5(v, u, b19)
    b13 = class3()
    for i in range(b16):
        b6 = class1(b2=i + 1)
        b13.b8.append(b6)
    b20 = class1(b2=1)
    b21 = fonk11(b18, b20)
    b22 = sum(b6.b1 for b6 in b21 if b6.b2 != 0 and b6.b3 != 0)
    print(b22)
if b23 = = "__main__":
    fonk12()