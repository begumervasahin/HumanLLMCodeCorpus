class class1:
    def fonk1(self,b2,val,b1 = None,right=None,b6=None):
        self.b2 = b2
        self.b3 = val
        self.b4 = b1
        self.b5 = right
        self.b6 = b6
    def fonk2(self):
        return self.b4
    def fonk3(self):
        return self.b5
    def fonk4(self):
        return self.b6 and self.b6.b4 = = self
    def fonk5(self):
        return self.b6 and self.b6.b5 = = self
    def fonk6(self):
        return not self.b6
    def fonk7(self):
        return not (self.b5 or self.b4)
    def fonk8(self):
        return self.b5 or self.b4
    def fonk9(self):
        return self.b5 and self.b4
    def fonk10(self,b2,value,lc,rc):
        self.b2 = b2
        self.b3 = value
        self.b4 = lc
        self.b5 = rc
        if self.fonk2():
            self.b4.b6 = self
        if self.fonk3():
            self.b5.b6 = self
class class2:
    def fonk11(self):
        self.b7 = None
        self.a1 = 0
    def fonk12(self):
        return self.a1
    def fonk13(self):
        return self.a1
    def fonk14(self,b2,val):
        if self.b7:
            self.fonk15(b2,val,self.b7)
        else:
            self.b7 = class1(b2,val)
        self.a1 = self.a1 + 1
    def fonk15(self,b2,val,b12):
        if b2 < b12.b2:
            if b12.fonk2():
                   self.fonk15(b2,val,b12.b4)
            else:
                   b12.b4 = class1(b2,val,b6=b12)
        else:
            if b12.fonk3():
                   self.fonk15(b2,val,b12.b5)
            else:
                   b12.b5 = class1(b2,val,b6=b12)
    def fonk16(self,k,v):
       self.fonk14(k,v)
    def fonk17(self,b2):
       if self.b7:
           b8 = self.fonk18(b2,self.b7)
           if b8:
                  return b8.b3
           else:
                  return None
       else:
           return None
    def fonk18(self,b2,b12):
       if not b12:
           return None
       elif b12.b2 = = b2:
           return b12
       elif b2 < b12.b2:
           return self.fonk18(b2,b12.b4)
       else:
           return self.fonk18(b2,b12.b5)
    def fonk19(self,b2):
       return self.fonk17(b2)
    def fonk20(self,b2):
       if self.fonk18(b2,self.b7):
           return True
       else:
           return False
    def fonk21(self,b2):
      if self.a1 > 1:
         b9 = self.fonk18(b2,self.b7)
         if b9:
             self.fonk26(b9)
             self.a1 = self.a1-1
         else:
             raise KeyError('Error, b2 not in tree')
      elif self.a1 = = 1 and self.b7.b2 == b2:
         self.b7 = None
         self.a1 = self.a1 - 1
      else:
         raise KeyError('Error, b2 not in tree')
    def fonk22(self,b2):
       self.fonk21(b2)
    def fonk23(self):
       if self.fonk7():
           if self.fonk4():
                  self.b6.b4 = None
           else:
                  self.b6.b5 = None
       elif self.fonk8():
           if self.fonk2():
                  if self.fonk4():
                     self.b6.b4 = self.b4
                  else:
                     self.b6.b5 = self.b4
                  self.b4.b6 = self.b6
           else:
                  if self.fonk4():
                     self.b6.b4 = self.b5
                  else:
                     self.b6.b5 = self.b5
                  self.b5.b6 = self.b6
    def fonk24(self):
      b10 = None
      if self.fonk3():
          b10 = self.b5.fonk25()
      else:
          if self.b6:
                 if self.fonk4():
                     b10 = self.b6
                 else:
                     self.b6.b5 = None
                     b10 = self.b6.fonk24()
                     self.b6.b5 = self
      return b10
    def fonk25(self):
      b11 = self
      while b11.fonk2():
          b11 = b11.b4
      return b11
    def fonk26(self,b12):
         if b12.fonk7():
           if b12 = = b12.b6.b4:
               b12.b6.b4 = None
           else:
               b12.b6.b5 = None
         elif b12.fonk9():
           b10 = b12.fonk24()
           b10.fonk23()
           b12.b2 = b10.b2
           b12.b3 = b10.b3
         else:
           if b12.fonk2():
             if b12.fonk4():
                 b12.b4.b6 = b12.b6
                 b12.b6.b4 = b12.b4
             elif b12.fonk5():
                 b12.b4.b6 = b12.b6
                 b12.b6.b5 = b12.b4
             else:
                 b12.fonk10(b12.b4.b2,
                                    b12.b4.b3,
                                    b12.b4.b4,
                                    b12.b4.b5)
           else:
             if b12.fonk4():
                 b12.b5.b6 = b12.b6
                 b12.b6.b4 = b12.b5
             elif b12.fonk5():
                 b12.b5.b6 = b12.b6
                 b12.b6.b5 = b12.b5
             else:
                 b12.fonk10(b12.b5.b2,
                                    b12.b5.b3,
                                    b12.b5.b4,
                                    b12.b5.b5)
b13 = class2()
b13[3]="red"
b13[4]="blue"
b13[6]="yellow"
b13[2]="at"
print(b13[6])
print(b13[2])