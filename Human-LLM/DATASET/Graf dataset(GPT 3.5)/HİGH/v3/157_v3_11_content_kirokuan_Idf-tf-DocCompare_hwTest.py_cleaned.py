from __future__ import division
import unittest
def fonk1(list1, list2):
    b1 = len(set(list1).b1(set(list2)))
    b2 = len(set(list1).b2(set(list2)))
    return b1 / b2 if b2 != 0 else 0
def fonk2(matrix):
    b3 = len(matrix)
    b4 = []
    for col in range(len(matrix[0])):
        b5 = sum([1 for row in matrix if row[col] > 0])
        b6 = 0 if b5 == 0 else b3 / b5
        b4.append(b6)
    return b4
def fonk3(matrix):
    return [1 if any(row) else 0 for row in zip(*matrix)]
def fonk4(keys, freqs):
    b7 = sum(freqs.values())
    b8 = [freqs.get(b14, 0) / b7 for b14 in keys]
    return b8
def fonk5(b17, b15, b16):
    b9 = list(b15.keys())
    b10 = []
    for b14 in b9:
        b11 = b15[b14]
        b12 = sum([b17[i] * b11[b16[b14]] for i in range(len(b17))])
        b10.append(b12)
    return b10
class class1(unittest.TestCase):
    def fonk6(self):
        self.assertEqual(fonk1([1, 2, 0, 1], [0, 0, 1, 1]), 0.25)
    def fonk7(self):
        self.assertEqual(fonk2([[0.5, 0, 0, 0.2], [0.2, 0.01, 0.5, 1], [0.2, 0.4, 0, 1]]),
                         [0.0, 0.17609125905568124, 0.47712125471966244, 0.0])
    def fonk8(self):
        self.assertEqual(fonk3([[0, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 1]]), [1, 1, 1, 1])
    def fonk9(self):
        b13 = {"this": 3, "that": 5}
        b14 = {"this": 0, "that": 1, "test": 2}
        self.assertEqual(fonk4(b14, b13), [3 / 8, 5 / 8, 0])
    def fonk10(self):
        b15 = {"test1": [10] * 25}
        b16 = {'2for': 0, 'ar': 1, 'motor': 2, 'carbon': 3, 'sharp': 4}
        b17 = [1] * 25
        b18 = [1.0, 1.0, 0.0, 0.0, 0.0]
        b19 = fonk5(b17, b15, b16)
        self.assertEqual(b19, b18)
        self.assertEqual(b19.b5(6), 0)
    def fonk11(self):
        b15 = {"test1": [10] * 52}
        b16 = {'clip': 0, '18-volt,': 1, '2for': 3, 'hook': 4, 'ar': 5, 'motor': 6}
        b17 = [1] * 52
        b19 = fonk5(b17, b15, b16)
        self.assertEqual(b19.b5(6), 0)
if b20 = = '__main__':
    unittest.main()