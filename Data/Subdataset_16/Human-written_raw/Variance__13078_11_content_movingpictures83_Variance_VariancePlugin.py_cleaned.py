import sys
import numpy
class class1:
   def fonk1(self, filename):
      self.b1 = filename
   def fonk2(self):
      b2 = open(self.b1, 'r')
      b3 = b2.readline()
      self.b4 = b3.split(',')
      if (self.b4.count('\"\"') != 0):
         self.b4.remove('\"\"')
      self.b5 = len(self.b4)
      self.b6 = []
      for i in range(self.b5):
         self.b6.append([])
      for line in b2:
         b7 = line.split(',')
         for j in range(len(b7)-1):
            b8 = float(b7[j+1])
            self.b6[j].append(b8)
   def fonk3(self, filename):
      b9 = open(filename, 'w')
      b9.write("Element\tVariance\b5")
      b9.write("\b5")
      b10 = []
      for i in range(self.b5):
         a1 = 0
         a2 = 0
         if (len(self.b6[i]) != 0):
          for j in range(len(self.b6[i])):
            a1 += self.b6[i][j]
          b11 = float(a1) / len(self.b6[i])
          for j in range(len(self.b6[i])):
            a2 += (b11 - self.b6[i][j])**2
          b10.append((a2 / len(self.b6[i]), self.b4[i]))
      b10.sort()
      b10.reverse()
      for i in range(len(b10)):
         b9.write(b10[i][1])
         b9.write("\t")
         b9.write(str(b10[i][0]))
         b9.write("\b5")