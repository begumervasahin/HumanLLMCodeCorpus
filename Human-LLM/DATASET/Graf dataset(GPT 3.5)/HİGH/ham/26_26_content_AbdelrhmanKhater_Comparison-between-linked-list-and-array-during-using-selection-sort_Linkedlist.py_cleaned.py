class class1:
    def fonk1(self,initdata):
        self.b1 = initdata
        self.b2 = None
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self,newdata):
        self.b1 = newdata
    def fonk5(self,newnext):
        self.b2 = newnext
class class2:
    def fonk6(self):
        self.b3 = None
    def fonk7(self):
        return self.b3 = = None
    def fonk8(self,item):
        b4 = class1(item)
        b4.fonk5(self.b3)
        self.b3 = b4
    def fonk9(self):
        b5 = self.b3
        a1 = 0
        while b5 != None:
            a1 = a1 + 1
            b5 = b5.fonk3()
        return a1
    def fonk10(self,item):
        b5 = self.b3
        b6 = False
        while b5 != None and not b6:
            if b5.fonk2() == item:
                b6 = True
            else:
                b5 = b5.fonk3()
        return b6
    def fonk11(self,item):
        b5 = self.b3
        b7 = None
        b6 = False
        while not b6 and b5 != None:
            if b5.fonk2() == item:
               b6 = True
            else:
                b7 = b5
                b5 = b5.fonk3()
        if b7 = = None:
            self.b3 = b5.fonk3()
        else:
            b7.fonk5(b5.fonk3())
class class3:
    def fonk12(self):
        self.b3 = class1(None)
    def fonk13(self):
        return self.b3.fonk3() == None
    def fonk14(self,item):
        b4 = class1(item)
        b4.fonk5(self.b3.fonk3())
        self.b3.fonk5(b4)
    def fonk15(self):
        b5 = self.b3.fonk3()
        a1 = 0
        while b5 != None:
            a1 = a1 + 1
            b5 = b5.fonk3()
        return a1
    def fonk16(self,item):
        b5 = self.b3.fonk3()
        b6 = False
        while b5 != None and not b6:
            if b5.fonk2() == item:
                b6 = True
            else:
                b5 = b5.fonk3()
        return b6
    def fonk17(self,item):
        b5 = self.b3.fonk3()
        b7 = None
        b6 = False
        while not b6 and b5 != None:
            if b5.fonk2() == item:
               b6 = True
            else:
                b7 = b5
                b5 = b5.fonk3()
        if b7 = = None:
            self.b3 = b5.fonk3()
        else:
            b7.fonk5(b5.fonk3())