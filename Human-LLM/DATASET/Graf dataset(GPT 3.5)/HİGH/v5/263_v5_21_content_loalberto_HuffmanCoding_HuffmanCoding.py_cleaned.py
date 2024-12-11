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
def fonk3(b15, node, b2):
    if node.b4 is None and node.b5 is None:
        b15[node.b1] = '{}{}'.format(node.b3, b2)
        return
    fonk3(b15, node.b4, b2 + node.b4.b3)
    fonk3(b15, node.b5, b2 + node.b5.b3)
def fonk4(data):
    if data is None:
        return None
    b2 = {}
    for char in data:
        b2[char] = b2.get(char, 0) + 1
    if len(b2) == 1:
        b6 = class1(b2[data[0]], data[0])
        b7 = class1(b6.b2)
        b7.b4 = b6
        b6.b3 = '0'
        b8 = '0' * b2[data[0]]
        return b8, b7
    b9 = sorted(b2.items(), b1=lambda x: x[1])
    b10 = [class1(value[1], value[0]) for value in b9]
    b10.append(class1(None))
    while len(b10) > 2:
        b11 = b10.pop(0)
        if b11.b2 is None:
            b10.append(b11)
            continue
        b12 = b10.pop(0)
        if b12.b2 is None:
            b10.append(b11)
            b10.append(b12)
            continue
        b13 = class1(b11.b2 + b12.b2)
        b13.b4 = b11
        b13.b5 = b12
        b10.append(b13)
    b7 = b10.pop(0)
    if b7.b2 is None:
        b7 = b10.pop(0)
    fonk2(b7)
    return b7
def fonk5(data):
    b14 = fonk4(data)
    if b14 is None:
        return None
    b15 = {}
    fonk3(b15, b14, '')
    b16 = ''.join(b15[char] for char in data)
    return b16, b14
def fonk6(data, dec_tree):
    if data is None or dec_tree is None:
        return None
    if dec_tree.b5 is None:
        b17 = len(data)
        b18 = dec_tree.b4.b1
        return b18 * b17
    b19 = ''
    b20 = {}
    fonk3(b20, dec_tree, '')
    b21 = {b20[b1]: b1 for b1 in b20}
    b22 = ''
    for char in data:
        b22 += char
        if b22 in b21:
            b19 += b21[b22]
            b22 = ''
    return b19
if b23 = = "__main__":
    b24 = "The bird is the word"
    print("Original Data: {}\n".format(b24))
    b16, b14 = fonk5(b24)
    print("Encoded Data: {}\n".format(b16))
    b25 = fonk6(b16, b14)
    print("Decoded Data: {}\n".format(b25))
    print("\nAdditional Test Cases:")
    b26 = [
        "The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg",
        None,
        "aaaaaaaa"
    ]
    for test_case in b26:
        print("Original Data: {}\n".format(test_case))
        try:
            b16, b14 = fonk5(test_case)
            print("Encoded Data: {}\n".format(b16))
            b25 = fonk6(b16, b14)
            print("Decoded Data: {}\n".format(b25))
        except (TypeError, ValueError):
            print('Error')