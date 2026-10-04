class class1:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, vertice):
        self.b1[vertice] = vertice
        self.b2[vertice] = 0
    def fonk3(self, vertice):
        if self.b1[vertice] != vertice:
            self.b1[vertice] = self.fonk3(self.b1[vertice])
        return self.b1[vertice]
    def fonk4(self, vertice1, vertice2):
        b3 = self.fonk3(vertice1)
        b4 = self.fonk3(vertice2)
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
        for vertice in self.b5:
            self.b8.fonk2(vertice)
        for edge in self.b6:
            v1, v2, b9 = edge
            if self.b8.fonk3(v1) != self.b8.fonk3(v2):
                self.b8.fonk4(v1, v2)
                self.a1 += b9
                self.b7.append((v1, v2, b9, self.a1))
    def fonk7(self):
        b10 = f"{'Vertex 1':<15}{'Vertex 2':<15}{'Distance':<10}{'Cumulative Distance':<20}"
        print("******************************************************************************")
        print(b10)
        print("******************************************************************************")
        for v1, v2, b9, cum_dist in self.b7:
            print(f"{v1:<15}{v2:<15}{b9:<10}{cum_dist:<20}")
if b11 = = "__main__":
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
    b12 = class2(b5, b6)
    b12.fonk6()
    b12.fonk7()