from LinkedList import LinkedList
import unittest
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = LinkedList()
        b1.add_at_the_beginning(10)
        self.assertEqual(b1.add_at_the_beginning(20).data, 20)
    def fonk2(self):
        b1 = LinkedList()
        b1.add_at_the_beginning(10)
        b1.add_at_the_beginning(20)
        self.assertEqual(b1.add_at_the_beginning(30).data, 30)
    def fonk3(self):
        b1 = LinkedList()
        self.assertEqual(b1.add_at_the_end(500).data, 500)
    def fonk4(self):
        b1 = LinkedList()
        b1.add_at_the_end(10)
        b1.add_at_the_end(20)
        b2 = b1.head.next
        self.assertEqual(b2.data, 20)
if b3 = = '__main__':
    unittest.main()