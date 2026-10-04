import unittest
import json
import requests
class TestHttpServer(unittest.TestCase):
    def setUp(self):
        with open('config.json') as file:
            self.conf = json.load(file)
    def test_fibonacci_from_a_to_b(self):
        url = f"http:
        response = requests.get(url)
        control_sequence = response.json()
        etalon_sequence = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(control_sequence, etalon_sequence)
    def test_get_sequence_from_a_to_b(self):
        url = f"http:
        response = requests.get(url)
        control_sequence = response.json()
        etalon_sequence = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(control_sequence, etalon_sequence)
if __name__ == '__main__':
    unittest.main()