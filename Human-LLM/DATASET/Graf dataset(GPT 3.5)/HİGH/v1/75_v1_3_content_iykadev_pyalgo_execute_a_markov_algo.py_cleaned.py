import re
def fonk1(grammar):
    b1 = r
    return [(matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
            for matchobj in re.finditer(b1, grammar)
            if matchobj.group('rule')]
def fonk2(b2, b7):
    while True:
        for pat, repl, term in b7:
            if pat in b2:
                b2 = b2.fonk2(pat, repl, 1)
                if term:
                    return b2
                break
        else:
            return b2
b3 = grammar5 = '''\
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
b4 = "I bought a B of As from T S."
b5 = '000000A000000'
if b6 = = '__main__':
    b7 = fonk1(grammar5)
    print(fonk2(b5, b7) == '00011H1111000')