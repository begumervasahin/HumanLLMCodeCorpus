import sys
from collections import defaultdict
class class1:
    def fonk1(self, b2, b1 = ''):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(node, b3 = ''):
    if node is None:
        return
    if node.b4 is None and node.b5 is None:
        node.b3 = b3
        return
    fonk2(node.b4, b3 + '0')
    fonk2(node.b5, b3 + '1')
def fonk3(b9):
    b6 = [class1(freq, char) for char, freq in b9.items()]
    while len(b6) > 1:
        b6.sort(b1 = lambda node: node.b2)
        b4 = b6.pop(0)
        b5 = b6.pop(0)
        b7 = class1(b4.b2 + b5.b2)
        b7.b4 = b4
        b7.b5 = b5
        b6.append(b7)
    return b6[0] if b6 else None
def fonk4(b12):
    b8 = {}
    fonk2(b12)
    fonk5(b12, b8)
    return b8
def fonk5(node, b8):
    if node.b4 is None and node.b5 is None:
        b8[node.b1] = node.b3
        return
    fonk5(node.b4, b8)
    fonk5(node.b5, b8)
def fonk6(data):
    if not data:
        return None, None
    b9 = defaultdict(int)
    for char in data:
        b9[char] += 1
    if len(b9) == 1:
        b10 = next(iter(b9))
        b11 = '0' * len(data)
        b12 = class1(b9[b10])
        b12.b4 = class1(b9[b10], b10)
        return b11, b12
    b12 = fonk3(b9)
    b8 = fonk4(b12)
    b11 = ''.join(b8[char] for char in data)
    return b11, b12
def fonk7(b11, b12):
    if not b11 or not b12:
        return None
    b13 = []
    b14 = b12
    for bit in b11:
        b14 = b14.b4 if bit == '0' else b14.b5
        if b14.b4 is None and b14.b5 is None:
            b13.append(b14.b1)
            b14 = b12
    return ''.join(b13)
def fonk8(data):
    print(f"Original data size: {sys.getsizeof(data)} bytes")
    print(f"Original data: {data}")
    b11, b15 = fonk6(data)
    if b11:
        print(f"Encoded data size: {sys.getsizeof(int(b11, b16 = 2))} bytes")
        print(f"Encoded data: {b11}")
        b13 = fonk7(b11, b15)
        print(f"Decoded data size: {sys.getsizeof(b13)} bytes")
        print(f"Decoded data: {b13}")
    else:
        print("Encoding failed. Data is empty or None.")
if b17 = = "__main__":
    b18 = [
        "The bird is the word",
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for data in b18:
        print("\n--- Test case ---")
        fonk8(data)