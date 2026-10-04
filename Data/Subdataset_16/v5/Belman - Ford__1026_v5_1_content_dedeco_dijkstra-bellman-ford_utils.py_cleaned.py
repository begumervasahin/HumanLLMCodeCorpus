def fonk1(graph, source):
    for vertex in graph.fonk16():
        vertex.fonk6(float('inf'))
    graph.fonk15(source).fonk6(0)
def fonk2(b8):
    b1 = min(b8, key=lambda v: v.fonk7())
    b8.remove(b1)
    return b1
def fonk3(b9, v):
    if v.fonk7() > b9.fonk7() + b9.fonk12(v):
        v.fonk6(b9.fonk7() + b9.fonk12(v))
        v.fonk8(b9)
def fonk4(v, b10):
    if v.fonk9():
        b10.append(v.fonk9().fonk10())
        fonk4(v.fonk9(), b10)
    return
class class1:
    def fonk5(self, b2):
        self.b2 = b2
        self.b3 = float('inf')
        self.b4 = None
        self.b5 = {}
    def fonk6(self, b3):
        self.b3 = b3
    def fonk7(self):
        return self.b3
    def fonk8(self, b4):
        self.b4 = b4
    def fonk9(self):
        return self.b4
    def fonk10(self):
        return self.b2
    def fonk11(self, destino, peso):
        self.b5[destino] = peso
    def fonk12(self, destino):
        return self.b5[destino]
class class2:
    def fonk13(self):
        self.b6 = {}
    def fonk14(self, b2):
        self.b6[b2] = class1(b2)
    def fonk15(self, b2):
        return self.b6[b2]
    def fonk16(self):
        return self.b6.values()
def fonk17():
    b7 = class2()
    b6 = ['a', 'b', 'c', 'd', 'e']
    for vertice in b6:
        b7.fonk14(vertice)
    b5 = [
        ('a', 'b', 10),
        ('a', 'c', 3),
        ('b', 'd', 2),
        ('c', 'b', 4),
        ('c', 'd', 8),
        ('c', 'e', 2),
        ('d', 'e', 7),
        ('e', 'd', 9)
    ]
    for origem, destino, peso in b5:
        b7.fonk15(origem).fonk11(b7.fonk15(destino), peso)
    fonk1(b7, 'a')
    b8 = list(b7.fonk16())
    while b8:
        b9 = fonk2(b8)
        for v in b9.b5:
            fonk3(b9, v)
    for v in b7.fonk16():
        b10 = [v.fonk10()]
        fonk4(v, b10)
        print(f'O menor b10 é: {b10[::-1]} com custo {v.fonk7()}.')
if b11 = = "__main__":
    fonk17()