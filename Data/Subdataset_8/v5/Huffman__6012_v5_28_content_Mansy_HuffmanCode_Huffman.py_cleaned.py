import heapq
from collections import Counter
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')
class Leaf:
    def __init__(self, char):
        self.char = char
    def walk(self, code, acc):
        code[self.char] = acc or '0'
def huffman_encode(string):
    frequencies = Counter(string)
    heap = [(freq, Leaf(char)) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        freq1, left = heapq.heappop(heap)
        freq2, right = heapq.heappop(heap)
        heapq.heappush(heap, (freq1 + freq2, Node(left, right)))
    code = {}
    if heap:
        [(_freq, root)] = heap
        root.walk(code, '')
    return code
def huffman_decode(encoded, code):
    decode = ""
    current_code = ""
    for bit in encoded:
        current_code += bit
        for char, huff_code in code.items():
            if huff_code == current_code:
                decode += char
                current_code = ""
                break
    return decode
if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        string = file.read()
    code = huffman_encode(string)
    encoded = ''.join(code[ch] for ch in string)
    print("Number of characters:", len(code))
    print("Encoded length:", len(encoded))
    for ch, huff_code in sorted(code.items(), key=lambda x: x[1]):
        print(ch + ':', huff_code)
    with open('encoded.bin', 'wb') as file:
        file.write(bytes(int(encoded[i:i + 8], 2) for i in range(0, len(encoded), 8)))
    print('\nEncoded string in binary:', int(encoded, 2))
    decoded = huffman_decode(encoded, code)
    print('\nDecoded string:', decoded)
    with open('test2.txt', 'w') as file:
        file.write(decoded)