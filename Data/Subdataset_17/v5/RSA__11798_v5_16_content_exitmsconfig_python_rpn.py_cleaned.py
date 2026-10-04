def calc(expression):
    if not isinstance(expression, list):
        expression = expression.split(' ')
    operators = ['+', '-', '*', '/']
    for i, item in enumerate(expression):
        if item in operators:
            result = eval(expression[i - 2] + item + expression[i - 1])
            expression.insert(i - 2, str(result))
            del expression[i - 1]
            del expression[i - 1]
            del expression[i - 1]
            return calc(expression)
    return sum(map(eval, expression))
def translate(expression):
    element = ''
    calc_list = []
    operator_stack = []
    output_queue = []
    i = 0
    for char in expression:
        if char.isdigit():
            element += char
        else:
            if element:
                calc_list.append(element)
                element = ''
            if char in ['+', '-', '*', '/', '(', ')']:
                calc_list.append(char)
    if element:
        calc_list.append(element)
    calc_list.insert(0, '(')
    calc_list.append(')')
    calc_list.append('')
    while calc_list[i]:
        if calc_list[i].isdigit():
            output_queue.append(calc_list[i])
        elif calc_list[i] == '(':
            operator_stack.append(calc_list[i])
        elif calc_list[i] == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()
        elif calc_list[i] in ['+', '-']:
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.append(calc_list[i])
        elif calc_list[i] in ['*', '/']:
            while operator_stack and operator_stack[-1] in ['*', '/']:
                output_queue.append(operator_stack.pop())
            operator_stack.append(calc_list[i])
        i += 1
    return output_queue
if __name__ == '__main__':
    expression = '11111111111111*9999999999999+(99-(12/4)+10)'
    translated_expr = translate(expression)
    print(translated_expr)
    result = calc(translated_expr)
    expected_result = 11111111111111 * 9999999999999 + (99 - (12 / 4) + 10)
    print(str(result) == str(expected_result), result, expected_result)
    expression2 = '12+1+12+33*9+4'
    translated_expr2 = translate(expression2)
    result2 = calc(translated_expr2)
    expected_result2 = 12 + 1 + 12 + 33 * 9 + 4
    print(str(result2) == str(expected_result2), result2, expected_result2)