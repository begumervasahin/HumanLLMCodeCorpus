import numpy as np
def fonk1(component):
    b1 = {
        'lum': np.array([
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 3, 4, 5, 6],
            [2, 2, 2, 2, 4, 5, 7, 9],
            [2, 2, 2, 4, 5, 7, 9, 12],
            [3, 3, 4, 5, 8, 10, 12, 12],
            [4, 4, 5, 7, 10, 12, 12, 12],
            [5, 5, 7, 9, 12, 12, 12, 12],
            [6, 6, 9, 12, 12, 12, 12, 12]
        ]),
        'chrom': np.array([
            [3, 3, 5, 9, 13, 15, 15, 15],
            [3, 4, 6, 11, 14, 12, 12, 12],
            [5, 6, 9, 14, 12, 12, 12, 12],
            [9, 11, 14, 12, 12, 12, 12, 12],
            [13, 14, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12],
            [15, 12, 12, 12, 12, 12, 12, 12]
        ])
    }
    if component not in b1:
        raise ValueError(f"Invalid component '{component}'. Must be 'lum' or 'chrom'.")
    return b1[component]
def fonk2(rows, cols):
    UP_RIGHT, b2 = (-1, 1), (1, -1)
    def fonk3(b3):
        return 0 <= b3[0] < rows and 0 <= b3[1] < cols
    b3 = (0, 0)
    b4 = True
    for _ in range(rows * cols):
        yield b3
        if b4:
            if fonk3((b3[0] + UP_RIGHT[0], b3[1] + UP_RIGHT[1])):
                b3 = (b3[0] + UP_RIGHT[0], b3[1] + UP_RIGHT[1])
            else:
                b4 = False
                if fonk3((b3[0], b3[1] + 1)):
                    b3 = (b3[0], b3[1] + 1)
                else:
                    b3 = (b3[0] + 1, b3[1])
        else:
            if fonk3((b3[0] + b2[0], b3[1] + b2[1])):
                b3 = (b3[0] + b2[0], b3[1] + b2[1])
            else:
                b4 = True
                if fonk3((b3[0] + 1, b3[1])):
                    b3 = (b3[0] + 1, b3[1])
                else:
                    b3 = (b3[0], b3[1] + 1)
def fonk4(b6):
    return b6.bit_length()
def fonk5(b7):
    if not set(b7).issubset({'0', '1'}):
        raise ValueError("Binary string should only contain '0's and '1's.")
    return ''.join('0' if b5 = = '1' else '1' for b5 in b7)
def fonk6(number, size):
    return bin(number)[2:].zfill(size)[-size:]
def fonk7(b6):
    if b6 = = 0:
        return ''
    b7 = bin(abs(b6))[2:]
    return b7 if b6 > 0 else fonk5(b7)
def fonk8(lst):
    return [item for sublist in lst for item in sublist]
if b8 = = "__main__":
    print("Luminance quantization table:")
    print(fonk1('lum'))
    print("\nZigzag points for a 4x4 matrix:")
    for b3 in fonk2(4, 4):
        print(b3)
    print("\nBits required to represent 37:", fonk4(37))
    print("Binary string flip of '1010':", fonk5('1010'))
    print("Binary representation of unsigned 13 with size 8:", fonk6(13, 8))
    print("Binary representation of signed -13:", fonk7(-13))
    b9 = [[1, 2, 3], [4, 5], [6, 7, 8]]
    print("\nFlattened list:", fonk8(b9))