def fonk1(b1):
    if not isinstance(b1, list):
        b1 = b1.split(' ')
    b2 = ['+', '-', '*', '/']
    for i, item in enumerate(b1):
        if item in b2:
            b3 = eval(f"{b1[i-2]} {item} {b1[i-1]}")
            b1.insert(i-2, str(b3))
            for _ in range(3):
                del b1[i-1]
            return fonk1(b1)
    return sum(map(eval, b1))
def fonk2(b1):
    elements, stack, b4 = [], [], []
    b5 = ''
    for b6 in b1:
        if b6.isdigit() or b6 = = '.':
            b5 += b6
        else:
            if b5:
                elements.append(b5)
                b5 = ''
            if b6 in ['+', '-', '*', '/', '(', ')']:
                elements.append(b6)
    if b5:
        elements.append(b5)
    elements.insert(0, '(')
    elements.append(')')
    for b7 in elements:
        if b7.isdigit() or '.' in b7:
            b4.append(b7)
        elif b7 = = '(':
            stack.append(b7)
        elif b7 = = ')':
            while stack and stack[-1] != '(':
                b4.append(stack.pop())
            stack.pop()
        elif b7 in ['+', '-']:
            while stack and stack[-1] != '(':
                b4.append(stack.pop())
            stack.append(b7)
        elif b7 in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                b4.append(stack.pop())
            stack.append(b7)
    return b4
if b8 = = '__main__':
    b9 = '11111111111111*9999999999999+(99-(12/4)+10)'
    b10 = fonk2(b9)
    b11 = fonk1(b10)
    b12 = 11111111111111 * 9999999999999 + (99 - (12 / 4) + 10)
    print(b10)
    print(f"Correct: {b11 = = b12}, Result: {b11}, Expected: {b12}")
    b13 = '12+1+12+33*9+4'
    b14 = fonk2(b13)
    b15 = fonk1(b14)
    b16 = 12 + 1 + 12 + 33 * 9 + 4
    print(b14)
    print(f"Correct: {b15 = = b16}, Result: {b15}, Expected: {b16}")