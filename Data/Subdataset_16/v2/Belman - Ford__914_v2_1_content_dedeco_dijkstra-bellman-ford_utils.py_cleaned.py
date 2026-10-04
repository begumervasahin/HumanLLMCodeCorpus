import sys
def fonk1(g, s):
    for v in g.fonk16():
        v.fonk6(float('inf'))
    g.fonk15(s).fonk6(0)
def fonk2(b9):
    b1 = min(b9, key=lambda v: v.fonk7())
    b9.remove(b1)
    return b1
def fonk3(b10, v):
    if v.fonk7() > b10.fonk7() + b10.fonk12(v):
        v.fonk6(b10.fonk7() + b10.fonk12(v))
        v.fonk8(b10)
def fonk4(v, b11):
    if v.fonk9():
        b11.append(v.fonk9().fonk10())
        fonk4(v.fonk9(), b11)
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
if b7 = = "__main__":
    b8 = class2()
    b6 = ['a', 'b', 'c', 'd', 'e']
    for vertice in b6:
        b8.fonk14(vertice)
    b8.fonk15('a').fonk11(b8.fonk15('b'), 10)
    b8.fonk15('a').fonk11(b8.fonk15('c'), 3)
    b8.fonk15('b').fonk11(b8.fonk15('d'), 2)
    b8.fonk15('c').fonk11(b8.fonk15('b'), 4)
    b8.fonk15('c').fonk11(b8.fonk15('d'), 8)
    b8.fonk15('c').fonk11(b8.fonk15('e'), 2)
    b8.fonk15('d').fonk11(b8.fonk15('e'), 7)
    b8.fonk15('e').fonk11(b8.fonk15('d'), 9)
    fonk1(b8, 'a')
    b9 = list(b8.fonk16())
    while b9:
        b10 = fonk2(b9)
        for v in b10.b5:
            fonk3(b10, v)
    for v in b8.fonk16():
        b11 = [v.fonk10()]
        fonk4(v, b11)
        print(f'O menor b11 é: {b11[::-1]} com custo {v.fonk7()}.')