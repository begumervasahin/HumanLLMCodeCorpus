from unittest import TestCase
from flask import json
from unittest.mock import patch
from application import application
class class1(TestCase):
    def fonk1(self):
        self.b1 = application.test_client()
    def fonk2(self, b3):
        b2 = json.loads(b3.data)
        return b2.get("message")
    def fonk3(self):
        b3 = self.b1.get('/fibonacci/-1')
        self.assertEqual(b3.status_code, 400)
    def fonk4(self):
        b3 = self.b1.get('/fibonacci/-1')
        b4 = self.fonk2(b3)
        self.assertEqual('Size must be a positive integer. Actual -1', b4)
    def fonk5(self):
        b3 = self.b1.get('/fibonacci/bad')
        self.assertEqual(b3.status_code, 400)
    def fonk6(self):
        b3 = self.b1.get('/fibonacci/bad')
        b4 = self.fonk2(b3)
        self.assertEqual('Size must be a positive integer. Actual bad', b4)
    def fonk7(self):
        b3 = self.b1.get('/fibonacci/1001')
        self.assertEqual(b3.status_code, 400)
    def fonk8(self):
        b3 = self.b1.get('/fibonacci/1001')
        b4 = self.fonk2(b3)
        self.assertEqual('Size must be a positive integer <= to 1000. Actual 1001', b4)
    def fonk9(self):
        b3 = self.b1.get('/fibonacci/test/1223')
        self.assertEqual(b3.status_code, 404)
    def fonk10(self):
        b3 = self.b1.get('/fibonacci/test/1223')
        self.assertEqual(b3.content_type, 'application/json')
    def fonk11(self):
        b3 = self.b1.get('/fibonacci/0')
        self.assertEqual(b3.status_code, 200)
    def fonk12(self):
        b3 = self.b1.get('/fibonacci/0')
        b2 = json.loads(b3.data)
        b5 = b2.get("fibonacci")
        self.assertEqual(len(b5), 0)
    def fonk13(self):
        b3 = self.b1.get('/fibonacci/5')
        b2 = json.loads(b3.data)
        b5 = b2.get("fibonacci")
        self.assertEqual(b3.status_code, 200)
        self.assertEqual(b5, [0, 1, 1, 2, 3])
    def fonk14(self):
        b3 = self.b1.post('/fibonacci/0')
        self.assertEqual(b3.status_code, 405)
    def fonk15(self):
        b3 = self.b1.post('/fibonacci/0')
        self.assertEqual(b3.content_type, 'application/json')
    @patch('sequence_generators.fibonacci.generate_sequence')
    def fonk16(self, mock_generator):
        self.b1.get('/fibonacci/0')
        mock_generator.assert_called_with(0)