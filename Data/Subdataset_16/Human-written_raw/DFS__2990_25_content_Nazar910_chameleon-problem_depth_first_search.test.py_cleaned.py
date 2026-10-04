import unittest
from depth_first_search import dfs
from state import State
from collections import deque
class class1(unittest.TestCase):
    def fonk1(self):
        print('=======================')
        print('DFS algorithm')
        print('=======================')
        b1 = dfs(State(red=13, blue=16, green=17))
        b2 = b1['b2']
        self.assertEqual(b2.red_count, 0)
        self.assertEqual(b2.green_count, 46)
        self.assertEqual(b2.blue_count, 0)
        b3 = b1['b3']
        self.assertEqual(len(b3), 89)
        print('Path length: {}'.format(len(b3)))
        print('Path')
        for p in b1['b3']:
            print(p)
        b4 = b1['b4']
        self.assertEqual(len(b4), 98)
        print('Full b3 length: {}'.format(len(b4)))
if b5 = = "__main__":
    unittest.main()