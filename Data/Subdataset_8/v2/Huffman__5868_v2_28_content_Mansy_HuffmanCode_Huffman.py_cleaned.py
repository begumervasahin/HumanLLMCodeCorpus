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
    with open('test.txt', 'r') as fp:
        string = fp.read()
    code = huffman_encode(string)
    encoded = ''.join(code[ch] for ch in string)
    print("Character codes:")
    for ch in sorted(code, key=code.get):
        print(ch + ':', code[ch])
    print("\nEncoded string:")
    print(encoded)
    decoded = huffman_decode(encoded, code)
    print("\nDecoded string:")
    print(decoded)
    with open('test2.txt', 'w') as fp1:
        fp1.write(decoded)