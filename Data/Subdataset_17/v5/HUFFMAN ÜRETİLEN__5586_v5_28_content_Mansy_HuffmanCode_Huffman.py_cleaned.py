import heapq
from collections import namedtuple, Counter
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'
def huffman_encode(string):
    heap = [(freq, len(heap), Leaf(char)) for char, freq in Counter(string).items()]
    heapq.heapify(heap)
    count = len(heap)
    while len(heap) > 1:
        freq1, _count1, left = heapq.heappop(heap)
        freq2, _count2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if heap:
        [(_, _, root)] = heap
        root.walk(code, '')
    return code
def huffman_decode(encoded, code):
    reverse_code = {v: k for k, v in code.items()}
    decoded = []
    buffer = ""
    for bit in encoded:
        buffer += bit
        if buffer in reverse_code:
            decoded.append(reverse_code[buffer])
            buffer = ""
    return "".join(decoded)
def save_encoded_to_file(encoded, filename):
    with open(filename, 'wb') as output:
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            output.write(int(byte, 2).to_bytes(1, 'big'))
def load_encoded_from_file(filename):
    with open(filename, 'rb') as file:
        return ''.join(f'{byte:08b}' for byte in file.read())
def main():
    with open('test.txt', 'r', encoding='utf-8') as fp:
        string = fp.read()
    code = huffman_encode(string)
    encoded = ''.join(code[char] for char in string)
    print(f"Number of unique codes: {len(code)}, Encoded string length: {len(encoded)}\n")
    for char, huff_code in sorted(code.items(), key=lambda item: item[1]):
        print(f"{char}: {huff_code}")
    print('\n')
    print("Encoded binary string:")
    print(encoded)
    print('\n')
    save_encoded_to_file(encoded, 'encoded.bin')
    hex_representation = f"0x{int(encoded, 2):x}"
    print("Hexadecimal representation:")
    print(hex_representation)
    print('\n')
    decoded = huffman_decode(encoded, code)
    print("Decoded string:")
    print(decoded)
    with open('test2.txt', 'w', encoding='utf-8') as fp1:
        fp1.write(decoded)
if __name__ == '__main__':
    main()