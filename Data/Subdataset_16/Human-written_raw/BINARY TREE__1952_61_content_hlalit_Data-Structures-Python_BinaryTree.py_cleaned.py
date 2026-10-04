class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = None
        self.b5 = []
    def fonk3(self,b1):
        self.b5.append(b1)
        return
    def fonk4(self,b1,address,index):
        if(self.b4 = = None):
            b6 = class1(b1)
            b7 = b6
            self.b4 = b7
        else:
            b7 = address
        b8 = 2*index + 1
        b9 = 2*index + 2
        if(b8 < len(self.b5)):
            b10 = class1(self.b5[b8])
            b2 = self.b5[b8]
            b7.b2 = b10
            self.fonk4(b2,b10,b8)
        else:
            return
        if(b9 < len(self.b5)):
            b11 = class1(self.b5[b9])
            b3 = self.b5[b9]
            b7.b3 = b11
            self.fonk4(b3,b11,b9)
        else:
            return
    def fonk5(self,b7):
        if(b7 = = None):
            return
        else:
            self.fonk5(b7.b2)
            print(b7.b1)
            self.fonk5(b7.b3)
    def fonk6(self,b7):
        if(b7 = = None):
            return
        b12 = []
        b12.append(b7)
        while len(b12) > 0:
            print(b12[0].b1)
            b13 = b12.pop(0)
            if(b13.b2):
                b12.append(b13.b2)
            if(b13.b3):
                b12.append(b13.b3)
    def fonk7(self,b7):
        if(b7 = = None):
            return -1
        else:
            b14 = self.fonk7(b7.b2)
            b15 = self.fonk7(b7.b3)
            if(b14 > b15):
                return b14 + 1
            else:
                return b15 + 1
b16 = class2()
b16.fonk3(2)
b16.fonk3(3)
b16.fonk3(5)
b16.fonk3(7)
b16.fonk3(1)
b16.fonk3(10)
b16.fonk3(9)
b16.fonk3(8)
b16.fonk4(b16.b5[0],b16.b4,0)
b16.fonk5(b16.b4)
print()
b16.fonk6(b16.b4)
print()
b16.fonk7(b16.b4)
print()