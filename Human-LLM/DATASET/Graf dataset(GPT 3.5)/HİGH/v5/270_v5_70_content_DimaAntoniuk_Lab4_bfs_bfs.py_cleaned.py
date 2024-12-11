import queue
def fonk1(a, b):
    return max(a, b)
def fonk2(b4, b7, b6):
    with open('output.txt', 'w') as output_file:
        output_file.write(str(b4[b7]) + '\n')
        b1 = b7
        output_file.write(str(b7) + ' ')
        while b6[b1] != -1:
            output_file.write(str(b6[b1] + 1) + ' ')
            b1 = b6[b1]
def fonk3(b12, b9):
    b2 = queue.Queue()
    b2.put(b9)
    b3 = len(b12)
    b4 = [-1] * b3
    b5 = [False] * b3
    b6 = [None] * b3
    b4[b9] = 0
    b5[b9] = True
    b6[b9] = -1
    while not b2.empty():
        b1 = b2.get()
        for neighbor in b12[b1]:
            if not b5[neighbor]:
                b5[neighbor] = True
                b4[neighbor] = b4[b1] + 1
                b6[neighbor] = b1
                b2.put(neighbor)
    b7 = b9
    for b1 in range(b3):
        if b4[b1] > b4[b7]:
            b7 = b1
    fonk2(b4, b7, b6)
if b8 = = "__main__":
    with open('input.txt', 'r') as input_file:
        num_edges, b9 = map(int, input_file.readline().split())
        b9 -= 1
        b3 = 0
        b10 = []
        for _ in range(num_edges):
            from_node, b11 = map(int, input_file.readline().split())
            b10.append((from_node, b11))
            b3 = fonk1(b3, fonk1(b10[-1][0], b10[-1][1]))
        b12 = [[] for _ in range(b3)]
        for from_node, b11 in b10:
            b12[from_node - 1].append(b11 - 1)
    fonk3(b12, b9)