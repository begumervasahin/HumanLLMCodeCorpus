import heapq
from collections import Counter
from functools import partial
from io import StringIO
class Huffman:
    def __init__(self, data, width):
        if not data or width <= 0:
            raise ValueError("Invalid data or width.")
        self.original_data = data
        self.width = width
        self.data = [chunk for chunk in iter(partial(StringIO(data).read, width), '')]
        self._dictionary = {}
    def encode_huffman(self):
        freq_map = self._create_frequency()
        root = self._build_huffman_tree(freq_map)
        self._generate_huffman_codes(root)
        return self._encode()
    def decode_huffman(self, encoded_value):
        if not encoded_value:
            raise ValueError("Invalid encoded value.")
        bit_pattern = ''
        decoded_value = ''
        reversed_dict = self._get_reversed_dictionary()
        for bit in encoded_value:
            bit_pattern += bit
            if bit_pattern in reversed_dict:
                decoded_value += reversed_dict[bit_pattern]
                bit_pattern = ''
        return decoded_value
    def get_compression_ratio(self, encoded_value):
        if not encoded_value or not self.data:
            raise ValueError("Invalid encoded value or original data.")
        original_bits = len(self.original_data) * 8
        compressed_bits = len(encoded_value)
        return 1 - (compressed_bits / float(original_bits))
    @property
    def dictionary(self):
        return self._dictionary
    @dictionary.setter
    def dictionary(self, value):
        self._dictionary = value
    def _get_reversed_dictionary(self):
        return {v: k for k, v in self._dictionary.items()}
    def _create_frequency(self):
        return [(freq, char) for char, freq in Counter(self.data).items()]
    def _build_huffman_tree(self, frequency):
        if not frequency:
            raise ValueError("Invalid frequency table.")
        heapq.heapify(frequency)
        while len(frequency) > 1:
            left_node = heapq.heappop(frequency)
            right_node = heapq.heappop(frequency)
            parent_node = (left_node[0] + right_node[0], left_node, right_node)
            heapq.heappush(frequency, parent_node)
        return frequency[0]
    def _generate_huffman_codes(self, tree):
        stack = [(tree, '')]
        while stack:
            node, prefix = stack.pop()
            if len(node) == 2:
                self._dictionary[node[1]] = prefix
            else:
                stack.append((node[1], prefix + '0'))
                stack.append((node[2], prefix + '1'))
    def _encode(self):
        if not self._dictionary:
            raise ValueError("Huffman encoding table has not been created.")
        encoded_value = ''.join(self._dictionary[char] for char in self.data if char in self._dictionary)
        return encoded_value
def test_encoding_decoding(data):
    print("************** Test Encoding **************")
    huffman = Huffman(data, 4)
    encoded_data = huffman.encode_huffman()
    decoded_data = huffman.decode_huffman(encoded_data)
    print(f"Original data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")
    print(f"Original and decoded data are the same: {data == decoded_data}")
    print(f"Compression Ratio: {huffman.get_compression_ratio(encoded_data)}")
    return decoded_data
if __name__ == "__main__":
    test_data_1 = "a"
    test_data_2 = "abcdefghijklmnopqrstuvwxyz"
    test_data_3 = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    test_data_4 = "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
    test_data_5 = "test_data.txt"
    test_encoding_decoding(test_data_1)
    test_encoding_decoding(test_data_2)
    test_encoding_decoding(test_data_3)
    test_encoding_decoding(test_data_4)
    with open(test_data_5, "rb") as file:
        data = test_encoding_decoding(file.read())