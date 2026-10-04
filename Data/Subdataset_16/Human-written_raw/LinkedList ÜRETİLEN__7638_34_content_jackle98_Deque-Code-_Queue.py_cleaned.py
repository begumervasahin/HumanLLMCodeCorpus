from Deque_Generator import get_deque
class class1:
  def fonk1(self):
    self.b1 = get_deque(1)
  def fonk2(self):
      b2 = self.b1.fonk2()
      return b2
  def fonk3(self):
      b3 = self.b1.fonk3()
      return b3
  def fonk4(self, val):
    self.b1.push_back(val)
  def fonk5(self):
    if len(self.b1) == 0:
        return None
    b4 = self.b1.pop_front()
    return b4