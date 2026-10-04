import sys
class class1:
    def fonk1(self, b2, b1 = ''):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(node):
    if node.b4 is None and node.b5 is None:
        return
    if node.b4 is not None:
        node.b4.b3 = '0'
        fonk2(node.b4)
    if node.b5 is not None:
        node.b5.b3 = '1'
        fonk2(node.b5)
def fonk3(b13, node, b2):
    if node.b4 is None and node.b5 is None:
        b13[node.b1] = '{}'.format(node.b3) + b2
        return
    fonk3(b13, node.b4, b2 + node.b4.b3)
    fonk3(b13, node.b5, b2 + node.b5.b3)
def fonk4(data):
    if data is None or len(data) == 0:
        return None, None
    b6 = {}
    for char in data:
        if char not in b6:
            b6[char] = 1
        else:
            b6[char] += 1
    if len(b6) == 1:
        b7 = class1(b6[data[0]], data[0])
        b8 = class1(b7.b2)
        b8.b4 = b7
        b7.b3 = '0'
        b9 = '0' * b6[data[0]]
        return b9, b8
    b10 = sorted(b6.items(), b1=lambda x: x[1])
    b11 = [class1(value[1], value[0]) for value in b10]
    while len(b11) > 1:
        b4 = b11.pop(0)
        b5 = b11.pop(0)
        b12 = class1(b4.b2 + b5.b2)
        b12.b4 = b4
        b12.b5 = b5
        b11.append(b12)
        b11 = sorted(b11, b1=lambda x: x.b2)
    b8 = b11[0]
    fonk2(b8)
    b13 = {}
    fonk3(b13, b8, '')
    b14 = ''.join(b13[char] for char in data)
    return b14, b8
def fonk5(data, b18):
    if data is None or b18 is None:
        return None
    b15 = ""
    b16 = b18
    for b17 in data:
        if b17 = = '0':
            b16 = b16.b4
        else:
            b16 = b16.b5
        if b16.b4 is None and b16.b5 is None:
            b15 += b16.b1
            b16 = b18
    return b15
def fonk6(data):
    print("Original data size:", sys.getsizeof(data))
    print("Original data:", data)
    b14, b18 = fonk4(data)
    if b14:
        print("Encoded data size:", sys.getsizeof(int(b14, b19 = 2)))
        print("Encoded data:", b14)
        b15 = fonk5(b14, b18)
        print("Decoded data size:", sys.getsizeof(b15))
        print("Decoded data:", b15)
    else:
        print("Encoding failed. Data is empty or None.")
if b20 = = "__main__":
    b21 = [
        "The bird is the word",
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for data in b21:
        print("\n--- Test case ---")
        fonk6(data)