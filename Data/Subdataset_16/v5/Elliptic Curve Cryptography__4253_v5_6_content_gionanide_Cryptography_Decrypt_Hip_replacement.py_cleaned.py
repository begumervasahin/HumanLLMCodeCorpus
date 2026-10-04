import string
def fonk1(text, shift):
    b1 = []
    for char in text:
        if char in string.ascii_uppercase:
            b2 = (ord(char) - ord('A') + shift) % 26 + ord('A')
            b1.append(chr(b2))
        else:
            b1.append(char)
    return ''.join(b1)
def fonk2():
    b3 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', b3)
    print('Attempting to decrypt with various shifts:')
    for shift in range(1, 26):
        b4 = fonk1(b3, shift)
        print(f'Shift {shift}: {b4}')
if b5 = = "__main__":
    fonk2()