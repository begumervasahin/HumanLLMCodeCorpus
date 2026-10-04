import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(b22, b12, b3):
    b4 = queue.PriorityQueue()
    b4.put(class1(b22, 0))
    b3[b22] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b2
        b7 = b5.b3
        for neighbor in b12[b6]:
            if b7 + neighbor.b3 < b3[neighbor.b2]:
                b3[neighbor.b2] = b7 + neighbor.b3
                b4.put(class1(neighbor.b2, b3[neighbor.b2]))
def fonk4():
    b8 = int(input())
    b9 = int(input())
    b10 = int(input())
    b11 = int(input())
    b12 = [[] for _ in range(b8 + 1)]
    b3 = [b1 for _ in range(b8 + 1)]
    for _ in range(b11):
        a, b28, b7 = map(int, input().split())
        b12[b28].append(class1(a, b7))
    fonk3(b9, b12, b3)
    b13 = sum(1 for i in range(1, b8 + 1) if b3[i] <= b10)
    print(b13)
class class2:
    def fonk5(self, b14, b15):
        self.b14 = b14
        self.b15 = b15
    def fonk6(self, other):
        return self.b15 <= other.b15
def fonk7(b22, b12, b15):
    b4 = queue.PriorityQueue()
    b4.put(class2(b22, 0))
    b15[b22] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b14
        b7 = b5.b15
        for neighbor in b12[b6]:
            if b7 + neighbor.b15 < b15[neighbor.b14]:
                b15[neighbor.b14] = b7 + neighbor.b15
                b4.put(class2(neighbor.b14, b15[neighbor.b14]))
def fonk8():
    b16 = int(input())
    for _ in range(b16):
        b8 = int(input())
        b12 = [[] for _ in range(b8 + 1)]
        b17 = []
        for i in range(b8):
            b14 = input().strip()
            b17.append(b14)
            b18 = int(input())
            for _ in range(b18):
                nr, b19 = map(int, input().split())
                b12[i + 1].append(class2(nr, b19))
        b20 = int(input())
        for _ in range(b20):
            b15 = [b1 for _ in range(b8 + 1)]
            source, b21 = input().split()
            b22 = b17.index(source) + 1
            b23 = b17.index(b21) + 1
            fonk7(b22, b12, b15)
            print(b15[b23])
class class3:
    def fonk9(self, b14, b24):
        self.b14 = b14
        self.b24 = b24
    def fonk10(self, other):
        return self.b24 <= other.b24
def fonk11(b22, b12, distance):
    b4 = queue.PriorityQueue()
    b4.put(class3(b22, 0))
    distance[b22] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b14
        b7 = b5.b24
        for neighbor in b12[b6]:
            if b7 + neighbor.b24 < distance[neighbor.b14]:
                distance[neighbor.b14] = b7 + neighbor.b24
                b4.put(class3(neighbor.b14, distance[neighbor.b14]))
def fonk12():
    b8, b11, k, b25 = map(int, input().split())
    b26 = list(map(int, input().split()))
    b12 = [[] for _ in range(b8 + 1)]
    for _ in range(b11):
        b6, b33, b27 = map(int, input().split())
        b12[b6].append(class3(b33, b27))
        b12[b33].append(class3(b6, b27))
    a, b28 = map(int, input().split())
    b29 = [b1 for _ in range(b8 + 1)]
    fonk11(a, b12, b29)
    b30 = [b1 for _ in range(b8 + 1)]
    fonk11(b28, b12, b30)
    b31 = min((b29[b26[i]] + b30[b26[i]] for i in range(k) if b30[b26[i]] <= b25), default=b1)
    print(b31 if b31 < b1 else -1)
def fonk13(b22, b12, distance):
    b32 = queue.Queue()
    b32.put(b22)
    distance[b22] = 0
    while not b32.empty():
        b6 = b32.get()
        for neighbor in b12[b6]:
            if distance[neighbor] == b1:
                distance[neighbor] = distance[b6] + 1
                b32.put(neighbor)
def fonk14():
    b10 = int(input())
    for b19 in range(b10):
        b8 = int(input())
        b12 = [[] for _ in range(b8)]
        b20 = int(input())
        for _ in range(b20):
            b6, b33 = map(int, input().split())
            b12[b6].append(b33)
            b12[b33].append(b6)
        s, b27 = map(int, input().split())
        b34 = [b1 for _ in range(b8)]
        b35 = [b1 for _ in range(b8)]
        fonk13(s, b12, b34)
        fonk13(b27, b12, b35)
        b36 = max(b34[i] + b35[i] for i in range(b8) if b34[i] != b1 and b35[i] != b1)
        print(f'Case {b19 + 1}: {b36}')
if b37 = = "__main__":
    fonk4()
    fonk8()
    fonk12()
    fonk14()