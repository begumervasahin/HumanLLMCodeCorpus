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
        print(f'Full b5 length: {len(b4)}')
        self.assertEqual(len(b4), 3295)
        b5 = b2['b5']
        print(f'Path length: {len(b5)}')
        self.assertEqual(len(b5), 17)
        for i, node in enumerate(b5, b6 = 1):
            print(f'{i}: {node}')
if b7 = = "__main__":
    unittest.main()