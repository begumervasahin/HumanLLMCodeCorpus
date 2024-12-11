print('Huffman Encoding Program')
b1 = input('Enter the name of a text file to open: ') + '.txt'
with open(b1, 'r') as file:
    b2 = file.read()
b3 = []
b4 = []
for letter in b2:
    if letter not in b3:
        b5 = b2.count(letter)
        b3.append(b5)
        b3.append(letter)
        b4.append(letter)
b6 = list.copy(b3)
b7 = []
for i in range(0, len(b6), 2):
    b8 = [b6[i], b6[i + 1]]
    b7.append(b8)
b7.sort(b9 = lambda x: x[0], reverse=True)
b10 = []
while len(b3) > 0:
    b10.append(b3[0:2])
    b3 = b3[2:]
b10.sort()
b11 = []
b11.append(b10)
def fonk1(b10):
    a1 = 0
    b12 = []
    if len(b10) > 1:
        b10.sort(b9 = lambda x: int(x[0]))
        b10[a1].append('0')
        b10[a1 + 1].append('1')
        b13 = str(b10[a1][0]) + str(b10[a1 + 1][0])
        b14 = str(b10[a1][1]) + str(b10[a1 + 1][1])
        b12.append(b13)
        b12.append(b14)
        b15 = []
        b15.append(b12)
        b15 = b15 + b10[2:]
        b10 = b15
        b11.append(b10)
        fonk1(b10)
    return b11
b15 = fonk1(b10)
b11.sort(b9 = lambda x: str(x[0]), reverse=True)
b16 = []
for level in b11:
    for node in level:
        if node not in b16:
            b16.append(node)
        else:
            level.remove(node)
b17 = []
if len(b4) == 1:
    b18 = [b4[0], '0']
    b17.append(b18 * len(b2))
else:
    for letter in b4:
        b19 = ''
        for node in b16:
            if len(node) > 2 and letter in node[1]:
                b19 = b19 + node[2]
        b18 = [letter, b19]
        b17.append(b18)
b20 = {y: x for x, y in b7}
b21 = sorted(b17, b9=lambda x: b20[x[0]], reverse=True)
print('Binary codes are: ')
print('Character\tBinary Huffman\tBinary ASCII')
for i in range(len(b21)):
    print('\'%s\'\t\t%s\t\t%s' % (b21[i][0], b21[i][1], bin(ord(b21[i][0][0]))[2:]))
b22 = ''
for character in b2:
    for item in b17:
        if character in item:
            b22 = b22 + item[1]
print("The b2 of the file are: \'%s\'" % b2)
print('The Huffman encoded b2 are: \'%s\'' % b22)