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
    def _make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency
    def _make_heap(self, frequency):
        for char, freq in frequency.items():
            node = self.HeapNode(char, freq)
            heapq.heappush(self.heap, node)
    def _merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
    def _make_codes_helper(self, node, current_code):
        if node is None:
            return
        if node.char is not None:
            self.codes[node.char] = current_code
            self.reverse_mapping[current_code] = node.char
        self._make_codes_helper(node.left, current_code + "0")
        self._make_codes_helper(node.right, current_code + "1")
    def _make_codes(self):
        root = heapq.heappop(self.heap)
        self._make_codes_helper(root, "")
    def _get_encoded_text(self, text):
        return ''.join(self.codes[char] for char in text)
    def _pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        padded_info = f"{extra_padding:08b}"
        padded_encoded_text = padded_info + encoded_text + "0" * extra_padding
        return padded_encoded_text
    def _get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            raise ValueError("Encoded text not padded properly")
        return bytearray(int(padded_encoded_text[i:i+8], 2) for i in range(0, len(padded_encoded_text), 8))
    def compress(self):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r') as file:
            text = file.read().rstrip()
        frequency = self._make_frequency_dict(text)
        self._make_heap(frequency)
        self._merge_nodes()
        self._make_codes()
        encoded_text = self._get_encoded_text(text)
        padded_encoded_text = self._pad_encoded_text(encoded_text)
        byte_array = self._get_byte_array(padded_encoded_text)
        with open(output_path, 'wb') as output:
            output.write(bytes(byte_array))
        print("File compressed successfully.")
        return output_path
    def _remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    def _decode_text(self, encoded_text):
        current_code = ""
        decoded_text = []
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text.append(self.reverse_mapping[current_code])
                current_code = ""
        return ''.join(decoded_text)
    def decompress(self, input_path):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"
        with open(input_path, 'rb') as file:
            bit_string = "".join(f"{byte:08b}" for byte in file.read())
        encoded_text = self._remove_padding(bit_string)
        decompressed_text = self._decode_text(encoded_text)
        with open(output_path, 'w') as output:
            output.write(decompressed_text)
        print("File decompressed successfully.")
        return output_path
if __name__ == "__main__":
    path = "example.txt"
    huffman_coding = HuffmanCoding(path)
    compressed_file = huffman_coding.compress()
    print("Compressed file path:", compressed_file)
    decompressed_file = huffman_coding.decompress(compressed_file)
    print("Decompressed file path:", decompressed_file)