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
    h = []
    for char, freq in Counter(string).items():
        h.append((freq, len(h), Leaf(char)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        cur_freq, _cur_count, left = heapq.heappop(h)
        next_freq, _next_count, right = heapq.heappop(h)
        heapq.heappush(h, (cur_freq + next_freq, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code
def parse_tree(tree, cnt=0, side=''):
    if isinstance(tree, Node):
        parse_tree(tree.left, cnt + 1, 'left')
        parse_tree(tree.right, cnt + 1, 'right')
    if isinstance(tree, Leaf):
        print('  ' * cnt, side + ' ' + tree.char)
def huffman_decode(encoded, code):
    sx = []
    enc_ch = ""
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ""
                break
    return "".join(sx)
if __name__ == '__main__':
    with open('test.txt', 'r', encoding='utf-8') as fp:
        string = fp.read()
    code = huffman_encode(string)
    encoded = ''.join(code[ch] for ch in string)
    print("Number of symbols:", len(code))
    print("Encoded string length:", len(encoded))
    print("\nHuffman Codes:")
    for ch in sorted(code, key=code.get):
        print(f'{ch}: {code[ch]}')
    print("\nEncoded String:")
    print(encoded)
    with open('encoded.bin', 'wb') as output:
        tmp = [encoded[i:i+8] for i in range(0, len(encoded), 8)]
        for elem in tmp:
            output.write(int(elem, 2).to_bytes(1, byteorder='big'))
    print("\nHexadecimal Representation of Encoded Data:")
    tt = "0x%x" % int(encoded, 2)
    print(tt)
    re_tt = bin(int(tt, 16))[2:].zfill(len(encoded))
    print("\nBinary Representation from Hexadecimal:")
    print(re_tt)
    decoded = huffman_decode(encoded, code)
    print("\nDecoded String:")
    print(decoded)
    with open('test2.txt', 'w', encoding='utf-8') as fp1:
        fp1.write(decoded)