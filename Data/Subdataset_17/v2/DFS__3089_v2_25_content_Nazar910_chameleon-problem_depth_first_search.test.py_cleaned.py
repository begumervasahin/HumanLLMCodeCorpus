import unittest
from depth_first_search import dfs
from state import State
class TestDFSAlgorithm(unittest.TestCase):
    def test_dfs_algorithm(self):
        self._print_header()
        initial_state = State(red=13, blue=16, green=17)
        result = dfs(initial_state)
        self._assert_final_state(result['final_state'])
        self._print_and_assert_path(result['path'], expected_length=89, description='Path')
        self._print_and_assert_path(result['full_path'], expected_length=98, description='Full path')
    def _print_header(self):
        print('=======================')
        print('DFS Algorithm')
        print('=======================')
    def _assert_final_state(self, final_state):
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
    def _print_and_assert_path(self, path, expected_length, description):
        path_length = len(path)
        print(f'{description} length: {path_length}')
        self.assertEqual(path_length, expected_length)
        if description == 'Path':
            print(f'{description}:')
            for step in path:
                print(step)
if __name__ == "__main__":
    unittest.main()