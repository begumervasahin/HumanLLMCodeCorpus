class class1:
    def fonk1(self,b1 = None,b2=None):
        self.b1 = b1
        self.b2 = b2
class class2:
    def fonk2(self):
        self.b3 = None
        self.b4 = None
    def fonk3(self,x,pos):
        b5 = class1(x)
        b5.b2 = pos.b2
        pos.b2 = b5
    def fonk4(self,x):
        if self.b3 = =None:
            b5 = class1(x)
            self.b3 = b5
            self.b4 = b5
        else:
            b5 = class1(x)
            self.b4.b2 = b5
            self.b4 = b5
    def fonk5(self,x):
        b6 = self.b3
        while b6.b2 != None and b6.b1!=x:
            b6 = b6.b2
        if b6.b2 = = None and b6.b1 != x:
            return False
        else:
            return b6
    def fonk6(self):
        b6 = self.b3
        while b6:
            fonk6(b6.b1.task_no)
            b6 = b6.b2
    def fonk7(self,x):
        if self.b3 = =None:
            b5 = class1(x)
            self.b3 = b5
            self.b4 = b5
        else:
            b6 = self.b3
            if b6.b1.cpu>x.cpu:
                b7 = class1(x)
                self.b3 = b7
                b7.b2 = b6
                return
            while b6.b2 !=None and b6.b2.b1.cpu<x.cpu:
                b6 = b6.b2
            b7 = class1(x)
            if b6.b2 = =None:
                b6.b2 = b7
                self.b4 = b7
                return
            b5 = b6.b2
            b6.b2 = b7
            b7.b2 = b5
    def fonk8(self):
        b8 = None
        b7 = None
        b6 = self.b3.b2
        while b6:
            b7 = b6.b2
            b6.b2 = b8
            b8 = b6
            b6 = b7
        self.b3.b2 = b8
        self.fonk6()
    def fonk9(self,x):
        if self.b3 = =None:
            b5 = class1(x)
            self.b3 = b5
            self.b4 = b5
        else:
            b5 = class1(x)
            b5.b2 = self.b3
            self.b3 = b5
    def fonk10(self):
        if self.b3 = =None:
            fonk6("empty")
            return
        if self.b3.b2 = =None:
            b5 = self.b3
            self.b3 = None
            self.b4 = None
            return b5
        else:
            b5 = self.b3
            self.b3 = self.b3.b2
            b5.b2 = None
            return b5
def fonk11():
    b9 = class2()
    '''b9.fonk9(8)
    b9.fonk9(6)
    b9.fonk9(5)'''
    b9.fonk9(1)
    b9.fonk7(3)
    b9.fonk6()
    fonk6("b4",b9.b4.b1)
    b9.fonk10()
    b9.fonk10()
    b9.fonk10()
    b9.fonk10()
    b9.fonk10()
if b10 = ="__main__":
    fonk11()