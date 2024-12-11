import heapq
from collections import Counter
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, b6, acc):
        self.b1.fonk4(b6, acc + '0')
        self.b2.fonk4(b6, acc + '1')
class class2:
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self, b6, acc):
        b6[self.b3] = acc or '0'
def fonk5(b11):
    b4 = Counter(b11)
    b5 = [(freq, class2(b3)) for b3, freq in b4.items()]
    heapq.heapify(b5)
    while len(b5) > 1:
        freq1, b1 = heapq.heappop(b5)
        freq2, b2 = heapq.heappop(b5)
        heapq.heappush(b5, (freq1 + freq2, class1(b1, b2)))
    b6 = {}
    if b5:
        [(_freq, root)] = b5
        root.fonk4(b6, '')
    return b6
def fonk6(b12, b6):
    b7 = ""
    b8 = ""
    for bit in b12:
        b8 += bit
        for b3, b9 in b6.items():
            if b9 = = b8:
                b7 += b3
                b8 = ""
                break
    return b7
if b10 = = '__main__':
    with open('test.txt', 'r') as file:
        b11 = file.read()
    b6 = fonk5(b11)
    b12 = ''.join(b6[ch] for ch in b11)
    print("Number of characters:", len(b6))
    print("Encoded length:", len(b12))
    for ch, b9 in sorted(b6.items(), b13 = lambda x: x[1]):
        print(ch + ':', b9)
    with open('b12.bin', 'wb') as file:
        file.write(bytes(int(b12[i:i + 8], 2) for i in range(0, len(b12), 8)))
    print('\nEncoded b11 in binary:', int(b12, 2))
    b14 = fonk6(b12, b6)
    print('\nDecoded b11:', b14)
    with open('test2.txt', 'w') as file:
        file.write(b14)