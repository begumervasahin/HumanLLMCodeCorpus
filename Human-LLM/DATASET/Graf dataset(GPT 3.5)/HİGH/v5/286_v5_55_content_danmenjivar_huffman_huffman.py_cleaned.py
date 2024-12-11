
def fonk1(b9):
    with open(b9, 'r') as file:
        return file.read()
def fonk2(b10):
    b1 = {}
    for letter in b10:
        b1[letter] = b1.get(letter, 0) + 1
    return b1
def fonk3(b1):
    b2 = [[weight, [char, '']] for char, weight in b1.items()]
    while len(b2) > 1:
        b2.sort()
        b3 = b2.pop(0)
        b4 = b2.pop(0)
        b5 = [b3[0] + b4[0], [b3, b4]]
        b2.append(b5)
    return b2[0]
def fonk4(b11):
    b6 = {}
    def fonk5(node, b7 = ''):
        if len(node[1]) == 2:
            fonk5(node[1][0], b7 + '0')
            fonk5(node[1][1], b7 + '1')
        else:
            b6[node[1][0]] = b7
    fonk5(b11)
    return b6
def fonk6(b6):
    print('Binary b6 are:')
    print('Character\tBinary Huffman\tBinary ASCII')
    for char, b7 in b6.items():
        print(f'\'{char}\'\t\t{b7}\t\t{bin(ord(char))[2:]}')
def fonk7(b10, b6):
    b8 = ''.join(b6[char] for char in b10)
    return b8
def fonk8():
    print('Huffman Encoding Program')
    b9 = input('Enter the name of a text file to open: ') + '.txt'
    b10 = fonk1(b9)
    b1 = fonk2(b10)
    b11 = fonk3(b1)
    b6 = fonk4(b11)
    fonk6(b6)
    b12 = fonk7(b10, b6)
    print(f"The b10 of the file are: \'{b10}\'")
    print(f'The Huffman encoded b10 are: \'{b12}\'')
if b13 = = "__main__":
    fonk8()