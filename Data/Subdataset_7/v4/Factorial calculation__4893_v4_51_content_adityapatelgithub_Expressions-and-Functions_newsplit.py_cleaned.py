def fonk1(expression):
    b1 = set('+-*/%()=<>!?;,:')
    expression += ";"
    a1 = 0
    while expression[a1] != ";":
        if expression[a1].isspace():
            a1 += 1
            continue
        if expression[a1].isalpha():
            b2 = a1
            while a1 < len(expression) and expression[a1] not in b1 and not expression[a1].isspace():
                a1 += 1
            yield expression[b2:a1]
            continue
        if expression[a1].isdigit():
            b2 = a1
            while a1 < len(expression) and expression[a1].isdigit():
                a1 += 1
            yield expression[b2:a1]
            continue
        if expression[a1] in '=!<' and expression[a1 + 1] == '=':
            yield expression[a1:a1 + 2]
            a1 += 2
            continue
        yield expression[a1]
        a1 += 1
    yield ";"
for token in fonk1("b3 = 10; if (b3 > 5) { b3 += 2; }"):
    print(token)