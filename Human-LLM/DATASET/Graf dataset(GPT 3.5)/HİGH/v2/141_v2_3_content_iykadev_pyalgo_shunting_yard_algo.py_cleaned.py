from collections import namedtuple
b1 = namedtuple('b1', 'b4 associativity')
LEFT, b2 = 'Left Right'.split()
b3 = {
    '^': b1(b4 = 4, associativity=b2),
    '*': b1(b4 = 3, associativity=LEFT),
    '/': b1(b4 = 3, associativity=LEFT),
    '+': b1(b4 = 2, associativity=LEFT),
    '-': b1(b4 = 2, associativity=LEFT),
    '(': b1(b4 = 9, associativity=LEFT),
    ')': b1(b4 = 0, associativity=LEFT),
}
NUMBER, LPAREN, b5 = 'NUMBER ( )'.split()
def fonk1(b6 = None):
    if b6 is None:
        b6 = input('expression: ')
    b7 = b6.strip().split()
    b8 = []
    for token in b7:
        if token in b3:
            b8.append((token, b3[token]))
        else:
            b8.append((NUMBER, token))
    return b8
def fonk2(b8):
    output_queue, b9 = [], []
    b10 = [['TOKEN', 'ACTION', 'RPN OUTPUT', 'OP STACK', 'NOTES']]
    for token, val in b8:
        if token is NUMBER:
            output_queue.append(val)
            b10.append((val, 'Add number to output', ' '.join(output_queue), ' '.join(s[0] for s in b9), ''))
        elif token in b3:
            token_type, (prec, b12) = token, val
            b11 = token_type
            while b9:
                top_token, (top_prec, top_assoc) = b9[-1]
                if (b12 = = LEFT and prec <= top_prec) or (b12 == b2 and prec < top_prec):
                    if token_type != b5:
                        if top_token != LPAREN:
                            b9.pop()
                            output_queue.append(top_token)
                        else:
                            break
                    else:
                        if top_token != LPAREN:
                            b9.pop()
                            output_queue.append(top_token)
                        else:
                            b9.pop()
                            b10.append((b11, '(Pop & discard "(")', ' '.join(output_queue), ' '.join(s[0] for s in b9), ''))
                            break
                else:
                    break
            if token_type != b5:
                b9.append((token, val))
            else:
                pass
            b10.append((b11, 'Push op token to stack' if token_type != b5 else 'Discard ")"', ' '.join(output_queue), ' '.join(s[0] for s in b9), ''))
    while b9:
        top_token, (top_prec, top_assoc) = b9[-1]
        b9.pop()
        output_queue.append(top_token)
        b10.append(('', '(Pop op)', ' '.join(output_queue), ' '.join(s[0] for s in b9), 'Drain stack to output'))
    return b10
if b13 = = '__main__':
    b14 = '3 + 4 * 2 / (1 - 5) ^ 2 ^ 3'
    print('Infix expression: %r\n' % b14)
    b15 = fonk2(fonk1(b14))
    b16 = [len(max(x, key=len)) for x in zip(*b15)]
    b17 = b15[0]
    print(' '.join('{cell:^{b18}}'.format(b18 = b18, cell=cell) for (b18, cell) in zip(b16, b17)))
    for b17 in b15[1:]:
        print(' '.join('{cell:<{b18}}'.format(b18 = b18, cell=cell) for (b18, cell) in zip(b16, b17)))
    print('\n The final output RPN is: %r' % b15[-1][2])