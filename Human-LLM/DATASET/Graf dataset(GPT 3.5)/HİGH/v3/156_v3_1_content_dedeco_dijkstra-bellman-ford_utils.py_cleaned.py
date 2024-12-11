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
def fonk14(b9, source):
    for vertex in b9.fonk10():
        vertex.fonk4(sys.maxsize)
    b9.fonk11(source).fonk4(0)
def fonk15(b11):
    b6 = min(b11, key=lambda vertex: vertex.fonk3())
    b11.remove(b6)
    return b6
def fonk16(start_vertex, end_vertex):
    b7 = start_vertex.fonk3() + start_vertex.fonk7()[end_vertex]
    if end_vertex.fonk3() > b7:
        end_vertex.fonk4(b7)
        end_vertex.fonk6(start_vertex)
def fonk17(vertex, b13):
    if vertex.fonk5():
        b13.append(vertex.fonk5().fonk2())
        fonk17(vertex.fonk5(), b13)
    return b13
if b8 = = "__main__":
    b9 = class2()
    b5 = ['a', 'b', 'c', 'd', 'e']
    for vertex in b5:
        b9.fonk12(vertex)
    b10 = [
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
    for edge in b10:
        b9.fonk13(*edge)
    fonk14(b9, 'a')
    b11 = b9.fonk10()
    while b11:
        b12 = fonk15(b11)
        for v in b12.fonk7():
            fonk16(b12, v)
    for vertex in b9.fonk10():
        b13 = [vertex.fonk2()]
        b14 = fonk17(vertex, b13)
        print(f'The shortest b13 from a to {vertex.fonk2()} is: {b14[::-1]} with cost {vertex.fonk3()}.')