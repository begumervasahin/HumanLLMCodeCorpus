
class class1:
    def fonk1(self,b1):
        self.b1 = b1
        self.b2 = None
class class2:
    def fonk2(self):
        self.b3 = None
    def fonk3(self,new_data):
        b4 = class1(new_data)
        b4.b2 = self.b3
        self.b3 = b4
    def fonk4(self):
        b5 = self.b3
        while(b5):
            print(b5.b1)
            b5 = b5.b2
    def fonk5(self,n):
        b6 = self.b3
        b5 = self.b3
        a1 = 0
        if self.b3!=None:
            while(a1<n):
                if b6 is None:
                    return
                b6 = b6.b2
                a1+=1
        while b6 is not None:
            b5 = b5.b2
            b6 = b6.b2
        print(b5.b1)
b7 = class2()
b7.fonk3(6)
b7.fonk3(5)
b7.fonk3(4)
b7.fonk3(3)
b7.fonk3(2)
b7.fonk3(1)
b7.fonk4()
b7.fonk5(2)