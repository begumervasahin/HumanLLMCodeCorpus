import heapq
import os
class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        def __lt__(self, other):
            return self.freq < other.freq
        def __eq__(self, other):
            return other is not None and isinstance(other, HuffmanCoding.HeapNode) and self.freq == other.freq
    def make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency
    def make_heap(self, frequency):
        for char, freq in frequency.items():
            node = self.HeapNode(char, freq)
            heapq.heappush(self.heap, node)
    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged_node = self.HeapNode(None, node1.freq + node2.freq)
            merged_node.left = node1
            merged_node.right = node2
            heapq.heappush(self.heap, merged_node)
    def make_codes_helper(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        self.make_codes_helper(node.left, current_code + "0")
        self.make_codes_helper(node.right, current_code + "1")
    def make_codes(self):
        root = heapq.heappop(self.heap)
        self.make_codes_helper(root, "")
    def get_encoded_text(self, text):
        return ''.join(self.codes[char] for char in text)
    def pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * extra_padding
        padded_info = "{0:08b}".format(extra_padding)
        return padded_info + encoded_text
    def get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            raise ValueError("Encoded text not padded properly")
        return bytearray(int(padded_encoded_text[i:i + 8], 2) for i in range(0, len(padded_encoded_text), 8))
    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read().rstrip()
            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()
            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            byte_array = self.get_byte_array(padded_encoded_text)
            output.write(bytes(byte_array))
        print("File compressed successfully.")
        return output_path
    def remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    def decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""
        return decoded_text
    def decompress(self, input_path):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            encoded_text = self.remove_padding(bit_string)
            decompressed_text = self.decode_text(encoded_text)
            output.write(decompressed_text)
        print("File decompressed successfully.")
        return output_path