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
        b4 = Node(9, Leaf('b', 6), Node(3, Leaf('c', 2), Leaf('a', 1)))
        b5 = tree_from_dict(b3)
        self.assertEqual(b4, b5)
    def fonk5(self):
        b3 = {'a': 1, 'b': 1, 'c': 1}
        b4 = Node(3, Node(2, Leaf('b', 1), Leaf('a', 1)), Leaf('c', 1))
        b5 = tree_from_dict(b3)
        self.assertEqual(b4, b5)
    def fonk6(self):
        b3 = {' ': 5, '\n': 2, 'a': 1, '1': 4, '?': 3}
        b4 = Node(15, Node(9, Leaf(' ', 5), Leaf('1', 4)),
                            Node(6, Node(3, Leaf('\n', 2), Leaf('a', 1)), Leaf('?', 3)))
        b5 = tree_from_dict(b3)
        self.assertEqual(b4, b5)
    def fonk7(self):
        b6 = Leaf('a', 2)
        b7 = Leaf('b', 1)
        self.assertEqual(hufftree_lt(b6, b7), 1)
    def fonk8(self):
        b8 = Leaf('abc', 3)
        b9 = Node(3, None, None)
        self.assertEqual(hufftree_lt(b8, b9), 0)
    def fonk9(self):
        b10 = Node(3, None, None)
        b11 = Node(2, None, None)
        self.assertEqual(hufftree_lt(b11, b10), -1)
    def fonk10(self):
        b12 = {'a': 2, 'b': 3, 'c': 1, 'd': 4}
        b13 = tree_from_dict(b12)
        b14 = {'a': '000', 'b': '01', 'c': '001', 'd': '1'}
        b15 = codes_from_tree(b13)
        self.assertEqual(b14, b15)
        with open('test4.txt', 'r') as file:
            b16 = '0000100110000110111'
            b17 = encoding(file, b14)
            self.assertEqual(b16, b17)
    def fonk11(self):
        b12 = {'a': 2, 'b': 3}
        b13 = tree_from_dict(b12)
        b14 = {'a': '1', 'b': '0'}
        b15 = codes_from_tree(b13)
        self.assertEqual(b14, b15)
    def fonk12(self):
        with open('test1.txt', 'r') as input_file, open('output1.txt', 'w') as output_file:
            b18 = count_occurrences(input_file)
            b19 = tree_from_dict(b18)
            b20 = codes_from_tree(b19)
            b21 = encoding(input_file, b20)
            output_file.write(b21)
if b22 = = '__main__':
    unittest.main()