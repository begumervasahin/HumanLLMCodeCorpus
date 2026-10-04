def new_split_iter(expr):
    operators = ['+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ',']
    expr = expr + ";"
    pos = 0
    while expr[pos] != ";":
        if expr[pos] == ' ':
            pos += 1
        elif expr[pos].isalpha():
            temp = pos
            while pos < len(expr) and expr[pos] not in operators and expr[pos] != ' ':
                pos += 1
            yield expr[temp:pos]
        elif expr[pos].isdigit():
            temp = pos
            while pos < len(expr) and expr[pos].isdigit():
                pos += 1
            yield expr[temp:pos]
        elif expr[pos] in ['=', '!', '<', '>'] and pos + 1 < len(expr) and expr[pos + 1] == '=':
            yield expr[pos] + expr[pos + 1]
            pos += 2
        else:
            yield expr[pos]
            pos += 1
    yield ";"
if __name__ == "__main__":
    expr = "a = 10 + b * (c - d) >= 5;"
    tokens = list(new_split_iter(expr))
    print("Tokens:", tokens)
