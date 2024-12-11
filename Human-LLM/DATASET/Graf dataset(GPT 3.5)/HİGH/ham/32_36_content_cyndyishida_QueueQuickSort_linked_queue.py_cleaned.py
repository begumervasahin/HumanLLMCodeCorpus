class class1:
  b1 = 'b2', 'b3'
  def fonk1(self, b2, b3):
    self.b2 = b2
    self.b3 = b3
  def fonk2(self, other):
    return self.b2 <= other.b2
  def fonk3(self, other):
    return self.b2 <= other.b2
class class2:
  def fonk4(self):
    self.b4 = None
    self.b5 = None
    self.a1 = 0
  def fonk5(self):
    b4 = self.b4
    b6 = list()
    while b4:
      b6.append(str(b4.b2))
      b4 = b4.b3
    return ", ".join(b6)
  b7 = __str__
  def fonk6(self):
    return self.a1
  def fonk7(self):
    return self.a1 = = 0
  def fonk8(self):
    b8 = self.b4.b2
    self.b4 = self.b4.b3
    self.a1 -= 1
    if self.fonk7():
      self.b5 = None
    return b8
  def fonk9(self, element):
    b9 = class1(element, None)
    if self.fonk7():
      self.b4 = b9
    else:
      self.b5.b3 = b9
    self.b5 = b9
    self.a1 += 1
  def fonk10(self,index):
    b10 = self.b4
    for i in range(index):
      b10 = b10.b3
    return b10
  def fonk11(self, index, b2 ):
    b10 = self.b4
    for i in range(index):
      b10 = b10.b3
    b10.b2 = b2