import heapq
from collections import namedtuple, Counter
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'
def huffman_encode(text):
    heap = [(freq, len(heap), Leaf(char)) for char, freq in Counter(text).items()]
    heapq.heapify(heap)
    count = len(heap)
    while len(heap) > 1:
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if heap:
        [(_freq, _count, root)] = heap
        root.walk(code, '')
    return code
def huffman_decode(encoded_text, code):
    reverse_code = {v: k for k, v in code.items()}
    decoded_text = []
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_code:
            decoded_text.append(reverse_code[current_code])
            current_code = ''
    return ''.join(decoded_text)
def save_encoded_binary(encoded_text, filename):
    with open(filename, 'wb') as output_file:
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            output_file.write(int(byte, 2).to_bytes(1, byteorder='big'))
def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
def save_text(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
if __name__ == '__main__':
    input_text = load_text('test.txt')
    code_map = huffman_encode(input_text)
    encoded_text = ''.join(code_map[char] for char in input_text)
    print(f"Number of symbols: {len(code_map)}")
    print(f"Encoded string length: {len(encoded_text)}\n")
    print("Huffman Codes:")
    for char in sorted(code_map, key=code_map.get):
        print(f'{repr(char)}: {code_map[char]}')
    save_encoded_binary(encoded_text, 'encoded.bin')
    decoded_text = huffman_decode(encoded_text, code_map)
    print("\nDecoded String:")
    print(decoded_text)
    save_text(decoded_text, 'test2.txt')