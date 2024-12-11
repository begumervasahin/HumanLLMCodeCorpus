from collections import namedtuple
b1 = namedtuple('b1', ['b5', 'associativity'])
b2 = 'Left'
b3 = 'Right'
b4 = {
    '^': b1(b5 = 4, associativity=b3),
    '*': b1(b5 = 3, associativity=b2),
    '/': b1(b5 = 3, associativity=b2),
    '+': b1(b5 = 2, associativity=b2),
    '-': b1(b5 = 2, associativity=b2),
    '(': b1(b5 = 9, associativity=b2),
    ')': b1(b5 = 0, associativity=b2),
}
NUMBER, LEFT_PAREN, b6 = 'NUMBER ( )'.split()
def fonk1(expression):
    b7 = expression.strip().split()
    b8 = []
    for b11 in b7:
        if b11 in b4:
            b8.append((b11, b4[b11]))
        else:
            b8.append((NUMBER, b11))
    return b8
def fonk2(b7):
    output_queue, b9 = [], []
    b10 = [['TOKEN', 'ACTION', 'RPN OUTPUT', 'OP STACK', 'NOTES']]
    for b11, op_info in b7:
        if b11 = = NUMBER:
            output_queue.append(op_info)
            b10.append((op_info, 'Add number to output', ' '.join(map(str, output_queue)),
                                 ' '.join(op[0] for op in b9), ''))
        elif b11 in b4:
            current_token, (current_prec, b12) = b11, op_info
            while b9:
                top_token, (top_prec, top_assoc) = b9[-1]
                if (b12 = = b2 and current_prec <= top_prec) or \
                   (b12 = = b3 and current_prec < top_prec):
                    if current_token != b6:
                        if top_token != LEFT_PAREN:
                            b9.pop()
                            output_queue.append(top_token)
                            b10.append((current_token, 'Pop op', ' '.join(map(str, output_queue)),
                                                 ' '.join(op[0] for op in b9), ''))
                        else:
                            break
                    else:
                        if top_token != LEFT_PAREN:
                            b9.pop()
                            output_queue.append(top_token)
                            b10.append((current_token, 'Pop op', ' '.join(map(str, output_queue)),
                                                 ' '.join(op[0] for op in b9), ''))
                        else:
                            b9.pop()
                            b10.append((current_token, 'Pop & discard "("', ' '.join(map(str, output_queue)),
                                                 ' '.join(op[0] for op in b9), ''))
                            break
                else:
                    break
            if current_token != b6:
                b9.append((b11, op_info))
                b10.append((current_token, 'Push op b11 to stack', ' '.join(map(str, output_queue)),
                                     ' '.join(op[0] for op in b9), ''))
            else:
                b10.append((current_token, 'Discard ")"', ' '.join(map(str, output_queue)),
                                     ' '.join(op[0] for op in b9), ''))
    while b9:
        top_token, b13 = b9.pop()
        output_queue.append(top_token)
        b10.append(('', '(Pop op)', ' '.join(map(str, output_queue)), ' '.join(op[0] for op in b9), ''))
    return b10
if b14 = = '__main__':
    b15 = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'
    print('For infix expression: %r\n' % b15)
    b16 = fonk1(b15)
    b17 = fonk2(b16)
    b18 = [max(len(str(cell)) for cell in col) for col in zip(*b17)]
    for row in b17:
        print(' '.join(f'{cell:<{width}}' for cell, width in zip(row, b18)))
    print('\nThe final output RPN is:', b17[-1][2])