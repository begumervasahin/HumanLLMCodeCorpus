import sys
import math
class Point:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def equals(self, p):
    return (self.x == p.x and self.y == p.y)
class ECurve:
  def __init__(self, a, b, p):
    self.a, self.b, self.p = a, b, p
  def check(self, p):
    l = self.mod(p.y * p.y)
    r = self.mod(p.x * p.x * p.x + self.a * p.x + self.b)
    c = 4 * self.a*self.a*self.a  + 27 * self.b*self.b
    return l == r and c != 0
  def mod(self, x):
    return x % self.p
  def invmod(self, x):
    s0, s1 = 0, 1
    r0, r1 = self.p, x
    while r0 != 0:
      q = r1
      r1, r0 = r0, r1 - q * r0
      s1, s0 = s0, s1 - q * s0
    return s1 % self.p
  def add(self, p, q):
    r = Point(0, 0)
    if p.equals(r): return q
    if q.equals(r): return p
    if p.equals(q):
      if p.y != 0:
        l = self.mod(self.mod(3*p.x*p.x + self.a) * self.invmod(2*p.y))
        r.x = self.mod(l*l - 2*p.x)
        r.y = self.mod(l*(p.x - r.x) - p.y)
    else:
      if q.x - p.x != 0:
        l = self.mod(self.mod(q.y - p.y) * self.invmod(q.x - p.x))
        r.x = self.mod(l*l - p.x - q.x)
        r.y = self.mod(l*(p.x - r.x) - p.y)
    return r
  def double(self, p):
    return self.add(p, p)
  def multiply(self, p, n):
    if n == 0:
      return Point(0, 0)
    elif n == 1:
      return p
    elif n % 2 == 1:
      return self.add(p, self.multiply(p, n-1))
    else:
      return self.multiply(self.double(p), n/2)
class Decipher:
  def __init__(self, curve, p, q, n):
    self.curve, self.p, self.q, self.n = curve, p, q, n
  def run(self):
    r = Point(0, 0)
    for d in range(1, self.n):
      r = self.curve.add(self.p, r)
      if not self.curve.check(r): return 0
      if r.equals(self.q): return d
    return 0
def main(argv=None):
  a = -0x3
  b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
  p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
  P = Point(
    0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
    0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
  )
  Q = Point(
    0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
    0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
  )
  curve = ECurve(a, b, p)
  if not curve.check(P) or not curve.check(Q):
    return 0
  decip = Decipher(curve, P, Q, p)
  return decip.run()
if __name__ == "__main__":
  value = main()
  print(value)