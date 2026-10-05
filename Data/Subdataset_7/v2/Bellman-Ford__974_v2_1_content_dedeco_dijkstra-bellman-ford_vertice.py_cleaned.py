class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
        self.a1 = 0
        self.b3 = False
        self.b4 = None
    def fonk2(self):
        return self.b1
    def fonk3(self, b5 = None, weight=0):
        self.b2[b5] = weight
    def fonk4(self):
        return self.b2.keys()
    def fonk5(self):
        return self.a1
    def fonk6(self, a1):
        self.a1 = a1
    def fonk7(self):
        self.b3 = True
    def fonk8(self):
        return self.b3
    def fonk9(self, b5):
        return self.b2[b5]
    def fonk10(self, b4):
        self.b4 = b4
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
    print("class1 ID:", b7.fonk2())
    print("Adjacent Vertices:", b7.fonk4())
    print("Distance:", b7.fonk5())
    b7.fonk6(20)
    print("Updated Distance:", b7.fonk5())
    b7.fonk7()
    print("Visited:", b7.fonk8())
    print("Weight to class1 B:", b7.fonk9(b8))
    b7.fonk10(b9)
    print("Previous class1:", b7.fonk11())
    print("class1 Details:", b7)