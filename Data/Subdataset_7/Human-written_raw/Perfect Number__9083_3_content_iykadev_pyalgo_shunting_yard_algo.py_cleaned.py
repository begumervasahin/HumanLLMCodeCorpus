from collections import namedtuple
from pprint import pprint as pp
b1 = namedtuple('b1', 'b4 assoc')
L, b2 = 'Left Right'.split()
b3 = {
 '^': b1(b4 = 4, assoc=b2),
 '*': b1(b4 = 3, assoc=L),
 '/': b1(b4 = 3, assoc=L),
 '+': b1(b4 = 2, assoc=L),
 '-': b1(b4 = 2, assoc=L),
 '(': b1(b4 = 9, assoc=L),
 ')': b1(b4 = 0, assoc=L),
 }
NUM, LPAREN, b5 = 'NUMBER ( )'.split()
def fonk1(b6 = None):
    'Inputs an expression and returns list of (TOKENTYPE, tokenvalue)'
    if b6 is None:
        b6 = input('expression: ')
    b7 = b6.strip().split()
    b8 = []
    for token in b7:
        if token in b3:
            b8.append((token, b3[token]))
        else:
            b8.append((NUM, token))
    return b8
def fonk2(b8):
    outq, b9 = [], []
    b10 = ['TOKEN,ACTION,RPN OUTPUT,OP STACK,NOTES'.split(',')]
    for token, val in b8:
        b11 = b12 = ''
        if token is NUM:
            b12 = 'Add number to output'
            outq.append(val)
            b10.append( (val, b12, ' '.join(outq), ' '.join(s[0] for s in b9), b11) )
        elif token in b3:
            t1, (p1, b14) = token, val
            b13 = t1
            b11 = 'Pop b3 from b9 to output'
            while b9:
                t2, (p2, a2) = b9[-1]
                if (b14 = = L and p1 <= p2) or (b14 == b2 and p1 < p2):
                    if t1 != b5:
                        if t2 != LPAREN:
                            b9.pop()
                            b12 = '(Pop op)'
                            outq.append(t2)
                        else:
                            break
                    else:
                        if t2 != LPAREN:
                            b9.pop()
                            b12 = '(Pop op)'
                            outq.append(t2)
                        else:
                            b9.pop()
                            b12 = '(Pop & discard "(")'
                            b10.append( (b13, b12, ' '.join(outq), ' '.join(s[0] for s in b9), b11) )
                            break
                    b10.append( (b13, b12, ' '.join(outq), ' '.join(s[0] for s in b9), b11) )
                    b13 = b11 = ''
                else:
                    b11 = ''
                    break
                b11 = ''
            b11 = ''
            if t1 != b5:
                b9.append((token, val))
                b12 = 'Push op token to b9'
            else:
                b12 = 'Discard ")"'
            b10.append( (b13, b12, ' '.join(outq), ' '.join(s[0] for s in b9), b11) )
    b11 = 'Drain b9 to output'
    while b9:
        b13 = ''
        t2, (p2, a2) = b9[-1]
        b12 = '(Pop op)'
        b9.pop()
        outq.append(t2)
        b10.append( (b13, b12, ' '.join(outq), ' '.join(s[0] for s in b9), b11) )
        b13 = b11 = ''
    return b10
if b15 = = '__main__':
    b16 = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
    print( 'For b16 expression: %r\n' % b16 )
    b17 = fonk2(fonk1(b16))
    b18 = [len(max(x, key=len)) for x in zip(*b17)]
    b19 = b17[0]
    print( ' '.join('{cell:^{b20}}'.format(b20 = b20, cell=cell) for (b20, cell) in zip(b18, b19)))
    for b19 in b17[1:]:
        print( ' '.join('{cell:<{b20}}'.format(b20 = b20, cell=cell) for (b20, cell) in zip(b18, b19)))
    print('\n The final output RPN is: %r' % b17[-1][2])