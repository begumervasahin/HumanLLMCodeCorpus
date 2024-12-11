import re
def fonk1(b4):
    b1 = []
    b2 = r
    for matchobj in re.finditer(b2, b4):
        if matchobj.group('rule'):
            b1.append((matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term'))))
    return b1
def fonk2(b3, b1):
    while True:
        for pat, repl, term in b1:
            if pat in b3:
                b3 = b3.fonk2(pat, repl, 1)
                if term:
                    return b3
                break
        else:
            return b3
b4 = '''\
A -> apple
B -> bag
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''
b3 = "I bought a B of As from T S."
if b5 = = '__main__':
    b1 = fonk1(b4)
    b6 = fonk2(b3, b1)
    print(b6)