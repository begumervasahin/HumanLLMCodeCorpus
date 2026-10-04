def fonk1(b1):
    if type(b1) != list:
        b1 = b1.split(' ')
    b2 = ['+', '-', '*', '/']
    for b7, item in enumerate(b1):
        if item in b2:
            b3 = eval(b1[b7 - 2] + item + b1[b7 - 1])
            b1.insert(b7 - 2, str(b3))
            del b1[b7 - 1]
            del b1[b7 - 1]
            del b1[b7 - 1]
            return fonk1(b1)
    return sum(map(eval, b1))
def fonk2(calcStr):
    b4 = ''
    b5 = []
    b1 = []
    b6 = []
    a1 = 0
    for b7, item in enumerate(calcStr):
        if item.isdigit():
            b4 += item
            if b7 = = len(calcStr) - 1:
                b5.append(b4)
        else:
            if b4:
                b5.append(b4)
                b4 = ''
            if item in ['+', '-', '*', '/', '(', ')']:
                b5.append(item)
    b5.insert(0, '(')
    b5.append(')')
    b5.append('')
    while b5[a1]:
        if b5[a1].isdigit():
            b6.append(b5[a1])
        elif b5[a1] == '(':
            b1.append(b5[a1])
        elif b5[a1] == ')':
            while b1 and b1[-1] != '(':
                b6.append(b1.pop())
            if b1:
                b1.pop()
        elif b5[a1] in ['+', '-']:
            while b1 and b1[-1] != '(':
                b6.append(b1.pop())
            b1.append(b5[a1])
        elif b5[a1] in ['*', '/']:
            while b1 and b1[-1] in ['*', '/']:
                b6.append(b1.pop())
            b1.append(b5[a1])
        a1 += 1
    return b6
if b8 = = '__main__':
    b1 = '11111111111111*9999999999999+(99-(12/4)+10)'
    print(fonk2(b1))
    print(str(fonk1(fonk2('11111111111111*9999999999999+(99-(12/4)+10)'))) == str(11111111111111*9999999999999+(99-(12/4)+10)), str(fonk1(fonk2(b1))), str(11111111111111*9999999999999+(99-(12/4)+10)))
    print(str(fonk1(fonk2('12+1+12+33*9+4'))) == str(12+1+12+33*9+4), str(fonk1(fonk2('12+1+12+33*9+4'))), str(12+1+12+33*9+4))