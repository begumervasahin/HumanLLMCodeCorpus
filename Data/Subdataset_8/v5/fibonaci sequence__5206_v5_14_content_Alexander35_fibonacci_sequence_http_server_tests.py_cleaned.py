import unittest
import json
import requests
class TestHttpServer(unittest.TestCase):
    def setUp(self):
        with open('config.json') as file:
            self.config = json.load(file)
    def test_fibonacci_sequence_from_a_to_b(self):
        url = 'http:
        response = requests.get(url)
        control_sequence = response.content
        expected_sequence = [
            "<div>[9] == b'34'</div>",
            "<div>[10] == b'55'</div>",
            "<div>[11] == b'89'</div>",
            "<div>[12] == b'144'</div>"
        ]
        self.assertTrue(control_sequence, expected_sequence)
    def test_get_sequence_from_a_to_b(self):
        url = 'http:
        response = requests.get(url)
        control_sequence = response.content
        expected_sequence = [
            "<div>[9] == b'34'</div>",
            "<div>[10] == b'55'</div>",
            "<div>[11] == b'89'</div>",
            "<div>[12] == b'144'</div>"
        ]
        self.assertTrue(control_sequence, expected_sequence)
if __name__ == '__main__':
    unittest.main()