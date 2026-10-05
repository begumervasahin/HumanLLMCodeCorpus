from __future__ import division
import unittest
import hwNew
import nltk
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = [1, 2, 0, 1]
        b2 = [0, 0, 1, 1]
        self.assertEqual(hwNew.jaccard(b1, b2), 0.25)
    def fonk2(self):
        b3 = [[0.5, 0, 0, 0.2], [0.2, 0.01, 0.5, 1], [0.2, 0.4, 0, 1]]
        b4 = [0.0, 0.17609125905568124, 0.47712125471966244, 0.0]
        self.assertEqual(hwNew.BuildIdf(b3), b4)
    def fonk3(self):
        b3 = [[0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1]]
        b4 = [1, 1, 1, 1]
        self.assertEqual(hwNew.BuildIdfDummy(b3), b4)
    def fonk4(self):
        b5 = {"this": 3, "that": 5}
        b6 = {"this": 0, "that": 1, "test": 2}
        b4 = [3 / 8, 5 / 8, 0]
        self.assertEqual(hwNew.tf(b6, b5), b4)
    def fonk5(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b7 = {"test1": [10] * 25}
        b8 = {'2for': 0, 'ar': 1, 'motor': 2, 'carbon': 3, 'sharp': 4}
        b9 = [1] * 25
        b4 = [1.0, 1.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0]
        b10 = hwNew.feedback(b9, b7, b8)
        self.assertEqual(b10, b4)
        self.assertEqual(b10.count(6), 17)
    def fonk6(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b7 = {"test1": [10] * 52}
        b8 = {'clip': 0, '18-volt,': 1, '2for': 3, 'hook': 4, 'ar': 5, 'motor': 6, 'steelwir': 38, 'sharp': 8, 'mobil': 9, 'belt': 11, 'impact': 12}
        b9 = [1] * 52
        b10 = hwNew.feedback(b9, b7, b8)
        self.assertEqual(b10.count(6), 28)
if b11 = = '__main__':
    unittest.main()