import sys
from b14 import Point
from b10.general import is_prime, inverse
class class1(object):
  def fonk1(self, b1, b2, b3):
    self.b1 = b1
    self.b2 = b2
    self.b3 = b3
  def fonk2(self):
    return self.b1
  def fonk3(self):
    return self.b2
  def fonk4(self):
    return self.b3
  def fonk5(self, p):
    b4 = Point()
    if p._get_y() == 0:
      b4._set_x(sys.maxsize)
      b4._set_y(sys.maxsize)
    else:
      b5 = inverse(2 * p._get_y(), self.fonk4())
      b6 = ((3 * (p._get_x())**2 + self.fonk2()) * b5) % self.fonk4()
      b6 = int(b6 % self.fonk4())
      b7 = (b6**2 - (2 * p._get_x())) % self.fonk4()
      b8 = (b6 * (p._get_x() - b7) - p._get_y()) % self.fonk4()
      b4._set_x(int(b7))
      b4._set_y(int(b8))
    return b4
  def fonk6(self, b15, b16):
    b4 = Point()
    if b15._get_x() == 0 and b15._get_y() == 0:
      b4._set_x(b16._get_x())
      b4._set_x(b16._get_y())
    elif b16._get_x() == 0 and b16._get_y() == 0:
      b4._set_x(b15._get_x())
      b4._set_x(b15._get_y())
    elif b15._get_y() - b16._get_y() == 0:
      b4._set_x((0 - b15._get_x() - b16._get_x()) % self.fonk4())
      b4._set_x((0 - b15._get_x()) % self.fonk4())
    elif b15._get_x() - b16._get_x() == 0:
      b4._set_x(sys.maxsize)
      b4._set_y(sys.maxsize)
    else:
      b5 = inverse((b15._get_x() - b16._get_x()), self.fonk4())
      b6 = ((b15._get_y() - b16._get_y()) * b5) % self.fonk4()
      b7 = (b6**2 - b15._get_x() - b16._get_x()) % self.fonk4()
      b8 = (b6*(b15._get_x()-b7)-b15._get_y()) % self.fonk4()
      b4._set_x(b7)
      b4._set_y(b8)
    return b4
  def fonk7(self, b15, b16):
    b9 = Point()
    b9._set_x(b16._get_x())
    b9._set_y(-b16._get_y())
    return self.fonk6(b15, b9)
  def fonk8(self, k, p):
    b4 = Point()
    b10 = Point()
    b10._set_x(p._get_x())
    b10._set_y(p._get_y())
    b11 = bin(k).lstrip('0b')
    for b12 in range(len(b11)):
      if b12 = = len(b11)-1:
        if b11[b12] == '0':
          b4 = b10
        else:
          b4 = self.fonk6(b10, p)
      b10 = self.fonk5(b10)
    return b4
if b13 = = '__main__':
  b14 = Point()
  b14._set_x(1)
  b14._set_y(375)
  b15 = Point()
  b15._set_x(361)
  b15._set_y(41)
  b16 = Point()
  b16._set_x(2)
  b16._set_y(4)
  b17 = class1(-1,751,11)
  b4 = b17.fonk8(2, b14)
  b18 = b17.fonk5(b14)
  print(b4._get_x(), b4._get_y())
  print(b18._get_x(), b18._get_y())