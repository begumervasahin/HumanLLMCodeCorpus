import heapq
import os
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
    def __eq__(self, other):
        return other is not None and isinstance(other, HeapNode) and self.freq == other.freq
class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    def _make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency
    def _build_heap(self, frequency):
        for char, freq in frequency.items():
            node = HeapNode(char, freq)
            heapq.heappush(self.heap, node)
    def _merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
    def _make_codes_helper(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
            return
        self._make_codes_helper(node.left, current_code + "0")
        self._make_codes_helper(node.right, current_code + "1")
    def _make_codes(self):
        root = heapq.heappop(self.heap)
        self._make_codes_helper(root, "")
    def _get_encoded_text(self, text):
        return ''.join(self.codes[char] for char in text)
    def _pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * extra_padding
        padded_info = f"{extra_padding:08b}"
        return padded_info + encoded_text
    def _get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            raise ValueError("Encoded text is not padded properly.")
        return bytearray(int(padded_encoded_text[i:i + 8], 2) for i in range(0, len(padded_encoded_text), 8))
    def compress(self):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r') as file:
            text = file.read().rstrip()
        frequency = self._make_frequency_dict(text)
        self._build_heap(frequency)
        self._merge_nodes()
        self._make_codes()
        encoded_text = self._get_encoded_text(text)
        padded_encoded_text = self._pad_encoded_text(encoded_text)
        byte_array = self._get_byte_array(padded_encoded_text)
        with open(output_path, 'wb') as output:
            output.write(byte_array)
        print(f"File compressed successfully to {output_path}.")
        return output_path
    def _remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    def _decode_text(self, encoded_text):
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
        with open(input_path, 'rb') as file:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
        encoded_text = self._remove_padding(bit_string)
        decompressed_text = self._decode_text(encoded_text)
        with open(output_path, 'w') as output:
            output.write(decompressed_text)
        print(f"File decompressed successfully to {output_path}.")
        return output_path