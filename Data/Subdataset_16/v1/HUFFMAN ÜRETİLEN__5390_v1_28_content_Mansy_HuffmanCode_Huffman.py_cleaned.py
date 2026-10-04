import heapq
from collections import namedtuple, Counter
class class1(namedtuple('class1', ['b3', 'b4'])):
    def fonk1(self, b5, acc):
        self.b3.fonk2(b5, acc + '0')
        self.b4.fonk2(b5, acc + '1')
class class2(namedtuple('class2', ['char'])):
    def fonk2(self, b5, acc):
        b5[self.char] = acc or '0'
def fonk3(b11):
    b1 = []
    for char, freq in Counter(b11).items():
        b1.append((freq, len(b1), class2(char)))
    heapq.heapify(b1)
    b2 = len(b1)
    while len(b1) > 1:
        cur_freq, _cur_count, b3 = heapq.heappop(b1)
        next_freq, _next_count, b4 = heapq.heappop(b1)
        heapq.heappush(b1, (cur_freq + next_freq, b2, class1(b3, b4)))
        b2 += 1
    b5 = {}
    if b1:
        [(_freq, _count, root)] = b1
        root.fonk2(b5, '')
    return b5
def fonk4(tree, b6 = 0, side=''):
    if isinstance(tree, class1):
        fonk4(tree.b3, b6 + 1, 'b3')
        fonk4(tree.b4, b6 + 1, 'b4')
    if isinstance(tree, class2):
        print('  ' * b6, side + ' ' + tree.char)
def fonk5(b12, b5):
    b7 = []
    b8 = ""
    for ch in b12:
        b8 += ch
        for dec_ch in b5:
            if b5.get(dec_ch) == b8:
                b7.append(dec_ch)
                b8 = ""
                break
    return "".join(b7)
if b9 = = '__main__':
    with open('test.txt', 'r', b10 = 'utf-8') as fp:
        b11 = fp.read()
    b5 = fonk3(b11)
    b12 = ''.join(b5[ch] for ch in b11)
    print("Number of symbols:", len(b5))
    print("Encoded b11 length:", len(b12))
    print("\nHuffman Codes:")
    for ch in sorted(b5, b13 = b5.get):
        print(f'{ch}: {b5[ch]}')
    print("\nEncoded String:")
    print(b12)
    with open('b12.bin', 'wb') as output:
        b14 = [b12[i:i+8] for i in range(0, len(b12), 8)]
        for elem in b14:
            output.write(int(elem, 2).to_bytes(1, b15 = 'big'))
    print("\nHexadecimal Representation of Encoded Data:")
    b16 = "0x%x" % int(b12, 2)
    print(b16)
    b17 = bin(int(b16, 16))[2:].zfill(len(b12))
    print("\nBinary Representation from Hexadecimal:")
    print(b17)
    b18 = fonk5(b12, b5)
    print("\nDecoded String:")
    print(b18)
    with open('test2.txt', 'w', b10 = 'utf-8') as fp1:
        fp1.write(b18)