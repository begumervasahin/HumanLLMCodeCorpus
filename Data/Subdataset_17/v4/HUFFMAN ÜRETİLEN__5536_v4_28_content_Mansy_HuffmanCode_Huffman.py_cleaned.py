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
    heap = []
    for char, freq in Counter(string).items():
        heap.append((freq, len(heap), Leaf(char)))
    sorted_heap = sorted(heap, reverse=True)
    for freq, _, leaf in sorted_heap:
        print(freq, leaf.char)
    print('\n')
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
def parse_tree(tree, depth=0, side=''):
    if isinstance(tree, Node):
        parse_tree(tree.left, depth + 1, 'left')
        parse_tree(tree.right, depth + 1, 'right')
    elif isinstance(tree, Leaf):
        print('  ' * depth + f"{side} {tree.char}")
def huffman_decode(encoded, code):
    decoded = []
    buffer = ""
    for bit in encoded:
        buffer += bit
        for char in code:
            if code[char] == buffer:
                decoded.append(char)
                buffer = ""
                break
    return "".join(decoded)
if __name__ == '__main__':
    with open('test.txt', 'r') as fp:
        string = fp.read().decode('utf-8')
    code = huffman_encode(string)
    encoded = ''.join(code[char] for char in string)
    print(f"Number of unique codes: {len(code)}, Encoded string length: {len(encoded)}\n")
    for char in sorted(code, key=code.get):
        print(f"{char}: {code[char]}")
    print('\n')
    print(encoded)
    with open('encoded.bin', 'wb') as output:
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            output.write(chr(int(byte, 2)).encode('latin1'))
    hex_representation = f"0x{int(encoded, 2):x}"
    print(hex_representation)
    binary_representation = bin(int(hex_representation, 16))[2:]
    print(binary_representation)
    print('\n')
    decoded = huffman_decode(encoded, code)
    print(decoded)
    with open('test2.txt', 'w') as fp1:
        fp1.write(decoded.encode('utf-8'))