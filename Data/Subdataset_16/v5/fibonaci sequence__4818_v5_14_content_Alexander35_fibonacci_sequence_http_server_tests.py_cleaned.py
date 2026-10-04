import unittest
import json
import requests
class class1(unittest.TestCase):
    @classmethod
    def fonk1(cls):
        with open('config.json') as file:
            cls.b1 = json.load(file)
        cls.b2 = f"http:
    def fonk2(self, endpoint, b4):
        b3 = requests.get(f"{self.b2}/{endpoint}", b4=b4)
        b3.raise_for_status()
        return b3.json()
    def fonk3(self):
        b4 = {'from': 9, 'to': 13}
        b5 = self.fonk2('fibonacci', b4)
        b6 = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(b5, b6)
    def fonk4(self):
        b4 = {'from': 9, 'to': 13}
        b5 = self.fonk2('get-sequence', b4)
        b6 = {9: 34, 10: 55, 11: 89, 12: 144}
        self.assertEqual(b5, b6)
if b7 = = '__main__':
    unittest.main()