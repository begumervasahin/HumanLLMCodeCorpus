import queue
def fonk1(a, b):
    return a if a >= b else b
def fonk2(distance, b8, b6):
    with open('output.txt', 'w') as output:
        output.write(f"{distance}\n")
        b1 = []
        b2 = b8
        while b2 != -1:
            b1.append(b2 + 1)
            b2 = b6[b2]
        output.write(' '.join(map(str, b1[::-1])))
def fonk3(b12, start, a1):
    b3 = queue.Queue()
    b3.put(start)
    b4 = [-1] * a1
    b5 = [False] * a1
    b6 = [None] * a1
    b4[start] = 0
    b5[start] = True
    b6[start] = -1
    while not b3.empty():
        b7 = b3.get()
        for neighbor in b12[b7]:
            if not b5[neighbor]:
                b5[neighbor] = True
                b4[neighbor] = b4[b7] + 1
                b6[neighbor] = b7
                b3.put(neighbor)
    b8 = start
    for b2 in range(a1):
        if b4[b2] > b4[b8]:
            b8 = b2
    fonk2(b4[b8], b8, b6)
def fonk4():
    with open('input.txt', 'r') as input_file:
        edges, b9 = map(int, input_file.readline().split())
        b9 -= 1
        a1 = 0
        b10 = []
        for _ in range(edges):
            from_node, b11 = map(int, input_file.readline().split())
            b10.append((from_node - 1, b11 - 1))
            a1 = fonk1(a1, fonk1(from_node, b11))
        a1 += 1
        b12 = [[] for _ in range(a1)]
        for from_node, b11 in b10:
            b12[from_node].append(b11)
    fonk3(b12, b9, a1)
if b13 = = "__main__":
    fonk4()