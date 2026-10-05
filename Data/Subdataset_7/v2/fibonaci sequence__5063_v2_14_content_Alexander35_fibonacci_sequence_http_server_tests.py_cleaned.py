import unittest
import http_server
import json
import requests
class class1(unittest.TestCase):
    def fonk1(self):
        with open('config.json') as file:
            self.b1 = json.load(file)
    def fonk2(self):
        b2 = requests.get('http:
        b3 = b2.content
        b4 = [b"<div>[9] == 34</div>", b"<div>[10] == 55</div>", b"<div>[11] == 89</div>", b"<div>[12] == 144</div>"]
        self.assertEqual(b3, b"".join(b4))
    def fonk3(self):
        b2 = requests.get('http:
        b3 = b2.content
        b4 = [b"<div>[9] == 34</div>", b"<div>[10] == 55</div>", b"<div>[11] == 89</div>", b"<div>[12] == 144</div>"]
        self.assertEqual(b3, b"".join(b4))
if b5 = = '__main__':
    unittest.main()