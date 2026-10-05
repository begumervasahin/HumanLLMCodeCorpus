import queue
def fonk1(a, b):
    if a >= b:
        return a
    else:
        return b
def fonk2(distance, b6, b5):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(distance) + '\n')
        b1 = b6
        output_file.write(str(b6) + ' ')
        while b5[b1] != -1:
            output_file.write(str(b5[b1] + 1) + ' ')
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
    num_edges, b7 = map(int, input_file.readline().split())
    b7 -= 1
    a1 = 0
    b8 = []
    for _ in range(num_edges):
        from_node, b9 = map(int, input_file.readline().split())
        b8.append((from_node, b9))
        a1 = fonk1(a1, fonk1(b8[-1][0], b8[-1][1]))
    b10 = [[] for _ in range(a1)]
    for from_node, b9 in b8:
        b10[from_node - 1].append(b9 - 1)
fonk3(b10, b7)