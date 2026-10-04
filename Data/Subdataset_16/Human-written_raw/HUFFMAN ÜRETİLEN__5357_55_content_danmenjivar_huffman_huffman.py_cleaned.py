'''
Algorithms HW
Huffman
Based on: https:
'''
print('Huffman Encoding Program')
b1 = input('Enter the name of a text b2 to open: ') + '.txt'
b2 = open(b1, 'r')
if b2.b3 = = 'r':
    b4 = b2.read()
b5 = []
b6 = []
for letter in b4:
    if letter not in b5:
        b7 = b4.count(letter)
        b5.append(b7)
        b5.append(letter)
        b6.append(letter)
b8 = list.copy(b5)
b9 = []
for i in range(0, len(b8), 2):
    b10 = [b8[i], b8[i + 1]]
    b9.append(b10)
b9.sort(b11 = lambda x : x[0], reverse=True)
b12 = []
while len(b5) > 0:
    b12.append(b5[0:2])
    b5 = b5[2:]
b12.sort()
b13 = []
b13.append(b12)
def fonk1(b12):
    a1 = 0
    b14 = []
    if len(b12) > 1:
        b12.sort(b11 = lambda x : int(x[0]))
        b12[a1].append('0')
        b12[a1 + 1].append('1')
        b15 = str(b12[a1][0]) + str(b12[a1 + 1][0])
        b16 = str(b12[a1][1]) + str(b12[a1 + 1][1])
        b14.append(b15)
        b14.append(b16)
        b17 = []
        b17.append(b14)
        b17 = b17 + b12[2:]
        b12 = b17
        b13.append(b12)
        fonk1(b12)
    return b13
b17 = fonk1(b12)
b13.sort(b11 = lambda x: str(x[0]), reverse=True)
b18 = []
for level in b13:
    for node in level:
        if node not in b18:
            b18.append(node)
        else:
            level.remove(node)
b19 = []
if len(b6) == 1:
    b20 = [b6[0], '0']
    b19.append(b20 * len(b4))
else:
    for letter in b6:
        b21 = ''
        for node in b18:
            if len(node) > 2 and letter in node[1]:
                b21 = b21 + node[2]
        b20 = [letter, b21]
        b19.append(b20)
b22 = {y : x for x, y in b9}
b23 = sorted(b19, b11=lambda x: b22[x[0]], reverse=True)
print('Binary codes are: ')
print('Character\tBinary Huffman\tBinary ASCII')
for i in range(len(b23)):
    print('\'%s\'\t\t%s\t\t%s' % (b23[i][0], b23[i][1], bin(ord(b23[i][0][0]))[2:]))
b24 = ''
for character in b4:
    for item in b19:
        if character in item:
            b24 = b24 + item[1]
print("The b4 of the b2 are: \'%s\'" % b4)
print('The huffman encoded b4 are: \'%s\'' % b24)