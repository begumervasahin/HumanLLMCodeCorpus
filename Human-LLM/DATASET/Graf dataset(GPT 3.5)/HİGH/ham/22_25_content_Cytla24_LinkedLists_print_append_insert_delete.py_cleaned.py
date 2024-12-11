class class1():
  def fonk1(self, b1 = None):
    self.b1 = b1
    self.b2 = None
class class2():
  def fonk2(self):
    self.b3 = None
  def fonk3(self):
    b4 = self.b3
    while b4 is not None:
      print(b4.b1)
      b4 = b4.b2
  def fonk4(self, data_a):
    b5 = class1(data_a)
    b5.b2 = self.b3
    self.b3 = b5
  def fonk5(self,nodes,data_a):
    b5 = class1(data_a)
    b5.b2 = nodes.b2
    nodes.b2 = b5
  def fonk6(self, data_a):
    b6 = class1(data_a)
    if self.b3 is None:
      self.b3 = b6
      return
    b7 = self.b3
    while b7.b2 is not None:
      b7 = b7.b2
    b7.b2 = b6
  def fonk7(self, data_a):
    b8 = self.b3
    if b8 is not None and b8.b1 = = data_a:
      self.b3 = b8.b2
      b8 = None
      return
    b9 = None
    while b8 is not None and b8.b1 != data_a:
      b9 = b8
      b8 = b8.b2
    if b8 is None:
      return
    b9.b2 = b8.b2
    b8 = None
b10 = class2()
b10.b3 = class1("Aimie Ojuba")
b11 = class1("latifs")
b12 = class1("Toni")
b13 = class1("slap")
b10.b3.b2 = b11
b11.b2 = b12
b12.b2 = b13
b10.fonk4("imaa")
b10.fonk6("beast")
b10.fonk5(b10.b3.b2,"shile")
b10.fonk7("slap")
b10.fonk3()