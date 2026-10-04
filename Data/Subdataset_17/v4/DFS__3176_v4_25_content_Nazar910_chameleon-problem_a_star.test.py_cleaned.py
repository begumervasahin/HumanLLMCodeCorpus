import unittest
from a_star import a_star
from state import State
class TestAStarAlgorithm(unittest.TestCase):
    def test_result(self):
        print('=======================')
        print('A* Algorithm')
        print('=======================')
        initial_state = State(red=13, blue=16, green=17)
        result = a_star(initial_state)
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        full_path = result['full_path']
        full_path_length = len(full_path)
        print(f'Full path length: {full_path_length}')
        self.assertEqual(full_path_length, 3295)
        path = result['path']
        path_length = len(path)
        print(f'Path length: {path_length}')
        self.assertEqual(path_length, 17)
        for i, node in enumerate(path, start=1):
            print(f'{i}: {node}')
if __name__ == "__main__":
    unittest.main()