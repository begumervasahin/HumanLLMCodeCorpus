def fonk1(b1):
    if not isinstance(b1, list):
        b1 = b1.split(' ')
    b2 = ['+', '-', '*', '/']
    for a1, item in enumerate(b1):
        if item in b2:
            b3 = eval(b1[a1 - 2] + item + b1[a1 - 1])
            b1.insert(a1 - 2, str(b3))
            del b1[a1 - 1]
            del b1[a1 - 1]
            del b1[a1 - 1]
            return fonk1(b1)
    return sum(map(eval, b1))
def fonk2(b1):
    b4 = ''
    b5 = []
    b6 = []
    b7 = []
    a1 = 0
    for char in b1:
        if char.isdigit():
            b4 += char
        else:
            if b4:
                b5.append(b4)
                b4 = ''
            if char in ['+', '-', '*', '/', '(', ')']:
                b5.append(char)
    if b4:
        b5.append(b4)
    b5.insert(0, '(')
    b5.append(')')
    b5.append('')
    while b5[a1]:
        if b5[a1].isdigit():
            b7.append(b5[a1])
        elif b5[a1] == '(':
            b6.append(b5[a1])
        elif b5[a1] == ')':
            while b6 and b6[-1] != '(':
                b7.append(b6.pop())
            if b6:
                b6.pop()
        elif b5[a1] in ['+', '-']:
            while b6 and b6[-1] != '(':
                b7.append(b6.pop())
            b6.append(b5[a1])
        elif b5[a1] in ['*', '/']:
            while b6 and b6[-1] in ['*', '/']:
                b7.append(b6.pop())
            b6.append(b5[a1])
        a1 += 1
    return b7
if b8 = = '__main__':
    b1 = '11111111111111*9999999999999+(99-(12/4)+10)'
    b9 = fonk2(b1)
    print(b9)
    b3 = fonk1(b9)
    b10 = 11111111111111 * 9999999999999 + (99 - (12 / 4) + 10)
    print(str(b3) == str(b10), b3, b10)
    b11 = '12+1+12+33*9+4'
    b12 = fonk2(b11)
    b13 = fonk1(b12)
    b14 = 12 + 1 + 12 + 33 * 9 + 4
    print(str(b13) == str(b14), b13, b14)