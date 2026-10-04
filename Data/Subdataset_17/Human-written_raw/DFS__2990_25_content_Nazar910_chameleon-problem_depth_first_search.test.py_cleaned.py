import unittest
from depth_first_search import dfs
from state import State
from collections import deque
class TestDfs(unittest.TestCase):
    def test_result(self):
        print('=======================')
        print('DFS algorithm')
        print('=======================')
        result = dfs(State(red=13, blue=16, green=17))
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        path = result['path']
        self.assertEqual(len(path), 89)
        print('Path length: {}'.format(len(path)))
        print('Path')
        for p in result['path']:
            print(p)
        full_path = result['full_path']
        self.assertEqual(len(full_path), 98)
        print('Full path length: {}'.format(len(full_path)))
if __name__ == "__main__":
    unittest.main()