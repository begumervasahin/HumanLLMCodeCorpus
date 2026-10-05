def fonk1(expression):
    b1 = set('+-*/%()=<>!?;,:')
    expression += ";"
    a1 = 0
    while expression[a1] != ";":
        if expression[a1].isspace():
            a1 += 1
        elif expression[a1].isalpha():
            b2 = a1
            while expression[a1] not in b1 and not expression[a1].isspace():
                a1 += 1
            yield expression[b2:a1]
        elif expression[a1].isdigit():
            b2 = a1
            while expression[a1].isdigit():
                a1 += 1
            yield expression[b2:a1]
        elif expression[a1] in '=!<' and expression[a1 + 1] == '=':
            yield expression[a1:a1 + 2]
            a1 += 2
        else:
            yield expression[a1]
            a1 += 1
    yield ";"
b3 = "if (a >= 12) { return a + 1; }"
for token in fonk1(b3):
    print(token)