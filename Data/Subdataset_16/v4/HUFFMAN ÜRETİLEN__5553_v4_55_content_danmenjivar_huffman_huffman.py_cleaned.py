
print('Huffman Encoding Program')
b1 = input('Enter the name of a text file to open: ') + '.txt'
with open(b1, 'r') as file:
    b2 = file.read()
b3 = {}
for letter in b2:
    if letter in b3:
        b3[letter] += 1
    else:
        b3[letter] = 1
b4 = [[frequency, letter] for letter, frequency in b3.items()]
b4.sort()
def fonk1(b4):
    while len(b4) > 1:
        b5 = b4.pop(0)
        b6 = b4.pop(0)
        b7 = [b5[0] + b6[0], b5, b6]
        b5.append('0')
        b6.append('1')
        b4.append(b7)
        b4.sort(b8 = lambda x: x[0])
    return b4[0]
b9 = fonk1(b4)
def fonk2(tree, b10 = ''):
    if len(tree) == 2:
        return {tree[1]: b10}
    else:
        b11 = {}
        b11.update(fonk2(tree[1], b10 + tree[1][-1]))
        b11.update(fonk2(tree[2], b10 + tree[2][-1]))
        return b11
b12 = fonk2(b9)
print('Binary b11 are:')
print('Character\tBinary Huffman\tBinary ASCII')
for char, code in sorted(b12.items(), b8 = lambda item: b3[item[0]], reverse=True):
    print(f"'{char}'\t\t{code}\t\t{bin(ord(char))[2:]}")
b13 = ''.join(b12[char] for char in b2)
print(f"The b2 of the file are: '{b2}'")
print(f"The Huffman encoded b2 are: '{b13}'")