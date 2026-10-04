import random
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, connection):
        self.b2.append(connection)
    def fonk3(self, connection):
        if connection in self.b2:
            self.b2.remove(connection)
    def fonk4(self, target_vertex):
        return any(connection[0] == target_vertex for connection in self.b2)
def fonk5(num_vertices, degree):
    b3 = [class1(i) for i in range(num_vertices)]
    b4 = []
    b5 = list(range(num_vertices))
    random.shuffle(b5)
    for i in range(num_vertices):
        b6 = b5[i]
        for k in range(degree
            b7 = (i + k + 1) % num_vertices
            b8 = b5[b7]
            b9 = random.randint(0, 100)
            b3[b6].fonk2([b8, b9])
            b3[b8].fonk2([b6, b9])
            b10 = sorted([b6, b8]) + [b9]
            b4.append(b10)
            b11 = (i - k - 1) % num_vertices
            b12 = b5[b11]
            b9 = random.randint(0, 100)
            b3[b6].fonk2([b12, b9])
            b3[b12].fonk2([b6, b9])
            b10 = sorted([b6, b12]) + [b9]
            b4.append(b10)
    with open('b4.txt', 'a') as file:
        for b10 in b4:
            file.write(f"{b10[0]} {b10[1]} {b10[2]}\n")
    return b3
fonk5(5000, 6)
fonk5(5000, 1000)