import unittest
from huffman import *
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = {}
        b1['a'] = 1
        b1['b'] = 1
        b1['c'] = 1
        b2 = open('test1.txt', 'r')
        b3 = count_occurrences(b2)
        self.assertEqual(b1, b3)
    def fonk2(self):
        b1 = {}
        b1['1'] = 5
        b1['\n'] = 4
        b2 = open('test2.txt', 'r')
        b3 = count_occurrences(b2)
        self.assertEqual(b1, b3)
    def fonk3(self):
        b1 = {}
        for char in 'what\'s up?':
            b1[char] = 1
        b2 = open('test3.txt', 'r')
        b3 = count_occurrences(b2)
        self.assertEqual(b1, b3)
    def fonk4(self):
        b4 = {}
        b4['a'] = 1
        b4['b'] = 6
        b4['c'] = 2
        b1 = Node(9, Leaf('b', 6), Node(3, Leaf('c', 2), Leaf('a', 1)))
        b3 = tree_from_dict(b4)
        self.assertEqual(b1, b3)
    def fonk5(self):
        b4 = {}
        b4['a'] = 1
        b4['b'] = 1
        b4['c'] = 1
        b1 = Node(3, Node(2, Leaf('b', 1), Leaf('a', 1)), Leaf('c', 1))
        b3 = tree_from_dict(b4)
        self.assertEqual(b1, b3)
    def fonk6(self):
        b4 = {}
        b4[' '] = 5
        b4['\n'] = 2
        b4['a'] = 1
        b4['1'] = 4
        b4['?'] = 3
        b1 = Node(15, Node(9, Leaf(' ', 5), Leaf('1', 4)),
                            Node(6,
                                 Node(3, Leaf('\n', 2), Leaf('a', 1)),
                                 Leaf('?', 3)))
        b3 = tree_from_dict(b4)
        self.assertEqual(b1, b3)
    def fonk7(self):
        b5 = Leaf('a', 2)
        b6 = Leaf('b', 1)
        self.assertEqual(hufftree_lt(b5, b6), 1)
    def fonk8(self):
        b7 = Leaf('abc', 3)
        b8 = Node(3, None, None)
        self.assertEqual(hufftree_lt(b7, b8), 0)
    def fonk9(self):
        b9 = Node(3, None, None)
        b10 = Node(2, None, None)
        self.assertEqual(hufftree_lt(b10, b9), -1)
    def fonk10(self):
        b2 = open('test4.txt', 'r')
        b11 = {}
        b11['a'] = 2
        b11['b'] = 3
        b11['c'] = 1
        b11['d'] = 4
        b12 = tree_from_dict(b11)
        b3 = codes_from_tree(b12)
        b1 = {}
        b1['a'] = '000'
        b1['b'] = '01'
        b1['c'] = '001'
        b1['d'] = '1'
        self.assertEqual(b1, b3)
        b13 = encoding(b2, b1)
        b14 = '0000100110000110111'
        self.assertEqual(b13, b14)
    def fonk11(self):
        b11 = {}
        b11['a'] = 2
        b11['b'] = 3
        b12 = tree_from_dict(b11)
        b3 = codes_from_tree(b12)
        b1 = {}
        b1['a'] = '1'
        b1['b'] = '0'
        self.assertEqual(b1, b3)
    def fonk12(self):
        b4 = open('test1.txt', 'r')
        b15 = open('output1.txt', 'w')
        b16 = count_occurrences(b4)
        b17 = tree_from_dict(b16)
        b18 = codes_from_tree(b17)
        b19 = encoding(b4, b18)
        b15.write(b19)
        b4.close()
        b15.close()
if b20 = = '__main__':
    unittest.main()