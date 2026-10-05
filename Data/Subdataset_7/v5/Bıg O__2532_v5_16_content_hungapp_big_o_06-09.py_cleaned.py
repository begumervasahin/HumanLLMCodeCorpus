import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(b9, b15, b16):
    b4 = queue.PriorityQueue()
    b4.put(class1(b15, 0))
    b3 = [b1] * len(b9)
    b3[b15] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b2
        b7 = b5.b3
        if b6 = = b16:
            return b3[b16]
        for neighbor in b9[b6]:
            if b7 + neighbor.b3 < b3[neighbor.b2]:
                b3[neighbor.b2] = b7 + neighbor.b3
                b4.put(class1(neighbor.b2, b3[neighbor.b2]))
def fonk4():
    b8 = int(input())
    b9 = [[] for _ in range(b8 + 1)]
    b10 = []
    for i in range(b8):
        b2 = input()
        b10.append(b2)
        b11 = int(input())
        for _ in range(b11):
            nr, b12 = map(int, input().split())
            b9[i + 1].append(class1(nr, b12))
    b13 = int(input())
    for _ in range(b13):
        source, b14 = input().split()
        b15 = b10.index(source) + 1
        b16 = b10.index(b14) + 1
        b17 = fonk3(b9, b15, b16)
        print(b17)
def fonk5():
    b18 = int(input())
    for _ in range(b18):
        fonk4()
        if _ < b18 - 1:
            input()
if b19 = = "__main__":
    fonk5()