import heapq
from collections import Counter
from functools import partial
from io import StringIO
class Huffman:
    def __init__(self, data, width):
        if not data:
            raise ValueError("Invalid data.")
        if width <= 0:
            raise ValueError("Width must be greater than 0.")
        self.original_data = data
        self.width = width
        self.data = [segment for segment in iter(partial(StringIO(data).read, self.width), '')]
        self._dictionary = {}
    def encode_huffman(self):
        frequency_map = self._create_frequency_map()
        huffman_tree = self._build_huffman_tree(frequency_map)
        self._generate_huffman_codes(huffman_tree)
        return self._encode_data()
    def decode_huffman(self, encoded_value):
        if not encoded_value:
            raise ValueError("Invalid encoded value.")
        decoded_value = []
        bit_pattern = ''
        reversed_dictionary = self._reversed_dictionary
        for bit in encoded_value:
            bit_pattern += bit
            if bit_pattern in reversed_dictionary:
                decoded_value.append(reversed_dictionary[bit_pattern])
                bit_pattern = ''
        return ''.join(decoded_value)
    def get_compression_ratio(self, encoded_value):
        if not encoded_value:
            raise ValueError("Invalid encoded value.")
        original_size = len(self.original_data) * 8
        encoded_size = len(encoded_value)
        return 1 - (encoded_size / original_size)
    @property
    def dictionary(self):
        return self._dictionary
    @property
    def _reversed_dictionary(self):
        return {v: k for k, v in self._dictionary.items()}
    def _create_frequency_map(self):
        return [(freq, char) for char, freq in Counter(self.data).items()]
    def _build_huffman_tree(self, frequency_map):
        if not frequency_map:
            raise ValueError("Invalid frequency map.")
        heapq.heapify(frequency_map)
        while len(frequency_map) > 1:
            left_node = heapq.heappop(frequency_map)
            right_node = heapq.heappop(frequency_map)
            merged_node = (left_node[0] + right_node[0], left_node, right_node)
            heapq.heappush(frequency_map, merged_node)
        return frequency_map[0]
    def _generate_huffman_codes(self, tree):
        stack = [(tree, '1' if len(tree) == 2 else '')]
        while stack:
            node, code = stack.pop()
            if len(node) == 2:
                self._dictionary[node[1]] = code
            else:
                stack.append((node[1], code + '0'))
                stack.append((node[2], code + '1'))
    def _encode_data(self):
        if not self._dictionary:
            raise ValueError("Huffman dictionary has not been created.")
        encoded_value = ''.join(self._dictionary[char] for char in self.data)
        return encoded_value
def test_huffman_encoding_decoding(data):
    huffman = Huffman(data, 4)
    encoded_data = huffman.encode_huffman()
    decoded_data = huffman.decode_huffman(encoded_data)
    print("************** Test Encoding **************")
    print("Encoded data:", encoded_data)
    print("Decoding successful:", decoded_data == data)
    print("Compression Ratio:", huffman.get_compression_ratio(encoded_data))
    print()
    return decoded_data
if __name__ == "__main__":
    test_cases = [
        "a",
        "abcdefghijklmnopqrstuvwxyz",
        "aaaaaaaaaaaaaaaaaaaaaaaaaa",
        "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
    ]
    for test_data in test_cases:
        test_huffman_encoding_decoding(test_data)
    with open("test_data.txt", "r") as file:
        test_data_file = file.read()
    test_huffman_encoding_decoding(test_data_file)