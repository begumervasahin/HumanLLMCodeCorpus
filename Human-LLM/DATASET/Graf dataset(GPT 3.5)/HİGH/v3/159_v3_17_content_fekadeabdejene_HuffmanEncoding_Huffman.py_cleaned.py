from collections import Counter
import heapq
from functools import partial
import io
class class1:
    def fonk1(self, b27, b2):
        if b27 is None or len(b27) == 0:
            raise ValueError("Invalid b27.")
        if b2 <= 0:
            raise ValueError("Width must be > 0")
        self.b1 = b27
        self.b2 = b2
        self.b3 = [chunk for chunk in iter(partial(io.StringIO(b27).read, self.b2), '')]
        self.b4 = {}
    def fonk2(self):
        b5 = self.fonk8()
        b6 = self.fonk9(b5)
        self.fonk10(b6)
        return self.fonk11()
    def fonk3(self, encoded_value):
        if encoded_value is None or len(encoded_value) == 0:
            raise ValueError("Invalid encoded b17.")
        b7 = ''
        b8 = ''
        b9 = self.fonk7()
        for bit in encoded_value:
            b7 += bit
            if b7 in b9:
                b8 += b9[b7]
                b7 = ''
        return b8
    def fonk4(self, encoded_value):
        if encoded_value is None or len(encoded_value) == 0:
            raise ValueError("Invalid argument 'encoded_value'.")
        if self.b1 is None or len(self.b1) == 0:
            raise ValueError("Invalid member 'b1'.")
        return 1 - (len(encoded_value) / float((len(self.b1)*8)))
    @property
    def fonk5(self):
        return self.b4
    @b4.setter
    def fonk6(self, b17):
        self.b4 = b17
    def fonk7(self):
        return {v: k for k, v in self.b4.items()}
    def fonk8(self):
        b10 = Counter(self.b3).items()
        return [(v,k) for k, v in b10]
    def fonk9(self, frequency):
        if frequency is None or len(frequency) == 0:
            raise ValueError("Invalid frequency table.")
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
            raise ValueError("class1 encoding table has not been created.")
        b17 = ''
        for c in self.b3:
            if c in self.b4:
                b17 += self.b4[c]
            else:
                raise ValueError("Invalid b18 key.")
        return b17
def fonk12(b27):
    b1 = b27
    b18 = class1(b1, 4)
    b19 = b18.fonk2()
    b20 = b18.fonk3(b19)
    print("************** Test Encoding **************")
    print("Encoded b27: ", b19)
    print("Compare: (b1 = = re-b19) = ", b20 == b1)
    print("Compression Ratio: ", b18.fonk4(b19))
    return b20
if b21 = = "__main__":
    b22 = "a"
    b23 = "abcdefghijklmnopqrstuvwxyz"
    b24 = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
    b25 = "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
    b26 = "test_data.txt"
    fonk12(b22)
    fonk12(b23)
    fonk12(b24)
    fonk12(b25)
    b27 = fonk12(open(b26, "rb").read())