import heapq
from collections import Counter
from functools import partial
from io import StringIO
class class1:
    def fonk1(self, b3, b2):
        if not b3 or b2 <= 0:
            raise ValueError("Invalid b3 or b2.")
        self.b1 = b3
        self.b2 = b2
        self.b3 = [chunk for chunk in iter(partial(StringIO(b3).read, b2), '')]
        self.b4 = {}
    def fonk2(self):
        b5 = self.fonk8()
        b6 = self.fonk9(b5)
        self.fonk10(b6)
        return self.fonk11()
    def fonk3(self, b17):
        if not b17:
            raise ValueError("Invalid encoded value.")
        b7 = ''
        b8 = ''
        b9 = self.fonk7()
        for bit in b17:
            b7 += bit
            if b7 in b9:
                b8 += b9[b7]
                b7 = ''
        return b8
    def fonk4(self, b17):
        if not b17 or not self.b3:
            raise ValueError("Invalid encoded value or original b3.")
        b10 = len(self.b1) * 8
        b11 = len(b17)
        return 1 - (b11 / float(b10))
    @property
    def fonk5(self):
        return self.b4
    @dictionary.setter
    def fonk6(self, value):
        self.b4 = value
    def fonk7(self):
        return {v: k for k, v in self.b4.items()}
    def fonk8(self):
        return [(freq, char) for char, freq in Counter(self.b3).items()]
    def fonk9(self, frequency):
        if not frequency:
            raise ValueError("Invalid frequency table.")
        heapq.heapify(frequency)
        while len(frequency) > 1:
            b12 = heapq.heappop(frequency)
            b13 = heapq.heappop(frequency)
            b14 = (b12[0] + b13[0], b12, b13)
            heapq.heappush(frequency, b14)
        return frequency[0]
    def fonk10(self, tree):
        b15 = [(tree, '')]
        while b15:
            node, b16 = b15.pop()
            if len(node) == 2:
                self.b4[node[1]] = b16
            else:
                b15.append((node[1], b16 + '0'))
                b15.append((node[2], b16 + '1'))
    def fonk11(self):
        if not self.b4:
            raise ValueError("class1 encoding table has not been created.")
        b17 = ''.join(self.b4[char] for char in self.b3 if char in self.b4)
        return b17
def fonk12(b3):
    print("************** Test Encoding **************")
    b18 = class1(b3, 4)
    b19 = b18.fonk2()
    b20 = b18.fonk3(b19)
    print(f"Original b3: {b3}")
    print(f"Encoded b3: {b19}")
    print(f"Decoded b3: {b20}")
    print(f"Original and decoded b3 are the same: {b3 = = b20}")
    print(f"Compression Ratio: {b18.fonk4(b19)}")
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
    with open(b26, "rb") as file:
        b3 = fonk12(file.read())