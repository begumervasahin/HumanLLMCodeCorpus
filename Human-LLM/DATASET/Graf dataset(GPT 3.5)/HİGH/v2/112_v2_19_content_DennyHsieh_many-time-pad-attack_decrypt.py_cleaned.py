def fonk1(hex_str):
    return ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))
def fonk2(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))
def fonk3(b4, b5):
    b1 = 'Hackers should be judged by their acting, not bogus criteria.'
    b2 = fonk2(b5, b1)
    for ciphertext in b4:
        print(fonk2(ciphertext, b2))
    print(b1)
if b3 = = '__main__':
    b4 = []
    with open('msg', 'r') as file:
        for line in file:
            b4.append(line.strip().replace(' ', ''))
    b5 = open('msg_challenge', 'r').read().replace(' ', '')
    b6 = [fonk1(ciphertext) for ciphertext in b4]
    b7 = fonk1(b5)
    b8 = []
    for i in range(len(b7)):
        b9 = set()
        for j in range(len(b6)):
            if i < len(b6[j]):
                b10 = chr(ord(b6[j][i]) ^ ord(b7[i]))
                if 'A' <= b10 <= 'z':
                    b11 = chr(ord(b10) ^ ord(' '))
                    b9.add(b11)
        b8.append(b9)
    for chg_char in b8:
        print(chg_char)
    fonk3(b6, b7)