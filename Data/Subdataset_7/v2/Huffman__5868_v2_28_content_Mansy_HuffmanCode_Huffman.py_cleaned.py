import heapq
from collections import namedtuple, Counter
class class1(namedtuple('class1', ['b3', 'b4'])):
    def fonk1(self, b5, acc):
        self.b3.fonk2(b5, acc + '0')
        self.b4.fonk2(b5, acc + '1')
class class2(namedtuple('class2', ['char'])):
    def fonk2(self, b5, acc):
        b5[self.char] = acc or '0'
def fonk3(b9):
    b1 = []
    for char, freq in Counter(b9).items():
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
def fonk4(b10, b5):
    b6 = []
    b7 = ""
    for ch in b10:
        b7 += ch
        for dec_ch in b5:
            if b5.get(dec_ch) == b7:
                b6.append(dec_ch)
                b7 = ""
                break
    return "".join(b6)
if b8 = = '__main__':
    with open('test.txt', 'r') as fp:
        b9 = fp.read()
    b5 = fonk3(b9)
    b10 = ''.join(b5[ch] for ch in b9)
    print("Character codes:")
    for ch in sorted(b5, b11 = b5.get):
        print(ch + ':', b5[ch])
    print("\nEncoded b9:")
    print(b10)
    b12 = fonk4(b10, b5)
    print("\nDecoded b9:")
    print(b12)
    with open('test2.txt', 'w') as fp1:
        fp1.write(b12)