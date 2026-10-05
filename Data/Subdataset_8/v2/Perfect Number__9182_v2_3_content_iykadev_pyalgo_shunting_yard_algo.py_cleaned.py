from collections import namedtuple
OperatorInfo = namedtuple('OperatorInfo', 'precedence associativity')
LEFT, RIGHT = 'Left Right'.split()
operators = {
    '^': OperatorInfo(precedence=4, associativity=RIGHT),
    '*': OperatorInfo(precedence=3, associativity=LEFT),
    '/': OperatorInfo(precedence=3, associativity=LEFT),
    '+': OperatorInfo(precedence=2, associativity=LEFT),
    '-': OperatorInfo(precedence=2, associativity=LEFT),
    '(': OperatorInfo(precedence=9, associativity=LEFT),
    ')': OperatorInfo(precedence=0, associativity=LEFT),
}
NUMBER, LPAREN, RPAREN = 'NUMBER ( )'.split()
def get_input(inp=None):
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    token_vals = []
    for token in tokens:
        if token in operators:
            token_vals.append((token, operators[token]))
        else:
            token_vals.append((NUMBER, token))
    return token_vals
def shunting(token_vals):
    output_queue, operator_stack = [], []
    table = [['TOKEN', 'ACTION', 'RPN OUTPUT', 'OP STACK', 'NOTES']]
    for token, val in token_vals:
        if token is NUMBER:
            output_queue.append(val)
            table.append((val, 'Add number to output', ' '.join(output_queue), ' '.join(s[0] for s in operator_stack), ''))
        elif token in operators:
            token_type, (prec, assoc) = token, val
            v = token_type
            while operator_stack:
                top_token, (top_prec, top_assoc) = operator_stack[-1]
                if (assoc == LEFT and prec <= top_prec) or (assoc == RIGHT and prec < top_prec):
                    if token_type != RPAREN:
                        if top_token != LPAREN:
                            operator_stack.pop()
                            output_queue.append(top_token)
                        else:
                            break
                    else:
                        if top_token != LPAREN:
                            operator_stack.pop()
                            output_queue.append(top_token)
                        else:
                            operator_stack.pop()
                            table.append((v, '(Pop & discard "(")', ' '.join(output_queue), ' '.join(s[0] for s in operator_stack), ''))
                            break
                else:
                    break
            if token_type != RPAREN:
                operator_stack.append((token, val))
            else:
                pass
            table.append((v, 'Push op token to stack' if token_type != RPAREN else 'Discard ")"', ' '.join(output_queue), ' '.join(s[0] for s in operator_stack), ''))
    while operator_stack:
        top_token, (top_prec, top_assoc) = operator_stack[-1]
        operator_stack.pop()
        output_queue.append(top_token)
        table.append(('', '(Pop op)', ' '.join(output_queue), ' '.join(s[0] for s in operator_stack), 'Drain stack to output'))
    return table
if __name__ == '__main__':
    infix_expr = '3 + 4 * 2 / (1 - 5) ^ 2 ^ 3'
    print('Infix expression: %r\n' % infix_expr)
    rpn_output = shunting(get_input(infix_expr))
    max_column_widths = [len(max(x, key=len)) for x in zip(*rpn_output)]
    row = rpn_output[0]
    print(' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(max_column_widths, row)))
    for row in rpn_output[1:]:
        print(' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(max_column_widths, row)))
    print('\n The final output RPN is: %r' % rpn_output[-1][2])