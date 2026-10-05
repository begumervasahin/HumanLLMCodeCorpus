import unittest
from fibonacci import Fibonacci
import json
class TestFibonacci(unittest.TestCase):
    def setUp(self):
        with open('config.json') as file:
            config_data = json.load(file)
        self.fibonacci_instance = Fibonacci(config_data['redis_host'], config_data['redis_db'])
    def test_generate_numbers(self):
        self.fibonacci_instance.numbers(9, 13)
        generated_sequence = self.fibonacci_instance.control(9, 13)
        expected_sequence = [
            "<div>[9] == b'34'</div>",
            "<div>[10] == b'55'</div>",
            "<div>[11] == b'89'</div>",
            "<div>[12] == b'144'</div>"
        ]
        self.assertEqual(generated_sequence, expected_sequence)
    def test_starter_sequence(self):
        initial_sequence = self.fibonacci_instance.control(1, 3)
        expected_initial_sequence = [
            "<div>[1] == b'1'</div>",
            "<div>[2] == b'1'</div>"
        ]
        self.assertEqual(initial_sequence, expected_initial_sequence)
if __name__ == '__main__':
    unittest.main()