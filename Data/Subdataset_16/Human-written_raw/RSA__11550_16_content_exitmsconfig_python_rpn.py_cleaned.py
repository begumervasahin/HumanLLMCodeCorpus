def fonk1(b1):
    if type(b1) != list:b1 = b1.split(' ')
    b2 = ['+', '-', '*', '/'];
    for b6, item in enumerate(b1):
        if item in b2:
            b3 = eval(b1[b6 - 2] + item + b1[b6 - 1])
            b1.insert(b6 - 2, str(b3))
            for x in ['1','2','3']:del b1[b6 - 1]
            fonk1(b1)
    return sum(map(eval, b1))
def fonk2(calcStr):
    b5, calcList,b1,stackStr,b4 = '', [],[],[],0
    for b6,item in enumerate(calcStr):
        if item.isdigit():
            b5 = b5 + item
            if b6 = = len(calcStr)-1:calcList.append(b5)
        else:
            if b5 != '':
                calcList.append(b5)
                b5 = ''
            if item in ['+', '-', '*', '/', '(', ')']:
                calcList.append(item)
    calcList.insert(0,'(')
    calcList.append(')')
    calcList.append('
    while calcList[b4] != "
        if (calcList[b4].isdigit()):
            stackStr.append(calcList[b4])
        elif calcList[b4] == '(':
            b1.append(calcList[b4])
        elif calcList[b4] == ')':
            while b1[-1] != '(':
                stackStr.append(b1.pop())
            b1.pop()
        elif calcList[b4] in ['+', '-']:
            while b1[-1] != '(':
                stackStr.append(b1.pop())
            b1.append(calcList[b4])
        elif calcList[b4] in ['*', '/']:
            while b1[-1] in ['*', '/']:
                stackStr.append(b1.pop())
            b1.append(calcList[b4])
        b4 = b4 + 1
    return stackStr
if b7 = = '__main__':
    b1 = '11111111111111*9999999999999+(99-(12/4)+10)'
    print fonk2(b1)
    print str(fonk1(fonk2('11111111111111*9999999999999+(99-(12/4)+10)'))) == str(11111111111111*9999999999999+(99-(12/4)+10)),str(fonk1(fonk2(b1))) , str(11111111111111*9999999999999+(99-(12/4)+10))
    print str(fonk1(fonk2('12+1+12+33*9+4'))) == str(12+1+12+33*9+4),str(fonk1(fonk2('12+1+12+33*9+4'))) , str(12+1+12+33*9+4)