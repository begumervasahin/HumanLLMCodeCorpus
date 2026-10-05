def fonk1(b5):
    b1 = []
    b2 = len(b5)
    for i in range(1, 26):
        b3 = ""
        for char in b5:
            if 'A' <= char <= 'Z':
                b4 = chr((ord(char) - i - 65) % 26 + 65)
            else:
                b4 = char
            b3 += b4
        b1.append(b3)
    return b1
def fonk2():
    b5 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Ciphertext:', b5)
    b1 = fonk1(b5)
    for i, message in enumerate(b1, b6 = 1):
        print(f'Decryption {i}: {message}')
if b7 = = "__main__":
    fonk2()