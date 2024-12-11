def fonk1(b3):
    for shift in range(1, 26):
        b1 = ""
        for char in b3:
            if 'A' <= char <= 'Z':
                b2 = chr(((ord(char) - shift - ord('A')) % 26) + ord('A'))
            else:
                b2 = char
            b1 += b2
        print(f"Decryption {shift}: {b1}")
def fonk2():
    b3 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Ciphertext:', b3)
    fonk1(b3)
if b4 = = "__main__":
    fonk2()