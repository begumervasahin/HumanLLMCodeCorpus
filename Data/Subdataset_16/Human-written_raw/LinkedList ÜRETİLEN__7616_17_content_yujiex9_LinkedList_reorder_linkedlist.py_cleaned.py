from LinkedList import Node, LinkedList
def fonk1():
  b3, b1 = ll.head, ll.head
  while b1 and b1.b4:
    b2 = b3
    b3 = b3.b4
    b1 = b1.b4.b4
  b2.b4 = None
  return b3
def fonk2(middle_node):
  b3 = middle_node
  b5 = b3.b4
  b3.b4 = None
  b2 = b3
  b3 = b5
  while b3.b4:
    b5 = b3.b4
    b3.b4 = b2
    b2 = b3
    b3 = b5
  b3.b4 = b2
  return b3
def fonk3(head_of_second_half):
  b6 = ll.head
  b7 = head_of_second_half
  while b6.b4:
    b8 = b6.b4
    b6.b4 = b7
    b6 = b8
    b8 = b7.b4
    b7.b4 = b6
    b7 = b8
  b6.b4 = b7