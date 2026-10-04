class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.a1 = 0
        self.b2 = {i: [] for i in range(b1)}
    def fonk2(self, vertex):
        return vertex in self.b2
    def fonk3(self):
        return list(self.b2.keys())
    def fonk4(self, vertex):
        if self.fonk2(vertex):
            return self.b2[vertex]
        return False
    def fonk5(self, vertex1, vertex2):
        if self.fonk2(vertex1):
            return vertex2 in self.b2[vertex1]
        return False
    def fonk6(self, vertex1, vertex2):
        if not self.fonk5(vertex1, vertex2):
            self.b2[vertex1].append(vertex2)
            self.b2[vertex2].append(vertex1)
            self.a1 += 1
            return True
        return False
    def fonk7(self):
        return self.b1
    def fonk8(self):
        return self.a1
    def fonk9(self, vertex):
        if self.fonk2(vertex):
            return len(self.b2[vertex])
        return False