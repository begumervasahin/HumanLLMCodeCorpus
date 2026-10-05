from GF2 import zero, one
import mat
import random
def fonk1(input_string):
    b1 = []
    for b5 in input_string:
        b2 = [one if ord(b5) & (1 << i) else zero for i in range(8)]
        b1.extend(b2)
    return b1
def fonk2(input_bits):
    b3 = []
    for i in range(0, len(input_bits), 8):
        b4 = input_bits[i:i+8]
        b5 = chr(sum(bit.val for bit in b4))
        b3.append(b5)
    return ''.join(b3)
def fonk3(b1, b6 = 4, b10=False):
    b7 = len(b1)
    b8 = {(i, j): one for j in range(b7) for i in range(b6) if b1[b6 * j + i]}
    b9 = mat.Mat((set(range(b6)), set(range(b7))), b8)
    if b10:
        b9 = mat.b10(b9)
    return b9
def fonk4(matrix, b10 = False):
    if b10:
        return [matrix[i, j] for i in sorted(matrix.D[0]) for j in sorted(matrix.D[1])]
    else:
        return [matrix[i, j] for j in sorted(matrix.D[1]) for i in sorted(matrix.D[0])]
def fonk5(matrix, freq):
    b8 = {(i, j): one for i in matrix.D[0] for j in matrix.D[1] if random.random() < freq}
    return mat.Mat(matrix.D, b8)