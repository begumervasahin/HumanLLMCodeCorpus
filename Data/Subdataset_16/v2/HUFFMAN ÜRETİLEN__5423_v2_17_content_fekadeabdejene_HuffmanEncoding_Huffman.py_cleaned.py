import heapq
from collections import Counter
from functools import partial
from io import StringIO
class class1:
    def fonk1(self, b3, b2):
        if not b3:
            raise ValueError("Invalid b3.")
        if b2 <= 0:
            raise ValueError("Width must be greater than 0.")
        self.b1 = b3
        self.b2 = b2
        self.b3 = [segment for segment in iter(partial(StringIO(b3).read, self.b2), '')]
        self.b4 = {}
    def fonk2(self):
        b5 = self.fonk7()
        b6 = self.fonk8(b5)
        self.fonk9(b6)
        return self.fonk10()
    def fonk3(self, b17):
        if not b17:
            raise ValueError("Invalid encoded value.")
        b7 = []
        b8 = ''
        b9 = self._reversed_dictionary
        for bit in b17:
            b8 += bit
            if b8 in b9:
                b7.append(b9[b8])
                b8 = ''
        return ''.join(b7)
    def fonk4(self, b17):
        if not b17:
            raise ValueError("Invalid encoded value.")
        b10 = len(self.b1) * 8
        b11 = len(b17)
        return 1 - (b11 / b10)
    @property
    def fonk5(self):
        return self.b4
    @property
    def fonk6(self):
        return {v: k for k, v in self.b4.items()}
    def fonk7(self):
        return [(freq, char) for char, freq in Counter(self.b3).items()]
    def fonk8(self, b5):
        if not b5:
            raise ValueError("Invalid frequency map.")
        heapq.heapify(b5)
        while len(b5) > 1:
            b12 = heapq.heappop(b5)
            b13 = heapq.heappop(b5)
            b14 = (b12[0] + b13[0], b12, b13)
            heapq.heappush(b5, b14)
        return b5[0]
    def fonk9(self, tree):
        b15 = [(tree, '1' if len(tree) == 2 else '')]
        while b15:
            node, b16 = b15.pop()
            if len(node) == 2:
                self.b4[node[1]] = b16
            else:
                b15.append((node[1], b16 + '0'))
                b15.append((node[2], b16 + '1'))
    def fonk10(self):
        if not self.b4:
            raise ValueError("class1 dictionary has not been created.")
        b17 = ''.join(self.b4[char] for char in self.b3)
        return b17
def fonk11(b3):
    b18 = class1(b3, 4)
    b19 = b18.fonk2()
    b20 = b18.fonk3(b19)
    print("************** Test Encoding **************")
    print("Encoded b3:", b19)
    print("Decoding successful:", b20 = = b3)
    print("Compression Ratio:", b18.fonk4(b19))
    print()
    return b20
if b21 = = "__main__":
    b22 = [
        "a",
        "abcdefghijklmnopqrstuvwxyz",
        "aaaaaaaaaaaaaaaaaaaaaaaaaa",
        "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
    ]
    for test_data in b22:
        fonk11(test_data)
    with open("test_data.txt", "r") as file:
        b23 = file.read()
    fonk11(b23)