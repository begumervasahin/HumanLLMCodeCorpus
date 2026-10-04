import unittest
from depth_first_search import dfs
from state import State
class TestDfsAlgorithm(unittest.TestCase):
    def test_dfs_algorithm(self):
        print('=======================')
        print('DFS Algorithm')
        print('=======================')
        initial_state = State(red=13, blue=16, green=17)
        result = dfs(initial_state)
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        path = result['path']
        path_length = len(path)
        print(f'Path length: {path_length}')
        self.assertEqual(path_length, 89)
        print('Path:')
        for step in path:
            print(step)
        full_path = result['full_path']
        full_path_length = len(full_path)
        print(f'Full path length: {full_path_length}')
        self.assertEqual(full_path_length, 98)
if __name__ == "__main__":
    unittest.main()