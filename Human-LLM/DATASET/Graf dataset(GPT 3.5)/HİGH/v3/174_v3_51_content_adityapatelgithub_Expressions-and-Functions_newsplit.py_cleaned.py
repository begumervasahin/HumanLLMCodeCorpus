def fonk1(expression):
    b1 = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    b2 = {"==", "!=", "<=", ">="}
    expression += ";"
    a1 = 0
    while expression[a1] != ";":
        b3 = expression[a1]
        if b3.isspace():
            a1 += 1
            continue
        if b3.isalpha():
            b4 = a1
            while a1 < len(expression) and (expression[a1].isalnum() or expression[a1] == '_'):
                a1 += 1
            yield expression[b4:a1]
            continue
        if b3.isdigit():
            b4 = a1
            while a1 < len(expression) and expression[a1].isdigit():
                a1 += 1
            yield expression[b4:a1]
            continue
        if b3 in b1:
            b5 = expression[a1 + 1] if a1 + 1 < len(expression) else ""
            b6 = b3 + b5
            if b6 in b2:
                yield b6
                a1 += 2
            else:
                yield b3
                a1 += 1
            continue
    yield ";"
b7 = "if (a >= 12) { return a + 1; }"
print(list(fonk1(b7)))