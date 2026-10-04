import queue
def fonk1(a, b):
    return a if a >= b else b
def fonk2(dist, b7, b6):
    with open('output.txt', 'w') as output_file:
        output_file.write(f"{dist}\n")
        b1 = b7
        b2 = []
        while b1 != -1:
            b2.append(b1 + 1)
            b1 = b6[b1]
        output_file.write(' '.join(map(str, b2[::-1])) + '\n')
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
        for neighbor in b11[b1]:
            if not b5[neighbor]:
                b5[neighbor] = True
                b4[neighbor] = b4[b1] + 1
                b6[neighbor] = b1
                b3.put(neighbor)
    b7 = b4.index(fonk1(b4))
    fonk2(b4[b7], b7, b6)
def fonk4(filename):
    with open(filename, 'r') as input_file:
        edges, b8 = map(int, input_file.readline().split())
        b8 -= 1
        a1 = 0
        b9 = []
        for _ in range(edges):
            f, b10 = map(int, input_file.readline().split())
            b9.append((f - 1, b10 - 1))
            a1 = fonk1(a1, fonk1(f, b10))
        b11 = [[] for _ in range(a1)]
        for f, b10 in b9:
            b11[f].append(b10)
    return b11, b8, a1
if b12 = = "__main__":
    b11, b8, a1 = fonk4('input.txt')
    fonk3(b11, b8, a1)