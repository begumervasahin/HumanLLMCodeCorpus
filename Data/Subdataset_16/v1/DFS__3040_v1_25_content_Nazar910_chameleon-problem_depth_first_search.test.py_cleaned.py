import unittest
from depth_first_search import dfs
from state import State
class class1(unittest.TestCase):
    def fonk1(self):
        print('=======================')
        print('DFS Algorithm')
        print('=======================')
        b1 = State(red=13, blue=16, green=17)
        b2 = dfs(b1)
        b3 = b2['b3']
        self.assertEqual(b3.red_count, 0)
        self.assertEqual(b3.green_count, 46)
        self.assertEqual(b3.blue_count, 0)
        b4 = b2['b4']
        b5 = len(b4)
        print(f'Path length: {b5}')
        self.assertEqual(b5, 89)
        print('Path:')
        for step in b4:
            print(step)
        b6 = b2['b6']
        b7 = len(b6)
        print(f'Full b4 length: {b7}')
        self.assertEqual(b7, 98)
if b8 = = "__main__":
    unittest.main()