def fonk1(expression):
    b1 = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    expression += ';'
    a1 = 0
    b2 = len(expression)
    while a1 < b2:
        b3 = expression[a1]
        if b3.isspace():
            a1 += 1
            continue
        if b3.isalpha():
            b4 = a1
            while a1 < b2 and expression[a1] not in b1 and not expression[a1].isspace():
                a1 += 1
            yield expression[b4:a1]
            continue
        if b3.isdigit():
            b4 = a1
            while a1 < b2 and expression[a1].isdigit():
                a1 += 1
            yield expression[b4:a1]
            continue
        if b3 in ('=', '!', '<', '>') and a1 + 1 < b2 and expression[a1 + 1] == '=':
            yield expression[a1:a1 + 2]
            a1 += 2
            continue
        yield b3
        a1 += 1
b5 = "x = 10; if (x > 5) { x += 2; }"
for token in fonk1(b5):
    print(token)