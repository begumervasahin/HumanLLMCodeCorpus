def grid_values(grid):
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        elif c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))
def display(values):
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print()
def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values if len(values[box]) == 0]):
            return False
    return values
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = [r + c for r in rows for c in cols]
def eliminate(values):
    return values
def only_choice(values):
    return values
def naked_twins(values):
    return values
if __name__ == "__main__":
    puzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    values = grid_values(puzzle)
    values = search(values)
    display(values)