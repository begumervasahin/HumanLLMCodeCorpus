class class1:
    def fonk1(self,rootObj):
        self.b1 = rootObj
        self.b2 = None
        self.b3 = None
    def fonk2(self,newNode):
        if self.b2 = = None:
            self.b2 = class1(newNode)
        else:
            b4 = class1(newNode)
            b4.b2 = self.b2
            self.b2 = b4
    def fonk3(self,newNode):
        if self.b3 = = None:
            self.b3 = class1(newNode)
        else:
            b4 = class1(newNode)
            b4.b3 = self.b3
            self.b3 = b4
    def fonk4(self):
        return self.b3
    def fonk5(self):
        return self.b2
    def fonk6(self,obj):
        self.b1 = obj
    def fonk7(self):
        return self.b1
b5 = class1('a')
print(b5.fonk7())
print(b5.fonk5())
b5.fonk2('b')
print(b5.fonk5())
print(b5.fonk5().fonk7())
b5.fonk3('c')
print(b5.fonk4())
print(b5.fonk4().fonk7())
b5.fonk4().fonk6('hello')
print(b5.fonk4().fonk7())