import unittest
from a_star import a_star
from state import State
from collections import deque
class class1(unittest.TestCase):
    def fonk1(self):
        print('=======================')
        print('A* algorithm')
        print('=======================')
        b1 = a_star(State(red=13, blue=16, green=17))
        b2 = b1['b2']
        self.assertEqual(b2.red_count, 0)
        self.assertEqual(b2.green_count, 46)
        self.assertEqual(b2.blue_count, 0)
        b3 = b1['b3']
        print('Full b4 length: {}'.format(len(b3)))
        self.assertEqual(len(b3), 3295)
        b4 = b1['b4']
        print('Path length is {}'.format(len(b4)))
        self.assertEqual(len(b4), 17)
        a1 = 1
        for node in b4:
            print('{}:{}'.format(a1, node))
            a1 += 1
if b5 = = "__main__":
    unittest.main()