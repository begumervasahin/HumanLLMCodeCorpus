def fonk1(s):
    return s and chr(int(s[:2], b1 = 16)) + fonk1(s[2:]) or ''
def fonk2(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
def fonk3(str_ciphers, str_chg_cipher):
    b2 = 'Hackers should be judged by their acting, not bogus criteria.'
    b3 = fonk2(str_chg_cipher, b2)
    for str_cipher in str_ciphers:
        print(fonk2(str_cipher, b3))
    print(b2)
if b4 = = '__main__':
    b5 = []
    with open('msg', 'r') as f:
        for line in f:
            b6 = ''.join(line.split())
            b5.append(b6)
    b7 = open('msg_challenge', 'r').read()
    b7 = ''.join(b7.split())
    b8 = []
    for text in b5:
        b8.append(fonk1(text))
    b9 = fonk1(b7)
    b10 = []
    for i in range(len(b9)):
        b11 = []
        for j in range(len(b8)):
            b12 = len(b8[j])
            if i >= b12:
                continue
            '''
            XOR challenge cipher text with other cipher text. If lower alphabetic from challenge cipher text meets space
            from other cipher text, it will be showed in same upper alphabetic. Also, The upper alphabetic will be
            showed in same lower alphabetic.
            '''
            b13 = (chr(ord(b8[j][i:i + 1]) ^ ord(b9[i:i + 1])))
            if 'A' <= b13 <= 'z':
                b14 = chr(ord(b13) ^ ord(' '))
                if b14 not in b11:
                    b11.append(b14)
        b10.append(b11)
    '''
    If the array is empty [], that is, neither msg_1 nor msg_2 has space, any alphabetic is possible.
    If the array appears above 5 alphabetic, the challenge cipher text is space or other symbols in this part.
    '''
    for chg_char in b10:
        print(chg_char)
    fonk3(b8, b9)