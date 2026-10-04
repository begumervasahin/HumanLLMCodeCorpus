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
        b7, b6 = i, i
        for _ in range(degree
            b7 = (b7 + 1) % num_vertices
            b6 = (b6 - 1) % num_vertices
            if b7 > i:
                b8 = random.randint(0, 100)
                b3[b5[i]].fonk2(b5[b7], b8)
                b3[b5[b7]].fonk2(b5[i], b8)
                b4.append((min(b5[i], b5[b7]),
                              max(b5[i], b5[b7]),
                              b8))
            if b6 > i:
                b8 = random.randint(0, 100)
                b3[b5[i]].fonk2(b5[b6], b8)
                b3[b5[b6]].fonk2(b5[i], b8)
                b4.append((min(b5[i], b5[b6]),
                              max(b5[i], b5[b6]),
                              b8))
    with open('./b4.txt', 'a') as file:
        for edge in b4:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
    return b3
fonk5(5000, 6)
fonk5(5000, 1000)