import queue
def fonk1(a, b):
    return a if a >= b else b
def fonk2(dist, b6, b5):
    with open('output.txt', 'w') as output:
        output.write(str(dist) + '\n')
        b1 = b6
        output.write(str(b6 + 1) + ' ')
        while b5[b1] != -1:
            output.write(str(b5[b1] + 1) + ' ')
            b1 = b5[b1]
def fonk3(b10, b7):
    b2 = queue.Queue()
    b2.put(b7)
    b3 = [-1] * a1
    b4 = [False] * a1
    b5 = [None] * a1
    b3[b7] = 0
    b4[b7] = True
    b5[b7] = -1
    while not b2.empty():
        b1 = b2.get()
        for neighbor in b10[b1]:
            if not b4[neighbor]:
                b4[neighbor] = True
                b3[neighbor] = b3[b1] + 1
                b5[neighbor] = b1
                b2.put(neighbor)
    b6 = b7
    for b1 in range(a1):
        if b3[b1] > b3[b6]:
            b6 = b1
    fonk2(b3[b6], b6, b5)
with open('input.txt', 'r') as input_file:
    edges, b7 = map(int, input_file.readline().split())
    b7 -= 1
    a1 = 0
    b8 = []
    for _ in range(edges):
        f, b9 = map(int, input_file.readline().split())
        b8.append((f, b9))
        a1 = fonk1(a1, fonk1(f, b9))
    b10 = [[] for _ in range(a1)]
    for f, b9 in b8:
        b10[f - 1].append(b9 - 1)
fonk3(b10, b7)