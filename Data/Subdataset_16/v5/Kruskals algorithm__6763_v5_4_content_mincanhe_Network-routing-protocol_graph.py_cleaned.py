import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, target_vertex, b11):
        self.b2.append((target_vertex, b11))
    def fonk3(self, target_vertex):
        self.b2 = [
            connection for connection in self.b2
            if connection[0] != target_vertex
        ]
    def fonk4(self, target_vertex):
        return any(connection[0] == target_vertex for connection in self.b2)
def fonk5(num_vertices, degree):
    b3 = [class1(i) for i in range(num_vertices)]
    b4 = []
    b5 = list(range(num_vertices))
    random.shuffle(b5)
    for i in range(num_vertices):
        b6 = b5[i]
        for k in range(1, degree
            b7 = (i + k) % num_vertices
            b8 = b5[b7]
            fonk6(b3, b6, b8, b4)
            b9 = (i - k) % num_vertices
            b10 = b5[b9]
            fonk6(b3, b6, b10, b4)
    fonk7('b4.txt', b4)
    return b3
def fonk6(b3, vertex_a, vertex_b, b4):
    b11 = random.randint(0, 100)
    b3[vertex_a].fonk2(vertex_b, b11)
    b3[vertex_b].fonk2(vertex_a, b11)
    b4.append(sorted([vertex_a, vertex_b]) + [b11])
def fonk7(filename, b4):
    with open(filename, 'a') as file:
        for edge in b4:
            file.write(f"{edge[0]} {edge[1]} {edge[2]}\n")
fonk5(5000, 6)
fonk5(5000, 1000)