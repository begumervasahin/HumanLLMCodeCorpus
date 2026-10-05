def new_split_iter(expr):
    operators = ['+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ',']
    expr += ";"
    pos = 0
    while expr[pos] != ";":
        if expr[pos] == ' ':
            pos += 1
        elif expr[pos].isalpha():
            start = pos
            while expr[pos] not in operators and expr[pos] != ' ':
                pos += 1
            yield expr[start:pos]
        elif expr[pos].isdigit():
            start = pos
            while expr[pos].isdigit():
                pos += 1
            yield expr[start:pos]
        elif expr[pos] in ['=', '!', '<', '>'] and expr[pos + 1] == '=':
            yield expr[pos:pos + 2]
            pos += 2
        else:
            yield expr[pos]
            pos += 1
    yield ";"
expression = "a = 5;"
for token in new_split_iter(expression):
    print(token)