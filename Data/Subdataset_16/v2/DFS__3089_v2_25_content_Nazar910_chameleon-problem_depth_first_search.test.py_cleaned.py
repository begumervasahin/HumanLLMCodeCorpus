import unittest
from depth_first_search import dfs
from state import State
class class1(unittest.TestCase):
    def fonk1(self):
        self.fonk2()
        b1 = State(red=13, blue=16, green=17)
        b2 = dfs(b1)
        self.fonk3(b2['final_state'])
        self.fonk4(b2['path'], b3 = 89, b5='Path')
        self.fonk4(b2['full_path'], b3 = 98, b5='Full path')
    def fonk2(self):
        print('=======================')
        print('DFS Algorithm')
        print('=======================')
    def fonk3(self, final_state):
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
    def fonk4(self, path, b3, b5):
        b4 = len(path)
        print(f'{b5} length: {b4}')
        self.assertEqual(b4, b3)
        if b5 = = 'Path':
            print(f'{b5}:')
            for step in path:
                print(step)
if b6 = = "__main__":
    unittest.main()