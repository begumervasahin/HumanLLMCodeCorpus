
def fonk1(b6):
  b1 = dict()
  for b2 in b6:
    b2 = b2.lower()
    if b2.isalpha():
      if b2 not in b1.keys():
        b1.update({b2: 1})
      else:
        b1[b2] += 1
  return b1
def fonk2(b5, b6):
  b1 = fonk1(b6)
  b3 = None
  for b23 in b5:
    b4 = fonk1(b23)
    for key in b1.keys():
      if key in b4.keys():
        b4[key] -= b1[key]
        if b4[key] < 0:
          continue
      else:
        continue
    if sum([True for v in b4.values() if v < 0]) > 0:
      if b3 is None:
        b3 = b23
      elif len(b3) > len(b23):
        b3 = b23
  return b3
b5 = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
b6 = 'NY10NJ'
print("Working solution for the b3 b23: {}\n".
      format(fonk2(b5, b6)))
class class1:
  def fonk3(self, b7 = None, b9=None):
    self.b8 = b7
    self.b9 = b9
    self.b10 = None
    self.b11 = None
class class2:
  def fonk4(self):
    self.b12 = None
  def fonk5(self, trieNode):
    if self.b12 is None:
      self.b12 = trieNode
      return
    b13 = self.b12
    while b13.b11 is not None:
      b13 = b13.b11
    b13.b11 = trieNode
    b13.b11.b10 = b13
  def fonk6(self, trieNode):
    if self.b12 is None:
      raise Exception("There are no nodes left to delete!")
    if trieNode.b10:
      trieNode.b10.b11 = None
    else:
      self.b12 = None
b14 = class1('e', {'j':1, 'n':2, 'y':1})
b15 = class1('n', {'j':1, 'n':1, 'y':1})
b16 = class1('j', {'n':1, 'y':1})
b17 = class2()
b17.fonk5(b14)
b17.fonk5(b15)
b17.fonk5(b16)
print("Constructing...")
b18 = b17.b12
while b18:
  print(b18.b10.b8 if b18.b10 else None,
        b18.b8,
        b18.b9)
  b18 = b18.b11
print("Deleting... and inserting...")
b17.fonk6(b16)
b19 = class1('o', {'n':1, 'y':1})
b20 = class1('y', {'n':1})
b17.fonk5(b19)
b18 = b17.b12
while b18:
  print(b18.b8, b18.b9)
  b18 = b18.b11
def fonk7(b22, b23, b1):
  if b22.b12 is not None:
    b21 = b22.b12
  for b2 in b23:
    b1 = b1.copy()
    if b2 in b1.keys():
      b1[b2] -= 1
    if b22.b12 is None:
      b22.fonk5(class1(b2, b1))
      b21 = b22.b12
    if b21 is None:
      b21 = class1(b2, b1)
      b22.fonk5(b21)
      b21 = b21.b11
    elif b2 = = b21.b8:
      b21 = b21.b11
    else:
      b22.fonk6(b21)
      b21 = class1(b2, b1)
      b22.fonk5(b21)
      b21 = b21.b11
  return b1
print('\nTesting...')
b22 = class2()
b23 = 'enjoy'
b1 = {'j':1, 'n':2, 'y':1}
fonk7(b22, b23, b1)
print(b23)
b18 = b22.b12
while b18:
  print(b18.b8, b18.b9)
  b18 = b18.b11
b23 = 'english'
fonk7(b22, b23, b1)
print(b23)
b18 = b22.b12
while b18:
  print(b18.b8, b18.b9)
  b18 = b18.b11
def fonk8(b5, b6):
  b3 = None
  b22 = class2()
  b1 = fonk1(b6)
  for b23 in b5:
    b24 = fonk7(b22, b23, b1)
    if not any(v > 0 for v in b24.values()):
      if b3 is None:
        b3 = b23
      elif len(b3)>len(b23):
        b3 = b23
    print(b23, b3, b24)
  return b3
b25 = fonk8(b5, b6)
print("\nSolution...\nfor {} and {} is ...\n\n{}"
      .format(b5, b6, b25))