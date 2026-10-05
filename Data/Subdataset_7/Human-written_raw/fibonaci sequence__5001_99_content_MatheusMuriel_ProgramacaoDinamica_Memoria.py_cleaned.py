class class1():
  def fonk1(self, b3, b4):
    self.b1 = {}
    self.b2 = {}
    self.b3 = b3
    self.b4 = b4
  def fonk2(self, b5, b6):
    b5 = str(b5)
    b6 = int(b6)
    if (len(self.b1) >= self.b3):
      self.fonk4(b5)
    self.b1[b5] = b6
    self.b2[b5] = 1
  def fonk3(self, b5):
    if (b5 in self.b1):
      self.b2[b5] += 1
      return self.b1[b5]
    else:
      return -1
  def fonk4(self, iteracao_atual):
    print("Chamada de limpeza na iteraÃ§Ã£o", iteracao_atual)
    while(len(self.b1) > self.b3*(self.b4)):
      b7 = min(self.b2.items(), key=lambda x: x[1])
      self.b1.pop(b7[0])
      self.b2.pop(b7[0])