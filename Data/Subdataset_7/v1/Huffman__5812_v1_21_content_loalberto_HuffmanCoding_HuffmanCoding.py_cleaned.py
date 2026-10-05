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
def fonk3(b14, node, b2):
    if node.b4 is None and node.b5 is None:
        b14[node.b1] = '{}'.format(node.b3) + b2
        return
    fonk3(b14, node.b4, b2 + node.b4.b3)
    fonk3(b14, node.b5, b2 + node.b5.b3)
def fonk4(data):
    if data is None:
        return None
    b2 = {}
    for char in data:
        if char not in b2:
            b2[char] = 1
            continue
        b2[char] += 1
    if len(b2) == 1:
        b6 = class1(b2[data[0]], data[0])
        b7 = class1(b6.b2)
        b7.b4 = b6
        b6.b3 = 0
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
    b14 = {}
    fonk3(b14, b7, '')
    b15 = ''
    for char in data:
        b15 += b14[char]
    return b15, b7
def fonk5(data, dec_tree):
    if data is None or dec_tree is None:
        return
    if dec_tree.b5 is None:
        b16 = len(data)
        b17 = dec_tree.b4.b1
        return b17 * b16
    b18 = ''
    b19 = {}
    fonk3(b19, dec_tree, '')
    b20 = {}
    for b1 in b19:
        b20[b19[b1]] = b1
    b21 = ''
    for char in data:
        b21 += char
        if b21 in b20:
            b18 += b20[b21]
            b21 = ''
    return b18
def fonk6(input_data):
    print("The size of the data is: {}\n".format(sys.getsizeof(input_data)))
    print("The content of the data is: {}\n".format(input_data))
    encoded_data, b22 = fonk4(input_data)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, b23 = 2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    b24 = fonk5(encoded_data, b22)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(b24)))
    print("The content of the decoded data is: {}\n".format(b24))
if b25 = = "__main__":
    fonk6("The bird is the word")
if b25 = = "__main__":
    fonk6("The bird is the word23y rkuwejfkjgfkj vduhdqlihoi fhglkrhtieriyweo iwefhli whiflhevidfghierhg")
if b25 = = "__main__":
    fonk6(None)
if b25 = = "__main__":
    fonk6("aaaaaaaa")