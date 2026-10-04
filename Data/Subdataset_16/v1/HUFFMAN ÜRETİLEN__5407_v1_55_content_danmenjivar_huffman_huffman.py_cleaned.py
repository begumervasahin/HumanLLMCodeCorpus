import collections
def fonk1(b12: str) -> str:
    with open(b12, 'r') as file:
        return file.read()
def fonk2(b13: str) -> list:
    b1 = collections.Counter(b13)
    return sorted([[freq, char] for char, freq in b1.items()], b2 = lambda x: x[0], reverse=True)
def fonk3(b14: list) -> list:
    b3 = [[freq, char] for freq, char in b14]
    while len(b3) > 1:
        b3.sort(b2 = lambda x: x[0])
        b4 = b3.pop(0)
        b5 = b3.pop(0)
        b6 = [b4[0] + b5[0], b4[1] + b5[1]]
        b4.append('0')
        b5.append('1')
        b3.append(b6)
        b3.sort(b2 = lambda x: x[0])
    return b3
def fonk4(tree: list, b15: list) -> list:
    b7 = []
    for node in tree:
        if node not in b7:
            b7.append(node)
    if len(b15) == 1:
        return [[b15[0], '0']]
    b8 = []
    for char in b15:
        b9 = ''.join([node[2] for node in b7 if len(node) > 2 and char in node[1]])
        b8.append([char, b9])
    return b8
def fonk5(b13: str, b17: list) -> str:
    b10 = ''.join([b9 for char in b13 for item, b9 in b17 if char == item])
    return b10
def fonk6(b17: list, b14: dict):
    print('Character\tBinary Huffman\tBinary ASCII')
    b11 = sorted(b17, b2=lambda x: b14[x[0]], reverse=True)
    for char, b9 in b11:
        print(f"'{char}'\t\t{b9}\t\t{bin(ord(char))[2:]}")
def fonk7():
    print('Huffman Encoding Program')
    b12 = input('Enter the name of a text file to open: ') + '.txt'
    b13 = fonk1(b12)
    b14 = fonk2(b13)
    b15 = [char for _, char in b14]
    b16 = fonk3(b14)
    b17 = fonk4(b16, b15)
    b10 = fonk5(b13, b17)
    print("The b13 of the file are:", repr(b13))
    print("The Huffman encoded b13 are:", repr(b10))
    b18 = {char: freq for freq, char in b14}
    fonk6(b17, b18)
if b19 = = '__main__':
    fonk7()