def fonk1():
    print("Huffman Encoding Program")
    b1 = input("Enter the name of a text file to open: ") + ".txt"
    b2 = fonk2(b1)
    b3 = fonk3(b2)
    b4 = fonk4(b3)
    b5 = fonk5(b4)
    fonk6(b5, b3)
    b6 = fonk7(b2, b5)
    print(f"The b2 of the file are: '{b2}'")
    print(f"The Huffman encoded b2 are: '{b6}'")
def fonk2(b1):
    with open(b1, 'r') as file:
        return file.read()
def fonk3(b2):
    b3 = {}
    for char in b2:
        b3[char] = b3.get(char, 0) + 1
    return b3
def fonk4(b3):
    b7 = [[freq, char] for char, freq in b3.items()]
    b7.sort(b8 = lambda x: x[0])
    while len(b7) > 1:
        b9 = b7.pop(0)
        b10 = b7.pop(0)
        b11 = [b9[0] + b10[0], b9, b10]
        b7.append(b11)
        b7.sort(b8 = lambda x: x[0])
    return b7[0]
def fonk5(tree, b12 = ''):
    if len(tree) == 2:
        return {tree[1]: b12}
    b13 = {}
    b13.update(fonk5(tree[1], b12 + '0'))
    b13.update(fonk5(tree[2], b12 + '1'))
    return b13
def fonk6(b5, b3):
    print('Binary b13 are:')
    print('Character\tBinary Huffman\tBinary ASCII')
    for char, code in sorted(b5.items(), b8 = lambda item: b3[item[0]], reverse=True):
        print(f"'{char}'\t\t{code}\t\t{bin(ord(char))[2:]}")
def fonk7(b2, b5):
    return ''.join(b5[char] for char in b2)
if b14 = = "__main__":
    fonk1()