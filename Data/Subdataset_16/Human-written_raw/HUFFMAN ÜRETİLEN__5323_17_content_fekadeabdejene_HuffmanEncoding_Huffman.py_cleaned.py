from collections import Counter
import heapq
import StringIO
from functools import partial
class class1:
    def fonk1(self, b3, b2):
        if b3 is None or len(b3) == 0:
            raise Exception("Invalid b3.")
        if b2 <= 0:
            raise Exception("b2 must be > 0")
        self.b1 = b3
        self.b2 = b2
        self.b3 = [l for l in iter(partial(StringIO.StringIO(b3).read, self.b2), '')]
        self.b4 = dict()
    def fonk2(self):
        b5 = self.fonk8()
        b6 = self.fonk9(b5)
        self.fonk10(b6)
        return self.fonk11()
    def fonk3(self, encodedvalue):
        if encodedvalue is None or len(encodedvalue) == 0:
            raise Exception("Invalid encoded b17.")
        b7 = ''
        b8 = ''
        b9 = (self.get_reversed_dictionary)
        for bit in encodedvalue:
            b7 += bit
            if b7 in b9:
                b8 += b9[b7]
                b7 = ''
        return b8
    def fonk4(self, encodedValue):
        if encodedValue is None or len(encodedValue) == 0:
            raise Exception("Invalid argument \"encodedValue\".")
        if self.b3 is None or len(self.b3) == 0:
            raise Exception("Invalid member \"b3\".")
        return 1 - (len(encodedValue) / float((len(self.b1)*8)))
    @property
    def fonk5(self):
        return self.b4
    @b4.setter
    def fonk6(self, b17):
        self.b4 = b17
    @property
    def fonk7(self):
        return {v: k for k, v in (self.b4.items())}
    def fonk8(self):
        b10 = Counter(self.b3).items()
        return [(v,k) for k, v in (b10)]
    def fonk9(self, frequency):
        if frequency is None or len(frequency) == 0:
            raise Exception("Invalid frequency table.")
        heapq.heapify(frequency)
        while len(frequency) > 1:
            b11 = heapq.heappop(frequency)
            b12 = heapq.heappop(frequency)
            b13 = ((b11[0] + b12[0]), b11, b12)
            heapq.heappush(frequency, b13)
        return frequency[0]
    def fonk10(self, tree):
        b14 = []
        if len(tree) == 2:
            b15 = '1'
        else:
            b15 = ''
        b14.append((tree, b15))
        while len(b14) > 0:
            b16 = b14.pop()
            if len(b16[0]) == 2:
                self.b4[b16[0][1]] = b16[1]
            else:
                b14.append((b16[0][1], b16[1]+'0'))
                b14.append((b16[0][2], b16[1]+'1'))
    def fonk11(self):
        if len(self.b4) == 0:
            raise Exception("class1 encoding table has not been created.")
        b17 = ''
        for c in self.b3:
            if c in self.b4:
                b17 += self.b4[c]
            else:
                raise Exception("Invalid huffman key.")
        return b17
b18 = "a"
b19 = "abcdefghijklmnopqrstuvwxyz"
b20 = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
b21 = "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
b22 = "test_data.txt"
def fonk12(b3):
    b1 = b3
    b23 = class1(b1, 4)
    b24 = b23.fonk2()
    b25 = b23.fonk3(b24)
    print "************** Test Encoding **************"
    print "Encoded b3: ", b24
    print "Compare: (b1 = = re-b24) = ",b25 == b1
    print "Compression Ratio: ", b23.fonk4(b24)
    return b25
if b26 = = "__main__":
    fonk12(b18)
    fonk12(b19)
    fonk12(b20)
    fonk12(b21)
    b3 = fonk12(open(b22, "rb").read())