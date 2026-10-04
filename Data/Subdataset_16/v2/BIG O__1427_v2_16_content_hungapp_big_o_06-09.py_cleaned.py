import queue
b1 = int(1e9)
class class1:
    def fonk1(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
    def fonk2(self, other):
        return self.b3 <= other.b3
def fonk3(b13, b25, distances):
    b4 = queue.PriorityQueue()
    b4.put(class1(b25, 0))
    distances[b25] = 0
    while not b4.empty():
        b5 = b4.get()
        b6 = b5.b2
        b7 = b5.b3
        for neighbor in b13[b6]:
            if b7 + neighbor.b3 < distances[neighbor.b2]:
                distances[neighbor.b2] = b7 + neighbor.b3
                b4.put(class1(neighbor.b2, distances[neighbor.b2]))
def fonk4(b13, b25, distances):
    b8 = queue.Queue()
    b8.put(b25)
    distances[b25] = 0
    while not b8.empty():
        b6 = b8.get()
        for neighbor in b13[b6]:
            if distances[neighbor] == b1:
                distances[neighbor] = distances[b6] + 1
                b8.put(neighbor)
def fonk5():
    b9 = int(input())
    b10 = int(input())
    b11 = int(input())
    b12 = int(input())
    b13 = [[] for _ in range(b9 + 1)]
    b14 = [b1 for _ in range(b9 + 1)]
    for _ in range(b12):
        a, b30, b15 = map(int, input().split())
        b13[b30].append(class1(a, b15))
    fonk3(b13, b10, b14)
    b16 = sum(1 for i in range(1, b9 + 1) if b14[i] <= b11)
    print(b16)
def fonk6():
    b17 = int(input())
    for _ in range(b17):
        b9 = int(input())
        b13 = [[] for _ in range(b9 + 1)]
        b18 = []
        for i in range(b9):
            b19 = input().strip()
            b18.append(b19)
            b20 = int(input())
            for _ in range(b20):
                nr, b21 = map(int, input().split())
                b13[i + 1].append(class1(nr, b21))
        b22 = int(input())
        for _ in range(b22):
            b23 = [b1 for _ in range(b9 + 1)]
            source, b24 = input().split()
            b25 = b18.index(source) + 1
            b26 = b18.index(b24) + 1
            fonk3(b13, b25, b23)
            print(b23[b26])
        input()
def fonk7():
    b9, b12, k, b27 = map(int, input().split())
    b28 = list(map(int, input().split()))
    b13 = [[] for _ in range(b9 + 1)]
    for _ in range(b12):
        b6, b34, b29 = map(int, input().split())
        b13[b6].append(class1(b34, b29))
        b13[b34].append(class1(b6, b29))
    a, b30 = map(int, input().split())
    b31 = [b1 for _ in range(b9 + 1)]
    b32 = [b1 for _ in range(b9 + 1)]
    fonk3(b13, a, b31)
    fonk3(b13, b30, b32)
    b33 = min((b31[k] + b32[k] for k in b28 if b32[k] <= b27), default=b1)
    print(b33 if b33 < b1 else -1)
def fonk8():
    b11 = int(input())
    for b21 in range(b11):
        b9 = int(input())
        b13 = [[] for _ in range(b9)]
        b22 = int(input())
        for _ in range(b22):
            b6, b34 = map(int, input().split())
            b13[b6].append(b34)
            b13[b34].append(b6)
        s, b29 = map(int, input().split())
        b35 = [b1 for _ in range(b9)]
        b36 = [b1 for _ in range(b9)]
        fonk4(b13, s, b35)
        fonk4(b13, b29, b36)
        b37 = max(b35[i] + b36[i] for i in range(b9) if b35[i] != b1 and b36[i] != b1)
        print(f'Case {b21 + 1}: {b37}')
if b38 = = "__main__":
    b39 = int(input("Select problem to solve (1-4): "))
    if b39 = = 1:
        fonk5()
    elif b39 = = 2:
        fonk6()
    elif b39 = = 3:
        fonk7()
    elif b39 = = 4:
        fonk8()
    else:
        print("Invalid selection.")