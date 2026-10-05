class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = None
    def fonk2(self, distance):
        self.b2 = distance
    def fonk3(self):
        return self.b2
    def fonk4(self, b12):
        self.b3 = b12
    def fonk5(self):
        return self.b1
class class2:
    def fonk6(self, b4, b5, b6):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
    def fonk7(self):
        return self.b4
    def fonk8(self):
        return self.b5
    def fonk9(self):
        return self.b6
class class3:
    def fonk10(self, b7, b8):
        self.b7 = b7
        self.b8 = b8
        self.b9 = []
    def fonk11(self, src_name):
        for b12 in self.b7:
            if b12.b1 = = src_name:
                return b12
        return None
    def fonk12(self, src_name):
        b10 = self.fonk11(src_name)
        if not b10:
            print("Source b12 not found!")
            return
        b10.fonk2(0)
        for _ in range(len(self.b7) - 1):
            for edge in self.b8:
                if edge.fonk7().fonk3() == float('inf'):
                    continue
                b11 = edge.fonk7().fonk3() + edge.fonk9()
                if b11 < edge.fonk8().fonk3():
                    edge.fonk8().fonk2(b11)
                    edge.fonk8().fonk4(edge.fonk7())
        for edge in self.b8:
            if edge.fonk7().fonk3() != float('inf'):
                if self.fonk13(edge):
                    self.fonk14(edge)
                    return
    def fonk13(self, edge):
        return edge.fonk8().fonk3() > edge.fonk7().fonk3() + edge.fonk9()
    def fonk14(self, edge):
        b12 = edge.fonk7()
        while b12 != edge.fonk8():
            self.b9.append(b12)
            b12 = b12.get_previous_vertex()
        self.b9.append(edge.fonk8())
    def fonk15(self):
        if self.b9:
            print("An arbitrage opportunity has been detected:")
            for b12 in self.b9:
                print(b12)
        else:
            print("No arbitrage opportunity!")
if b13 = = "__main__":
    b14 = class1('A')
    b15 = class1('B')
    b16 = class1('C')
    b17 = class2(b14, b15, 10)
    b18 = class2(b15, b16, 5)
    b19 = class2(b16, b14, -15)
    b20 = [b14, b15, b16]
    b21 = [b17, b18, b19]
    b22 = class3(b20, b21)
    b22.fonk12('A')
    b22.fonk15()