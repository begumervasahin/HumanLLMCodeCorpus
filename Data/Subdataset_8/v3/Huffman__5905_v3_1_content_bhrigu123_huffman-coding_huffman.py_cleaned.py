import heapq
import os
class HuffmanCoding:
    def __init__(self, path: str) -> None:
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    class HeapNode:
        def __init__(self, char: str, freq: int) -> None:
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None
        def __lt__(self, other: 'HuffmanCoding.HeapNode') -> bool:
            return self.freq < other.freq
    def make_frequency_dict(self, text: str) -> Dict[str, int]:
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency
    def make_heap(self, frequency: Dict[str, int]) -> None:
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)
    def merge_nodes(self) -> None:
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
    def make_codes_helper(self, root: 'HuffmanCoding.HeapNode', current_code: str) -> None:
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")
    def make_codes(self) -> None:
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)
    def get_encoded_text(self, text: str) -> str:
        encoded_text = "".join(self.codes[char] for char in text)
        return encoded_text
    def pad_encoded_text(self, encoded_text: str) -> str:
        extra_padding = 8 - len(encoded_text) % 8
        padded_info = format(extra_padding, '08b')
        padded_encoded_text = padded_info + encoded_text + "0" * extra_padding
        return padded_encoded_text
    def get_byte_array(self, padded_encoded_text: str) -> bytearray:
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            byte_array.append(int(byte, 2))
        return byte_array
    def compress(self) -> str:
        filename, _ = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read()
            frequency = self.make_frequency_dict(text)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()
            encoded_text = self.get_encoded_text(text)
            padded_encoded_text = self.pad_encoded_text(encoded_text)
            byte_array = self.get_byte_array(padded_encoded_text)
            output.write(bytes(byte_array))
        return output_path
    def remove_padding(self, padded_encoded_text: str) -> str:
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    def decode_text(self, encoded_text: str) -> str:
        decoded_text = ""
        current_code = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""
        return decoded_text
    def decompress(self, input_path: str) -> str:
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = "".join(format(byte, '08b') for byte in file.read())
            encoded_text = self.remove_padding(bit_string)
            decoded_text = self.decode_text(encoded_text)
            output.write(decoded_text)
        return output_path
if __name__ == "__main__":
    huffman = HuffmanCoding("example.txt")
    compressed_file_path = huffman.compress()
    decompressed_file_path = huffman.decompress(compressed_file_path)