def tokenize_expression(expression):
    operators = set('+-*/%()=<>!?;,:')
    expression += ";"
    position = 0
    while expression[position] != ";":
        if expression[position].isspace():
            position += 1
        elif expression[position].isalpha():
            start = position
            while expression[position] not in operators and not expression[position].isspace():
                position += 1
            yield expression[start:position]
        elif expression[position].isdigit():
            start = position
            while expression[position].isdigit():
                position += 1
            yield expression[start:position]
        elif expression[position] in '=!<' and expression[position + 1] == '=':
            yield expression[position:position + 2]
            position += 2
        else:
            yield expression[position]
            position += 1
    yield ";"
example_expression = "if (a >= 12) { return a + 1; }"
for token in tokenize_expression(example_expression):
    print(token)