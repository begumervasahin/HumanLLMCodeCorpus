import re
def fonk1(grammar):
    return [ (matchobj.group('pat'), matchobj.group('repl'), bool(matchobj.group('term')))
                for matchobj in re.finditer(b2, grammar)
                if matchobj.group('rule')]
def fonk2(b1, replacements):
    while True:
        for pat, repl, term in replacements:
            if pat in b1:
                b1 = b1.fonk2(pat, repl, 1)
                if term:
                    return b1
                break
        else:
            return b1
b2 = r
b3 = grammar2 = '''\
A -> apple
B -> bag
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''
b4 = '''\
A -> apple
WWWW -> with
Bgage -> ->.*
B -> bag
->.* -> money
W -> WW
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''
b5 = '''\
_+1 -> _1+
1+1 -> 11+
1! -> !1
,! -> !+
_! -> _
1*1 -> x,@y
1x -> xX
X, -> 1,1
X1 -> 1X
_x -> _X
,x -> ,X
y1 -> 1y
y_ -> _
1@1 -> x,@y
1@_ -> @_
,@_ -> !_
++ -> +
_1 -> 1
1+_ -> 1
_+_ ->
'''
b6 = '''\
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
b7 = "I bought a B of As from T S."
b8 = "I bought a B of As W my Bgage from T S."
b9 = '_1111*11111_'
b10 = '000000A000000'
if b11 = = '__main__':
    print(fonk2(b10, fonk1(b6)) == '00011H1111000')
    print(fonk2(b7, fonk1(b3)) == 'I bought a bag of apples from my brother.')