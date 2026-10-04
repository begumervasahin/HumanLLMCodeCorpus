def new_split_iter(expr):
    operators = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    expr = expr + ";"
    pos = 0
    while pos < len(expr) and expr[pos] != ";":
        char = expr[pos]
        if char.isspace():
            pos += 1
        elif char.isalpha():
            start = pos
            while pos < len(expr) and (expr[pos].isalnum() or expr[pos] == '_'):
                pos += 1
            yield expr[start:pos]
        elif char.isdigit():
            start = pos
            while pos < len(expr) and expr[pos].isdigit():
                pos += 1
            yield expr[start:pos]
        elif char in {'=', '!', '<', '>'} and pos + 1 < len(expr) and expr[pos + 1] == '=':
            yield expr[pos] + expr[pos + 1]
            pos += 2
        elif char in operators:
            yield char
            pos += 1
        else:
            raise ValueError(f"Unexpected character '{char}' in expression")
    yield ";"
if __name__ == "__main__":
    expr = "a = 10 + b * (c - d) >= 5;"
    tokens = list(new_split_iter(expr))
    print("Tokens:", tokens)
