import unittest
from huffman import *
class TestHuffmanEncoding(unittest.TestCase):
    def test_count_occurrences_simple(self):
        expected = {'a': 1, 'b': 1, 'c': 1}
        with open('test1.txt', 'r') as file:
            result = count_occurrences(file)
        self.assertEqual(result, expected)
    def test_count_occurrences_with_newlines(self):
        expected = {'1': 5, '\n': 4}
        with open('test2.txt', 'r') as file:
            result = count_occurrences(file)
        self.assertEqual(result, expected)
    def test_count_occurrences_with_spaces(self):
        expected = {char: 1 for char in "what's up?"}
        with open('test3.txt', 'r') as file:
            result = count_occurrences(file)
        self.assertEqual(result, expected)
    def test_tree_from_dict_three_entries(self):
        input_dict = {'a': 1, 'b': 6, 'c': 2}
        expected = Node(9, Leaf('b', 6), Node(3, Leaf('c', 2), Leaf('a', 1)))
        result = tree_from_dict(input_dict)
        self.assertEqual(result, expected)
    def test_tree_from_dict_equal_frequency(self):
        input_dict = {'a': 1, 'b': 1, 'c': 1}
        expected = Node(3, Node(2, Leaf('b', 1), Leaf('a', 1)), Leaf('c', 1))
        result = tree_from_dict(input_dict)
        self.assertEqual(result, expected)
    def test_tree_from_dict_multiple_entries(self):
        input_dict = {' ': 5, '\n': 2, 'a': 1, '1': 4, '?': 3}
        expected = Node(
            15,
            Node(9, Leaf(' ', 5), Leaf('1', 4)),
            Node(6, Node(3, Leaf('\n', 2), Leaf('a', 1)), Leaf('?', 3))
        )
        result = tree_from_dict(input_dict)
        self.assertEqual(result, expected)
    def test_hufftree_comparator_two_leaves(self):
        leaf1 = Leaf('a', 2)
        leaf2 = Leaf('b', 1)
        self.assertEqual(hufftree_lt(leaf1, leaf2), 1)
    def test_hufftree_comparator_leaf_and_node(self):
        leaf = Leaf('abc', 3)
        node = Node(3, None, None)
        self.assertEqual(hufftree_lt(leaf, node), 0)
    def test_hufftree_comparator_two_nodes(self):
        node1 = Node(3, None, None)
        node2 = Node(2, None, None)
        self.assertEqual(hufftree_lt(node2, node1), -1)
    def test_huffman_encoding_with_multiple_chars(self):
        with open('test4.txt', 'r') as file:
            input_dict = {'a': 2, 'b': 3, 'c': 1, 'd': 4}
            expected_codes = {'a': '000', 'b': '01', 'c': '001', 'd': '1'}
            huffman_tree = tree_from_dict(input_dict)
            result_codes = codes_from_tree(huffman_tree)
            self.assertEqual(result_codes, expected_codes)
            file.seek(0)
            encoded_string = encoding(file, expected_codes)
            expected_string = '0000100110000110111'
            self.assertEqual(encoded_string, expected_string)
    def test_huffman_encoding_two_chars(self):
        input_dict = {'a': 2, 'b': 3}
        expected_codes = {'a': '1', 'b': '0'}
        huffman_tree = tree_from_dict(input_dict)
        result_codes = codes_from_tree(huffman_tree)
        self.assertEqual(result_codes, expected_codes)
    def test_full_workflow(self):
        with open('test1.txt', 'r') as input_file, open('output1.txt', 'w') as output_file:
            occurrences = count_occurrences(input_file)
            huffman_tree = tree_from_dict(occurrences)
            char_codes = codes_from_tree(huffman_tree)
            input_file.seek(0)
            encoded_string = encoding(input_file, char_codes)
            output_file.write(encoded_string)
if __name__ == '__main__':
    unittest.main()