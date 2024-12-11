from LinkedList import LinkedList
import unittest
class class1(unittest.TestCase):
	def fonk1(self):
		b1 = LinkedList()
		b1.add_at_the_begining(10)
		self.assertEqual(b1.add_at_the_begining(20).data, 20)
	def fonk2(self):
		b1 = LinkedList()
		b1.add_at_the_begining(10)
		b1.add_at_the_begining(20)
		self.assertEqual(b1.add_at_the_begining(30).data, 30)
	def fonk3(self):
		b1 = LinkedList()
		self.assertEqual(b1.add_at_the_end(500).data, 500)
	def fonk4(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b2 = b1.head.next
		self.assertEqual(b2.data, 20)
	def fonk5(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		self.assertEqual(b1.add_at_nth_position(5, 1).data, 5)
	def fonk6(self):
		b1 = LinkedList()
		self.assertEqual(b1.add_at_nth_position(5, 0), "Invalid position, it can not be less than or equal to 0")
	def fonk7(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		b1.add_at_the_end(40)
		self.assertEqual(b1.add_at_nth_position(25, 3).next.next.data, 25)
	def fonk8(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		b1.add_at_the_end(40)
		self.assertEqual(b1.add_at_nth_position(50, 6), "Invalid position, it exceeds the size of the linked list")
	def fonk9(self):
		b1 = LinkedList()
		self.assertEqual(b1.remove_at_the_begining(), "List is empty, nothing to remove")
	def fonk10(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		self.assertEqual(b1.remove_at_the_begining().data, 20)
	def fonk11(self):
		b1 = LinkedList()
		self.assertEqual(b1.remove_at_the_end(), "List is empty, nothing to remove")
	def fonk12(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		self.assertEqual(b1.remove_at_the_end(), None)
	def fonk13(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		self.assertEqual(b1.remove_at_the_end().next.data, 20)
	def fonk14(self):
		b1 = LinkedList()
		self.assertEqual(b1.remove_at_nth_position(0), "Invalid position, it can not be less than or equal to 0")
	def fonk15(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		self.assertEqual(b1.remove_at_nth_position(1).data, 20)
	def fonk16(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		b1.add_at_the_end(40)
		self.assertEqual(b1.remove_at_nth_position(3).next.next.data, 40)
	def fonk17(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		self.assertEqual(b1.remove_at_nth_position(4), "Invalid position, it exceeds the size of the linked list")
	def fonk18(self):
		b1 = LinkedList()
		self.assertEqual(b1.reverse(), "List is empty, nothing to reverse")
	def fonk19(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		b1.add_at_the_end(40)
		self.assertEqual(b1.reverse().data, 40)
	def fonk20(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		self.assertEqual(b1.reverse().data, 10)
	def fonk21(self):
		b1 = LinkedList()
		self.assertEqual(b1.reverse_using_recursion(b1.head), "List is empty, nothing to reverse")
	def fonk22(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		self.assertEqual(b1.reverse_using_recursion(b1.head).data, 10)
	def fonk23(self):
		b1 = LinkedList()
		b1.add_at_the_end(10)
		b1.add_at_the_end(20)
		b1.add_at_the_end(30)
		b1.add_at_the_end(40)
		b1.add_at_the_end(50)
		b1.add_at_the_end(60)
		self.assertEqual(b1.reverse_using_recursion(b1.head).data, 60)
if b3 = = '__main__':
	unittest.main()