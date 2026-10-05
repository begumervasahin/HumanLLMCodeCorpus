class node():
  def __init__(self, datavalue=None):
    self.datavalue = datavalue
    self.nextvalue = None
class linkedlist():
  def __init(self):
    self.headvalue = None
  def printing(self):
    printvalue = self.headvalue
    while printvalue is not None:
      print(printvalue.datavalue)
      printvalue = printvalue.nextvalue
  def begin(self, data_a):
    new = node(data_a)
    new.nextvalue = self.headvalue
    self.headvalue = new
  def between(self,nodes,data_a):
    new = node(data_a)
    new.nextvalue = nodes.nextvalue
    nodes.nextvalue = new
  def end(self, data_a):
    newest = node(data_a)
    if self.headvalue is None:
      self.headvalue = newest
      return
    lastNode = self.headvalue
    while lastNode.nextvalue is not None:
      lastNode = lastNode.nextvalue
    lastNode.nextvalue = newest
  def delete(self, data_a):
    current = self.headvalue
    if current is not None and current.datavalue == data_a:
      self.headvalue = current.nextvalue
      current = None
      return
    prev = None
    while current is not None and current.datavalue != data_a:
      prev = current
      current = current.nextvalue
    if current is None:
      return
    prev.nextvalue = current.nextvalue
    current = None
x = linkedlist()
x.headvalue = node("Aimie Ojuba")
data2 = node("latifs")
data3 = node("Toni")
data4 = node("slap")
x.headvalue.nextvalue = data2
data2.nextvalue = data3
data3.nextvalue = data4
x.begin("imaa")
x.end("beast")
x.between(x.headvalue.nextvalue,"shile")
x.delete("slap")
x.printing()