import unittest
from LinkedList import LinkedList
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = LinkedList()
    def fonk2(self):
        b2 = self.b1.add_at_the_beginning(10)
        self.assertEqual(b2.data, 10)
    def fonk3(self):
        self.b1.add_at_the_beginning(10)
        b2 = self.b1.add_at_the_beginning(20)
        self.assertEqual(b2.data, 20)
    def fonk4(self):
        b2 = self.b1.add_at_the_end(500)
        self.assertEqual(b2.data, 500)
    def fonk5(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        b3 = self.b1.head.next
        self.assertEqual(b3.data, 20)
    def fonk6(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        b2 = self.b1.add_at_nth_position(5, 1)
        self.assertEqual(b2.data, 5)
    def fonk7(self):
        b2 = self.b1.add_at_nth_position(5, 0)
        self.assertEqual(b2, "Invalid position, it cannot be less than or equal to 0")
    def fonk8(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        self.b1.add_at_the_end(40)
        b2 = self.b1.add_at_nth_position(25, 3)
        self.assertEqual(self.b1.head.next.next.data, 25)
    def fonk9(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        self.b1.add_at_the_end(40)
        b2 = self.b1.add_at_nth_position(50, 6)
        self.assertEqual(b2, "Invalid position, it exceeds the size of the linked list")
    def fonk10(self):
        b2 = self.b1.remove_at_the_beginning()
        self.assertEqual(b2, "List is empty, nothing to remove")
    def fonk11(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        b2 = self.b1.remove_at_the_beginning()
        self.assertEqual(b2.data, 20)
    def fonk12(self):
        b2 = self.b1.remove_at_the_end()
        self.assertEqual(b2, "List is empty, nothing to remove")
    def fonk13(self):
        self.b1.add_at_the_end(10)
        b2 = self.b1.remove_at_the_end()
        self.assertEqual(b2, None)
    def fonk14(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        b2 = self.b1.remove_at_the_end()
        self.assertEqual(self.b1.head.next.next, None)
    def fonk15(self):
        b2 = self.b1.remove_at_nth_position(0)
        self.assertEqual(b2, "Invalid position, it cannot be less than or equal to 0")
    def fonk16(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        b2 = self.b1.remove_at_nth_position(1)
        self.assertEqual(b2.data, 20)
    def fonk17(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        self.b1.add_at_the_end(40)
        b2 = self.b1.remove_at_nth_position(3)
        self.assertEqual(self.b1.head.next.next.data, 40)
    def fonk18(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        b2 = self.b1.remove_at_nth_position(4)
        self.assertEqual(b2, "Invalid position, it exceeds the size of the linked list")
    def fonk19(self):
        b2 = self.b1.reverse()
        self.assertEqual(b2, "List is empty, nothing to reverse")
    def fonk20(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        self.b1.add_at_the_end(40)
        b2 = self.b1.reverse()
        self.assertEqual(self.b1.head.data, 40)
    def fonk21(self):
        self.b1.add_at_the_end(10)
        b2 = self.b1.reverse()
        self.assertEqual(self.b1.head.data, 10)
    def fonk22(self):
        b2 = self.b1.reverse_using_recursion(self.b1.head)
        self.assertEqual(b2, "List is empty, nothing to reverse")
    def fonk23(self):
        self.b1.add_at_the_end(10)
        b2 = self.b1.reverse_using_recursion(self.b1.head)
        self.assertEqual(self.b1.head.data, 10)
    def fonk24(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        self.b1.add_at_the_end(30)
        self.b1.add_at_the_end(40)
        self.b1.add_at_the_end(50)
        self.b1.add_at_the_end(60)
        b2 = self.b1.reverse_using_recursion(self.b1.head)
        self.assertEqual(self.b1.head.data, 60)
if b4 = = '__main__':
    unittest.main()