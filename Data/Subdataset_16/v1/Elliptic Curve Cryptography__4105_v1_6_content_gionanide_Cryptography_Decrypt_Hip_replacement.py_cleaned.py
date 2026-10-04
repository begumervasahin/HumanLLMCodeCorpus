import string
def fonk1(text, shift):
    b1 = []
    for char in text:
        if char in string.ascii_uppercase:
            b2 = chr((ord(char) - shift - 65) % 26 + 65)
            b1.append(b2)
        else:
            b1.append(char)
    return ''.join(b1)
def fonk2():
    b3 = 'YMJJDJXHFSRNXQJFIYMJXRNQJHFSQNJGZYYMJXMTJXYJQQYMJYWZYM'
    print('Encrypted message:', b3)
    for shift in range(1, 26):
        b4 = fonk1(b3, shift)
        print(f'Shift {shift}: {b4}')
if b5 = = "__main__":
    fonk2()