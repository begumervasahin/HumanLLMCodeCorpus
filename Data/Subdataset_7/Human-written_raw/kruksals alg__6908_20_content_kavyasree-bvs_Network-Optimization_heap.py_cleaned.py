class class1(object):
    def fonk1(self):
        super(class1, self).fonk1()
        self.b1 = [-1]
        self.b2 = [-1]
        self.a1 = 0
    def fonk2(self):
        return self.b1[1]
    def fonk3(self, name, value):
        self.a1 = self.a1+1
        self.b1.append(name)
        self.b2.append(value)
        self.fonk6(self.a1);
    def fonk4(self, name, value):
        print value
        print self.a1
    def fonk5(self, b5):
        if(self.a1 = = 1 or b5 == self.a1 ):
            b3 = self.b2.pop()
            b4 = self.b1.pop()
            self.a1 = self.a1-1
        else:
            self.b2[b5]=self.b2.pop()
            self.b1[b5]=self.b1.pop()
            self.a1 = self.a1-1
            self.fonk6(b5)
    def fonk6(self, k):
        if(k>1 and self.b2[k]>self.b2[k/2]):
            b5 = k;
            while(b5>1 and self.b2[b5]>self.b2[b5/2]):
                self.fonk7(b5,b5/2);
                b5 = b5/2;
        else:
            if(k <= self.a1/2 and ( ( (2*k+1) <= self.a1 and self.b2[k] < max(self.b2[2*k],self.b2[(2*k)+1]) )
                or ( 2*k+1 > self.a1 and self.b2[k] < self.b2[2*k] ) ) ):
                b5 = k
                while( b5 <= (self.a1)/2 and ( ( (2*b5+1) <= self.a1 and self.b2[b5] < max( self.b2[2*b5], self.b2[(2*b5)+1]) )
                    or ( 2*b5+1 > self.a1 and self.b2[b5] < self.b2[2*b5] )  ) ):
                    b6 = 2*b5
                    if((2*b5+1) <= self.a1 and self.b2[2*b5]<self.b2[(2*b5)+1]):
                        b6 = 2*b5 +1
                    self.fonk7(b5,b6);
                    b5 = b6
    def fonk7(self, b5,b6):
        b7 = self.b2[b5]
        self.b2[b5]=self.b2[b6]
        self.b2[b6]=b7
        b7 = self.b1[b5]
        self.b1[b5]=self.b1[b6]
        self.b1[b6]=b7
    def fonk8(self):
        b8 = []
        b9 = []
        while(self.a1 >= 1):
            b8.append(self.b1[1])
            b9.append(self.b2[1])
            self.fonk5(1)
        return [b9,b8]
'''
b10 = class1()
b10.fonk3(1,10)
print '\a1', b10.b1, b10.b2
b10.fonk3(2,30)
print '\a1', b10.b1, b10.b2
b10.fonk3(3,40)
print '\a1', b10.b1, b10.b2
b10.fonk3(4,15)
print '\a1', b10.b1, b10.b2
b10.fonk3(5,60)
print '\a1', b10.b1, b10.b2
print b10.fonk2()
b10.fonk5(1)
print '\a1', b10.b1, b10.b2
print b10.fonk2()
'''
'''
b10 = class1()
b10.fonk3(3)
print b10.b2
b10.fonk3(2)
print b10.b2
b10.fonk3(1)
print b10.b2
b10.fonk3(15)
print b10.b2
b10.fonk3(5)
print b10.b2
b10.fonk3(4)
print b10.b2
b10.fonk3(45)
print b10.b2
b10.fonk5(1)
print b10.b2
print b10.fonk2()
b10.fonk3(677)
print b10.b2
print b10.fonk2()
'''