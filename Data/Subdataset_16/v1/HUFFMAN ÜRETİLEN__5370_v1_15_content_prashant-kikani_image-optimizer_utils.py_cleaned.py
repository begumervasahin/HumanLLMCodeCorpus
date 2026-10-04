import numpy as np
def fonk1(b1):
    if b1 = = 'lum':
        b2 = np.array([[2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 3, 4, 5, 6],
                      [2, 2, 2, 2, 4, 5, 7, 9],
                      [2, 2, 2, 4, 5, 7, 9, 12],
                      [3, 3, 4, 5, 8, 10, 12, 12],
                      [4, 4, 5, 7, 10, 12, 12, 12],
                      [5, 5, 7, 9, 12, 12, 12, 12],
                      [6, 6, 9, 12, 12, 12, 12, 12]])
    elif b1 = = 'chrom':
        b2 = np.array([[3, 3, 5, 9, 13, 15, 15, 15],
                      [3, 4, 6, 11, 14, 12, 12, 12],
                      [5, 6, 9, 14, 12, 12, 12, 12],
                      [9, 11, 14, 12, 12, 12, 12, 12],
                      [13, 14, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12],
                      [15, 12, 12, 12, 12, 12, 12, 12]])
    else:
        raise ValueError(f"Component should be either 'lum' or 'chrom', but '{b1}' was found")
    return b2
def fonk2(rows, cols):
    UP, DOWN, RIGHT, LEFT, UP_RIGHT, b3 = range(6)
    def fonk3(direction, b4):
        return {
            UP: lambda b4: (b4[0] - 1, b4[1]),
            DOWN: lambda b4: (b4[0] + 1, b4[1]),
            LEFT: lambda b4: (b4[0], b4[1] - 1),
            RIGHT: lambda b4: (b4[0], b4[1] + 1),
            UP_RIGHT: lambda b4: fonk3(UP, fonk3(RIGHT, b4)),
            b3: lambda b4: fonk3(DOWN, fonk3(LEFT, b4))
        }[direction](b4)
    def fonk4(b4):
        return 0 <= b4[0] < rows and 0 <= b4[1] < cols
    b4 = (0, 0)
    b5 = True
    for _ in range(rows * cols):
        yield b4
        if b5:
            if fonk4(fonk3(UP_RIGHT, b4)):
                b4 = fonk3(UP_RIGHT, b4)
            else:
                b5 = False
                if fonk4(fonk3(RIGHT, b4)):
                    b4 = fonk3(RIGHT, b4)
                else:
                    b4 = fonk3(DOWN, b4)
        else:
            if fonk4(fonk3(b3, b4)):
                b4 = fonk3(b3, b4)
            else:
                b5 = True
                if fonk4(fonk3(DOWN, b4)):
                    b4 = fonk3(DOWN, b4)
                else:
                    b4 = fonk3(RIGHT, b4)
def fonk5(b6):
    b6 = abs(b6)
    a1 = 0
    while b6 > 0:
        b6 >>= 1
        a1 += 1
    return a1
def fonk6(b8):
    if not set(b8).issubset('01'):
        raise ValueError("b8 should have only '0's and '1's")
    return ''.join('0' if b7 = = '1' else '1' for b7 in b8)
def fonk7(number, size):
    return bin(number)[2:][-size:].zfill(size)
def fonk8(b6):
    if b6 = = 0:
        return ''
    b8 = bin(abs(b6))[2:]
    return b8 if b6 > 0 else fonk6(b8)
def fonk9(lst):
    return [item for sublist in lst for item in sublist]
if b9 = = "__main__":
    print("Luminance quantization table:")
    print(fonk1('lum'))
    print("\nZigzag points for a 4x4 matrix:")
    for b4 in fonk2(4, 4):
        print(b4)
    print("\nBits required to represent 37:", fonk5(37))
    print("Binary string flip of '1010':", fonk6('1010'))
    print("Binary representation of unsigned 13 with size 8:", fonk7(13, 8))
    print("Binary representation of signed -13:", fonk8(-13))
    b10 = [[1, 2, 3], [4, 5], [6, 7, 8]]
    print("\nFlattened list:", fonk9(b10))