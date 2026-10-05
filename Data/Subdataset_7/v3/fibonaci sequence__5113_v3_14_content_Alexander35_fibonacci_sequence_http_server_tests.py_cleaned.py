import unittest
import http_server
import json
import requests
class class1(unittest.TestCase):
    def fonk1(self):
        with open('b1.json') as config_file:
            self.b1 = json.load(config_file)
    def fonk2(self):
        b2 = 'http:
        b3 = requests.get(b2)
        b4 = b3.content
        b5 = [b"<div>[9] == 34</div>", b"<div>[10] == 55</div>", b"<div>[11] == 89</div>", b"<div>[12] == 144</div>"]
        self.assertEqual(b4, b"".join(b5))
    def fonk3(self):
        b2 = 'http:
        b3 = requests.get(b2)
        b4 = b3.content
        b5 = [b"<div>[9] == 34</div>", b"<div>[10] == 55</div>", b"<div>[11] == 89</div>", b"<div>[12] == 144</div>"]
        self.assertEqual(b4, b"".join(b5))
if b6 = = '__main__':
    unittest.main()