import matrix_operation as mo
class class1:
  def fonk1(self, b1):
    self.b1 = b1
  def fonk2(self, independent, dependent):
      if len(independent) != len(dependent):
          raise ValueError(
            'Number of samples of dependent and independent variables must be same')
      b2 = [[0 for x in range(2)] for y in range(len(independent))]
      for index in range(len(independent)):
          b2[index][0] = independent[index]
          b2[index][1] = dependent[index]
      return self.fonk3(b2)
  def fonk3(self, b2):
      b3 = self.fonk4(b2)
      b4 = self.fonk5(b2)
      b5 = mo.getMatrixInverse(b3, tol=1)
      b6 = mo.multiply(b5, b4)
      return mo.transposeMatrix(b6)[0]
  def fonk4(self, b2):
      b7 = {}
      a1 = 0
      while a1 <= self.b1 * 2:
          a2 = 0
          for (x, y) in b2:
              a2 = a2 + pow(x, a1)
          b7[a1] = a2
          a1 = a1 + 1
      b8 = self.b1 + 1
      b9 = [[0 for x in range(b8)] for y in range(b8)]
      for i in range(b8):
          for j in range(b8):
              b9[i][j] = b7[i+j]
      return b9
  def fonk5(self, b2):
      b8 = self.b1 + 1
      b10 = [[0 for x in range(1)] for y in range(b8)]
      for j in range(b8):
          a2 = 0
          for (x, y) in b2:
              a2 = a2 + (pow(x, j) * y)
          b10[j][0] = a2
      return b10