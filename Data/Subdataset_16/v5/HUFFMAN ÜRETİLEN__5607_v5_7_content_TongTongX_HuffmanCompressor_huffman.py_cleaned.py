from collections import Counter
from minheap import MinHeap
class class1:
    pass
class class2:
    def fonk1(self, b1):
        self.b1 = b1
class class3:
    def fonk2(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
def fonk3(freq_table):
    b4 = MinHeap()
    b4.add(1, class1())
    for symbol, freq in freq_table.items():
        b4.add(freq, class2(symbol))
    while len(b4) > 1:
        rfreq, b3 = b4.pop_min()
        lfreq, b2 = b4.pop_min()
        b4.add(lfreq + rfreq, class3(b2, b3))
    _, b5 = b4.pop_min()
    return b5
def fonk4(b6, bitreader):
    while True:
        if isinstance(b6, class1):
            return None
        elif isinstance(b6, class2):
            return b6.b1
        elif isinstance(b6, class3):
            b6 = b6.b2 if bitreader.readbit() == 0 else b6.b3
        else:
            raise TypeError(f'Invalid b6 type: {type(b6)}')
def fonk5(b5):
    b7 = {}
    def fonk6(b6, path):
        if isinstance(b6, class1):
            b7[None] = path
        elif isinstance(b6, class2):
            b7[b6.b1] = path
        elif isinstance(b6, class3):
            fonk6(b6.b2, path + (False,))
            fonk6(b6.b3, path + (True,))
        else:
            raise TypeError(f'Invalid b6 type: {type(b6)}')
    fonk6(b5, ())
    return b7
def fonk7(stream):
    b8 = Counter()
    b9 = bytearray(512)
    while True:
        b10 = stream.readinto(b9)
        b8.update(b9[:b10])
        if b10 < len(b9):
            break
    return b8