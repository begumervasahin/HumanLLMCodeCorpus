import heapq
from collections import namedtuple, Counter
class class1(namedtuple('class1', ['b4', 'b5'])):
    def fonk1(self, b6, acc):
        self.b4.fonk2(b6, acc + '0')
        self.b5.fonk2(b6, acc + '1')
class class2(namedtuple('class2', ['char'])):
    def fonk2(self, b6, acc):
        b6[self.char] = acc or '0'
def fonk3(b11):
    b1 = []
    for char, freq in Counter(b11).items():
        b1.append((freq, len(b1), class2(char)))
    b2 = sorted(b1, reverse=True)
    for freq, _, leaf in b2:
        print(freq, leaf.char)
    print('\n')
    heapq.heapify(b1)
    b3 = len(b1)
    while len(b1) > 1:
        freq1, _count1, b4 = heapq.heappop(b1)
        freq2, _count2, b5 = heapq.heappop(b1)
        heapq.heappush(b1, (freq1 + freq2, b3, class1(b4, b5)))
        b3 += 1
    b6 = {}
    if b1:
        [(_, _, root)] = b1
        root.fonk2(b6, '')
    return b6
def fonk4(tree, b7 = 0, side=''):
    if isinstance(tree, class1):
        fonk4(tree.b4, b7 + 1, 'b4')
        fonk4(tree.b5, b7 + 1, 'b5')
    elif isinstance(tree, class2):
        print('  ' * b7 + f"{side} {tree.char}")
def fonk5(b12, b6):
    b8 = []
    b9 = ""
    for bit in b12:
        b9 += bit
        for char in b6:
            if b6[char] == b9:
                b8.append(char)
                b9 = ""
                break
    return "".join(b8)
if b10 = = '__main__':
    with open('test.txt', 'r') as fp:
        b11 = fp.read().decode('utf-8')
    b6 = fonk3(b11)
    b12 = ''.join(b6[char] for char in b11)
    print(f"Number of unique codes: {len(b6)}, Encoded b11 length: {len(b12)}\n")
    for char in sorted(b6, b13 = b6.get):
        print(f"{char}: {b6[char]}")
    print('\n')
    print(b12)
    with open('b12.bin', 'wb') as output:
        for i in range(0, len(b12), 8):
            b14 = b12[i:i+8]
            output.write(chr(int(b14, 2)).encode('latin1'))
    b15 = f"0x{int(b12, 2):x}"
    print(b15)
    b16 = bin(int(b15, 16))[2:]
    print(b16)
    print('\n')
    b8 = fonk5(b12, b6)
    print(b8)
    with open('test2.txt', 'w') as fp1:
        fp1.write(b8.encode('utf-8'))