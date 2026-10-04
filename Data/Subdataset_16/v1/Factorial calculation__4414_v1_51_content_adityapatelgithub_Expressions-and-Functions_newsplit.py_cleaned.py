def fonk1(b2):
    b1 = ['+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ',']
    b2 = b2 + ";"
    a1 = 0
    while b2[a1] != ";":
        if b2[a1] == ' ':
            a1 += 1
        elif b2[a1].isalpha():
            b3 = a1
            while a1 < len(b2) and b2[a1] not in b1 and b2[a1] != ' ':
                a1 += 1
            yield b2[b3:a1]
        elif b2[a1].isdigit():
            b3 = a1
            while a1 < len(b2) and b2[a1].isdigit():
                a1 += 1
            yield b2[b3:a1]
        elif b2[a1] in ['=', '!', '<', '>'] and a1 + 1 < len(b2) and b2[a1 + 1] == '=':
            yield b2[a1] + b2[a1 + 1]
            a1 += 2
        else:
            yield b2[a1]
            a1 += 1
    yield ";"
if b4 = = "__main__":
    b2 = "a = 10 + b * (c - d) >= 5;"
    b5 = list(fonk1(b2))
    print("Tokens:", b5)
