class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = False
    def fonk2(self):
        return self.b2
    def fonk3(self, b2):
        self.b2 = b2
    def fonk4(self):
        self.b3 = True
    def fonk5(self):
        return self.b3
class class2:
    def fonk6(self):
        self.b4 = {}
        self.b5 = []
    def fonk7(self, vertex_id):
        if vertex_id not in self.b4:
            self.b4[vertex_id] = class1(vertex_id)
    def fonk8(self, source, destination, weight):
        self.fonk7(source)
        self.fonk7(destination)
        self.b5.append((source, destination, weight))
    def fonk9(self):
        return self.b4.values()
    def fonk10(self):
        return [(self.b4[u], self.b4[v], weight) for u, v, weight in self.b5]
def fonk11(b6, source):
    for vertex in b6.fonk9():
        vertex.fonk3(float('inf'))
        vertex.b3 = False
    b6.b4[source].fonk3(0)
def fonk12(u, v, weight):
    if v.fonk2() > u.fonk2() + weight:
        v.fonk3(u.fonk2() + weight)
def fonk13(b6, source):
    fonk11(b6, source)
    for _ in range(len(b6.fonk9()) - 1):
        for u, v, weight in b6.fonk10():
            if not v.fonk5():
                fonk12(u, v, weight)
    for u, v, weight in b6.fonk10():
        if v.fonk2() > u.fonk2() + weight:
            return False
    return True
b6 = class2()
b6.fonk8('A', 'B', -1)
b6.fonk8('A', 'C', 4)
b6.fonk8('B', 'C', 3)
b6.fonk8('B', 'D', 2)
b6.fonk8('B', 'E', 2)
b6.fonk8('D', 'C', 5)
b6.fonk8('D', 'B', 1)
b6.fonk8('E', 'D', -3)
b7 = not fonk13(b6, 'A')
print("class2 contains negative-weight cycle:", b7)