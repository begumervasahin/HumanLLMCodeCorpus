class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertex):
        self.b1[vertex] = vertex
        self.b2[vertex] = 0
    def fonk3(self, vertex):
        if self.b1[vertex] != vertex:
            self.b1[vertex] = self.fonk3(self.b1[vertex])
        return self.b1[vertex]
    def fonk4(self, vertex1, vertex2):
        b3 = self.fonk3(vertex1)
        b4 = self.fonk3(vertex2)
        if b3 != b4:
            if self.b2[b3] < self.b2[b4]:
                self.b1[b3] = b4
            else:
                self.b1[b4] = b3
                if self.b2[b3] == self.b2[b4]:
                    self.b2[b3] += 1
class class2:
    def fonk5(self, b5, b6):
        self.b5 = b5
        self.b6 = sorted(b6, key=lambda x: x[2])
        self.b7 = []
        self.a1 = 0
        self.b8 = class1()
    def fonk6(self):
        for vertex in self.b5:
            self.b8.fonk2(vertex)
        for v1, v2, weight in self.b6:
            if self.b8.fonk3(v1) != self.b8.fonk3(v2):
                self.b8.fonk4(v1, v2)
                self.a1 += weight
                self.b7.append((v1, v2, weight, self.a1))
    def fonk7(self):
        print("******************************************************************************")
        print(f"{'Vertex 1':<15}{'Vertex 2':<15}{'Distance':<10}{'Cumulative Distance':<20}")
        print("******************************************************************************")
        for v1, v2, weight, cum_dist in self.b7:
            print(f"{v1:<15}{v2:<15}{weight:<10}{cum_dist:<20}")
if b9 = = "__main__":
    b5 = {'A', 'B', 'C', 'D', 'E'}
    b6 = [
        ('A', 'B', 1),
        ('A', 'C', 3),
        ('B', 'C', 2),
        ('B', 'D', 6),
        ('C', 'D', 4),
        ('C', 'E', 2),
        ('D', 'E', 5)
    ]
    b10 = class2(b5, b6)
    b10.fonk6()
    b10.fonk7()