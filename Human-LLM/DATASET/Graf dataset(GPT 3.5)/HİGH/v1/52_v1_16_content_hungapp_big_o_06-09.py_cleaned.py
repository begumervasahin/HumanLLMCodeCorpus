import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(e, b12, b25, m, edges):
    b4 = queue.PriorityQueue()
    b4.put(class2(e, 0))
    b3 = [b1 for _ in range(b12 + 1)]
    b3[e] = 0
    b5 = [[] for _ in range(b12 + 1)]
    for a, b22, b8 in edges:
        b5[b22].append(class2(a, b8))
    while not b4.empty():
        b6 = b4.get()
        b7 = b6.b2
        b8 = b6.b3
        for neighbor in b5[b7]:
            if b8 + neighbor.b3 < b3[neighbor.b2]:
                b3[neighbor.b2] = b8 + neighbor.b3
                b4.put(class2(neighbor.b2, b3[neighbor.b2]))
    a1 = 0
    for i in range(1, b12 + 1):
        if b3[i] <= b25:
            a1 += 1
    print(a1)
def fonk4():
    class class2:
        def fonk5(self, b9, b10):
            self.b9 = b9
            self.b10 = b10
        def fonk6(self, other):
            return self.b10 <= other.b10
    def fonk7(s, f, b12, b5, b13):
        b4 = queue.PriorityQueue()
        b4.put(class2(s, 0))
        b10 = [b1 for _ in range(b12 + 1)]
        b10[s] = 0
        while not b4.empty():
            b6 = b4.get()
            b7 = b6.b9
            b8 = b6.b10
            if b7 = = f:
                return
            for neighbor in b5[b7]:
                if b8 + neighbor.b10 < b10[neighbor.b9]:
                    b10[neighbor.b9] = b8 + neighbor.b10
                    b4.put(class2(neighbor.b9, b10[neighbor.b9]))
    b11 = int(input())
    for _ in range(b11):
        b12 = int(input())
        b5 = [[] for _ in range(b12 + 1)]
        b13 = []
        for i in range(b12):
            b9 = input()
            b13.append(b9)
            b14 = int(input())
            for j in range(b14):
                nr, a1 = map(int, input().split())
                b5[i + 1].append(class2(nr, a1))
        b15 = int(input())
        for i in range(b15):
            b10 = [b1 for _ in range(b12 + 1)]
            source, b16 = input().split()
            b17 = b13.index(source) + 1
            b18 = b13.index(b16) + 1
            fonk9(b17, b18, b12, b5, b13)
            print(b10[b18])
        input()
def fonk8():
    def fonk9(s, distance, b5):
        b4 = queue.PriorityQueue()
        b4.put(class2(s, 0))
        distance[s] = 0
        while not b4.empty():
            b6 = b4.get()
            b7 = b6.b9
            b8 = b6.dist
            for neighbor in b5[b7]:
                if b8 + neighbor.dist < distance[neighbor.b9]:
                    distance[neighbor.b9] = b8 + neighbor.dist
                    b4.put(class2(neighbor.b9, distance[neighbor.b9]))
    b12, m, k, b19 = map(int, input().split())
    b20 = list(map(int, input().split()))
    b5 = [[] for _ in range(b12 + 1)]
    for i in range(m):
        b7, b26, b21 = map(int, input().split())
        b5[b7].append(class2(b26, b21))
        b5[b26].append(class2(b7, b21))
    a, b22 = map(int, input().split())
    b23 = [b1 for _ in range(b12 + 1)]
    fonk9(a, b23, b5)
    b24 = [b1 for _ in range(b12 + 1)]
    fonk9(b22, b24, b5)
    a2 = b1
    for i in range(k):
        if b24[b20[i]] <= b19:
            a2 = min(a2, b23[b20[i]] + b24[b20[i]])
    if a2 < b1:
        print(a2)
    else:
        print(-1)
def fonk10():
    def fonk11(s, distance, b5):
        b4 = queue.Queue()
        b4.put(s)
        distance[s] = 0
        while not b4.empty():
            b7 = b4.get()
            for neighbor in b5[b7]:
                if distance[neighbor] == b1:
                    distance[neighbor] = distance[b7] + 1
                    b4.put(neighbor)
    b25 = int(input())
    for a1 in range(b25):
        b12 = int(input())
        b5 = [[] for _ in range(b12)]
        b15 = int(input())
        for i in range(b15):
            b7, b26 = map(int, input().split())
            b5[b7].append(b26)
            b5[b26].append(b7)
        s, b21 = map(int, input().split())
        b27 = [b1 for _ in range(b12)]
        b28 = [b1 for _ in range(b12)]
        fonk11(s, b27, b5)
        fonk11(b21, b28, b5)
        a3 = 0
        for i in range(b12):
            if b27[i] != b1 and b28[i] != b1:
                a3 = max(a3, b27[i] + b28[i])
        print('Case {}: {}'.format(a1 + 1, a3))
