import sys
class class1:
    def fonk1(self, b2, b1 = ''):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
def fonk2(node):
    if not node.b4 and not node.b5:
        return
    if node.b4:
        node.b4.b3 = '0'
        fonk2(node.b4)
    if node.b5:
        node.b5.b3 = '1'
        fonk2(node.b5)
def fonk3(b13, node, current_code):
    if not node.b4 and not node.b5:
        b13[node.b1] = current_code
        return
    if node.b4:
        fonk3(b13, node.b4, current_code + node.b4.b3)
    if node.b5:
        fonk3(b13, node.b5, current_code + node.b5.b3)
def fonk4(data):
    if not data:
        return None, None
    b6 = {}
    for char in data:
        b6[char] = b6.get(char, 0) + 1
    if len(b6) == 1:
        b7 = list(b6.keys())[0]
        b8 = class1(b6[b7])
        b8.b4 = class1(b6[b7], b7)
        b8.b4.b3 = '0'
        return '0' * len(data), b8
    b9 = [class1(b2, b1) for b1, b2 in sorted(b6.items(), b1=lambda x: x[1])]
    while len(b9) > 1:
        b10 = b9.pop(0)
        b11 = b9.pop(0)
        b12 = class1(b10.b2 + b11.b2)
        b12.b4 = b10
        b12.b5 = b11
        b9.append(b12)
        b9.sort(b1 = lambda x: x.b2)
    b8 = b9[0]
    fonk2(b8)
    b13 = {}
    fonk3(b13, b8, '')
    b14 = ''.join(b13[char] for char in data)
    return b14, b8
def fonk5(b14, b18):
    if not b14 or not b18:
        return None
    if b18.b4 is None and b18.b5 is None:
        return b18.b4.b1 * len(b14)
    b15 = ''
    b16 = b18
    for bit in b14:
        b16 = b16.b4 if bit == '0' else b16.b5
        if b16.b4 is None and b16.b5 is None:
            b15 += b16.b1
            b16 = b18
    return b15
def fonk6():
    b17 = [
        "The bird is the word",
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for sentence in b17:
        print(f"\nOriginal sentence: {sentence}")
        if sentence is not None:
            print(f"Size of original data: {sys.getsizeof(sentence)} bytes")
        try:
            b14, b18 = fonk4(sentence)
            if b14:
                print(f"Encoded data: {b14}")
                print(f"Size of encoded data: {sys.getsizeof(int(b14, b19 = 2))} bytes")
            b15 = fonk5(b14, b18)
            if b15:
                print(f"Decoded data: {b15}")
                print(f"Size of decoded data: {sys.getsizeof(b15)} bytes")
        except (TypeError, ValueError) as e:
            print(f"Error processing the sentence: {e}")
if b20 = = "__main__":
    fonk6()