import unittest
from a_star import a_star
from state import State
class TestAStar(unittest.TestCase):
    def test_result(self):
        print('=======================')
        print('A* Algorithm')
        print('=======================')
        result = a_star(State(red=13, blue=16, green=17))
        final_state = result['final_state']
        self.assertEqual(final_state.red_count, 0)
        self.assertEqual(final_state.green_count, 46)
        self.assertEqual(final_state.blue_count, 0)
        full_path = result['full_path']
        print('Full path length: {}'.format(len(full_path)))
        self.assertEqual(len(full_path), 3295)
        path = result['path']
        print('Path length: {}'.format(len(path)))
        self.assertEqual(len(path), 17)
        for i, node in enumerate(path, start=1):
            print('{}: {}'.format(i, node))
if __name__ == "__main__":
    unittest.main()