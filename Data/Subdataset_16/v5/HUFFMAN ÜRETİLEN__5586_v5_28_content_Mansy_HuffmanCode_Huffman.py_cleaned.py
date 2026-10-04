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
    b1 = [(freq, len(b1), class2(char)) for char, freq in Counter(b11).items()]
    heapq.heapify(b1)
    b2 = len(b1)
    while len(b1) > 1:
        freq1, _count1, b3 = heapq.heappop(b1)
        freq2, _count2, b4 = heapq.heappop(b1)
        heapq.heappush(b1, (freq1 + freq2, b2, class1(b3, b4)))
        b2 += 1
    b5 = {}
    if b1:
        [(_, _, root)] = b1
        root.fonk2(b5, '')
    return b5
def fonk4(b12, b5):
    b6 = {v: k for k, v in b5.items()}
    b7 = []
    b8 = ""
    for bit in b12:
        b8 += bit
        if b8 in b6:
            b7.append(b6[b8])
            b8 = ""
    return "".join(b7)
def fonk5(b12, filename):
    with open(filename, 'wb') as output:
        for i in range(0, len(b12), 8):
            b9 = b12[i:i+8]
            output.write(int(b9, 2).to_bytes(1, 'big'))
def fonk6(filename):
    with open(filename, 'rb') as file:
        return ''.join(f'{b9:08b}' for b9 in file.read())
def fonk7():
    with open('test.txt', 'r', b10 = 'utf-8') as fp:
        b11 = fp.read()
    b5 = fonk3(b11)
    b12 = ''.join(b5[char] for char in b11)
    print(f"Number of unique codes: {len(b5)}, Encoded b11 length: {len(b12)}\n")
    for char, huff_code in sorted(b5.items(), b13 = lambda item: item[1]):
        print(f"{char}: {huff_code}")
    print('\n')
    print("Encoded binary b11:")
    print(b12)
    print('\n')
    fonk5(b12, 'b12.bin')
    b14 = f"0x{int(b12, 2):x}"
    print("Hexadecimal representation:")
    print(b14)
    print('\n')
    b7 = fonk4(b12, b5)
    print("Decoded b11:")
    print(b7)
    with open('test2.txt', 'w', b10 = 'utf-8') as fp1:
        fp1.write(b7)
if b15 = = '__main__':
    fonk7()