def fonk1(b1):
    if type(b1) != list:
        b1 = b1.split(' ')
    b2 = ['+', '-', '*', '/']
    for b6, b5 in enumerate(b1):
        if b5 in b2:
            b3 = eval(b1[b6 - 2] + b5 + b1[b6 - 1])
            b1.insert(b6 - 2, str(b3))
            for _ in range(3):
                del b1[b6 - 1]
            return fonk1(b1)
    return sum(map(eval, b1))
def fonk2(calcStr):
    b7, calcList, b1, stackStr, b4 = '', [], [], [], 0
    for b6, b5 in enumerate(calcStr):
        if b5.isdigit() or b5 = = '.':
            b7 += b5
            if b6 = = len(calcStr) - 1:
                calcList.append(b7)
        else:
            if b7:
                calcList.append(b7)
                b7 = ''
            if b5 in ['+', '-', '*', '/', '(', ')']:
                calcList.append(b5)
    calcList.insert(0, '(')
    calcList.append(')')
    while b4 < len(calcList):
        if calcList[b4].isdigit() or '.' in calcList[b4]:
            stackStr.append(calcList[b4])
        elif calcList[b4] == '(':
            b1.append(calcList[b4])
        elif calcList[b4] == ')':
            while b1 and b1[-1] != '(':
                stackStr.append(b1.pop())
            b1.pop()
        elif calcList[b4] in ['+', '-']:
            while b1 and b1[-1] != '(':
                stackStr.append(b1.pop())
            b1.append(calcList[b4])
        elif calcList[b4] in ['*', '/']:
            while b1 and b1[-1] in ['*', '/']:
                stackStr.append(b1.pop())
            b1.append(calcList[b4])
        b4 += 1
    return stackStr
if b8 = = '__main__':
    b1 = '11111111111111*9999999999999+(99-(12/4)+10)'
    print(fonk2(b1))
    b9 = fonk2(b1)
    b10 = fonk1(b9)
    b11 = 11111111111111*9999999999999+(99-(12/4)+10)
    print(str(b10) == str(b11), str(b10), str(b11))
    b12 = '12+1+12+33*9+4'
    b13 = fonk2(b12)
    b14 = fonk1(b13)
    b15 = 12+1+12+33*9+4
    print(str(b14) == str(b15), str(b14), str(b15))