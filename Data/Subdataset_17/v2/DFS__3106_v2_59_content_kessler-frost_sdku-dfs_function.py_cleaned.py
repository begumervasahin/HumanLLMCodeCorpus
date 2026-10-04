import string
from typing import List, Dict
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = [r + c for r in rows for c in cols]
def grid_values(grid: str) -> Dict[str, str]:
    digits = '123456789'
    chars = [c if c in digits else digits for c in grid]
    assert len(chars) == 81, "Input grid must be a string of length 81"
    return dict(zip(boxes, chars))
def display(values: Dict[str, str]):
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF':
            print(line)
    print()
def search(values: Dict[str, str]) -> Dict[str, str]:
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
def reduce_puzzle(values: Dict[str, str]) -> Dict[str, str]:
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if any(len(values[box]) == 0 for box in boxes):
            return False
    return values
def eliminate(values: Dict[str, str]) -> Dict[str, str]:
    for box in boxes:
        if len(values[box]) == 1:
            digit = values[box]
            for peer in peers[box]:
                values[peer] = values[peer].replace(digit, '')
    return values
def only_choice(values: Dict[str, str]) -> Dict[str, str]:
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[1]] = digit
    return values
def naked_twins(values: Dict[str, str]) -> Dict[str, str]:
    for unit in unitlist:
        pairs = [box for box in unit if len(values[box]) == 2]
        naked_twins = [(box1, box2) for i, box1 in enumerate(pairs) for box2 in pairs[i + 1:] if values[box1] == values[box2]]
        for box1, box2 in naked_twins:
            digit1, digit2 = values[box1]
            for box in unit:
                if box != box1 and box != box2:
                    values[box] = values[box].replace(digit1, '').replace(digit2, '')
    return values
def cross(A, B):
    return [a + b for a in A for b in B]
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)
if __name__ == "__main__":
    puzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    values = grid_values(puzzle)
    solution = search(values)
    if solution:
        display(solution)
    else:
        print("No solution exists for the given Sudoku puzzle.")