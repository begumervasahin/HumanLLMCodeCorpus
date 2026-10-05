70. Repository: DimaAntoniuk/Lab4_bfs
   File: bfs.py
   URL: https:
   Code Content:
import queue
def fonk1(a, b):
    if(a >= b):
        return a
    else:
        return b
def fonk2(dist, b4, parents):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        b1 = b4
        output.write(str(b4) + ' ')
        while parents[b1] != -1:
            output.write(str(parents[b1] + 1) + ' ')
            b1 = parents[b1]
def fonk3(b8, b5):
    b2 = queue.Queue()
    b2.put(b5)
    d, used, b3 = [-1]*a1, [False]*a1, [None]*a1
    d[b5] = 0
    used[b5] = True
    b3[b5] = -1
    while not b2.empty():
        b1 = b2.get()
        for to in b8[b1]:
            if not used[to]:
                used[to] = True
                d[to] = d[b1] + 1
                b3[to] = b1
                b2.put(to)
    b4 = b5
    for b1 in range(a1):
        if d[b1]>d[b4]:
            b4 = b1
    fonk2(d[b4], b4, b3)
with open('input.txt', 'r') as input:
    edges, b5 = map(int, input.readline().split())
    b5 = b5 - 1
    a1 = 0
    b6 = [] * edges
    for i in range(edges):
        f, b7 = map(int, input.readline().split())
        b6.append((f, b7))
        a1 = fonk1(a1, fonk1(b6[i][0], b6[i][1]))
    b8 = []
    for b1 in range(a1):
        b8.append([])
    for i in range(edges):
        b8[b6[i][0]-1].append(b6[i][1]-1)
fonk3(b8, b5)
   README Content:
