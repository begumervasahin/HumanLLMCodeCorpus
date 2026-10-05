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
class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}
    def compress(self):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + ".bin"
        with open(self.path, 'r') as file, open(output_path, 'wb') as output:
            text = file.read().rstrip()
            frequency = self.__make_frequency_dict(text)
            self.__make_heap(frequency)
            self.__merge_nodes()
            self.__make_codes()
            encoded_text = self.__get_encoded_text(text)
            padded_encoded_text = self.__pad_encoded_text(encoded_text)
            byte_array = self.__get_byte_array(padded_encoded_text)
            output.write(bytes(byte_array))
        print("Compressed")
        return output_path
    def decompress(self, input_path):
        filename, _ = os.path.splitext(self.path)
        output_path = filename + "_decompressed.txt"
        with open(input_path, 'rb') as file, open(output_path, 'w') as output:
            bit_string = "".join(format(byte, '08b') for byte in file.read())
            encoded_text = self.__remove_padding(bit_string)
            decompressed_text = self.__decode_text(encoded_text)
            output.write(decompressed_text)
        print("Decompressed")
        return output_path
    def __make_frequency_dict(self, text):
        frequency = {}
        for character in text:
            frequency[character] = frequency.get(character, 0) + 1
        return frequency
    def __make_heap(self, frequency):
        for key, value in frequency.items():
            node = HeapNode(key, value)
            heapq.heappush(self.heap, node)
    def __merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)
    def __make_codes_helper(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.__make_codes_helper(root.left, current_code + "0")
        self.__make_codes_helper(root.right, current_code + "1")
    def __make_codes(self):
        root = heapq.heappop(self.heap)
        self.__make_codes_helper(root, "")
    def __get_encoded_text(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
        return encoded_text
    def __pad_encoded_text(self, encoded_text):
        extra_padding = 8 - len(encoded_text) % 8
        encoded_text += "0" * extra_padding
        padded_info = "{0:08b}".format(extra_padding)
        encoded_text = padded_info + encoded_text
        return encoded_text
    def __get_byte_array(self, padded_encoded_text):
        if len(padded_encoded_text) % 8 != 0:
            print("Encoded text not padded properly")
            exit(0)
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i + 8]
            byte_array.append(int(byte, 2))
        return byte_array
    def __remove_padding(self, padded_encoded_text):
        padded_info = padded_encoded_text[:8]
        extra_padding = int(padded_info, 2)
        return padded_encoded_text[8:-extra_padding]
    def __decode_text(self, encoded_text):
        current_code = ""
        decoded_text = ""
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                character = self.reverse_mapping[current_code]
                decoded_text += character
                current_code = ""
        return decoded_text
if __name__ == "__main__":
    path = "sample.txt"
    huffman = HuffmanCoding(path)
    compressed_path = huffman.compress()
    decompressed_path = huffman.decompress(compressed_path)