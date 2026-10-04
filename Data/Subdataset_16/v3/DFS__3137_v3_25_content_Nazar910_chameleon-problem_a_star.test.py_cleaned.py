import unittest
from a_star import a_star
from state import State
class class1(unittest.TestCase):
    def fonk1(self):
        print('=======================')
        print('A* Algorithm')
        print('=======================')
        b1 = State(red=13, blue=16, green=17)
        b2 = a_star(b1)
        b3 = b2['b3']
        self.assertEqual(b3.red_count, 0)
        self.assertEqual(b3.green_count, 46)
        self.assertEqual(b3.blue_count, 0)
        b4 = b2['b4']
        b5 = len(b4)
        print(f'Full path length: {b5}')
        self.assertEqual(b5, 3295)
        b6 = b2['path']
        b7 = len(b6)
        print(f'Simplified path length: {b7}')
        self.assertEqual(b7, 17)
        for i, node in enumerate(b6, b8 = 1):
            print(f'{i}: {node}')
if b9 = = "__main__":
    unittest.main()