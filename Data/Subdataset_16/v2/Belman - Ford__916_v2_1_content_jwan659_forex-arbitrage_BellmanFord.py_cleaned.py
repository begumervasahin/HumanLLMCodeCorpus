class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = float('inf')
        self.b3 = None
    def fonk2(self, dist):
        self.b2 = dist
    def fonk3(self):
        return self.b2
    def fonk4(self, vertex):
        self.b3 = vertex
    def fonk5(self):
        return self.b3
    def fonk6(self):
        return self.b1
if b4 = = "__main__":
    b5 = class1('A')
    b6 = class1('B')
    b7 = class1('C')
    b5.fonk2(0)
    b6.fonk2(10)
    b7.fonk2(20)
    b6.fonk4(b5)
    b7.fonk4(b6)
    print(f"class1 {b5}: Min Distance -> {b5.fonk3()}")
    print(f"class1 {b6}: Min Distance -> {b6.fonk3()}, Previous class1 -> {b6.fonk5()}")
    print(f"class1 {b7}: Min Distance -> {b7.fonk3()}, Previous class1 -> {b7.fonk5()}")