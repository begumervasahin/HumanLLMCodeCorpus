def fonk1(b4):
    b1 = []
    for shift in range(1, 26):
        b2 = ""
        for char in b4:
            if 'A' <= char <= 'Z':
                b3 = chr(((ord(char) - shift - ord('A')) % 26) + ord('A'))
            else:
                b3 = char
            b2 += b3
        b1.append(b2)
    return b1
def fonk2():
    b4 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Ciphertext:', b4)
    b1 = fonk1(b4)
    for i, message in enumerate(b1, b5 = 1):
        print(f'Decryption {i}: {message}')
if b6 = = "__main__":
    fonk2()