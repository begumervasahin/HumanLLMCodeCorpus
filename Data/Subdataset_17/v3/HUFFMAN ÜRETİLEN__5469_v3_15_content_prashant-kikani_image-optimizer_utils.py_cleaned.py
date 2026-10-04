import numpy as np
def load_quantization_table(component):
    tables = {
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
    if component not in tables:
        raise ValueError(f"Invalid component '{component}'. Must be 'lum' or 'chrom'.")
    return tables[component]
def zigzag_points(rows, cols):
    UP_RIGHT, DOWN_LEFT = (-1, 1), (1, -1)
    def inbounds(point):
        return 0 <= point[0] < rows and 0 <= point[1] < cols
    point = (0, 0)
    move_up = True
    for _ in range(rows * cols):
        yield point
        if move_up:
            if inbounds((point[0] + UP_RIGHT[0], point[1] + UP_RIGHT[1])):
                point = (point[0] + UP_RIGHT[0], point[1] + UP_RIGHT[1])
            else:
                move_up = False
                if inbounds((point[0], point[1] + 1)):
                    point = (point[0], point[1] + 1)
                else:
                    point = (point[0] + 1, point[1])
        else:
            if inbounds((point[0] + DOWN_LEFT[0], point[1] + DOWN_LEFT[1])):
                point = (point[0] + DOWN_LEFT[0], point[1] + DOWN_LEFT[1])
            else:
                move_up = True
                if inbounds((point[0] + 1, point[1])):
                    point = (point[0] + 1, point[1])
                else:
                    point = (point[0], point[1] + 1)
def bits_required(n):
    return n.bit_length()
def binstr_flip(binstr):
    if not set(binstr).issubset({'0', '1'}):
        raise ValueError("Binary string should only contain '0's and '1's.")
    return ''.join('0' if c == '1' else '1' for c in binstr)
def uint_to_binstr(number, size):
    return bin(number)[2:].zfill(size)[-size:]
def int_to_binstr(n):
    if n == 0:
        return ''
    binstr = bin(abs(n))[2:]
    return binstr if n > 0 else binstr_flip(binstr)
def flatten(lst):
    return [item for sublist in lst for item in sublist]
if __name__ == "__main__":
    print("Luminance quantization table:")
    print(load_quantization_table('lum'))
    print("\nZigzag points for a 4x4 matrix:")
    for point in zigzag_points(4, 4):
        print(point)
    print("\nBits required to represent 37:", bits_required(37))
    print("Binary string flip of '1010':", binstr_flip('1010'))
    print("Binary representation of unsigned 13 with size 8:", uint_to_binstr(13, 8))
    print("Binary representation of signed -13:", int_to_binstr(-13))
    nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
    print("\nFlattened list:", flatten(nested_list))