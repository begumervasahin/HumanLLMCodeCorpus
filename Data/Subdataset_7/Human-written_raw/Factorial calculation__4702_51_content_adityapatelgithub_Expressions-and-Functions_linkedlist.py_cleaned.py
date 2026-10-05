class class1:
    class class2:
        b1 = "b2","b3"
        def fonk1(self, v, n):
            self.b2 = v
            self.b3 = n
    def fonk2(self):
        self.b4 = None
        self.b5 = None
        self.a1 = 0
    def fonk3(self):
        b6 = self.b5
        while (b6 is not None):
            yield b6.b2
            b6 = b6.b3
    def fonk4(self):
        return self.a1
    def fonk5(self):
        return "".join( list(iter(self)))
    def fonk6(self,value):
        b7 = self.class2(value, None)
        if(self.b5 is None):
            self.b5 = self.b4 = b7
        else:
            b7.b3 = self.b5
            self.b5 = b7
        self.a1+=1
    def fonk7(self):
        b8 = self.b5.b2
        self.b5 = self.b5.b3
        self.a1-=1
        return b8
    def fonk8(self):
        return self.b4.b2
    def fonk9(self):
        return (self.a1 = = 0)