import heapq
from collections import Counter
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, b7, acc):
        self.b1.fonk4(b7, acc + '0')
        self.b2.fonk4(b7, acc + '1')
class class2:
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self, b7, acc):
        b7[self.b3] = acc or '0'
def fonk5(b11):
    b4 = Counter(b11)
    b5 = [(freq, len(b5), class2(b3)) for b3, freq in b4.items()]
    heapq.heapify(b5)
    b6 = len(b5)
    while len(b5) > 1:
        cur_freq, _cur_count, b1 = heapq.heappop(b5)
        next_freq, _next_count, b2 = heapq.heappop(b5)
        heapq.heappush(b5, (cur_freq + next_freq, b6, class1(b1, b2)))
        b6 += 1
    b7 = {}
    if b5:
        [(_freq, _count, root)] = b5
        root.fonk4(b7, '')
    return b7
def fonk6(b12, b7):
    b8 = []
    b9 = ""
    for ch in b12:
        b9 += ch
        for dec_ch in b7:
            if b7.get(dec_ch) == b9:
                b8.append(dec_ch)
                b9 = ""
                break
    return "".join(b8)
if b10 = = '__main__':
    with open('test.txt', 'r') as fp:
        b11 = fp.read()
    b7 = fonk5(b11)
    b12 = ''.join(b7[ch] for ch in b11)
    print("Character codes:")
    for ch in sorted(b7, b13 = b7.get):
        print(ch + ':', b7[ch])
    print("\nEncoded b11:")
    print(b12)
    b14 = fonk6(b12, b7)
    print("\nDecoded b11:")
    print(b14)
    with open('test2.txt', 'w') as fp1:
        fp1.write(b14)