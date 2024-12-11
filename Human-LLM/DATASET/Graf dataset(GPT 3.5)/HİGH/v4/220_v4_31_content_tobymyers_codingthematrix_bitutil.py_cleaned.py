
from GF2 import zero, one
import mat
import random
def fonk1(input_string):
    b1 = [1 << i for i in range(8)]
    return [one if ord(char) & bit else zero for char in input_string for bit in b1]
def fonk2(input_bits):
    b1 = [1 << i for i in range(8)]
    return ''.join(chr(sum(bit_val if bit else 0 for bit_val, bit in zip(b1, input_bits[i:i+8]))) for i in range(0, len(input_bits), 8))
def fonk3(bits, b2 = 4, b6=False):
    b3 = len(bits)
    b4 = {(i, j): one for j in range(b3) for i in range(b2) if bits[b2 * j + i]}
    b5 = mat.Mat((set(range(b2)), set(range(b3))), b4)
    if b6:
        b5 = mat.b6(b5)
    return b5
def fonk4(matrix, b6 = False):
    if b6:
        return [matrix[i, j] for i in sorted(matrix.D[0]) for j in sorted(matrix.D[1])]
    else:
        return [matrix[i, j] for j in sorted(matrix.D[1]) for i in sorted(matrix.D[0])]
def fonk5(matrix, freq):
    b4 = {(i, j): one for i in matrix.D[0] for j in matrix.D[1] if random.random() < freq}
    return mat.Mat(matrix.D, b4)