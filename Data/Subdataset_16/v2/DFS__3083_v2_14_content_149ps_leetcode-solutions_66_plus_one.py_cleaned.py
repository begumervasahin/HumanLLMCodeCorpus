def fonk1(b5):
    b1 = ''.join(str(digit) for digit in b5)
    b2 = int(b1)
    b3 = b2 + 1
    b4 = [int(digit) for digit in str(b3)]
    return b4
b5 = [1, 2, 4, 5, 3, 2, 2, 9]
print(fonk1(b5))
b5 = [9, 9, 9]
print(fonk1(b5))
b5 = [0]
print(fonk1(b5))
b5 = [1, 0, 0, 0]
print(fonk1(b5))
