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
		b4 = ["<div>[9] == b'34'</div>", "<div>[10] == b'55'</div>", "<div>[11] == b'89'</div>", "<div>[12] == b'144'</div>"]
		self.assertTrue(b3, b4)
	def fonk3(self):
		b2 = requests.get('http:
		b3 = b2.content
		b4 = ["<div>[9] == b'34'</div>", "<div>[10] == b'55'</div>", "<div>[11] == b'89'</div>", "<div>[12] == b'144'</div>"]
		self.assertTrue(b3, b4)
if b5 = = '__main__':
	unittest.main()