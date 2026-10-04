import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, vertex_label, b8):
        self.b2.append((vertex_label, b8))
    def fonk3(self, vertex_label):
        self.b2 = [conn for conn in self.b2 if conn[0] != vertex_label]
    def fonk4(self, vertex_label):
        return any(conn[0] == vertex_label for conn in self.b2)
def fonk5(num_vertices, degree):
    b3 = [class1(i) for i in range(num_vertices)]
    b4 = []
    b5 = list(range(num_vertices))
    random.shuffle(b5)
    for i in range(num_vertices):
        fonk6(b3, b5, i, num_vertices, degree, b4)
    fonk8(b4, './b4.txt')
    return b3
def fonk6(b3, b5, i, num_vertices, degree, b4):
    b7, b6 = i, i
    for _ in range(degree
        b7 = (b7 + 1) % num_vertices
        b6 = (b6 - 1) % num_vertices
        fonk7(b3, b5, i, b7, b4)
        fonk7(b3, b5, i, b6, b4)
def fonk7(b3, b5, i, neighbor_index, b4):
    if neighbor_index > i:
        b8 = random.randint(0, 100)
        b9 = b3[b5[i]]
        b10 = b3[b5[neighbor_index]]
        b9.fonk2(b5[neighbor_index], b8)
        b10.fonk2(b5[i], b8)
        b4.append((
            min(b5[i], b5[neighbor_index]),
            max(b5[i], b5[neighbor_index]),
            b8
        ))
def fonk8(b4, filename):
    with open(filename, 'a') as file:
        for edge in b4:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
fonk5(5000, 6)
fonk5(5000, 1000)