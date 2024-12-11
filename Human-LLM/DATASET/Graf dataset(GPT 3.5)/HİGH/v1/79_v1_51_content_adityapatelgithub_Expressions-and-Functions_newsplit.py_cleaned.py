def fonk1(expr):
    b1 = ['+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ',']
    expr += ";"
    a1 = 0
    while expr[a1] != ";":
        if expr[a1] == ' ':
            a1 += 1
        elif expr[a1].isalpha():
            b2 = a1
            while expr[a1] not in b1 and expr[a1] != ' ':
                a1 += 1
            yield expr[b2:a1]
        elif expr[a1].isdigit():
            b2 = a1
            while expr[a1].isdigit():
                a1 += 1
            yield expr[b2:a1]
        elif expr[a1] in ['=', '!', '<', '>'] and expr[a1 + 1] == '=':
            yield expr[a1:a1 + 2]
            a1 += 2
        else:
            yield expr[a1]
            a1 += 1
    yield ";"
b3 = "a = 5;"
for token in fonk1(b3):
    print(token)