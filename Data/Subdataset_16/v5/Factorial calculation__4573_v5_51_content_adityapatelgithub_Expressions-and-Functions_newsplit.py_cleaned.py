def fonk1(b5):
    b1 = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    b5 += ";"
    a1 = 0
    while a1 < len(b5):
        b2 = b5[a1]
        if b2.isspace():
            a1 += 1
        elif b2.isalpha() or b2 = = '_':
            b3 = a1
            while a1 < len(b5) and (b5[a1].isalnum() or b5[a1] == '_'):
                a1 += 1
            yield b5[b3:a1]
        elif b2.isdigit():
            b3 = a1
            while a1 < len(b5) and b5[a1].isdigit():
                a1 += 1
            yield b5[b3:a1]
        elif b2 in {'=', '!', '<', '>'} and a1 + 1 < len(b5) and b5[a1 + 1] == '=':
            yield b5[a1] + b5[a1 + 1]
            a1 += 2
        elif b2 in b1:
            yield b2
            a1 += 1
        elif b2 = = ";":
            yield b2
            a1 += 1
        else:
            raise ValueError(f"Unexpected character '{b2}' in expression")
if b4 = = "__main__":
    b5 = "a = 10 + b * (c - d) >= 5;"
    b6 = list(fonk1(b5))
    print("Tokens:", b6)
