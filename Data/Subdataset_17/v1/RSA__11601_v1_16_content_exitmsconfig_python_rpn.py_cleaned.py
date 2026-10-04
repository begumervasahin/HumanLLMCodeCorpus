def calc(s):
    if type(s) != list:
        s = s.split(' ')
    operaList = ['+', '-', '*', '/']
    for key, item in enumerate(s):
        if item in operaList:
            val = eval(s[key - 2] + item + s[key - 1])
            s.insert(key - 2, str(val))
            for _ in range(3):
                del s[key - 1]
            return calc(s)
    return sum(map(eval, s))
def translate(calcStr):
    element, calcList, s, stackStr, i = '', [], [], [], 0
    for key, item in enumerate(calcStr):
        if item.isdigit() or item == '.':
            element += item
            if key == len(calcStr) - 1:
                calcList.append(element)
        else:
            if element:
                calcList.append(element)
                element = ''
            if item in ['+', '-', '*', '/', '(', ')']:
                calcList.append(item)
    calcList.insert(0, '(')
    calcList.append(')')
    while i < len(calcList):
        if calcList[i].isdigit() or '.' in calcList[i]:
            stackStr.append(calcList[i])
        elif calcList[i] == '(':
            s.append(calcList[i])
        elif calcList[i] == ')':
            while s and s[-1] != '(':
                stackStr.append(s.pop())
            s.pop()
        elif calcList[i] in ['+', '-']:
            while s and s[-1] != '(':
                stackStr.append(s.pop())
            s.append(calcList[i])
        elif calcList[i] in ['*', '/']:
            while s and s[-1] in ['*', '/']:
                stackStr.append(s.pop())
            s.append(calcList[i])
        i += 1
    return stackStr
if __name__ == '__main__':
    s = '11111111111111*9999999999999+(99-(12/4)+10)'
    print(translate(s))
    translated_expr = translate(s)
    result = calc(translated_expr)
    expected_result = 11111111111111*9999999999999+(99-(12/4)+10)
    print(str(result) == str(expected_result), str(result), str(expected_result))
    s2 = '12+1+12+33*9+4'
    translated_expr2 = translate(s2)
    result2 = calc(translated_expr2)
    expected_result2 = 12+1+12+33*9+4
    print(str(result2) == str(expected_result2), str(result2), str(expected_result2))