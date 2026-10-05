import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(b9):
    b4 = queue.PriorityQueue()
    b4.put(class2(b9, 0))
    b3[b9] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b2
        b7 = b5.b3
        for neighbor in b12[b6]:
            if b7 + neighbor.b3 < b3[neighbor.b2]:
                b3[neighbor.b2] = b7 + neighbor.b3
                b4.put(class2(neighbor.b2, b3[neighbor.b2]))
b8 = int(input())
b9 = int(input())
b10 = int(input())
b11 = int(input())
b12 = [[] for _ in range(b8 + 1)]
b3 = [b1 for _ in range(b8 + 1)]
for _ in range(b11):
    a, b, b7 = map(int, input().split())
    b12[b].append(class2(a, b7))
fonk6(b9)
a1 = 0
for i in range(1, b8 + 1):
    if b3[i] <= b10:
        a1 += 1
print(a1)
import queue
b1 = int(1e9)
class class2:
    def fonk4(self, b13, b14):
        self.b13 = b13
        self.b14 = b14
    def fonk5(self, other):
        return self.b14 <= other.b14
def fonk6(s, f):
    b4 = queue.PriorityQueue()
    b4.put(class2(s, 0))
    b14[s] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b13
        b7 = b5.b14
        if b6 = = f:
            return
        for neighbor in b12[b6]:
            if b7 + neighbor.b14 < b14[neighbor.b13]:
                b14[neighbor.b13] = b7 + neighbor.b14
                b4.put(class2(neighbor.b13, b14[neighbor.b13]))
b15 = int(input())
for _ in range(b15):
    b8 = int(input())
    b12 = [[] for _ in range(b8 + 1)]
    b16 = []
    for i in range(b8):
        b13 = input()
        b16.append(b13)
        b17 = int(input())
        for _ in range(b17):
            nr, a1 = map(int, input().split())
            b12[i + 1].append(class2(nr, a1))
    b18 = int(input())
    for _ in range(b18):
        b14 = [b1 for _ in range(b8 + 1)]
        source, b19 = input().split()
        b20 = b16.index(source) + 1
        b21 = b16.index(b19) + 1
        fonk6(b20, b21)
        print(b14[b21])
    input()