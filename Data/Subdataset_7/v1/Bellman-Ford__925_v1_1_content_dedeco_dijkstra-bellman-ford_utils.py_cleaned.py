import sys
class class1:
    def fonk1(self, id):
        self.b1 = id
        self.b2 = sys.maxsize
        self.b3 = None
        self.b4 = {}
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self, distancia):
        self.b2 = distancia
    def fonk5(self):
        return self.b3
    def fonk6(self, anterior):
        self.b3 = anterior
    def fonk7(self):
        return self.b4
    def fonk8(self, vertice, peso):
        self.b4[vertice] = peso
class class2:
    def fonk9(self):
        self.b5 = {}
    def fonk10(self):
        return self.b5.values()
    def fonk11(self, id):
        return self.b5.get(id)
    def fonk12(self, id):
        if id not in self.b5:
            self.b5[id] = class1(id)
    def fonk13(self, start, end, peso):
        if start in self.b5 and end in self.b5:
            self.b5[start].fonk8(self.b5[end], peso)
def fonk14(b8, s):
    for v in b8.fonk10():
        v.fonk4(sys.maxsize)
    b8.fonk11(s).fonk4(0)
def fonk15(b11):
    b6 = b11[0]
    for v in b11:
        if v.fonk3() < b6.fonk3():
            b6 = v
    b11.remove(b6)
    return b6
def fonk16(b12, v):
    if v.fonk3() > b12.fonk3() + b12.fonk7()[v]:
        v.fonk4(b12.fonk3() + b12.fonk7()[v])
        v.fonk6(b12)
def fonk17(v, b14):
    if v.fonk5():
        b14.append(v.fonk5().fonk2())
        fonk17(v.fonk5(), b14)
    return b14
if b7 = = "__main__":
    b8 = class2()
    b9 = ['a', 'b', 'c', 'd', 'e']
    for vertex in b9:
        b8.fonk12(vertex)
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
        b8.fonk13(*edge)
    fonk14(b8, 'a')
    b11 = b8.fonk10()
    while b11:
        b12 = fonk15(b11)
        for v in b12.fonk7():
            fonk16(b12, v)
    for vertex in b8.fonk10():
        b13 = [vertex.fonk2()]
        b14 = fonk17(vertex, b13)
        print(f'The shortest b13 from a to {vertex.fonk2()} is: {b14[::-1]} with cost {vertex.fonk3()}.')