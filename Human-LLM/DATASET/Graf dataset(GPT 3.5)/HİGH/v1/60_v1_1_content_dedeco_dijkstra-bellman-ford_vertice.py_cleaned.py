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
    b7 = class1('A')
    b8 = class1('B')
    b9 = class1('C')
    b7.fonk3(b8, 10)
    b7.fonk3(b9, 5)
    print("Vertex ID:", b7.fonk2())
    print("Adjacent Vertices:", b7.fonk4())
    print("Distance:", b7.fonk5())
    b7.fonk6(20)
    print("Updated Distance:", b7.fonk5())
    b7.fonk7()
    print("Visited:", b7.fonk8())
    print("Weight to Vertex B:", b7.fonk9(b8))
    b7.fonk10(b9)
    print("Previous Vertex:", b7.fonk11())
    print("Vertex Details:", b7)