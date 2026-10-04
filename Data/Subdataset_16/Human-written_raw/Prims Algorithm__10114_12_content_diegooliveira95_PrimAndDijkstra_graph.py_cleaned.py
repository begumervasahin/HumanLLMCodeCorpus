import sys
class class1:
  def fonk1(self, node):
    self.b1 = node
    self.b2 = {}
    self.b3 = sys.maxint
    self.b4 = False
    self.b5 = None
  def fonk2(self, neighbor, b6 = 0):
    self.b2[neighbor] = b6
  def fonk3(self):
    return self.b2.keys()
  def fonk4(self):
    return self.b1
  def fonk5(self, neighbor):
    return self.b2[neighbor]
  def fonk6(self, b3):
    self.b3 = b3
  def fonk7(self):
    return self.b3
  def fonk8(self, b5):
    self.b5 = b5
  def fonk9(self):
    self.b4 = True
  def fonk10(self):
    return str(self.b1) + ' adjacente(s): ' + str([x.b1 for x in self.b2])
class class2:
  def fonk11(self):
    self.b7 = {}
    self.a1 = 0
  def fonk12(self):
    return iter(self.b7.values())
  def fonk13(self, node):
    self.a1 = self.a1 + 1
    b8 = class1(node)
    self.b7[node] = b8
    return b8
  def fonk14(self, node):
    if node in self.b7:
      return self.b7[node]
    else:
      return none
  def fonk15(self, fromNode, toNode, b9 = 0):
    if fromNode not in self.b7:
      return 'node from not in graph'
    if toNode not in self.b7:
      return 'node to not in graph'
    self.b7[fromNode].fonk2(self.b7[toNode], b9)
    self.b7[toNode].fonk2(self.b7[fromNode], b9)
  def fonk16(self):
    return self.b7.keys()
  def fonk17(self, current):
    self.b5 = current
  def fonk18(self, current):
    return self.b5