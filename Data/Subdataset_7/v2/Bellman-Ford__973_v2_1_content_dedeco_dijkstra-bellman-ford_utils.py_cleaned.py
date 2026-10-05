import sys
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = sys.maxsize
        self.b3 = None
        self.b4 = {}
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, b2):
        self.b2 = b2
    def fonk5(self):
        return self.b3
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        return self.b4
    def fonk8(self, vertex, weight):
        self.b4[vertex] = weight
class class2:
    def fonk9(self):
        self.b5 = {}
    def fonk10(self):
        return self.b5.values()
    def fonk11(self, b1):
        return self.b5.get(b1)
    def fonk12(self, b1):
        if b1 not in self.b5:
            self.b5[b1] = class1(b1)
    def fonk13(self, start, end, weight):
        if start in self.b5 and end in self.b5:
            self.b5[start].fonk8(self.b5[end], weight)
def fonk14(b8, source):
    for vertex in b8.fonk10():
        vertex.fonk4(sys.maxsize)
    b8.fonk11(source).fonk4(0)
def fonk15(b10):
    b6 = b10[0]
    for vertex in b10:
        if vertex.fonk3() < b6.fonk3():
            b6 = vertex
    b10.remove(b6)
    return b6
def fonk16(start_vertex, end_vertex):
    if end_vertex.fonk3() > start_vertex.fonk3() + start_vertex.fonk7()[end_vertex]:
        end_vertex.fonk4(start_vertex.fonk3() + start_vertex.fonk7()[end_vertex])
        end_vertex.fonk6(start_vertex)
def fonk17(vertex, b12):
    if vertex.fonk5():
        b12.append(vertex.fonk5().fonk2())
        fonk17(vertex.fonk5(), b12)
    return b12
if b7 = = "__main__":
    b8 = class2()
    b5 = ['a', 'b', 'c', 'd', 'e']
    for vertex in b5:
        b8.fonk12(vertex)
    b9 = [
        ('a', 'b', 10),
        ('a', 'c', 3),
        ('b', 'c', 1),
        ('b', 'd', 2),
        ('c', 'b', 4),
        ('c', 'd', 8),
        ('c', 'e', 2),
        ('d', 'e', 7),
        ('e', 'd', 9)
    ]
    for edge in b9:
        b8.fonk13(*edge)
    fonk14(b8, 'a')
    b10 = b8.fonk10()
    while b10:
        b11 = fonk15(b10)
        for v in b11.fonk7():
            fonk16(b11, v)
    for vertex in b8.fonk10():
        b12 = [vertex.fonk2()]
        b13 = fonk17(vertex, b12)
        print(f'The shortest b12 from a to {vertex.fonk2()} is: {b13[::-1]} with cost {vertex.fonk3()}.')