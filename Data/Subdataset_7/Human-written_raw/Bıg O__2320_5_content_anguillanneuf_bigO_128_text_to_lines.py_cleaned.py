"""
Created on Mon Feb  5 13:50:13 2018
@author: harrisot
"Given a string of English text and a paragraph b2,
design an algorithm to break the texts into b8 not
exceeding the paragraph b2, and not too jagged."
"""
from itertools import product, combinations
class class1(object):
  def fonk1(self, b1 = "", b2=80):
    self.b1 = b1
    self.b2 = b2
    self.b3 = []
    self.b4 = []
    self.b5 = set()
    self.b6 = set()
  def fonk2(self):
    for b7 in range(len(self.b1)):
      if not self.b1[b7].isspace():
        if b7 = =0 or self.b1[b7-1].isspace():
          self.b3.append(b7)
        if self.b3 and b7-self.b3[-1]>self.b2:
          print("\"{}\" is longer than the allowed line b2 {}."
                .format(self.b1[self.b3[-1]:b7+1], self.b2))
          print("Please consider adjusting the line b2.")
          self.b3 = []
    self.b3.append(len(self.b1))
  def fonk3(self):
    self.fonk2()
    b8 = ['']
    a1 = 0
    a2 = 0
    for b in self.b3:
      if b-a2 < self.b2:
        b8[-1] += self.b1[a1:b]
      else:
        b8.append(self.b1[a1:b])
        a2 = a1
      a1 = b
    print([len(l) for l in b8])
    return b8
  def fonk4(self, b10, b9 = False):
    if not b9:
      if b10 = = len(self.b3)-1: return None
      b7 = b10
      b11 = len(self.b3)-1
      if self.b3[b11] - self.b3[b7] <= self.b2: return b11
      a3 = 1
    else:
      if b10 = = 0: return None
      b7 = 0
      b11 = b10
      if self.b3[b11] - self.b3[b7] <= self.b2: return b7
      a3 = -1
    while b7 < b11:
      b12 = (b7+b11)
      if self.b3[b12-1] <= self.b3[b10]+a3*self.b2 <= self.b3[b12]:
        b10 = b12-1*(not b9)
        break
      elif self.b3[b12] > self.b3[b10]+a3*self.b2:
        b11 = b12
      else:
        b7 = b12
    return b10
  def fonk5(self):
    b13 = []
    b10 = 0
    while b10 is not None and b10 <= len(self.b3):
      b13.append((b10, self.b3[b10]))
      b10 = self.fonk4(b10)
    print("front push results: ", b13)
    b14 = []
    b10 = len(self.b3)-1
    while b10 is not None and b10 >= 0:
      b14.append((b10, self.b3[b10]))
      b10 = self.fonk4(b10, b9=True)
    print("back push results: ", b14[::-1])
    b15 = float('inf')
    b16 = []
    for back,front in zip(b14[::-1], b13):
      b16.append(range(back[0], front[0]+1))
    print("Possible ranges: ", b16)
    a4 = 0
    for b20 in product(*b16):
      a4 += 1
      a5 = 0
      b17 = True
      for k in range(1,len(b20)):
        b18 = self.b3[b20[k]]-self.b3[b20[k-1]]
        if b18 > self.b2:
          a5 = float('inf')
          b17 = False
          break
        else:
          a5 += (self.b2 - b18)**2
      if b17:
        self.b6.add(tuple([self.b3[b7] for b7 in b20]))
      if a5 < b15:
        b15 = a5
        self.b4 = [self.b3[k] for k in b20]
    print("My solution runs {} times and evaluates a5 {} times.".format(a4, len(self.b6)))
    print("{} has least a5 of {}".format(self.b4, b15))
    for b in range(1,len(b8.b4)):
      print(b1[b8.b4[b-1]:b8.b4[b]])
  def fonk6(self):
    b3 = self.b3[1:len(self.b3)-1]
    b19 = len(self.b1)
    b15 = float('inf')
    a4 = 0
    for b20 in combinations(b3, b19):
      b17 = True
      a5 = 0
      b20 = [0] + list(b20) + [len(self.b1)]
      a4 += 1
      for k in range(1,len(b20)):
        b18 = b20[k]- b20[k-1]
        if b18 > self.b2:
          a5 = float('inf')
          b17 = False
          break
        else:
          a5 += (self.b2 - b18)**2
      if b17:
        self.b5.add(tuple(b20))
      if a5 < b15:
        b15 = a5
        self.b4 = b20
    print("Brute force solution runs {} times and evalutes a5 {} times.".format(a4, len(self.b5)))
    print("{} has least a5 of {}".format(self.b4, b15))
    for b in range(1,len(b8.b4)):
      print(b1[b8.b4[b-1]:b8.b4[b]])
  def fonk7(self):
    pass
b1 = "Try this: Given a string of English text and a paragraph b2, design an algorithm to break the texts into b8 not exceeding the paragraph b2, and not too jagged."
b8 = class1(b1, 80)
b8.fonk2()
print(b8.b3)
b8.fonk6()
b8.fonk5()