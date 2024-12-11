from __future__ import division
import unittest
import hwNew
import nltk
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertEqual(hwNew.jaccard([1, 2, 0, 1], [0, 0, 1, 1]), 0.25)
    def fonk2(self):
        self.assertEqual(hwNew.BuildIdf([[0.5, 0, 0, 0.2], [0.2, 0.01, 0.5, 1], [0.2, 0.4, 0, 1]]),
                         [0.0, 0.17609125905568124, 0.47712125471966244, 0.0])
    def fonk3(self):
        self.assertEqual(hwNew.BuildIdfDummy([[0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1]]), [1, 1, 1, 1])
    def fonk4(self):
        b1 = {"this": 3, "that": 5}
        b2 = {"this": 0, "that": 1, "test": 2}
        self.assertEqual(hwNew.tf(b2, b1), [3 / 8, 5 / 8, 0])
    def fonk5(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b3 = {"test1": [10] * 25}
        b4 = {'2for': 0, 'ar': 1, 'motor': 2, 'carbon': 3, 'sharp': 4}
        b5 = [1] * 25
        b6 = [1.0, 1.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0,
                  1.0, 6.0, 6.0, 6.0, 6.0]
        b7 = hwNew.feedback(b5, b3, b4)
        self.assertEqual(b7, b6)
        self.assertEqual(b7.count(6), 17)
    def fonk6(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b3 = {"test1": [10] * 52}
        b4 = {'clip': 0, '18-volt,': 1, '2for': 3, 'hook': 4, 'ar': 5, 'motor': 6, 'steelwir': 38,
                        'sharp': 8, 'mobil': 9, 'belt': 11, 'impact': 12}
        b5 = [1] * 52
        b7 = hwNew.feedback(b5, b3, b4)
        self.assertEqual(b7.count(6), 28)
if b8 = = '__main__':
    unittest.main()