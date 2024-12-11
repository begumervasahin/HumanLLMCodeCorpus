import unittest
from huffman import *
class class1(unittest.TestCase):
    def fonk1(self):
        b1 = {'a': 1, 'b': 1, 'c': 1}
        with open('test1.txt', 'r') as file:
            b2 = count_occurrences(file)
        self.assertEqual(b1, b2)
    def fonk2(self):
        b1 = {'1': 5, '\n': 4}
        with open('test2.txt', 'r') as file:
            b2 = count_occurrences(file)
        self.assertEqual(b1, b2)
    def fonk3(self):
        b1 = {char: 1 for char in "what's up?"}
        with open('test3.txt', 'r') as file:
            b2 = count_occurrences(file)
        self.assertEqual(b1, b2)
    def fonk4(self):
        b3 = {'a': 1, 'b': 6, 'c': 2}
        b1 = Node(9, Leaf('b', 6), Node(3, Leaf('c', 2), Leaf('a', 1)))
        b2 = tree_from_dict(b3)
        self.assertEqual(b1, b2)
    def fonk5(self):
        b3 = {'a': 1, 'b': 1, 'c': 1}
        b1 = Node(3, Node(2, Leaf('b', 1), Leaf('a', 1)), Leaf('c', 1))
        b2 = tree_from_dict(b3)
        self.assertEqual(b1, b2)
    def fonk6(self):
        b3 = {' ': 5, '\n': 2, 'a': 1, '1': 4, '?': 3}
        b1 = Node(15, Node(9, Leaf(' ', 5), Leaf('1', 4)),
                        Node(6, Node(3, Leaf('\n', 2), Leaf('a', 1)), Leaf('?', 3)))
        b2 = tree_from_dict(b3)
        self.assertEqual(b1, b2)
    def fonk7(self):
        b4 = Leaf('a', 2)
        b5 = Leaf('b', 1)
        self.assertEqual(hufftree_lt(b4, b5), 1)
    def fonk8(self):
        b6 = Leaf('abc', 3)
        b7 = Node(3, None, None)
        self.assertEqual(hufftree_lt(b6, b7), 0)
    def fonk9(self):
        b8 = Node(3, None, None)
        b9 = Node(2, None, None)
        self.assertEqual(hufftree_lt(b9, b8), -1)
    def fonk10(self):
        with open('test4.txt', 'r') as file:
            b10 = {'a': 2, 'b': 3, 'c': 1, 'd': 4}
            b11 = tree_from_dict(b10)
            b12 = codes_from_tree(b11)
            b13 = {'a': '000', 'b': '01', 'c': '001', 'd': '1'}
            self.assertEqual(b13, b12)
            b14 = encoding(file, b13)
            b15 = '0000100110000110111'
            self.assertEqual(b14, b15)
    def fonk11(self):
        b10 = {'a': 2, 'b': 3}
        b11 = tree_from_dict(b10)
        b2 = codes_from_tree(b11)
        b1 = {'a': '1', 'b': '0'}
        self.assertEqual(b1, b2)
    def fonk12(self):
        b16 = 'test1.txt'
        b17 = 'output1.txt'
        with open(b16, 'r') as input, open(b17, 'w') as output:
            b18 = count_occurrences(input)
            b19 = tree_from_dict(b18)
            b20 = codes_from_tree(b19)
            b21 = encoding(input, b20)
            output.write(b21)
if b22 = = '__main__':
    unittest.main()