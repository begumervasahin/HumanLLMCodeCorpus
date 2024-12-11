from unittest import TestCase
from flask import json
from mock import patch
from application import application
class class1(TestCase):
    def fonk1(self):
        self.b1 = application.test_client()
    def fonk2(self):
        b2 = self.b1.get('/fibonacci/-1')
        self.assertEqual(b2.status_code, 400)
    def fonk3(self):
        b2 = self.b1.get('/fibonacci/-1')
        b3 = self.fonk16(b2)
        b4 = 'Size must be a positive integer. Actual -1'
        self.assertEqual(b4, b3)
    def fonk4(self):
        b2 = self.b1.get('/fibonacci/bad')
        self.assertEqual(b2.status_code, 400)
    def fonk5(self):
        b2 = self.b1.get('/fibonacci/bad')
        b3 = self.fonk16(b2)
        b4 = 'Size must be a positive integer. Actual bad'
        self.assertEqual(b4, b3)
    def fonk6(self):
        b2 = self.b1.get('/fibonacci/1001')
        self.assertEqual(b2.status_code, 400)
    def fonk7(self):
        b2 = self.b1.get('/fibonacci/1001')
        b3 = self.fonk16(b2)
        b4 = 'Size must be a positive integer <= to 1000. Actual 1001'
        self.assertEqual(b4, b3)
    def fonk8(self):
        b2 = self.b1.get('/fibonacci/test/1223')
        self.assertEqual(b2.status_code, 404)
    def fonk9(self):
        b2 = self.b1.get('/fibonacci/test/1223')
        self.assertEqual(b2.content_type, 'application/json')
    def fonk10(self):
        b2 = self.b1.get('/fibonacci/0')
        self.assertEqual(b2.status_code, 200)
    def fonk11(self):
        b2 = self.b1.get('/fibonacci/0')
        b5 = json.loads(b2.data)
        b6 = b5.get("fibonacci")
        self.assertEqual(len(b6), 0)
    def fonk12(self):
        b2 = self.b1.get('/fibonacci/5')
        b5 = json.loads(b2.data)
        b6 = b5.get("fibonacci")
        b7 = [0, 1, 1, 2, 3]
        self.assertEqual(b2.status_code, 200)
        self.assertEqual(b7, b6)
    def fonk13(self):
        b2 = self.b1.post('/fibonacci/0')
        self.assertEqual(b2.status_code, 405)
    def fonk14(self):
        b2 = self.b1.post('/fibonacci/0')
        self.assertEqual(b2.content_type, 'application/json')
    @patch('sequence_generators.fibonacci.generate_sequence')
    def fonk15(self, mock_generator):
        self.b1.get('/fibonacci/0')
        mock_generator.assert_called_with(0)
    def fonk16(self, b2):
        b5 = json.loads(b2.data)
        b3 = b5.get("message")
        return b3