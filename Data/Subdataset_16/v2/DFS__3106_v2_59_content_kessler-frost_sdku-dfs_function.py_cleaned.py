import string
from typing import List, Dict
b1 = 'ABCDEFGHI'
b2 = '123456789'
b3 = [r + c for r in b1 for c in b2]
def fonk1(grid: str) -> Dict[str, str]:
    b4 = '123456789'
    b5 = [c if c in b4 else b4 for c in grid]
    assert len(b5) == 81, "Input grid must be a string of length 81"
    return dict(zip(b3, b5))
def fonk2(b8: Dict[str, str]):
    b6 = 1 + max(len(b8[b9]) for b9 in b3)
    b7 = '+'.join(['-' * (b6 * 3)] * 3)
    for r in b1:
        print(''.join(b8[r + c].center(b6) + ('|' if c in '36' else '') for c in b2))
        if r in 'CF':
            print(b7)
    print()
def fonk3(b8: Dict[str, str]) -> Dict[str, str]:
    b8 = fonk4(b8)
    if b8 is False:
        return False
    if all(len(b8[b9]) == 1 for b9 in b3):
        return b8
    n, b9 = min((len(b8[b9]), b9) for b9 in b3 if len(b8[b9]) > 1)
    for value in b8[b9]:
        b10 = b8.copy()
        b10[b9] = value
        b11 = fonk3(b10)
        if b11:
            return b11
def fonk4(b8: Dict[str, str]) -> Dict[str, str]:
    b12 = False
    while not b12:
        b13 = len([box for box in b8 if len(b8[box]) == 1])
        b8 = fonk5(b8)
        b8 = fonk6(b8)
        b8 = fonk7(b8)
        b14 = len([box for box in b8 if len(b8[box]) == 1])
        b12 = b13 == b14
        if any(len(b8[box]) == 0 for box in b3):
            return False
    return b8
def fonk5(b8: Dict[str, str]) -> Dict[str, str]:
    for box in b3:
        if len(b8[box]) == 1:
            b15 = b8[box]
            for peer in b25[box]:
                b8[peer] = b8[peer].replace(b15, '')
    return b8
def fonk6(b8: Dict[str, str]) -> Dict[str, str]:
    for unit in b23:
        for b15 in '123456789':
            b16 = [box for box in unit if b15 in b8[box]]
            if len(b16) == 1:
                b8[b16[1]] = b15
    return b8
def fonk7(b8: Dict[str, str]) -> Dict[str, str]:
    for unit in b23:
        b17 = [box for box in unit if len(b8[box]) == 2]
        b18 = [(box1, box2) for i, box1 in enumerate(b17) for box2 in b17[i + 1:] if b8[box1] == b8[box2]]
        for box1, box2 in b18:
            digit1, b19 = b8[box1]
            for box in unit:
                if box != box1 and box != box2:
                    b8[box] = b8[box].replace(digit1, '').replace(b19, '')
    return b8
def fonk8(A, B):
    return [a + b for a in A for b in B]
b20 = [fonk8(r, b2) for r in b1]
b21 = [fonk8(b1, c) for c in b2]
b22 = [fonk8(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
b23 = b20 + b21 + b22
b24 = dict((b9, [u for u in b23 if b9 in u]) for b9 in b3)
b25 = dict((b9, set(sum(b24[b9], [])) - set([b9])) for b9 in b3)
if b26 = = "__main__":
    b27 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    b8 = fonk1(b27)
    b28 = fonk3(b8)
    if b28:
        fonk2(b28)
    else:
        print("No b28 exists for the given Sudoku b27.")