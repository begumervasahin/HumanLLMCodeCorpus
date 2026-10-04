import heapq
from collections import Counter
from functools import partial
from io import StringIO
class class1:
    def fonk1(self, data, b2):
        if not data:
            raise ValueError("Invalid data.")
        if b2 <= 0:
            raise ValueError("Width must be greater than 0.")
        self.b1 = data
        self.b2 = b2
        self.b3 = [segment for segment in iter(partial(StringIO(data).read, self.b2), '')]
        self.b4 = {}
    def fonk2(self):
        b5 = self.fonk6()
        b6 = self.fonk7(b5)
        self.fonk8(b6)
        return self.fonk9()
    def fonk3(self, b18):
        if not b18:
            raise ValueError("Invalid encoded data.")
        b7 = []
        b8 = ''
        b9 = self._reversed_huffman_codes
        for bit in b18:
            b8 += bit
            if b8 in b9:
                b7.append(b9[b8])
                b8 = ''
        return ''.join(b7)
    def fonk4(self, b18):
        if not b18:
            raise ValueError("Invalid encoded data.")
        b10 = len(self.b1) * 8
        b11 = len(b18)
        return 1 - (b11 / b10)
    @property
    def fonk5(self):
        return {b16: char for char, b16 in self.b4.items()}
    def fonk6(self):
        return [(freq, char) for char, freq in Counter(self.b3).items()]
    def fonk7(self, b5):
        if not b5:
            raise ValueError("Invalid frequency map.")
        heapq.heapify(b5)
        while len(b5) > 1:
            b12 = heapq.heappop(b5)
            b13 = heapq.heappop(b5)
            b14 = (b12[0] + b13[0], b12, b13)
            heapq.heappush(b5, b14)
        return b5[0]
    def fonk8(self, tree):
        b15 = [(tree, '')]
        while b15:
            node, b16 = b15.pop()
            if len(node) == 2:
                self.b4[node[1]] = b16
            else:
                b15.append((node[1], b16 + '0'))
                b15.append((node[2], b16 + '1'))
    def fonk9(self):
        if not self.b4:
            raise ValueError("class1 codes have not been generated.")
        return ''.join(self.b4[segment] for segment in self.b3)
def fonk10(data):
    b17 = class1(data, 4)
    b18 = b17.fonk2()
    b7 = b17.fonk3(b18)
    print("************** Test Encoding **************")
    print(f"Original data: {data}")
    print(f"Encoded data: {b18}")
    print(f"Decoding successful: {b7 = = data}")
    print(f"Compression Ratio: {b17.fonk4(b18):.2%}")
    print()
    return b7
if b19 = = "__main__":
    b20 = [
        "a",
        "abcdefghijklmnopqrstuvwxyz",
        "aaaaaaaaaaaaaaaaaaaaaaaaaa",
        "asdfjbdsjkbfdifbeibfosdibfjkeboiuwebfisdbifbiobwieufbew"
    ]
    for test_data in b20:
        fonk10(test_data)
    with open("test_data.txt", "r") as file:
        b21 = file.read()
    fonk10(b21)