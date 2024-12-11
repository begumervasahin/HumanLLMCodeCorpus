import re
def fonk1(b7):
    b1 = []
    b2 = r
    for matchobj in re.finditer(b2, b7):
        if matchobj.group('rule'):
            b3 = matchobj.group('pat')
            b4 = matchobj.group('repl')
            b5 = bool(matchobj.group('term'))
            b1.append((b3, b4, b5))
    return b1
def fonk2(b6, b1):
    while True:
        for b3, b4, b5 in b1:
            if b3 in b6:
                b6 = b6.fonk2(b3, b4, 1)
                if b5:
                    return b6
                break
        else:
            return b6
b7 = '''\
A -> apple
B -> bag
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''
b6 = "I bought a B of As from T S."
if b8 = = '__main__':
    b1 = fonk1(b7)
    b9 = fonk2(b6, b1)
    print(b9)