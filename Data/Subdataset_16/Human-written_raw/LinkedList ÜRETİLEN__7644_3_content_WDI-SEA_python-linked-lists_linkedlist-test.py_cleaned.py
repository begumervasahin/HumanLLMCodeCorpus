import unittest
from linkedlist import *
class class1(unittest.TestCase):
  def fonk1(self):
    self.b1 = ListNode(0)
    self.b2 = LinkedList()
    self.b3 = LinkedList()
    self.b3.insert_in_front(1)
    self.b4 = LinkedList()
    self.b4.insert_in_front(2)
    self.b4.insert_in_front(1)
    self.b5 = LinkedList()
    self.b5.insert_in_front(3)
    self.b5.insert_in_front(2)
    self.b5.insert_in_front(1)
    self.b6 = LinkedList()
    for i in range(99, 0,-1):
      self.b6.insert_in_front(i)
  def fonk2(self):
    self.assertEqual(self.b1.data, 0)
  def fonk3(self):
    self.assertEqual(self.b2.is_empty(), True)
    self.assertEqual(len(self.b2), 0)
  def fonk4(self):
    self.assertEqual(self.b3.is_empty(), False)
    self.assertEqual(len(self.b3), 1)
    self.assertEqual(self.b4.is_empty(), False)
    self.assertEqual(len(self.b4), 2)
    self.assertEqual(self.b5.is_empty(), False)
    self.assertEqual(len(self.b5), 3)
    self.assertEqual(self.b6.is_empty(), False)
    self.assertEqual(len(self.b6), 99)
  def fonk5(self):
    self.assertEqual(str(self.b2), "[]")
    self.assertEqual(len(self.b2), 0)
  def fonk6(self):
    self.assertEqual(str(self.b3), "[1]")
    self.assertEqual(len(self.b3), 1)
  def fonk7(self):
    self.assertEqual(str(self.b4), "[1 -> 2]")
    self.assertEqual(len(self.b4), 2)
  def fonk8(self):
    self.assertEqual(str(self.b5), "[1 -> 2 -> 3]")
    self.assertEqual(len(self.b5), 3)
  def fonk9(self):
    self.assertEqual(str(self.b6), "[1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 11 -> 12 -> 13 -> 14 -> 15 -> 16 -> 17 -> 18 -> 19 -> 20 -> 21 -> 22 -> 23 -> 24 -> 25 -> 26 -> 27 -> 28 -> 29 -> 30 -> 31 -> 32 -> 33 -> 34 -> 35 -> 36 -> 37 -> 38 -> 39 -> 40 -> 41 -> 42 -> 43 -> 44 -> 45 -> 46 -> 47 -> 48 -> 49 -> 50 -> 51 -> 52 -> 53 -> 54 -> 55 -> 56 -> 57 -> 58 -> 59 -> 60 -> 61 -> 62 -> 63 -> 64 -> 65 -> 66 -> 67 -> 68 -> 69 -> 70 -> 71 -> 72 -> 73 -> 74 -> 75 -> 76 -> 77 -> 78 -> 79 -> 80 -> 81 -> 82 -> 83 -> 84 -> 85 -> 86 -> 87 -> 88 -> 89 -> 90 -> 91 -> 92 -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99]")
    self.assertEqual(len(self.b6), 99)
  def fonk10(self):
    self.b2.insert_in_front(1)
    self.b3.insert_in_front(0)
    self.b3.insert_in_front(0)
    self.b3.insert_in_front(0)
    self.b3.insert_in_front(0)
    self.assertEqual(str(self.b2), '[1]')
    self.assertEqual(str(self.b3), '[0 -> 0 -> 0 -> 0 -> 1]')
    self.assertEqual(len(self.b3), 5)
  def fonk11(self):
    self.assertFalse(self.b2.remove_front())
    self.b3.remove_front()
    self.assertEqual(str(self.b3), '[]')
    self.assertEqual(len(self.b3), 0)
    self.b4.remove_front()
    self.assertEqual(str(self.b4), '[2]')
    self.assertEqual(len(self.b4), 1)
    self.b5.remove_front()
    self.assertEqual(str(self.b5), '[2 -> 3]')
    self.assertEqual(len(self.b5), 2)
  def fonk12(self):
    self.b2.insert_at_end(98)
    self.assertEqual(str(self.b2), '[98]')
    self.assertEqual(len(self.b2), 1)
    self.b3.insert_at_end(98)
    self.assertEqual(str(self.b3), '[1 -> 98]')
    self.assertEqual(len(self.b3), 2)
    self.b4.insert_at_end(98)
    self.assertEqual(str(self.b4), '[1 -> 2 -> 98]')
    self.assertEqual(len(self.b4), 3)
    self.b5.insert_at_end(98)
    self.assertEqual(str(self.b5), '[1 -> 2 -> 3 -> 98]')
    self.assertEqual(len(self.b5), 4)
  def fonk13(self):
    b7 = self.b2.remove_last()
    self.assertFalse(b7)
    self.assertEqual(len(self.b2), 0)
  def fonk14(self):
    self.b3.remove_last()
    self.assertEqual(str(self.b3), '[]')
    self.assertEqual(len(self.b3), 0)
  def fonk15(self):
    self.b4.remove_last()
    self.assertEqual(str(self.b4), '[1]')
    self.assertEqual(len(self.b4), 1)
  def fonk16(self):
    self.b5.remove_last()
    self.assertEqual(str(self.b5), '[1 -> 2]')
    self.assertEqual(len(self.b5), 2)
  def fonk17(self):
    self.b2.insert_at_index(22)
    self.assertEqual(str(self.b2), '[22]')
    self.assertEqual(len(self.b2), 1)
  def fonk18(self):
    self.b2.insert_at_index(22, 0)
    self.assertEqual(str(self.b2), '[22]')
    self.assertEqual(len(self.b2), 1)
  def fonk19(self):
    self.b3.insert_at_index(22, 0)
    self.assertEqual(str(self.b3), '[22 -> 1]')
    self.assertEqual(len(self.b3), 2)
  def fonk20(self):
    self.b3.insert_at_index(22, 1)
    self.assertEqual(str(self.b3), '[1 -> 22]')
    self.assertEqual(len(self.b3), 2)
  def fonk21(self):
    self.b5.insert_at_index(22, 0)
    self.assertEqual(str(self.b5), '[22 -> 1 -> 2 -> 3]')
    self.assertEqual(len(self.b5), 4)
  def fonk22(self):
    self.b5.insert_at_index(22, 1)
    self.assertEqual(str(self.b5), '[1 -> 22 -> 2 -> 3]')
    self.assertEqual(len(self.b5), 4)
  def fonk23(self):
    self.b5.insert_at_index(22, 2)
    self.assertEqual(str(self.b5), '[1 -> 2 -> 22 -> 3]')
    self.assertEqual(len(self.b5), 4)
  def fonk24(self):
    self.b5.insert_at_index(22, 3)
    self.assertEqual(str(self.b5), '[1 -> 2 -> 3 -> 22]')
    self.assertEqual(len(self.b5), 4)
  def fonk25(self):
    b7 = self.b2.remove_at_index()
    self.assertFalse(b7)
  def fonk26(self):
    self.b3.remove_at_index(0)
    self.assertEqual(str(self.b3), '[]')
    self.assertEqual(len(self.b3), 0)
  def fonk27(self):
    self.b5.remove_at_index(0)
    self.assertEqual(str(self.b5), '[2 -> 3]')
    self.assertEqual(len(self.b5), 2)
  def fonk28(self):
    self.b5.remove_at_index(1)
    self.assertEqual(str(self.b5), '[1 -> 3]')
    self.assertEqual(len(self.b5), 2)
  def fonk29(self):
    self.b5.remove_at_index(2)
    self.assertEqual(str(self.b5), '[1 -> 2]')
    self.assertEqual(len(self.b5), 2)
  def fonk30(self):
    for (i, node) in enumerate(self.b5):
      self.assertEqual(node.data, i + 1)
unittest.main()