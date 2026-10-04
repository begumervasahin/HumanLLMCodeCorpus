def fonk1(b2):
    b1 = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    b2 = b2 + ";"
    a1 = 0
    def fonk2(b3):
        return b3 in b1
    def fonk3(start_pos):
        return (b2[start_pos] in {'=', '!', '<', '>'} and
                start_pos + 1 < len(b2) and
                b2[start_pos + 1] == '=')
    while a1 < len(b2):
        b3 = b2[a1]
        if b3.isspace():
            a1 += 1
        elif b3.isalpha() or b3 = = '_':
            b4 = a1
            while a1 < len(b2) and (b2[a1].isalnum() or b2[a1] == '_'):
                a1 += 1
            yield b2[b4:a1]
        elif b3.isdigit():
            b4 = a1
            while a1 < len(b2) and b2[a1].isdigit():
                a1 += 1
            yield b2[b4:a1]
        elif fonk3(a1):
            yield b2[a1:a1 + 2]
            a1 += 2
        elif fonk2(b3):
            yield b3
            a1 += 1
        elif b3 = = ";":
            yield b3
            a1 += 1
        else:
            raise ValueError(f"Unexpected character '{b3}' in expression")
if b5 = = "__main__":
    b2 = "a = 10 + b * (c - d) >= 5;"
    b6 = list(fonk1(b2))
    print("Tokens:", b6)
