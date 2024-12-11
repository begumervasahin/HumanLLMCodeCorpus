class class1(object):
    def fonk1(self, b2, b3, b4, b1 = 0, b5=False):
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b1 = b1
        self.b5 = b5
    def fonk2(self):
        return ("V1:  " + str(self.b2) + "  V2:  " +str(self.b3)+ "  W:  "+ str(self.b4)+ "  SEL:  "+ str(self.b5))
if b6 = = "__main__":
    b7 = class1(1, 2, 5)
    print(b7)
    b8 = class1(2, 3, 7, b1=2, b5=True)
    print(b8)