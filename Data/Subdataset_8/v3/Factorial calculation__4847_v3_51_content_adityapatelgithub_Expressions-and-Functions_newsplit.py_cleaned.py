def tokenize(expression):
    operators = {'+', '-', '*', '/', '%', '(', ')', '=', '<', '>', '!', '?', ':', ';', ','}
    double_operators = {"==", "!=", "<=", ">="}
    expression += ";"
    position = 0
    while expression[position] != ";":
        char = expression[position]
        if char.isspace():
            position += 1
            continue
        if char.isalpha():
            start_pos = position
            while position < len(expression) and (expression[position].isalnum() or expression[position] == '_'):
                position += 1
            yield expression[start_pos:position]
            continue
        if char.isdigit():
            start_pos = position
            while position < len(expression) and expression[position].isdigit():
                position += 1
            yield expression[start_pos:position]
            continue
        if char in operators:
            next_char = expression[position + 1] if position + 1 < len(expression) else ""
            potential_double = char + next_char
            if potential_double in double_operators:
                yield potential_double
                position += 2
            else:
                yield char
                position += 1
            continue
    yield ";"
example_expression = "if (a >= 12) { return a + 1; }"
print(list(tokenize(example_expression)))