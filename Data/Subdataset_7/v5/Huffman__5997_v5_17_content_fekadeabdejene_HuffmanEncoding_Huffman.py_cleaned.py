from collections import Counter
import heapq
import io
from functools import partial
class class1:
    def fonk1(self, b3, b2):
        self.fonk2(b3, b2)
        self.b1 = b3
        self.b2 = b2
        self.b3 = [l for l in iter(partial(io.StringIO(b3).read, self.b2), '')]
        self.b4 = {}
    def fonk2(self, b3, b2):
        if b3 is None or len(b3) == 0:
            raise ValueError("Invalid b3.")
        if b2 <= 0:
            raise ValueError("Width must be > 0")
    def fonk3(self):
        b5 = self.fonk11()
        b6 = self.fonk12(b5)
        self.fonk14(b6)
        return self.fonk15()
    def fonk4(self, b17):
        self.fonk5(b17)
        b7 = ''
        b8 = ''
        b9 = self.fonk10(b17)
        for bit in b17:
            b7 += bit
            if b7 in b9:
                b8 += b9[b7]
                b7 = ''
        return b8
    def fonk5(self, b17):
        if b17 is None or len(b17) == 0:
            raise ValueError("Invalid encoded value.")
    def fonk6(self, b17):
        self.fonk7(b17)
        return 1 - (len(b17) / float((len(self.b1) * 8)))
    def fonk7(self, b17):
        if b17 is None or len(b17) == 0:
            raise ValueError("Invalid argument \"b17\".")
        if self.b3 is None or len(self.b3) == 0:
            raise ValueError("Invalid member \"b3\".")
    @property
    def fonk8(self):
        return self.b4
    @b4.setter
    def fonk9(self, value):
        self.b4 = value
    def fonk10(self, b17):
        return {v: k for k, v in self.b4.items()}
    def fonk11(self):
        b10 = Counter(self.b3).items()
        return [(v, k) for k, v in b10]
    def fonk12(self, frequency):
        self.fonk13(frequency)
        heapq.heapify(frequency)
        while len(frequency) > 1:
            b11 = heapq.heappop(frequency)
            b12 = heapq.heappop(frequency)
            b13 = ((b11[0] + b12[0]), b11, b12)
            heapq.heappush(frequency, b13)
        return frequency[0]
    def fonk13(self, frequency):
        if frequency is None or len(frequency) == 0:
            raise ValueError("Invalid frequency table.")
    def fonk14(self, tree):
        b14 = []
        b15 = '1' if len(tree) == 2 else ''
        b14.append((tree, b15))
        while len(b14) > 0:
            b16 = b14.pop()
            if len(b16[0]) == 2:
                self.b4[b16[0][1]] = b16[1]
            else:
                b14.append((b16[0][1], b16[1] + '0'))
                b14.append((b16[0][2], b16[1] + '1'))
    def fonk15(self):
        self.fonk16()
        b17 = ''
        for c in self.b3:
            if c in self.b4:
                b17 += self.b4[c]
            else:
                raise ValueError("Invalid class1 key.")
        return b17
    def fonk16(self):
        if len(self.b4) == 0:
            raise ValueError("class1 encoding table has not been created.")
def fonk17(b3):
    b1 = b3
    b18 = class1(b1, 4)
    b19 = b18.fonk3()
    b20 = b18.fonk4(b19)
    print("************** Test Encoding **************")
    print("Encoded b3: ", b19)
    print("Compare: (b1 = = re-b19) = ", b20 == b1)
    print("Compression Ratio: ", b18.fonk6(b19))
    return b20
if b21 = = "__main__":
    fonk17("a")
    fonk17("abcdefghijklmnopqrstuvwxyz")
    fonk17("aaaaaaaaaaaaaaaaaaaaaaaaaa")
    fonk17("asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew")
    b3 = fonk17(open("test_data.txt", "rb").read())