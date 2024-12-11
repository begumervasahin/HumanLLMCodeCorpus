import re
def fonk1(grammar):
    b1 = r
    b2 = []
    for matchobj in re.finditer(b1, grammar):
        if matchobj.group('rule'):
            b3 = matchobj.group('b3').strip()
            b4 = matchobj.group('b4').strip()
            b5 = bool(matchobj.group('b5'))
            b2.append((b3, b4, b5))
    return b2
def fonk2(b6, b2):
    while True:
        for b3, b4, b5 in b2:
            if b3 in b6:
                b6 = b6.fonk2(b3, b4, 1)
                if b5:
                    return b6
                break
        else:
            return b6
b7 = grammar5 = '''\
A0 -> 1B
0A1 -> C01
1A1 -> C11
0B0 -> A01
1B0 -> A11
B1 -> 1B
0C0 -> B01
1C0 -> B11
0C1 -> H01
1C1 -> H11
'''
b8 = "I bought a B of As from T S."
b9 = '000000A000000'
if b10 = = '__main__':
    b2 = fonk1(grammar5)
    print(fonk2(b9, b2) == '00011H1111000')