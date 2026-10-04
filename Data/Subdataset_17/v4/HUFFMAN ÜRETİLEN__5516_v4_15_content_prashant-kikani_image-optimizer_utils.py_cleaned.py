import numpy as np
def load_quantization_table(component):
    if component == 'lum':
        q = np.array([
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 4, 5, 7, 9],
            [2, 2, 2, 4, 5, 7, 9, 12],
            [3, 3, 4, 5, 8, 10, 12, 12],
            [4, 4, 5, 7, 10, 12, 12, 12],
            [5, 5, 7, 9, 12, 12, 12, 12],
            [6, 6, 9, 12, 12, 12, 12, 12]
        ])
    elif component == 'chrom':
        q = np.array([
            [3, 3, 5, 9, 13, 15, 15, 15],
            [3, 4, 6, 11, 14, 12, 12, 12],
            [5, 6, 9, 14, 12, 12, 12, 12],
            [9, 11, 14, 12, 12, 12, 12, 12],
            [13, 14, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12]
        ])
    else:
        raise ValueError(f"component should be either 'lum' or 'chrom', but '{component}' was found")
    return q
def zigzag_points(rows, cols):
    UP, DOWN, RIGHT, LEFT, UP_RIGHT, DOWN_LEFT = range(6)
    def move(direction, point):
        moves = {
            UP: lambda p: (p[0] - 1, p[1]),
            DOWN: lambda p: (p[0] + 1, p[1]),
            LEFT: lambda p: (p[0], p[1] - 1),
            RIGHT: lambda p: (p[0], p[1] + 1),
            UP_RIGHT: lambda p: move(UP, move(RIGHT, p)),
            DOWN_LEFT: lambda p: move(DOWN, move(LEFT, p))
        }
        return moves[direction](point)
    def inbounds(point):
        return 0 <= point[0] < rows and 0 <= point[1] < cols
    point = (0, 0)
    move_up = True
    for _ in range(rows * cols):
        yield point
        if move_up:
            if inbounds(move(UP_RIGHT, point)):
                point = move(UP_RIGHT, point)
            else:
                move_up = False
                if inbounds(move(RIGHT, point)):
                    point = move(RIGHT, point)
                else:
                    point = move(DOWN, point)
        else:
            if inbounds(move(DOWN_LEFT, point)):
                point = move(DOWN_LEFT, point)
            else:
                move_up = True
                if inbounds(move(DOWN, point)):
                    point = move(DOWN, point)
                else:
                    point = move(RIGHT, point)
def bits_required(n):
    n = abs(n)
    bits = 0
    while n > 0:
        n >>= 1
        bits += 1
    return bits
def binstr_flip(binstr):
    if not set(binstr).issubset('01'):
        raise ValueError("binstr should contain only '0's and '1's")
    return ''.join('0' if c == '1' else '1' for c in binstr)
def uint_to_binstr(number, size):
    return bin(number)[2:][-size:].zfill(size)
def int_to_binstr(n):
    if n == 0:
        return ''
    binstr = bin(abs(n))[2:]
    return binstr if n > 0 else binstr_flip(binstr)
def flatten(lst):
    return [item for sublist in lst for item in sublist]