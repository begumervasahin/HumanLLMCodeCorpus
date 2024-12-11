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
        fonk4(tree.b3, b6+1, 'b3')
        fonk4(tree.b4, b6+1, 'b4')
    if isinstance(tree, class2):
        print '  ' * b6, side + ' ' + tree.char
def fonk5(b13, b5):
    b7 = []
    b8 = ""
    for ch in b13:
        b8 += ch
        for dec_ch in b5:
            if b5.get(dec_ch) == b8:
                b7.append(dec_ch)
                b8 = ""
                break
    return "".join(b7)
if b9 = = '__main__':
    b10 = open('test.txt', 'r')
    b11 = b10.read()
    b12 = b11.b20('utf-8')
    b5 = fonk3(b12)
    b13 = ''.join(b5[ch] for ch in b12)
    print(len(b5), len(b13))
    for ch in sorted(b5, b14 = b5.get):
        print ch + ':', b5[ch]
    print '\n'
    print b13
    b15 = open('b13.bin', 'wb')
    b16 = []
    b17 = len(b13) / 8
    for i in range(b17):
        b16.append(b13[i:i+8])
    for elem in b16:
        b15.write(chr(int(elem, 2)))
    b15.close()
    b18 = "0x%x" % int(b13, 2)
    print b18
    b19 = bin(int(b18, 16))[2:]
    print b19
    print '\n'
    b20 = fonk5(b13, b5)
    print b20
    b21 = open('test2.txt', 'w')
    b21.write(b20.encode('utf-8'))
    b21.close()