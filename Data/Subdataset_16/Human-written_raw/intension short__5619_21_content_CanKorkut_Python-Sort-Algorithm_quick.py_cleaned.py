from random import randint
b1 = []
b2 = []
b3 = []
b4 = []
b5 = [0,1,2,3,4,5,6,7,8,9]
b6 = [9,8,7,6,5,4,3,2,1,0]
def fonk1(Array,b7):
   while b7>0:
      Array.append(randint(0,10000))
      b7 = b7-1
fonk1(b1,10)
fonk1(b2,100)
fonk1(b3,1000)
fonk1(b4,10000)
class class1:
   def fonk2(self):
      self.a1 = 0
   def fonk3(self,Array,b,s):
      if b<s:
         self.a1 = self.a1+1
         b8 = self.fonk4(Array,b,s)
         self.a1 = self.a1+1
         self.fonk3(Array,b,b8-1)
         self.a1 = self.a1+1
         self.fonk3(Array,b8+1,s)
         self.a1 = self.a1+1
   def fonk4(self,Array,b,s):
      b9 = Array [s]
      self.a1 = self.a1+1
      b10 = b - 1
      self.a1 = self.a1+1
      for j in range (b,s):
         self.a1 = self.a1+1
         if(Array[j] <= b9):
            self.a1 = self.a1+1
            b10 = b10+1
            self.a1 = self.a1+1
            b11 = Array[b10]
            self.a1 = self.a1+1
            Array[b10] = Array[j]
            self.a1 = self.a1+1
            Array[j] = b11
            self.a1 = self.a1+1
      b11 = Array[b10+1]
      self.a1 = self.a1+1
      Array[b10+1] = Array[s]
      self.a1 = self.a1+1
      Array[s] = b11
      self.a1 = self.a1+1
      return b10+1
def fonk5(Array):
    print (Array)
    b7 = class1()
    b7.fonk3(Array,0,len(Array)-1)
    print (Array)
    print (b7.a1)
def fonk6():
    fonk5(b2)
if b12 = =__main__:
     fonk6()