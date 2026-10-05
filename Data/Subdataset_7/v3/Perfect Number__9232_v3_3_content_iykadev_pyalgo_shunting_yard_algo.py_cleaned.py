from collections import namedtuple
b1 = namedtuple('b1', 'b4 b11')
LEFT, b2 = 'Left Right'.split()
b3 = {
    '^': b1(b4 = 4, b11=b2),
    '*': b1(b4 = 3, b11=LEFT),
    '/': b1(b4 = 3, b11=LEFT),
    '+': b1(b4 = 2, b11=LEFT),
    '-': b1(b4 = 2, b11=LEFT),
    '(': b1(b4 = 9, b11=LEFT),
    ')': b1(b4 = 0, b11=LEFT),
}
NUMBER, LPAREN, b5 = 'NUMBER ( )'.split()
def fonk1(expression):
    b6 = expression.strip().split()
    b7 = []
    for token in b6:
        if token in b3:
            b7.append((token, b3[token]))
        else:
            b7.append((NUMBER, token))
    return b7
def fonk2(b7):
    output_queue, b8 = [], []
    b9 = [['TOKEN', 'ACTION', 'RPN OUTPUT', 'OP STACK', 'NOTES']]
    for token, value in b7:
        if token is NUMBER:
            output_queue.append(value)
            b9.append((value, 'Add number to output', ' '.join(output_queue), ' '.join(s[0] for s in b8), ''))
        elif token in b3:
            token_type, (b4, b11) = token, value
            b10 = token_type
            while b8:
                top_token, (top_precedence, top_associativity) = b8[-1]
                if (b11 = = LEFT and b4 <= top_precedence) or \
                        (b11 = = b2 and b4 < top_precedence):
                    if token_type != b5:
                        if top_token != LPAREN:
                            b8.pop()
                            output_queue.append(top_token)
                        else:
                            break
                    else:
                        if top_token != LPAREN:
                            b8.pop()
                            output_queue.append(top_token)
                        else:
                            b8.pop()
                            b9.append((b10, '(Pop & discard "(")', ' '.join(output_queue), ' '.join(s[0] for s in b8), ''))
                            break
                else:
                    break
            if token_type != b5:
                b8.append((token, value))
            else:
                pass
            b9.append((b10, 'Push op token to stack' if token_type != b5 else 'Discard ")"', ' '.join(output_queue), ' '.join(s[0] for s in b8), ''))
    while b8:
        top_token, (top_precedence, top_associativity) = b8.pop()
        output_queue.append(top_token)
        b9.append(('', '(Pop op)', ' '.join(output_queue), ' '.join(s[0] for s in b8), 'Drain stack to output'))
    return b9
if b12 = = '__main__':
    b13 = '3 + 4 * 2 / (1 - 5) ^ 2 ^ 3'
    print('Infix expression: %r\n' % b13)
    b14 = fonk2(fonk1(b13))
    b15 = [len(max(x, key=len)) for x in zip(*b14)]
    b16 = b14[0]
    print(' '.join('{cell:^{b17}}'.format(b17 = b17, cell=cell) for (b17, cell) in zip(b15, b16)))
    for row in b14[1:]:
        print(' '.join('{cell:<{b17}}'.format(b17 = b17, cell=cell) for (b17, cell) in zip(b15, row)))
    print('\n The final output RPN is: %r' % b14[-1][2])