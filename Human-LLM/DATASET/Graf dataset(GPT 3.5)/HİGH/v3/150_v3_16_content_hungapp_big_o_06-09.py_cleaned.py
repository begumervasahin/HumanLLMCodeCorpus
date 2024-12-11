import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(source, b9, b10):
    b4 = queue.PriorityQueue()
    b4.put(class1(source, 0))
    b5 = [b1] * (b9 + 1)
    b5[source] = 0
    while not b4.empty():
        b6 = b4.get()
        b7 = b6.b2
        b8 = b6.b3
        for neighbor in b10[b7]:
            if b8 + neighbor.b3 < b5[neighbor.b2]:
                b5[neighbor.b2] = b8 + neighbor.b3
                b4.put(class1(neighbor.b2, b5[neighbor.b2]))
    return b5
def fonk4():
    def fonk5():
        b9 = int(input())
        b10 = [[] for _ in range(b9 + 1)]
        b11 = []
        for i in range(b9):
            b2 = input()
            b11.append(b2)
            b12 = int(input())
            for j in range(b12):
                nr, b13 = map(int, input().split())
                b10[i + 1].append(class1(nr, b13))
        return b9, b10, b11
    b14 = int(input())
    for _ in range(b14):
        b9, b10, b11 = fonk5()
        b15 = int(input())
        for _ in range(b15):
            source, b16 = input().split()
            b17 = b11.index(source) + 1
            b18 = b11.index(b16) + 1
            b19 = fonk3(b17, b9, b10)
            print(b19[b18])
        input()
def fonk6():
    b9, m, k, b20 = map(int, input().split())
    b21 = list(map(int, input().split()))
    b10 = [[] for _ in range(b9 + 1)]
    for _ in range(m):
        b7, b27, b22 = map(int, input().split())
        b10[b7].append(class1(b27, b22))
        b10[b27].append(class1(b7, b22))
    a, b23 = map(int, input().split())
    b24 = fonk3(a, b9, b10)
    b25 = fonk3(b23, b9, b10)
    a1 = b1
    for i in range(k):
        if b25[b21[i]] <= b20:
            a1 = min(a1, b24[b21[i]] + b25[b21[i]])
    if a1 < b1:
        print(a1)
    else:
        print(-1)
def fonk7():
    def fonk8(s, b9, b10):
        b4 = queue.Queue()
        b4.put(s)
        b5 = [b1] * b9
        b5[s] = 0
        while not b4.empty():
            b7 = b4.get()
            for neighbor in b10[b7]:
                if b5[neighbor] == b1:
                    b5[neighbor] = b5[b7] + 1
                    b4.put(neighbor)
        return b5
    b26 = int(input())
    for b13 in range(b26):
        b9 = int(input())
        b10 = [[] for _ in range(b9)]
        b15 = int(input())
        for _ in range(b15):
            b7, b27 = map(int, input().split())
            b10[b7].append(b27)
            b10[b27].append(b7)
        s, b22 = map(int, input().split())
        b28 = fonk8(s, b9, b10)
        b29 = fonk8(b22, b9, b10)
        b30 = max(b28[i] + b29[i] for i in range(b9) if b28[i] != b1 and b29[i] != b1)
        print('Case {}: {}'.format(b13 + 1, b30))
