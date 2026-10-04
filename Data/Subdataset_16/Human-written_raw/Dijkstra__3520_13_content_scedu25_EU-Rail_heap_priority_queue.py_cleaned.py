from priority_queue_base import PriorityQueueBase
from Empty import Empty
class class1(PriorityQueueBase):
  def fonk1(self, j):
    return (j-1)
  def fonk2(self, j):
    return 2*j + 1
  def fonk3(self, j):
    return 2*j + 2
  def fonk4(self, j):
    return self.fonk2(j) < len(self.b5)
  def fonk5(self, j):
    return self.fonk3(j) < len(self.b5)
  def fonk6(self, i, j):
    self.b5[i], self.b5[j] = self.b5[j], self.b5[i]
  def fonk7(self, j):
    b1 = self.fonk1(j)
    if j > 0 and self.b5[j] < self.b5[b1]:
      self.fonk6(j, b1)
      self.fonk7(b1)
  def fonk8(self, j):
    if self.fonk4(j):
      b2 = self.fonk2(j)
      b3 = b2
      if self.fonk5(j):
        b4 = self.fonk3(j)
        if self.b5[b4] < self.b5[b2]:
          b3 = b4
      if self.b5[b3] < self.b5[j]:
        self.fonk6(j, b3)
        self.fonk8(b3)
  def fonk9(self):
    self.b5 = []
  def fonk10(self):
    return len(self.b5)
  def fonk11(self, key, value):
    self.b5.append(self._Item(key, value))
    self.fonk7(len(self.b5) - 1)
  def fonk12(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    b6 = self.b5[0]
    return (b6._key, b6._value)
  def fonk13(self):
    if self.is_empty():
      raise Empty('Priority queue is empty.')
    self.fonk6(0, len(self.b5) - 1)
    b6 = self.b5.pop()
    self.fonk8(0)
    return (b6._key, b6._value)