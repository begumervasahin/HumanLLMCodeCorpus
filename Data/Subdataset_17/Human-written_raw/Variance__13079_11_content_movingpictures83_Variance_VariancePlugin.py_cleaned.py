import sys
import numpy
class VariancePlugin:
   def input(self, filename):
      self.myfile = filename
   def run(self):
      filestuff = open(self.myfile, 'r')
      firstline = filestuff.readline()
      self.bacteria = firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)
      self.ADJ = []
      for i in range(self.n):
         self.ADJ.append([])
      for line in filestuff:
         contents = line.split(',')
         for j in range(len(contents)-1):
            value = float(contents[j+1])
            self.ADJ[j].append(value)
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      filestuff2.write("Element\tVariance\n")
      filestuff2.write("\n")
      variances = []
      for i in range(self.n):
         sum = 0
         variance = 0
         if (len(self.ADJ[i]) != 0):
          for j in range(len(self.ADJ[i])):
            sum += self.ADJ[i][j]
          average = float(sum) / len(self.ADJ[i])
          for j in range(len(self.ADJ[i])):
            variance += (average - self.ADJ[i][j])**2
          variances.append((variance / len(self.ADJ[i]), self.bacteria[i]))
      variances.sort()
      variances.reverse()
      for i in range(len(variances)):
         filestuff2.write(variances[i][1])
         filestuff2.write("\t")
         filestuff2.write(str(variances[i][0]))
         filestuff2.write("\n")