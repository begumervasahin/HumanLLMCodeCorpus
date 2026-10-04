from __future__ import division
import unittest
import hwNew
import nltk
class class1(unittest.TestCase):
    def fonk1(self):
        self.assertEqual(hwNew.jaccard([1, 2, 0, 1], [0, 0, 1, 1]), 0.25)
    def fonk2(self):
        self.assertEqual(hwNew.BuildIdf([[0.5, 0, 0, 0.2],
                                         [0.2, 0.01, 0.5, 1],
                                         [0.2, 0.4, 0, 1]]),
                         [0.0, 0.17609125905568124, 0.47712125471966244, 0.0])
    def fonk3(self):
        self.assertEqual(hwNew.BuildIdfDummy([[0, 0, 0, 1],
                                              [0, 0, 1, 1],
                                              [1, 1, 0, 1]]),
                         [1, 1, 1, 1])
    def fonk4(self):
        b1 = {"this": 3, "that": 5}
        b2 = {"this": 0, "that": 1, "test": 2}
        self.assertEqual(hwNew.tf(b2, b1), [3 / 8, 5 / 8, 0])
    def fonk5(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b3 = {"test1": [10] * 25}
        b4 = {'2for': 0, 'ar': 1, 'motor': 2, 'carbon': 3, 'sharp': 4, 'b': 5, 'c': 6, 'd': 7, 'e': 8, 'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'l': 15, 'm': 16, 'n': 17, 'o': 18, 'p': 19, 'q': 20, 'r': 21, 's': 22, 't': 23, 'u': 24}
        b5 = [1] * 25
        b6 = [1.0, 1.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 1.0, 1.0, 6.0, 6.0, 6.0, 6.0]
        b7 = hwNew.feedback(b5, b3, b4)
        self.assertEqual(b7, b6)
        self.assertEqual(b7.count(6), 17)
    def fonk6(self):
        nltk.data.path.append("/media/sf_shared/nltk")
        b3 = {"test1": [10] * 52}
        b4 = {'clip': 0, '18-volt,': 1, '2for': 2, 'hook': 3, 'ar': 4, 'motor': 5, 'steelwir': 6, 'sharp': 7, 'mobil': 8, 'belt': 9, 'impact': 10, 'another': 11, 'other': 12, 'words': 13, 'to': 14, 'fill': 15, 'up': 16, 'the': 17, 'position': 18, 'with': 19, 'dummy': 20, 'values': 21, 'in': 22, 'test': 23, 'case': 24, 'more': 25, 'random': 26, 'stuff': 27, 'for': 28, 'the': 29, 'test': 30, 'making': 31, 'sure': 32, 'to': 33, 'have': 34, '52': 35, 'positions': 36, 'including': 37, 'all': 38, 'these': 39, 'additional': 40, 'dummy': 41, 'words': 42, 'that': 43, 'are': 44, 'here': 45, 'to': 46, 'ensure': 47, 'we': 48, 'cover': 49, 'all': 50, 'cases': 51}
        b5 = [1] * 52
        b7 = hwNew.feedback(b5, b3, b4)
        self.assertEqual(b7.count(6), 28)
if b8 = = '__main__':
    unittest.main()