class class1:
    def fonk1(self, id):
        self.b1 = id
        self.b2 = {}
        self.a1 = 0
        self.b3 = False
        self.b4 = None
    def fonk2(self):
        return self.b1
    def fonk3(self, b5 = None, peso=0):
        self.b2[b5] = peso
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.a1
    def fonk6(self, distancia):
        self.a1 = distancia
    def fonk7(self):
        self.b3 = True
    def fonk8(self):
        return self.b3
    def fonk9(self, b5):
        return self.b2[b5]
    def fonk10(self, anterior):
        self.b4 = anterior
    def fonk11(self):
        return self.b4
    def fonk12(self):
        return str(self.b1)
if b6 = = "__main__":
    b7 = class1('b7')
    b8 = class1('b8')
    b9 = class1('b9')
    b7.fonk3(b8, 5)
    b7.fonk3(b9, 10)
    b8.fonk3(b9, 2)
    b7.fonk6(0)
    b8.fonk6(5)
    b9.fonk6(7)
    b7.fonk7()
    b8.fonk10(b7)
    b9.fonk10(b8)
    print(f"class1 {b7}: Adjacentes -> {b7.fonk4()}, Distancia -> {b7.fonk5()}")
    print(f"class1 {b8}: Adjacentes -> {b8.fonk4()}, Distancia -> {b8.fonk5()}, Anterior -> {b8.fonk11()}")
    print(f"class1 {b9}: Adjacentes -> {b9.fonk4()}, Distancia -> {b9.fonk5()}, Anterior -> {b9.fonk11()}")