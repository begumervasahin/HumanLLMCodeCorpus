import unittest
import json
from fibonacci import Fibonacci
class class1(unittest.TestCase):
    def fonk1(self):
        with open('b1.json') as file:
            b1 = json.load(file)
        self.b2 = Fibonacci(b1['redis_host'], b1['redis_db'])
    def fonk2(self):
        self.b2.ensure_numbers(9, 13)
        b3 = self.b2.control(9, 13)
        b4 = [
            "<div>[9] == b'34'</div>",
            "<div>[10] == b'55'</div>",
            "<div>[11] == b'89'</div>",
            "<div>[12] == b'144'</div>"
        ]
        self.assertEqual(b3, b4)
    def fonk3(self):
        b3 = self.b2.control(1, 3)
        b4 = [
            "<div>[1] == b'1'</div>",
            "<div>[2] == b'1'</div>"
        ]
        self.assertEqual(b3, b4)
if b5 = = '__main__':
    unittest.main()