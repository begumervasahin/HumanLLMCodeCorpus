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
def fonk3(code_dict, node, b22):
    if node.b4 is None and node.b5 is None:
        code_dict[node.b1] = '{}{}'.format(node.b3, b22)
        return
    fonk3(code_dict, node.b4, b22 + node.b4.b3)
    fonk3(code_dict, node.b5, b22 + node.b5.b3)
def fonk4(data):
    if data is None:
        return None
    b6 = {}
    for char in data:
        b6[char] = b6.get(char, 0) + 1
    if len(b6) == 1:
        b7 = class1(b6[data[0]], data[0])
        b8 = class1(b7.b2)
        b8.b4 = b7
        b7.b3 = '0'
        b9 = '0' * b6[data[0]]
        return b9, b8
    b10 = sorted(b6.items(), b1=lambda x: x[1])
    b11 = [class1(b2[1], b2[0]) for b2 in b10]
    b11.append(class1(None))
    while len(b11) > 2:
        b12 = b11.pop(0)
        if b12.b2 is None:
            b11.append(b12)
            continue
        b13 = b11.pop(0)
        if b13.b2 is None:
            b11.append(b12)
            b11.append(b13)
            continue
        b14 = class1(b12.b2 + b13.b2)
        b14.b4 = b12
        b14.b5 = b13
        b11.append(b14)
    b8 = b11.pop(0)
    if b8.b2 is None:
        b8 = b11.pop(0)
    fonk2(b8)
    b15 = {}
    fonk3(b15, b8, '')
    b16 = ''.join(b15[char] for char in data)
    return b16, b8
def fonk5(b16, decoding_tree):
    if b16 is None or decoding_tree is None:
        return None
    if decoding_tree.b5 is None:
        b17 = len(b16)
        b18 = decoding_tree.b4.b1
        return b18 * b17
    b19 = ''
    b20 = {}
    fonk3(b20, decoding_tree, '')
    b21 = {b3: b1 for b1, b3 in b20.items()}
    b22 = ''
    for char in b16:
        b22 += char
        if b22 in b21:
            b19 += b21[b22]
            b22 = ''
    return b19
def fonk6(input_data):
    print("Original Data Size: {}\n".format(sys.getsizeof(input_data)))
    print("Original Data Content: {}\n".format(input_data))
    b16, b23 = fonk4(input_data)
    print("Encoded Data Size: {}\n".format(sys.getsizeof(int(b16, b24 = 2))))
    print("Encoded Data Content: {}\n".format(b16))
    b25 = fonk5(b16, b23)
    print("Decoded Data Size: {}\n".format(sys.getsizeof(b25)))
    print("Decoded Data Content: {}\n".format(b25))
if b26 = = "__main__":
    fonk6("The bird is the word")
if b26 = = "__main__":
    fonk6("The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg")
if b26 = = "__main__":
    fonk6(None)
if b26 = = "__main__":
    fonk6("aaaaaaaa")