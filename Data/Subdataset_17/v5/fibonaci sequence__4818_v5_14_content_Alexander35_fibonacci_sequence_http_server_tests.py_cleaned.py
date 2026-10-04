import unittest
import json
import requests
class TestHttpServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('config.json') as file:
            cls.conf = json.load(file)
        cls.base_url = f"http:
    def get_response(self, endpoint, params):
        response = requests.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    def test_fibonacci_from_a_to_b(self):
        params = {'from': 9, 'to': 13}
        control_sequence = self.get_response('fibonacci', params)
        etalon_sequence = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(control_sequence, etalon_sequence)
    def test_get_sequence_from_a_to_b(self):
        params = {'from': 9, 'to': 13}
        control_sequence = self.get_response('get-sequence', params)
        etalon_sequence = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(control_sequence, etalon_sequence)
if __name__ == '__main__':
    unittest.main()