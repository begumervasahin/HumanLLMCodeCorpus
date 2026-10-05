from collections import Counter
import heapq
from functools import partial
import io
class Huffman:
    def __init__(self, data, width):
        if data is None or len(data) == 0:
            raise ValueError("Invalid data.")
        if width <= 0:
            raise ValueError("Width must be > 0")
        self.original_data = data
        self.width = width
        self.data_chunks = [chunk for chunk in iter(partial(io.StringIO(data).read, self.width), '')]
        self.encoding_dictionary = {}
    def encode_huffman(self):
        frequency_map = self.__create_frequency()
        root = self.__huffman_tree(frequency_map)
        self.__huffman_code(root)
        return self.__encode()
    def decode_huffman(self, encoded_value):
        if encoded_value is None or len(encoded_value) == 0:
            raise ValueError("Invalid encoded value.")
        bit_pattern = ''
        decoded_value = ''
        reversed_dictionary = self.get_reversed_dictionary()
        for bit in encoded_value:
            bit_pattern += bit
            if bit_pattern in reversed_dictionary:
                decoded_value += reversed_dictionary[bit_pattern]
                bit_pattern = ''
        return decoded_value
    def get_compression_ratio(self, encoded_value):
        if encoded_value is None or len(encoded_value) == 0:
            raise ValueError("Invalid argument 'encoded_value'.")
        if self.original_data is None or len(self.original_data) == 0:
            raise ValueError("Invalid member 'original_data'.")
        return 1 - (len(encoded_value) / float((len(self.original_data)*8)))
    @property
    def encoding_dictionary(self):
        return self.encoding_dictionary
    @encoding_dictionary.setter
    def encoding_dictionary(self, value):
        self.encoding_dictionary = value
    def get_reversed_dictionary(self):
        return {v: k for k, v in self.encoding_dictionary.items()}
    def __create_frequency(self):
        frequency_list = Counter(self.data_chunks).items()
        return [(v,k) for k, v in frequency_list]
    def __huffman_tree(self, frequency):
        if frequency is None or len(frequency) == 0:
            raise ValueError("Invalid frequency table.")
        heapq.heapify(frequency)
        while len(frequency) > 1:
            left_node = heapq.heappop(frequency)
            right_node = heapq.heappop(frequency)
            parent_node = ((left_node[0] + right_node[0]), left_node, right_node)
            heapq.heappush(frequency, parent_node)
        return frequency[0]
    def __huffman_code(self, tree):
        stack = []
        if len(tree) == 2:
            prefix = '1'
        else:
            prefix = ''
        stack.append((tree, prefix))
        while len(stack) > 0:
            ptr = stack.pop()
            if len(ptr[0]) == 2:
                self.encoding_dictionary[ptr[0][1]] = ptr[1]
            else:
                stack.append((ptr[0][1], ptr[1]+'0'))
                stack.append((ptr[0][2], ptr[1]+'1'))
    def __encode(self):
        if len(self.encoding_dictionary) == 0:
            raise ValueError("Huffman encoding table has not been created.")
        value = ''
        for c in self.data_chunks:
            if c in self.encoding_dictionary:
                value += self.encoding_dictionary[c]
            else:
                raise ValueError("Invalid huffman key.")
        return value
def test_encoding_decoding(data):
    original_data = data
    huffman = Huffman(original_data, 4)
    encoded_data = huffman.encode_huffman()
    reencoded_data = huffman.decode_huffman(encoded_data)
    print("************** Test Encoding **************")
    print("Encoded data: ", encoded_data)
    print("Compare: (original_data == re-encoded_data) = ", reencoded_data == original_data)
    print("Compression Ratio: ", huffman.get_compression_ratio(encoded_data))
    return reencoded_data
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
    data = test_encoding_decoding(open(test_data_5, "rb").read())