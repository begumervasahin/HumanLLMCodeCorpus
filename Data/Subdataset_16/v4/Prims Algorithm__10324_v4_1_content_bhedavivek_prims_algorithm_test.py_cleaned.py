import sys
class class1:
    def fonk1(self, b2, b1 = 9999999, b3=0, b4=0):
        self.b2 = b2
        self.b1 = b1
        self.b3 = b3
        self.b4 = b4
    def fonk2(self):
        return self.b1
class class2:
    def fonk3(self, n):
        self.b5 = [[] for _ in range(n)]
    def fonk4(self, u, v, b20):
        b6 = class1(b2=v, b3=u, b1=b20)
        self.b5[u-1].append(b6)
class class3:
    def fonk5(self):
        self.b7 = [0]
        self.b8 = []
    def fonk6(self, b6):
        self.b7.append(b6)
        self.b7[0] = len(self.b7) - 1
        self.fonk7(self.b7[0])
        self.b8[b6.b2 - 1].b4 = self.b7[0]
    def fonk7(self, b10):
        while b10 > 1:
            b9 = b10
            if self.b7[b9].b1 > self.b7[b10].b1:
                self.b8[self.b7[b10].b2 - 1].b4 = b9
                self.b8[self.b7[b9].b2 - 1].b4 = b10
                self.b7[b10], self.b7[b9] = self.b7[b9], self.b7[b10]
                b10 = b9
            else:
                break
    def fonk8(self):
        self.b8[self.b7[1].b2 - 1].b4 = 0
        b11 = self.b7[0]
        self.b8[self.b7[b11].b2 - 1].b4 = 1
        b12 = self.b7[1]
        self.b7[1] = self.b7[b11]
        self.b7[0] -= 1
        if self.b7[0] > 1:
            self.fonk10(1)
        self.b7.pop()
        return b12
    def fonk9(self, heap_index, updated_distance, b3):
        if heap_index > 0:
            self.b7[heap_index].b1 = updated_distance
            self.b7[heap_index].b3 = b3
            self.fonk7(heap_index)
    def fonk10(self, b10):
        while 2 * b10 <= self.b7[0]:
            b13 = 2 * b10
            if b13 < self.b7[0] and self.b7[b13 + 1].b1 < self.b7[b13].b1:
                b13 += 1
            if self.b7[b13].b1 < self.b7[b10].b1:
                self.b8[self.b7[b10].b2 - 1].b4 = b13
                self.b8[self.b7[b13].b2 - 1].b4 = b10
                self.b7[b10], self.b7[b13] = self.b7[b13], self.b7[b10]
                b10 = b13
            else:
                break
def fonk11(b19, b21):
    b14 = class3()
    b14.fonk6(b21)
    b15 = []
    for i in range(len(b14.b8)):
        if i != b21.b2 - 1:
            b6 = class1(b2=i + 1)
            b14.fonk6(b6)
    while len(b14.b7) > 1:
        b12 = b14.fonk8()
        b15.append(b12)
        for neighbor in b19.b5[b12.b2 - 1]:
            if neighbor.b1 < b14.b8[neighbor.b2 - 1].b1:
                b14.b8[neighbor.b2 - 1].b1 = neighbor.b1
                b14.fonk9(b14.b8[neighbor.b2 - 1].b4, neighbor.b1, b12.b2)
                b14.b8[neighbor.b2 - 1].b3 = b12.b2
    return b15
def fonk12():
    b16 = input().split()
    b17 = int(b16[0])
    b18 = int(b16[1])
    b19 = class2(b17)
    for _ in range(b18):
        u, v, b20 = map(int, input().split())
        b19.fonk6(u, v, b20)
        b19.fonk6(v, u, b20)
    b14 = class3()
    for i in range(b17):
        b6 = class1(b2=i + 1)
        b14.b8.append(b6)
    b21 = class1(b2=1)
    b22 = fonk11(b19, b21)
    b23 = sum(b6.b1 for b6 in b22 if b6.b2 != 0 and b6.b3 != 0)
    print(b23)
if b24 = = "__main__":
    fonk12()