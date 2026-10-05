def split_expression_into_tokens(expression):
    operators = set('+-*/%()=<>!?;,:')
    expression += ";"
    index = 0
    while expression[index] != ";":
        if expression[index].isspace():
            index += 1
            continue
        if expression[index].isalpha():
            start = index
            while index < len(expression) and expression[index] not in operators and not expression[index].isspace():
                index += 1
            yield expression[start:index]
            continue
        if expression[index].isdigit():
            start = index
            while index < len(expression) and expression[index].isdigit():
                index += 1
            yield expression[start:index]
            continue
        if expression[index] in '=!<' and expression[index + 1] == '=':
            yield expression[index:index + 2]
            index += 2
            continue
        yield expression[index]
        index += 1
    yield ";"
for token in split_expression_into_tokens("x = 10; if (x > 5) { x += 2; }"):
    print(token)