from LinkedList import LinkedList
import unittest
class class1(unittest.TestCase):
    def fonk1(self):
        self.b1 = LinkedList()
    def fonk2(self):
        self.b1.add_at_the_beginning(10)
        self.assertEqual(self.b1.add_at_the_beginning(20).data, 20)
    def fonk3(self):
        self.b1.add_at_the_beginning(10)
        self.b1.add_at_the_beginning(20)
        self.assertEqual(self.b1.add_at_the_beginning(30).data, 30)
    def fonk4(self):
        self.assertEqual(self.b1.add_at_the_end(500).data, 500)
    def fonk5(self):
        self.b1.add_at_the_end(10)
        self.b1.add_at_the_end(20)
        b2 = self.b1.head.next
        self.assertEqual(b2.data, 20)
if b3 = = '__main__':
    unittest.main()