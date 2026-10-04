import queue
def fonk1(a, b):
    return a if a >= b else b
def fonk2(dist, b7, parents):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        b1 = b7
        b2 = []
        while b1 != -1:
            b2.append(b1 + 1)
            b1 = parents[b1]
        output.write(' '.join(map(str, b2[::-1])))
def fonk3(b11, b8, a1):
    b3 = queue.Queue()
    b3.put(b8)
    b4 = [-1] * a1
    b5 = [False] * a1
    b6 = [None] * a1
    b4[b8] = 0
    b5[b8] = True
    b6[b8] = -1
    while not b3.empty():
        b1 = b3.get()
        for to in b11[b1]:
            if not b5[to]:
                b5[to] = True
                b4[to] = b4[b1] + 1
                b6[to] = b1
                b3.put(to)
    b7 = b8
    for b1 in range(a1):
        if b4[b1] > b4[b7]:
            b7 = b1
    fonk2(b4[b7], b7, b6)
def fonk4():
    with open('input.txt', 'r') as input:
        edges, b8 = map(int, input.readline().split())
        b8 = b8 - 1
        a1 = 0
        b9 = []
        for i in range(edges):
            f, b10 = map(int, input.readline().split())
            b9.append((f - 1, b10 - 1))
            a1 = fonk1(a1, fonk1(f, b10))
        a1 += 1
        b11 = [[] for _ in range(a1)]
        for f, b10 in b9:
            b11[f].append(b10)
    fonk3(b11, b8, a1)
if b12 = = "__main__":
    fonk4()