import heapq
from collections import namedtuple, Counter
class class1(namedtuple('class1', ['b5', 'b6'])):
    def fonk1(self, b7, acc):
        self.b5.fonk2(b7, acc + '0')
        self.b6.fonk2(b7, acc + '1')
class class2(namedtuple('class2', ['char'])):
    def fonk2(self, b7, acc):
        b7[self.char] = acc or '0'
def fonk3(b13):
    b1 = []
    for char, freq in Counter(b13).items():
        b1.append((freq, len(b1), class2(char)))
    b2 = []
    for i in range(len(sorted(b1))):
        b2.append([b1[i][0], b1[i][2][0]])
    b2.sort(b3 = lambda x: x[0], reverse=True)
    for item in b2:
        print(item[0], item[1])
    print('\n')
    heapq.heapify(b1)
    b4 = len(b1)
    while len(b1) > 1:
        cur_freq, _cur_count, b5 = heapq.heappop(b1)
        next_freq, _next_count, b6 = heapq.heappop(b1)
        heapq.heappush(b1, (cur_freq + next_freq, b4, class1(b5, b6)))
        b4 += 1
    b7 = {}
    if b1:
        [(_freq, _count, root)] = b1
        root.fonk2(b7, '')
    return b7
def fonk4(tree, b8 = 0, side=''):
    if isinstance(tree, class1):
        fonk4(tree.b5, b8 + 1, 'b5')
        fonk4(tree.b6, b8 + 1, 'b6')
    if isinstance(tree, class2):
        print('  ' * b8, side + ' ' + tree.char)
def fonk5(b15, b7):
    b9 = []
    b10 = ""
    for ch in b15:
        b10 += ch
        for dec_ch in b7:
            if b7.get(dec_ch) == b10:
                b9.append(dec_ch)
                b10 = ""
                break
    return "".join(b9)
if b11 = = '__main__':
    b12 = open('test.txt', 'r')
    b13 = b12.read()
    b14 = b13.b20('utf-8')
    b7 = fonk3(b14)
    b15 = ''.join(b7[ch] for ch in b14)
    print(len(b7), len(b15))
    for ch in sorted(b7, b3 = b7.get):
        print(ch + ':', b7[ch])
    print('\n')
    print(b15)
    b16 = open('b15.bin', 'wb')
    b2 = []
    b17 = len(b15) / 8
    for i in range(b17):
        b2.append(b15[i:i + 8])
    for elem in b2:
        b16.write(chr(int(elem, 2)))
    b16.close()
    b18 = "0x%x" % int(b15, 2)
    print(b18)
    b19 = bin(int(b18, 16))[2:]
    print(b19)
    print('\n')
    b20 = fonk5(b15, b7)
    print(b20)
    b21 = open('test2.txt', 'w')
    b21.write(b20.encode('utf-8'))
    b21.close()