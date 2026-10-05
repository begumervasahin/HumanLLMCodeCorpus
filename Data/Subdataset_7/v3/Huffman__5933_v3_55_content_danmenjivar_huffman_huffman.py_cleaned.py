def fonk1():
    print('Huffman Encoding Program')
    b1 = input('Enter the name of a text file to open: ') + '.txt'
    b2 = fonk2(b1)
    b3 = fonk3(b2)
    b4 = fonk4(b3)
    b5 = fonk5(b4)
    fonk7(b5)
    b6 = fonk8(b2, b5)
    fonk9(b2)
    fonk10(b6)
def fonk2(b1):
    with open(b1, 'r') as file:
        return file.read()
def fonk3(b2):
    b7 = {}
    for letter in b2:
        b7[letter] = b7.get(letter, 0) + 1
    return sorted(b7.items(), b8 = lambda x: x[1], reverse=True)
def fonk4(b3):
    b9 = [[(freq, letter)] for letter, freq in b3]
    while len(b9) > 1:
        b10 = b9[-2:]
        b11 = (b10[0][0][0] + b10[1][0][0], b10)
        b9 = b9[:-2] + [b11]
        b9.sort()
    return b9
def fonk5(b4):
    b12 = []
    fonk6(b4, '', b12)
    return sorted(b12, b8 = lambda x: x[0], reverse=True)
def fonk6(tree, code, b12):
    if len(tree) == 1:
        b12.append((tree[0][1], code))
    else:
        fonk6(tree[0][1], code + '0', b12)
        fonk6(tree[1][1], code + '1', b12)
def fonk7(b5):
    print('Binary codes are:')
    print('Character\tBinary Huffman\tBinary ASCII')
    for character, binary_code in b5:
        b13 = bin(ord(character))[2:]
        print(f'\'{character}\'\t\t{binary_code}\t\t{b13}')
def fonk8(b2, b5):
    b6 = ''
    for character in b2:
        for item in b5:
            if character in item:
                b6 += item[1]
    return b6
def fonk9(b2):
    print(f"The b2 of the file are: '{b2}'")
def fonk10(b6):
    print(f"The Huffman encoded b2 are: '{b6}'")
if b14 = = '__main__':
    fonk1()