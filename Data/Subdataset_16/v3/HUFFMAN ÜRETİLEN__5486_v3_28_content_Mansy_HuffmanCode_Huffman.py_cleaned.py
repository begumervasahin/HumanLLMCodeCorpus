import heapq
from collections import namedtuple, Counter
class class1(namedtuple('class1', ['b3', 'b4'])):
    def fonk1(self, b5, acc):
        self.b3.fonk2(b5, acc + '0')
        self.b4.fonk2(b5, acc + '1')
class class2(namedtuple('class2', ['char'])):
    def fonk2(self, b5, acc):
        b5[self.char] = acc or '0'
def fonk3(text):
    b1 = [(freq, len(b1), class2(char)) for char, freq in Counter(text).items()]
    heapq.heapify(b1)
    b2 = len(b1)
    while len(b1) > 1:
        freq1, _count1, b3 = heapq.heappop(b1)
        freq2, _count2, b4 = heapq.heappop(b1)
        heapq.heappush(b1, (freq1 + freq2, b2, class1(b3, b4)))
        b2 += 1
    b5 = {}
    if b1:
        [(_freq, _count, root)] = b1
        root.fonk2(b5, '')
    return b5
def fonk4(b15, b5):
    b6 = {v: k for k, v in b5.items()}
    b7 = []
    b8 = ''
    for bit in b15:
        b8 += bit
        if b8 in b6:
            b7.append(b6[b8])
            b8 = ''
    return ''.join(b7)
def fonk5(b15, filename):
    with open(filename, 'wb') as output_file:
        for i in range(0, len(b15), 8):
            b9 = b15[i:i+8]
            output_file.write(int(b9, 2).to_bytes(1, b10 = 'big'))
def fonk6(filename):
    with open(filename, 'r', b11 = 'utf-8') as file:
        return file.read()
def fonk7(text, filename):
    with open(filename, 'w', b11 = 'utf-8') as file:
        file.write(text)
if b12 = = '__main__':
    b13 = fonk6('test.txt')
    b14 = fonk3(b13)
    b15 = ''.join(b14[char] for char in b13)
    print(f"Number of symbols: {len(b14)}")
    print(f"Encoded string length: {len(b15)}\n")
    print("Huffman Codes:")
    for char in sorted(b14, b16 = b14.get):
        print(f'{repr(char)}: {b14[char]}')
    fonk5(b15, 'encoded.bin')
    b7 = fonk4(b15, b14)
    print("\nDecoded String:")
    print(b7)
    fonk7(b7, 'test2.txt')